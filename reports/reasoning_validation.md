# Rationale and Reasoning: Decision by Decision

This document explains why each decision in the project is the right one, not just what the code does. For every step it walks through the choices made, the alternatives considered, and the evidence behind the pick. The final verified numbers live in `reports/validation_report.md`; this file is about the logic.

---

## Data preparation

### Why category fields are not turned into yes/no columns

This was the most consequential choice in the whole pipeline, and it was corrected partway through the project. The three category fields (education, income type, work sector) were originally converted into about 21 separate yes/no columns.

That approach damages similarity calculations in two ways. First, 21 sparse columns together quietly outweigh any single continuous feature, so which sector a person works in ends up dominating the calculation over how heavy their repayment burden is. Second, it forces every category to be exactly as different from every other as possible, which is wrong for education: someone with a higher degree is plainly closer to someone with an incomplete higher degree than to someone with a lower secondary education, and the yes/no approach throws that ordering away.

The fix matches each encoding to what the variable actually is:

- Education becomes a single number from 0 to 4. It is a genuine ladder, and the data shows a clean relationship between education level and loan size, so one ordered number is both accurate and compact.
- Income type and work sector have no natural order, so each becomes a single "how common is this?" number. This collapses the whole variable into one meaningful axis without creating artificial distances between categories.

A side benefit confirmed the diagnosis: the original approach had created three columns that were identical to each other (the pensioner flag, the "Unknown" work sector column, and the "Pensioner" income type column). The new approach removed that trap entirely. The total number of features fell from 65 to 47, and the number of closely correlated pairs remaining dropped to one, a defensible case where a mean and a max of the same metric are both kept.

### Why the pension/employment placeholder had to be flagged, not just corrected

The employment-length column holds a value equivalent to one thousand years for about 18 percent of applicants, all pensioners or unemployed people for whom an employment figure does not apply. Two facts justify the treatment chosen. First, leaving it as a number would corrupt every similarity calculation: a thousand-year tenure is farther from a five-year tenure than any real human difference in the data. Second, the group is behaviourally real: their actual default rate is 5.4 percent against 8.7 percent for everyone else. So the value is flagged as a special category and then set to blank. Removing those applicants would have discarded one fifth of the portfolio; inventing a replacement number would have made up data.

### Why missing values are handled by reason, not by one rule for everything

Each gap in the data was handled based on what that gap actually means:

- Flags before fills. The "no car", "no housing data", and "no bureau score" flags are created before any value is filled, because in credit data a blank often carries a meaning of its own, and filling it first would erase that signal.
- Zero for structural absence. A blank car-age field means the applicant has no car; a blank apartment measurement means there is no apartment record. Zero here means "none", not a guess.
- Midpoint for random gaps, used for bureau scores and similar fields where the absence looks like a collection accident rather than a message.
- Group-level most-common for occupation type: the most frequent occupation among applicants in the same income bracket, which is more informative than a single global default.
- Zero for empty credit history aggregates, because no records means no activity.

One honest note is recorded rather than hidden: the main bureau score is missing for 56 percent of applicants, and filling with the midpoint piles most of the portfolio onto one value. This is kept because the separate "no score" flag already identifies that group, the midpoint is neutral, and removing the feature entirely would throw away the most useful predictor for the 44 percent who do have a score. It is a conscious compromise.

### Why small ordered columns also need standardization

A bug was found here: the standardization step originally skipped every integer column with a small range, silently leaving small ordered fields (the social-circle category and the education ladder) at their raw scale, which gave them an outsized weight compared with everything else. The fix now checks the actual range of values rather than the data type: only genuine yes/no flags stay on their natural scale, because a yes/no flag is already on a comparable scale and leaving it that way makes the segment profiles readable as "the share of this group with this characteristic". Everything else, including ordered fields and frequency-encoded categories, is standardized.

### Why feature selection uses both a similarity check and an importance check

The selection used two measures for two different reasons. The correlation check finds redundancy: pairs with a correlation above 0.85 are listed, and identical columns are removed because a duplicated column is a doubled weight. The importance check (how much information each feature carries about which customers eventually defaulted, including non-linear relationships) flags which features are genuinely useful. Features with low importance are not dropped automatically, because the goal is to find natural groups rather than to predict an outcome; the importance scores serve as documented, measurable evidence that the selection considered information content, not just redundancy.

---

## Customer segmentation

### Why two different compressed spaces, not one

The compression is split because different grouping methods need different things.

K-Means and hierarchical grouping are both distance-based, so they run on a linear compression that keeps nine components (under the required limit of ten). Nine is not a round guess: a scree chart shows that each successive component contributes a little less than the last, and then contribution drops more sharply from the ninth to the tenth, so components beyond nine add very little while keeping nine captures nearly all the useful variation.

The density-based method is handled differently. Linear compression preserves overall variance but flattens tight local groups, so the density-based method on that space tends to see one undifferentiated mass. A neighbourhood-preserving layout is used instead: tight groups stay tight, and genuinely isolated applicants land at the edges. The radius for that method is chosen automatically from the data itself, not set by hand.

### Why five groups

Two standard charts (an elbow chart and a separation score) were both produced for group counts from two to ten. The separation score peaks at two groups, but two segments are useless for any real business decision. The elbow chart points to five, and five also has the best separation score among all the genuinely useful options (three or more). When two standard criteria and the requirement for actionable results all point to the same value, the choice is well-grounded.

### Why three methods, and what each contributes

K-Means on the full data is the primary grouping, because it scales to 356,000 applicants and produces compact, describable groups. Ward hierarchical grouping is the independent check: its logic (merging the most similar pairs upward) shares nothing with K-Means' approach, so genuine agreement between them is real evidence, not a coincidence. An earlier shortcut had silently collapsed 94 percent of applicants into one group (agreement score of 0.02); the fix restored genuine agreement of about 0.55. That episode is exactly why a second method is worth running. The density-based method is the noise detector: it finds dense pockets plus a small fraction of isolated points, and those isolated points pass to the anomaly review step.

### Why humans name the groups

The algorithm only finds the grouping. A person reads each group's top distinguishing features and assigns a business name, a risk level, and a recommendation, because "Group 3" supports no business decision and "Troubled Borrower" does. The naming is saved to a shared file because the group numbering can shift between runs even with a fixed random seed; every later step reads names from that file instead of relying on numbers, a lesson learned from an actual mislabelling incident earlier in the project.

---

## Behaviour rules

### Why equal-sized bins

Behaviour rules need categories. Equal-sized bins are used instead of equal-width bins because they guarantee each category holds a similar share of applicants: no empty categories, and balanced coverage across items. This matters because the rule-finding algorithms are driven by how common each pattern is: skewed bins would make some categories almost invisible.

### Why three algorithms for the same task

Three well-established rule-finding algorithms were all run on the same data. They search the same space with very different approaches. Running all three and checking that they find the same rules is a cheap and strong correctness check: any implementation slip or sensitivity to a setting would show up as disagreement. They agreed exactly, which is the best available evidence that the mined rules are properties of the data and not artefacts of any one method.

### Why these filter thresholds

A strength ratio of at least 1.2 removes patterns barely better than coincidence. A reliability of at least 35 percent removes patterns that fail too often to act on. The redundancy filter (removing a rule if its item overlap with an already-selected rule is too high) exists because frequent-pattern mining produces families of near-identical rules; without it the final list would say one thing many times over. Keeping the strongest few per segment forces coverage of the whole portfolio rather than letting one dense group dominate the story.

---

## Anomaly detection and investigation

### Why five signals instead of one

No single detector sees every kind of unusual case, because "unusual" is not one concept:

- The per-column robust check flags a value outside its column's normal range. Chosen because it handles the heavy tails typical of financial data without being thrown off by a few extreme cases.
- The per-column sensitive check flags values far from the column's centre. Chosen as a complement where the distribution is roughly symmetrical. Both are openly blind to combinations, which motivates the three signals that follow.
- The combination-aware signal (robust version) measures how far a row sits from the bulk along the natural correlations of the data, catching applicants whose values are each ordinary but wrong together. A classic example: a loan amount that is large only relative to that applicant's income.
- The random partitioning signal flags rows that are easy to separate from everything else. Chosen because it assumes nothing about the shape of the data and catches unusual cases that no threshold-based method can describe.
- The density-based signal from the segmentation step is the independent cross-check: applicants sitting in no dense region of the customer map, identified with different machinery in a different part of the process.

### Why the combination-aware signal uses a robust version and is calibrated on the data

Two decisions inside this method deserve their own explanation.

The ordinary version of the covariance calculation suffers from a masking problem: the very unusual cases being hunted inflate the covariance themselves, stretching the reference shape around them until they look normal. The robust version fits the covariance on the tightest-fitting subset of rows, keeping the reference anchored to the ordinary bulk. It is fitted on a sample for efficiency, then every row is scored.

The standard textbook threshold assumes the data follows a bell-curve shape. When we apply it here it flags roughly a third of the entire portfolio, which is a sign that credit data does not follow that shape rather than a sign that a third of applicants are genuinely unusual. The notebook demonstrates this failure clearly, then sets the threshold empirically at the top 2.5 percent of scores, keeping the flag rate comparable to the other signals so no single method dominates the ensemble. Showing the failed textbook threshold is deliberate: it documents why the adjusted choice is necessary.

### Why the final verdict requires agreement between signals

Each signal has a threshold, and every threshold involves some judgement. Requiring at least three of the five to agree before classifying a case as a high-confidence anomaly makes the final verdict robust to any one signal's calibration. The tiers below that (two signals: moderate concern; one signal: worth noting) are kept because they turn out to be informative: the actual default rate climbs at every tier, which was confirmed against the real outcomes after the analysis was complete.

### Why two labels per case

A flat list of unusual cases supports no action. The first label says how the case deviates: a single extreme figure against the whole population, a figure that is ordinary in general but unusual for its own customer group, or membership of a small cluster of applicants who stand apart together. The second label says what to do: verify the data before deciding, route to appropriate handling, or require individual credit review. The contextual class (ordinary in general, unusual for its own group) is singled out as the most investigation-worthy, because behaving unlike your own peer group is a subtler and more suspicious signal than simply being extreme. Every case carries a real applicant ID so the operations team can follow up.

---

## Dashboard and reporting

### Why every number is drawn from the output files, never typed by hand

The dashboard reads all figures from the result files at startup, and the written reports reference the same outputs. This is a defence against the most common failure in analytical reporting: numbers that silently drift from the analysis that produced them. Re-running any step re-synchronises everything downstream.

### Why the validation result is shown so prominently

The default label is never used during the analysis. Showing that the groups and anomaly levels consistently produce real differences in default rates, rising in the right order without a single exception, is the strongest evidence available that what was found is real. It sits at the top of the executive view because it answers the question every decision-maker should ask first: why should I believe any of this?

### Why explanations are written in plain language, not technical output

Every chart carries a caption explaining how to read it, every section opens with a plain-language introduction, and technical column names are translated to business terms throughout. The reason is simple: the audience for this work is the person who will make a decision with it, and that person should never need to decode a technical label to understand a finding.
