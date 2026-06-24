# Phase 4 — Anomaly Investigation Log
**Dataset:** Home Credit Default Risk
**High-confidence anomalies investigated:** 5,511
_Log ini menampilkan detail 300 kasus paling anomalous (isolation score terendah); CSV berisi semuanya._

---

## SK_ID_CURR 176691

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 14.90 (300.3x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `EXT_SOURCE_1` = 0.61 (44.1x median), `EXT_SOURCE_3` = -1.78 (16.9x median), `AMT_ANNUITY` = -1.45 (16.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 303385

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 31.19 (627.4x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 15.25 (298.9x median), `EXT_SOURCE_1` = 1.31 (96.5x median), `BUREAU_BB_DPD_RATIO_MEAN` = 9.72 (51.0x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 242023

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 19.17 (386.0x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `EXT_SOURCE_1` = 0.58 (41.7x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_BB_DPD_RATIO_MEAN` = 3.59 (19.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 403582

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 25.61 (515.3x median), `EXT_SOURCE_1` = 1.76 (129.6x median), `PREV_APPROVAL_RATE` = -1.10 (55.2x median), `INST_DPD_MEAN` = 80.21 (28.2x median), `CREDIT_TERM_MONTHS` = 1.96 (26.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 349124

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | Tipe B (Rare but Valid) |
| Top Deviating Features | `YEARS_BIRTH` = -1.23 (37.1x median), `INST_SEVERE_LATE_RATIO` = 6.00 (36.7x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = -1.51 (32.4x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 1.54 (31.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## SK_ID_CURR 417331

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 12.34 (248.9x median), `POS_SK_DPD_MEAN` = 14.15 (73.9x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 3.54 (70.1x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `ANNUITY_TO_INCOME` = 2.98 (34.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 184984

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 55.93 (1124.3x median), `INST_DPD_MEAN` = 218.74 (78.7x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `ANNUITY_TO_INCOME` = 3.09 (36.0x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 450615

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 12.92 (260.4x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_ACTIVE_RATIO` = 1.41 (24.8x median), `CREDIT_TERM_MONTHS` = 1.68 (22.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 426346

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 30.85 (620.6x median), `EXT_SOURCE_1` = -2.78 (207.7x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 3.97 (78.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_BB_DPD_RATIO_MEAN` = 3.88 (21.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 302086

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 9.59 (193.6x median), `EXT_SOURCE_1` = 1.82 (134.0x median), `EXT_SOURCE_3` = -2.41 (22.6x median), `BUREAU_COUNT` = 2.46 (14.7x median), `DEF_30_CNT_SOCIAL_CIRCLE_BIN` = 4.63 (14.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 373492

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 23.36 (470.2x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `CREDIT_TERM_MONTHS` = 1.68 (22.8x median), `BUREAU_DAYS_CREDIT_MEAN` = -2.89 (17.2x median), `EXT_SOURCE_2` = -1.95 (10.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 155925

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = 1.88 (138.5x median), `AMT_CREDIT` = -2.04 (54.0x median), `CC_SK_DPD_MEAN` = 2.26 (46.5x median), `AMT_ANNUITY` = -2.08 (35.8x median), `INST_SEVERE_LATE_RATIO` = 4.51 (27.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 291047

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 18.89 (380.3x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `AMT_ANNUITY` = -1.34 (15.7x median), `ANNUITY_TO_INCOME` = -1.29 (13.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 198918

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 37.09 (725.2x median), `BUREAU_BB_DPD_RATIO_MEAN` = 22.76 (118.1x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `POS_SK_DPD_MEAN` = 8.45 (43.8x median), `EXT_SOURCE_3` = -1.35 (13.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 359511

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -1.68 (83.6x median), `POS_SK_DPD_MEAN` = 11.95 (62.3x median), `EXT_SOURCE_1` = 0.53 (38.7x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `CREDIT_TERM_MONTHS` = 1.28 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 381288

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 26.91 (541.4x median), `EXT_SOURCE_1` = -1.31 (98.6x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `POS_SK_DPD_MEAN` = 4.10 (20.7x median), `PREV_APPROVAL_RATE` = -0.36 (18.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 421780

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 31.78 (621.5x median), `BUREAU_BB_DPD_RATIO_MEAN` = 17.87 (92.9x median), `POS_SK_DPD_MEAN` = 9.29 (48.2x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `CREDIT_TERM_MONTHS` = 1.68 (22.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 311231

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 15.45 (311.3x median), `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = 0.84 (12.0x median), `AMT_ANNUITY` = -0.99 (11.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 228577

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 23.39 (470.7x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `INST_DPD_MEAN` = 48.03 (16.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 415980

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = 1.43 (105.2x median), `PREV_APPROVAL_RATE` = -1.51 (75.5x median), `POS_SK_DPD_MEAN` = 8.55 (44.3x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `BUREAU_BB_DPD_RATIO_MEAN` = 5.13 (27.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 455540

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 21.82 (439.2x median), `EXT_SOURCE_1` = 2.30 (169.5x median), `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CREDIT_TERM_MONTHS` = -1.41 (17.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 273754

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 15.95 (312.4x median), `BUREAU_BB_DPD_RATIO_MEAN` = 9.25 (48.6x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `POS_SK_DPD_MEAN` = 5.60 (28.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 336366

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 10.35 (53.8x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_BB_DPD_RATIO_MEAN` = 3.09 (16.9x median), `AMT_ANNUITY` = 1.48 (15.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 162232

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 14.28 (287.8x median), `EXT_SOURCE_1` = 0.98 (71.9x median), `PREV_APPROVAL_RATE` = -0.87 (43.9x median), `CREDIT_TERM_MONTHS` = 1.44 (19.7x median), `ANNUITY_TO_INCOME` = 1.36 (16.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 169968

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 9.75 (196.9x median), `EXT_SOURCE_1` = 0.79 (58.0x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `CREDIT_TERM_MONTHS` = -1.04 (12.5x median), `ANNUITY_TO_INCOME` = -0.92 (9.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 447102

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 15.58 (314.0x median), `CREDIT_TERM_MONTHS` = 1.68 (22.8x median), `CREDIT_TO_INCOME` = 1.92 (13.4x median), `ANNUITY_TO_INCOME` = 0.84 (10.6x median), `EXT_SOURCE_3` = -1.06 (10.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 213746

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 11.37 (229.3x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `ANNUITY_TO_INCOME` = 2.20 (26.0x median), `YEARS_EMPLOYED` = 4.57 (14.8x median), `BUREAU_ACTIVE_RATIO` = 0.78 (14.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 305791

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 9.89 (199.7x median), `POS_SK_DPD_MEAN` = 11.03 (57.4x median), `EXT_SOURCE_1` = 0.55 (39.7x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `CREDIT_TERM_MONTHS` = 1.97 (26.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 153265

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 3.70 (73.3x median), `POS_SK_DPD_MEAN` = 10.09 (52.4x median), `EXT_SOURCE_1` = 0.51 (37.0x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_3` = -2.38 (22.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 142357

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 7.91 (159.9x median), `PREV_APPROVAL_RATE` = -0.50 (25.8x median), `EXT_SOURCE_1` = -0.27 (20.7x median), `CNT_CHILDREN` = 6.39 (12.1x median), `EXT_SOURCE_3` = -1.14 (11.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 280230

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 27.31 (549.6x median), `POS_SK_DPD_MEAN` = 14.72 (77.0x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `EXT_SOURCE_1` = 0.39 (27.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 361080

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 24.67 (482.7x median), `BUREAU_BB_DPD_RATIO_MEAN` = 15.98 (83.2x median), `POS_SK_DPD_MEAN` = 12.21 (63.7x median), `CREDIT_TERM_MONTHS` = 0.62 (9.0x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 192426

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 10.80 (217.8x median), `EXT_SOURCE_1` = 0.93 (68.0x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `CREDIT_TERM_MONTHS` = -1.40 (17.2x median), `AMT_ANNUITY` = 1.16 (11.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 282103

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 10.95 (214.9x median), `PREV_APPROVAL_RATE` = -1.40 (69.7x median), `EXT_SOURCE_1` = 0.44 (31.7x median), `BUREAU_BB_DPD_RATIO_MEAN` = 5.63 (30.0x median), `POS_SK_DPD_MEAN` = 4.14 (20.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 241308

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 8.10 (163.6x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `ORGANIZATION_TYPE_FREQ` = 1.37 (8.9x median), `CC_MONTHS_COUNT` = 3.33 (8.6x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.25 (6.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 273907

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 16.09 (324.2x median), `EXT_SOURCE_1` = -0.82 (61.9x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `AMT_ANNUITY` = -1.05 (12.5x median), `CREDIT_TERM_MONTHS` = -0.74 (8.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 364577

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = 2.01 (148.4x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 3.89 (76.9x median), `PREV_APPROVAL_RATE` = -1.24 (62.0x median), `POS_SK_DPD_MEAN` = 9.57 (49.7x median), `EXT_SOURCE_2` = -2.66 (14.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 292151

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 18.65 (375.5x median), `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `CREDIT_TERM_MONTHS` = -1.51 (18.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.28 (9.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 238245

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 11.72 (236.4x median), `EXT_SOURCE_1` = -1.63 (122.0x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 2.18 (43.6x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `ANNUITY_TO_INCOME` = 2.13 (25.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 362915

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 9.87 (199.2x median), `EXT_SOURCE_1` = -0.81 (61.4x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CREDIT_TERM_MONTHS` = 1.19 (16.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 438111

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 14.10 (284.1x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `YEARS_BIRTH` = 1.68 (12.6x median), `CREDIT_TERM_MONTHS` = 0.85 (12.1x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (10.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 232011

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 18.55 (373.5x median), `EXT_SOURCE_1` = -0.62 (47.2x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `CREDIT_TERM_MONTHS` = -1.57 (19.4x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 169021

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 8.68 (175.3x median), `EXT_SOURCE_1` = -0.56 (42.8x median), `BUREAU_ACTIVE_RATIO` = 1.41 (24.8x median), `EXT_SOURCE_3` = -1.63 (15.6x median), `AMT_ANNUITY` = -0.66 (8.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 175301

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 12.32 (248.4x median), `EXT_SOURCE_1` = 1.42 (104.4x median), `BUREAU_COUNT` = 4.88 (28.1x median), `CREDIT_TERM_MONTHS` = -1.08 (13.1x median), `ANNUITY_TO_INCOME` = -1.24 (13.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 290449

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 20.14 (405.4x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `ANNUITY_TO_INCOME` = 2.37 (27.8x median), `BUREAU_BB_DPD_RATIO_MEAN` = 4.96 (26.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 215601

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 14.64 (295.0x median), `EXT_SOURCE_1` = 2.06 (151.7x median), `PREV_APPROVAL_RATE` = -0.87 (43.9x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_ACTIVE_RATIO` = 1.51 (26.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 284468

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 14.14 (277.1x median), `PREV_APPROVAL_RATE` = -1.24 (62.0x median), `BUREAU_BB_DPD_RATIO_MEAN` = 7.75 (40.9x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `POS_SK_DPD_MEAN` = 4.54 (23.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 150945

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 5.22 (103.0x median), `EXT_SOURCE_1` = 0.88 (64.3x median), `POS_MONTHS_COUNT` = 2.22 (58.3x median), `INST_DPD_MAX` = 4.91 (48.1x median), `BUREAU_BB_DPD_RATIO_MEAN` = 6.03 (32.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 119813

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 12.84 (67.0x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `CREDIT_TERM_MONTHS` = -1.62 (20.0x median), `PREV_APPROVAL_RATE` = -0.36 (18.6x median), `EXT_SOURCE_3` = -1.74 (16.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 235486

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 21.29 (428.5x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `CREDIT_TERM_MONTHS` = -1.45 (17.9x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `EXT_SOURCE_1` = 0.21 (14.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 249622

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 34.76 (699.1x median), `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `AMT_ANNUITY` = 1.10 (11.0x median), `AMT_INCOME_TOTAL` = 1.84 (9.6x median), `CC_MONTHS_COUNT` = 3.45 (8.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 122297

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = -2.04 (152.2x median), `PREV_APPROVAL_RATE` = -2.06 (102.6x median), `POS_SK_DPD_MEAN` = 18.34 (96.1x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 4.06 (80.3x median), `CREDIT_TERM_MONTHS` = 1.68 (22.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 113533

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = 2.06 (152.3x median), `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `CC_SK_DPD_MEAN` = 3.94 (80.1x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_ACTIVE_RATIO` = 0.78 (14.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 274469

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = 2.29 (169.3x median), `CC_SK_DPD_MEAN` = 6.93 (140.2x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = -1.39 (17.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 436376

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -1.74 (86.6x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `EXT_SOURCE_3` = -2.10 (19.8x median), `CC_SK_DPD_MEAN` = 0.85 (18.1x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.97 (11.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 443277

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 6.11 (123.7x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `CREDIT_TERM_MONTHS` = 1.68 (22.8x median), `BUREAU_BB_DPD_RATIO_MEAN` = 3.21 (17.5x median), `BUREAU_ACTIVE_RATIO` = 0.78 (14.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 183989

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 15.91 (320.6x median), `EXT_SOURCE_1` = 1.51 (111.3x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CREDIT_TERM_MONTHS` = -1.40 (17.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 231193

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = -1.88 (140.3x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 4.63 (91.5x median), `PREV_APPROVAL_RATE` = -1.24 (62.0x median), `POS_SK_DPD_MEAN` = 10.14 (52.7x median), `BUREAU_BB_DPD_RATIO_MEAN` = 2.39 (13.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 167670

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 21.86 (440.0x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `EXT_SOURCE_3` = -2.20 (20.7x median), `PREV_APPROVAL_RATE` = 0.41 (19.4x median), `CREDIT_TERM_MONTHS` = 1.18 (16.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 348410

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 3.23 (65.9x median), `EXT_SOURCE_1` = 0.84 (61.2x median), `INST_DPD_MAX` = 5.94 (58.0x median), `CREDIT_TERM_MONTHS` = 1.96 (44.3x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 372296

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = 2.73 (201.9x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 7.99 (157.1x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `ANNUITY_TO_INCOME` = 1.94 (23.1x median), `CREDIT_TERM_MONTHS` = 1.68 (22.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 403090

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 9.18 (185.4x median), `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `AMT_ANNUITY` = -2.13 (24.4x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `AMT_CREDIT` = -2.12 (14.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 254749

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = 1.06 (78.1x median), `PREV_APPROVAL_RATE` = -0.92 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_COUNT` = 4.66 (26.9x median), `AMT_ANNUITY` = -1.78 (20.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 179653

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 11.07 (217.1x median), `EXT_SOURCE_1` = -1.25 (94.1x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `BUREAU_BB_DPD_RATIO_MEAN` = 5.47 (29.1x median), `AMT_ANNUITY` = -1.91 (21.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 419331

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 17.32 (348.8x median), `EXT_SOURCE_1` = -1.09 (82.0x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 3.56 (70.6x median), `EXT_SOURCE_2` = -2.46 (13.1x median), `EXT_SOURCE_3` = -1.23 (12.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 123743

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = -1.90 (142.3x median), `PREV_APPROVAL_RATE` = -1.40 (69.7x median), `AMT_ANNUITY` = -2.30 (26.2x median), `POS_SK_DPD_MEAN` = 4.49 (22.8x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 325071

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 8.51 (167.1x median), `BUREAU_BB_DPD_RATIO_MEAN` = 7.49 (39.5x median), `PREV_APPROVAL_RATE` = -0.41 (21.3x median), `POS_SK_DPD_MEAN` = 3.36 (16.8x median), `ANNUITY_TO_INCOME` = -1.28 (13.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 185771

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 3.79 (75.1x median), `CC_SK_DPD_MEAN` = 2.31 (47.5x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_BB_DPD_RATIO_MEAN` = 4.17 (22.5x median), `CREDIT_TERM_MONTHS` = 1.49 (20.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 434069

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 6.59 (133.4x median), `PREV_APPROVAL_RATE` = 0.55 (26.1x median), `CREDIT_TERM_MONTHS` = 1.67 (22.7x median), `EXT_SOURCE_3` = -1.62 (15.6x median), `EXT_SOURCE_2` = -2.07 (11.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 178803

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = -2.43 (181.1x median), `PREV_APPROVAL_RATE` = -1.32 (66.1x median), `POS_SK_DPD_MEAN` = 10.56 (54.9x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `EXT_SOURCE_3` = -2.58 (24.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 376791

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 10.80 (217.9x median), `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `ANNUITY_TO_INCOME` = 2.68 (31.4x median), `AMT_ANNUITY` = 2.43 (25.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 417879

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 6.09 (119.9x median), `PREV_APPROVAL_RATE` = -1.51 (75.5x median), `BUREAU_BB_DPD_RATIO_MEAN` = 7.10 (37.5x median), `BUREAU_ACTIVE_RATIO` = 1.14 (20.3x median), `CREDIT_TERM_MONTHS` = -1.52 (18.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 192536

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = -1.52 (113.6x median), `POS_SK_DPD_MEAN` = 12.45 (64.9x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `BUREAU_ACTIVE_RATIO` = 1.59 (27.9x median), `EXT_SOURCE_3` = -1.43 (13.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 319829

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `POS_SK_DPD_MEAN` = 11.16 (58.1x median), `EXT_SOURCE_1` = 0.44 (32.0x median), `INST_DPD_MEAN` = 79.81 (28.1x median), `EXT_SOURCE_3` = -2.00 (19.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 291162

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 17.04 (333.8x median), `PREV_APPROVAL_RATE` = -1.68 (83.6x median), `BUREAU_BB_DPD_RATIO_MEAN` = 12.95 (67.6x median), `POS_SK_DPD_MEAN` = 12.89 (67.3x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 282593

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = 1.77 (130.7x median), `YEARS_BIRTH` = 1.50 (47.2x median), `INST_SEVERE_LATE_RATIO` = 5.95 (36.3x median), `POS_MONTHS_COUNT` = -0.93 (25.9x median), `INST_DPD_MAX` = 2.03 (20.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 439221

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = -2.40 (179.2x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 6.61 (130.1x median), `POS_SK_DPD_MEAN` = 10.84 (56.4x median), `PREV_APPROVAL_RATE` = -0.36 (18.6x median), `BUREAU_BB_DPD_RATIO_MEAN` = 3.27 (17.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 168241

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 23.77 (124.9x median), `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `EXT_SOURCE_1` = -1.22 (91.8x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `INST_DPD_MEAN` = 82.97 (29.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 205128

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 6.20 (122.1x median), `EXT_SOURCE_1` = 1.53 (112.3x median), `YEARS_BIRTH` = 1.45 (45.9x median), `POS_MONTHS_COUNT` = -1.13 (31.3x median), `INST_SEVERE_LATE_RATIO` = 4.83 (29.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 418483

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `CC_SK_DPD_MEAN` = 3.38 (69.0x median), `BUREAU_BB_DPD_RATIO_MEAN` = 7.21 (38.1x median), `YEARS_BIRTH` = 1.30 (9.5x median), `CREDIT_TERM_MONTHS` = -0.78 (9.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 408687

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 16.49 (332.1x median), `EXT_SOURCE_1` = -2.78 (207.4x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_ANNUITY` = 1.49 (15.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 193960

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 6.96 (140.8x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `AMT_ANNUITY` = -1.93 (22.1x median), `BUREAU_COUNT` = 3.34 (19.6x median), `PREV_APPROVAL_RATE` = 0.41 (19.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 209687

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 5.49 (108.1x median), `CREDIT_TERM_MONTHS` = 1.44 (32.8x median), `EXT_SOURCE_1` = -0.36 (28.0x median), `BUREAU_BB_DPD_RATIO_MEAN` = 3.30 (17.9x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 152282

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 21.07 (424.1x median), `EXT_SOURCE_3` = -1.57 (15.1x median), `BUREAU_COUNT` = 2.24 (13.4x median), `PREV_APPROVAL_RATE` = 0.23 (10.3x median), `AMT_ANNUITY` = -0.84 (10.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 369466

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = 2.43 (179.8x median), `CC_SK_DPD_MEAN` = 8.47 (171.2x median), `PREV_APPROVAL_RATE` = -1.40 (69.7x median), `AMT_ANNUITY` = -1.90 (21.8x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 123275

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 10.29 (207.6x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `AMT_ANNUITY` = -1.87 (21.5x median), `ANNUITY_TO_INCOME` = -1.42 (15.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 280528

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 8.50 (171.7x median), `EXT_SOURCE_1` = 0.96 (70.5x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `POS_SK_DPD_MEAN` = 4.79 (24.4x median), `CREDIT_TERM_MONTHS` = 0.86 (12.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 224576

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 7.67 (155.0x median), `ANNUITY_TO_INCOME` = 5.57 (64.2x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CREDIT_TERM_MONTHS` = -1.43 (17.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 362359

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = 1.50 (110.4x median), `CC_SK_DPD_MEAN` = 2.60 (53.2x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = -1.39 (17.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 325624

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 7.31 (147.7x median), `EXT_SOURCE_1` = -1.80 (135.0x median), `BUREAU_BB_DPD_RATIO_MEAN` = 2.53 (14.0x median), `CREDIT_TERM_MONTHS` = -1.04 (12.6x median), `EXT_SOURCE_3` = -1.13 (11.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 177479

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = 2.32 (171.6x median), `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `CC_SK_DPD_MEAN` = 2.03 (41.8x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `CREDIT_TERM_MONTHS` = 0.88 (12.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 308748

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 3.94 (80.2x median), `INST_DPD_MAX` = 6.80 (66.3x median), `POS_MONTHS_COUNT` = 2.18 (57.2x median), `YEARS_BIRTH` = 1.42 (44.7x median), `CREDIT_TERM_MONTHS` = 1.38 (31.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 185006

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 12.43 (250.6x median), `EXT_SOURCE_1` = 1.32 (97.0x median), `ANNUITY_TO_INCOME` = 6.85 (78.7x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `CREDIT_TO_INCOME` = 4.70 (31.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 279807

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 6.77 (137.0x median), `EXT_SOURCE_1` = 0.85 (62.1x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `PREV_APPROVAL_RATE` = -0.36 (18.6x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 0.67 (14.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 301354

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 13.06 (263.3x median), `EXT_SOURCE_1` = 2.18 (160.6x median), `PREV_APPROVAL_RATE` = -1.24 (62.0x median), `ANNUITY_TO_INCOME` = 3.79 (44.0x median), `CREDIT_TO_INCOME` = 2.79 (19.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 402272

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 23.75 (478.0x median), `AMT_ANNUITY` = -1.31 (15.4x median), `ANNUITY_TO_INCOME` = -1.07 (11.1x median), `EXT_SOURCE_3` = -0.98 (9.8x median), `AMT_CREDIT` = -1.01 (7.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 284516

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 27.59 (539.8x median), `POS_SK_DPD_MEAN` = 14.92 (78.0x median), `BUREAU_BB_DPD_RATIO_MEAN` = 14.69 (76.6x median), `AMT_ANNUITY` = 1.45 (14.9x median), `ANNUITY_TO_INCOME` = 0.83 (10.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 449600

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 15.83 (318.9x median), `EXT_SOURCE_1` = -0.64 (48.3x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `POS_SK_DPD_MEAN` = 5.78 (29.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 310854

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = -1.24 (93.4x median), `POS_SK_DPD_MEAN` = 6.99 (36.0x median), `BUREAU_COUNT` = 4.44 (25.7x median), `CREDIT_TERM_MONTHS` = 1.69 (23.0x median), `EXT_SOURCE_3` = -1.11 (11.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 251695

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 19.59 (394.4x median), `CREDIT_TERM_MONTHS` = 2.08 (28.0x median), `PREV_APPROVAL_RATE` = -0.36 (18.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CREDIT_TO_INCOME` = 2.15 (15.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 435935

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 41.39 (809.3x median), `BUREAU_BB_DPD_RATIO_MEAN` = 21.30 (110.6x median), `POS_SK_DPD_MEAN` = 5.14 (26.3x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `EXT_SOURCE_3` = 1.66 (13.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 344478

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 10.86 (219.1x median), `EXT_SOURCE_1` = -1.30 (97.7x median), `CREDIT_TERM_MONTHS` = -1.63 (20.1x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `INST_DPD_MEAN` = 42.94 (14.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 221714

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 17.62 (354.9x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `ANNUITY_TO_INCOME` = 1.92 (22.8x median), `CREDIT_TO_INCOME` = 2.69 (18.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 124075

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = 2.17 (160.0x median), `PREV_APPROVAL_RATE` = -1.16 (58.1x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = 1.96 (26.5x median), `YEARS_EMPLOYED` = 5.13 (16.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 199469

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = -1.41 (105.4x median), `POS_SK_DPD_MEAN` = 16.53 (86.5x median), `PREV_APPROVAL_RATE` = -1.24 (62.0x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `AMT_ANNUITY` = -1.56 (18.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 239541

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 7.61 (153.8x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = 1.97 (26.7x median), `AMT_ANNUITY` = 1.30 (13.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 209404

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 7.85 (158.7x median), `EXT_SOURCE_1` = 1.58 (116.4x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `DEF_30_CNT_SOCIAL_CIRCLE_BIN` = 4.63 (14.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 117413

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 13.34 (268.9x median), `EXT_SOURCE_1` = -1.79 (133.9x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = 2.16 (29.0x median), `PREV_APPROVAL_RATE` = 0.60 (28.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 414694

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 18.18 (366.2x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `ANNUITY_TO_INCOME` = 1.42 (17.1x median), `YEARS_BIRTH` = 1.65 (12.4x median), `EXT_SOURCE_2` = -1.87 (10.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 305834

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 20.01 (403.0x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `CREDIT_TERM_MONTHS` = -1.57 (19.4x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (10.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 198210

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = 0.92 (67.0x median), `PREV_APPROVAL_RATE` = -1.16 (58.1x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 2.49 (49.7x median), `EXT_SOURCE_3` = -2.25 (21.2x median), `POS_SK_DPD_MEAN` = 3.75 (18.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 401228

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 16.05 (323.3x median), `AMT_ANNUITY` = -2.30 (26.2x median), `AMT_CREDIT` = -1.73 (12.2x median), `ANNUITY_TO_INCOME` = -1.13 (11.8x median), `CC_UTILIZATION_MAX` = 4.77 (11.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 104489

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = -2.85 (212.9x median), `POS_SK_DPD_MEAN` = 9.81 (51.0x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `ANNUITY_TO_INCOME` = -1.47 (15.6x median), `AMT_ANNUITY` = -1.04 (12.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 313089

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 33.36 (671.0x median), `EXT_SOURCE_1` = 2.40 (176.9x median), `PREV_APPROVAL_RATE` = 0.49 (23.2x median), `CREDIT_TERM_MONTHS` = -1.52 (18.7x median), `EXT_SOURCE_3` = -1.50 (14.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 435965

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = -1.97 (147.2x median), `POS_SK_DPD_MEAN` = 22.29 (117.0x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `INST_DPD_MEAN` = 64.57 (22.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 270264

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 17.50 (352.6x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_ANNUITY` = -3.04 (34.3x median), `AMT_CREDIT` = -3.26 (22.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 176579

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 16.99 (342.3x median), `AMT_INCOME_TOTAL` = 2.31 (11.8x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.83 (10.5x median), `ANNUITY_TO_INCOME` = -0.97 (10.0x median), `AMT_ANNUITY` = 0.96 (9.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 254446

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 12.46 (251.2x median), `EXT_SOURCE_1` = -2.37 (177.2x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = -1.08 (13.0x median), `YEARS_BIRTH` = -1.04 (9.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 403449

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 13.81 (72.1x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `AMT_ANNUITY` = -2.10 (24.0x median), `ANNUITY_TO_INCOME` = -1.48 (15.8x median), `AMT_CREDIT` = -1.97 (13.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 284925

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 7.63 (154.2x median), `EXT_SOURCE_1` = -0.85 (64.2x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `ANNUITY_TO_INCOME` = 2.02 (24.0x median), `AMT_ANNUITY` = 1.48 (15.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 145429

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 10.07 (203.2x median), `EXT_SOURCE_1` = -1.09 (81.8x median), `PREV_APPROVAL_RATE` = -1.36 (68.0x median), `BUREAU_COUNT` = 2.90 (17.1x median), `PREV_COUNT` = 5.25 (14.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 107241

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `EXT_SOURCE_2` = -2.71 (14.4x median), `EXT_SOURCE_3` = -1.48 (14.3x median), `INST_SEVERE_LATE_RATIO` = 50.85 (13.1x median), `ANNUITY_TO_INCOME` = 0.92 (11.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 319263

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 19.10 (374.0x median), `BUREAU_BB_DPD_RATIO_MEAN` = 14.73 (76.8x median), `POS_SK_DPD_MEAN` = 8.38 (43.4x median), `PREV_APPROVAL_RATE` = -0.45 (23.2x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 318123

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe B (Rare but Valid) |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `ANNUITY_TO_INCOME` = 2.50 (29.4x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 1.27 (25.8x median), `AMT_ANNUITY` = 1.24 (12.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## SK_ID_CURR 266826

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 21.04 (423.7x median), `CREDIT_TERM_MONTHS` = -1.48 (18.2x median), `PREV_APPROVAL_RATE` = -0.27 (14.5x median), `BUREAU_ACTIVE_RATIO` = 0.78 (14.2x median), `EXT_SOURCE_1` = 0.14 (9.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 169516

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -1.87 (92.9x median), `POS_SK_DPD_MEAN` = 6.15 (31.6x median), `PREV_REFUSED_COUNT` = 8.46 (19.6x median), `BUREAU_ACTIVE_RATIO` = 0.69 (12.7x median), `PREV_COUNT` = 3.84 (10.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 359287

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 17.44 (351.4x median), `EXT_SOURCE_1` = -1.93 (144.3x median), `PREV_APPROVAL_RATE` = -1.79 (89.1x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 2.71 (53.9x median), `PREV_COUNT` = 8.78 (23.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 253643

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 15.19 (297.5x median), `PREV_APPROVAL_RATE` = -1.51 (75.5x median), `POS_SK_DPD_MEAN` = 8.90 (46.2x median), `EXT_SOURCE_1` = -0.57 (43.0x median), `BUREAU_BB_DPD_RATIO_MEAN` = 7.07 (37.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 400250

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 2.76 (56.4x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (10.1x median), `CC_MONTHS_COUNT` = 3.41 (8.8x median), `PREV_APPROVAL_RATE` = -0.14 (7.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 287668

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `POS_SK_DPD_MEAN` = 15.23 (79.7x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `YEARS_BIRTH` = 1.50 (11.1x median), `ANNUITY_TO_INCOME` = -1.06 (11.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 106799

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 14.38 (289.8x median), `PREV_APPROVAL_RATE` = -0.87 (43.9x median), `CREDIT_TERM_MONTHS` = 1.67 (22.7x median), `EXT_SOURCE_3` = -1.43 (13.8x median), `BUREAU_ACTIVE_RATIO` = -0.79 (12.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 204472

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 9.53 (187.0x median), `EXT_SOURCE_1` = -1.53 (114.8x median), `POS_SK_DPD_MEAN` = 6.20 (31.8x median), `BUREAU_BB_DPD_RATIO_MEAN` = 5.30 (28.3x median), `CC_AMT_BALANCE_MEAN` = 4.52 (15.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 127540

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | Tipe B (Rare but Valid) |
| Top Deviating Features | `EXT_SOURCE_1` = -0.66 (49.7x median), `AMT_CREDIT` = -1.35 (35.5x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `INST_LATE_RATIO` = 5.05 (32.2x median), `BUREAU_BB_DPD_RATIO_MEAN` = 5.85 (31.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## SK_ID_CURR 115608

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -1.40 (69.7x median), `ANNUITY_TO_INCOME` = 5.97 (68.7x median), `CREDIT_TO_INCOME` = 9.72 (64.1x median), `CREDIT_TERM_MONTHS` = 2.37 (31.9x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 271183

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 18.19 (366.4x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `EXT_SOURCE_3` = 2.11 (18.0x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 321755

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 8.30 (167.8x median), `EXT_SOURCE_1` = 2.09 (154.3x median), `AMT_ANNUITY` = -2.95 (33.3x median), `AMT_CREDIT` = -3.26 (22.2x median), `CREDIT_TERM_MONTHS` = -1.48 (18.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 122413

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 10.92 (214.2x median), `BUREAU_BB_DPD_RATIO_MEAN` = 7.00 (37.0x median), `INST_DPD_MAX` = 2.68 (26.8x median), `POS_MONTHS_COUNT` = 0.68 (17.3x median), `OWN_CAR_AGE` = 6.79 (15.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 447996

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 4.79 (97.2x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `ANNUITY_TO_INCOME` = 1.23 (15.0x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (10.1x median), `AMT_ANNUITY` = 0.96 (9.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 361925

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 5.03 (101.9x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `BUREAU_ACTIVE_RATIO` = 1.41 (24.8x median), `AMT_ANNUITY` = 1.51 (15.6x median), `EXT_SOURCE_3` = -1.59 (15.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 365889

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe B (Rare but Valid) |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `POS_SK_DPD_MEAN` = 5.26 (26.8x median), `AMT_ANNUITY` = 1.97 (20.5x median), `PREV_APPROVAL_RATE` = 0.41 (19.4x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## SK_ID_CURR 137848

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 9.75 (196.9x median), `EXT_SOURCE_1` = 1.44 (105.9x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `CC_MONTHS_COUNT` = 3.45 (8.9x median), `ORGANIZATION_TYPE_FREQ` = 1.37 (8.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 199158

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 14.92 (300.6x median), `PREV_APPROVAL_RATE` = -1.24 (62.0x median), `EXT_SOURCE_1` = 0.67 (48.5x median), `CREDIT_TERM_MONTHS` = -1.48 (18.2x median), `AMT_ANNUITY` = 1.52 (15.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 366356

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 24.51 (479.6x median), `EXT_SOURCE_1` = -2.55 (190.3x median), `BUREAU_BB_DPD_RATIO_MEAN` = 13.70 (71.4x median), `POS_SK_DPD_MEAN` = 8.12 (42.0x median), `EXT_SOURCE_3` = -2.51 (23.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 216856

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 9.26 (187.0x median), `CREDIT_TERM_MONTHS` = 1.68 (22.8x median), `PREV_APPROVAL_RATE` = 0.41 (19.4x median), `BUREAU_COUNT` = 2.46 (14.7x median), `CREDIT_TO_INCOME` = 2.04 (14.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 435757

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 14.74 (288.8x median), `POS_SK_DPD_MEAN` = 9.21 (47.8x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_BB_DPD_RATIO_MEAN` = 7.79 (41.1x median), `CREDIT_TERM_MONTHS` = 1.67 (22.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 143904

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 14.11 (284.3x median), `EXT_SOURCE_1` = 1.25 (91.7x median), `CREDIT_TERM_MONTHS` = 1.67 (22.7x median), `BUREAU_ACTIVE_RATIO` = 0.69 (12.7x median), `CREDIT_TO_INCOME` = 1.32 (9.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 353146

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 8.00 (161.6x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `YEARS_EMPLOYED` = 6.20 (19.7x median), `BUREAU_DAYS_CREDIT_MEAN` = -2.40 (14.1x median), `YEARS_BIRTH` = 1.61 (12.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 395418

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 9.27 (187.1x median), `PREV_APPROVAL_RATE` = -1.60 (80.0x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `EXT_SOURCE_3` = -1.80 (17.1x median), `PREV_REFUSED_COUNT` = 6.23 (14.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 304685

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 6.42 (129.9x median), `EXT_SOURCE_1` = 1.04 (76.2x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `CREDIT_TERM_MONTHS` = 1.70 (23.0x median), `BUREAU_COUNT` = 3.56 (20.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 356283

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 25.33 (509.8x median), `EXT_SOURCE_1` = 2.16 (159.4x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `ANNUITY_TO_INCOME` = -1.29 (13.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 427888

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = -2.27 (169.4x median), `PREV_APPROVAL_RATE` = -0.81 (41.1x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `ANNUITY_TO_INCOME` = 0.94 (11.7x median), `YEARS_BIRTH` = -1.22 (10.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 399100

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 9.01 (181.9x median), `EXT_SOURCE_1` = 1.89 (139.2x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `CREDIT_TERM_MONTHS` = -1.40 (17.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 165550

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 10.11 (204.0x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_ACTIVE_RATIO` = 1.41 (24.8x median), `CREDIT_TERM_MONTHS` = -1.45 (17.9x median), `YEARS_BIRTH` = 1.75 (13.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 402917

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | Tipe B (Rare but Valid) |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 4.74 (29.1x median), `BUREAU_ACTIVE_RATIO` = 1.51 (26.6x median), `EXT_SOURCE_2` = -1.78 (23.1x median), `BUREAU_BB_DPD_RATIO_MEAN` = 4.22 (22.7x median), `EXT_SOURCE_3` = -1.64 (15.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## SK_ID_CURR 286411

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 41.74 (839.3x median), `EXT_SOURCE_1` = 1.63 (119.9x median), `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `CREDIT_TERM_MONTHS` = 1.28 (17.7x median), `BUREAU_COUNT` = 2.68 (15.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 373146

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 8.93 (180.5x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_ACTIVE_RATIO` = 0.83 (15.0x median), `EXT_SOURCE_3` = -1.53 (14.7x median), `ANNUITY_TO_INCOME` = 0.93 (11.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 367868

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `POS_MONTHS_COUNT` = 3.39 (89.6x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_BB_DPD_RATIO_MEAN` = 5.88 (31.3x median), `CREDIT_TERM_MONTHS` = -1.20 (25.4x median), `YEARS_BIRTH` = -0.81 (24.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 225112

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 3.17 (64.7x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `AMT_ANNUITY` = -0.86 (10.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 371362

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 8.26 (166.8x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `CREDIT_TERM_MONTHS` = 1.70 (23.0x median), `BUREAU_COUNT` = 2.46 (14.7x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 166780

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `INST_DPD_MAX` = 5.95 (58.1x median), `POS_MONTHS_COUNT` = 1.89 (49.7x median), `CREDIT_TERM_MONTHS` = 1.96 (44.3x median), `BUREAU_DAYS_CREDIT_MEAN` = -3.04 (40.9x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 291656

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe B (Rare but Valid) |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `CC_AMT_BALANCE_MEAN` = 8.11 (27.4x median), `POS_SK_DPD_MEAN` = 5.18 (26.4x median), `BUREAU_ACTIVE_RATIO` = 1.41 (24.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## SK_ID_CURR 420319

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 9.78 (197.5x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `CREDIT_TERM_MONTHS` = 1.67 (22.8x median), `CREDIT_TO_INCOME` = 2.51 (17.3x median), `ANNUITY_TO_INCOME` = 1.33 (16.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 284341

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = 2.05 (151.0x median), `POS_SK_DPD_MEAN` = 3.94 (19.9x median), `CC_AMT_BALANCE_MEAN` = 4.87 (16.8x median), `ANNUITY_TO_INCOME` = -1.34 (14.2x median), `PREV_APPROVAL_RATE` = 0.30 (13.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 253092

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 12.42 (64.8x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `PREV_APPROVAL_RATE` = -0.36 (18.6x median), `AMT_ANNUITY` = 1.76 (18.3x median), `CREDIT_TERM_MONTHS` = 0.77 (11.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 100213

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 9.45 (185.5x median), `POS_SK_DPD_MEAN` = 15.15 (79.2x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_BB_DPD_RATIO_MEAN` = 8.06 (42.5x median), `ANNUITY_TO_INCOME` = 2.34 (27.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 291719

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 12.06 (243.1x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (10.1x median), `CC_MONTHS_COUNT` = 3.41 (8.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 411454

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = 2.32 (171.2x median), `YEARS_BIRTH` = 1.40 (44.3x median), `CREDIT_TERM_MONTHS` = 1.68 (38.1x median), `INST_SEVERE_LATE_RATIO` = 3.89 (24.1x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (21.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 422778

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 5.67 (114.9x median), `EXT_SOURCE_1` = -0.82 (62.1x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `CREDIT_TERM_MONTHS` = 1.51 (20.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 265740

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 23.04 (463.7x median), `EXT_SOURCE_1` = -0.97 (72.8x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `EXT_SOURCE_3` = 1.78 (15.0x median), `CREDIT_TERM_MONTHS` = -0.94 (11.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 152473

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `POS_SK_DPD_MEAN` = 9.58 (49.7x median), `CREDIT_TERM_MONTHS` = -1.46 (17.9x median), `EXT_SOURCE_2` = -2.17 (11.7x median), `AMT_CREDIT` = -1.62 (11.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 356195

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -2.12 (105.3x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `POS_SK_DPD_MEAN` = 6.43 (33.0x median), `EXT_SOURCE_3` = -1.28 (12.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 357463

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 4.20 (85.3x median), `EXT_SOURCE_1` = 0.83 (60.7x median), `CREDIT_TERM_MONTHS` = 1.27 (17.5x median), `ANNUITY_TO_INCOME` = 1.34 (16.2x median), `CREDIT_TO_INCOME` = 2.15 (15.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 389585

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 9.07 (183.2x median), `PREV_APPROVAL_RATE` = -0.96 (48.4x median), `AMT_ANNUITY` = -2.34 (26.6x median), `ANNUITY_TO_INCOME` = -1.73 (18.6x median), `YEARS_BIRTH` = 1.75 (13.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 410732

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | Tipe B (Rare but Valid) |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `INST_LATE_RATIO` = 4.30 (27.6x median), `BUREAU_BB_DPD_RATIO_MEAN` = 4.88 (26.1x median), `AMT_CREDIT` = 0.82 (23.1x median), `INST_SEVERE_LATE_RATIO` = 3.12 (19.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## SK_ID_CURR 351653

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 8.64 (174.6x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `CREDIT_TERM_MONTHS` = 1.26 (17.4x median), `ANNUITY_TO_INCOME` = 1.16 (14.2x median), `CREDIT_TO_INCOME` = 1.95 (13.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 282462

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 13.06 (263.3x median), `AMT_ANNUITY` = 2.06 (21.5x median), `AMT_CREDIT` = 1.89 (11.3x median), `EXT_SOURCE_3` = 1.24 (10.1x median), `AMT_INCOME_TOTAL` = 1.84 (9.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 296812

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 21.19 (426.6x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = 1.26 (17.4x median), `BUREAU_ACTIVE_RATIO` = 0.78 (14.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 107067

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 8.78 (177.3x median), `PREV_APPROVAL_RATE` = -1.24 (62.0x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `EXT_SOURCE_3` = -2.04 (19.4x median), `BUREAU_ACTIVE_RATIO` = 0.73 (13.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 371678

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 7.54 (152.3x median), `EXT_SOURCE_1` = -1.55 (116.2x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `ANNUITY_TO_INCOME` = 1.76 (21.0x median), `BUREAU_ACTIVE_RATIO` = -0.71 (11.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 347587

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | Tipe C (Risk Signal) |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `POS_MONTHS_COUNT` = 1.17 (30.2x median), `CREDIT_TERM_MONTHS` = 1.32 (30.2x median), `AMT_INCOME_TOTAL` = -2.51 (24.0x median), `CREDIT_TO_INCOME` = 4.65 (21.0x median) |
| Justifikasi | Kombinasi finansial kontradiktif (mis. rasio cicilan/pendapatan ekstrem, income rendah + credit besar, atau skor eksternal tinggi di cluster bermasalah). |
| Business Impact | Underwriting: matikan auto-approve, wajibkan manual review oleh underwriter senior + verifikasi pendapatan fisik. |

---

## SK_ID_CURR 326964

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 9.47 (191.1x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `YEARS_EMPLOYED` = 4.01 (13.1x median), `BUREAU_COUNT` = 2.02 (12.2x median), `CREDIT_TERM_MONTHS` = 0.85 (12.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 331349

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 6.14 (124.4x median), `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `BUREAU_ACTIVE_RATIO` = 1.18 (20.9x median), `EXT_SOURCE_3` = -1.83 (17.5x median), `CREDIT_TERM_MONTHS` = 1.26 (17.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 132466

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 14.55 (293.3x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `AMT_ANNUITY` = -1.72 (19.9x median), `PREV_APPROVAL_RATE` = 0.41 (19.4x median), `CC_MONTHS_COUNT` = 3.37 (8.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 426013

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 6.18 (125.1x median), `EXT_SOURCE_1` = 1.70 (125.0x median), `PREV_APPROVAL_RATE` = 0.63 (30.2x median), `BUREAU_ACTIVE_RATIO` = -0.58 (8.9x median), `CREDIT_TERM_MONTHS` = 0.60 (8.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 242116

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -1.24 (62.0x median), `EXT_SOURCE_1` = 0.45 (32.7x median), `CREDIT_TERM_MONTHS` = 1.25 (17.3x median), `OWN_CAR_AGE` = 6.68 (15.7x median), `POS_SK_DPD_MEAN` = 2.79 (13.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 422193

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 9.71 (190.6x median), `PREV_APPROVAL_RATE` = -1.02 (51.1x median), `BUREAU_BB_DPD_RATIO_MEAN` = 5.41 (28.8x median), `CREDIT_TERM_MONTHS` = 1.97 (26.7x median), `CREDIT_TO_INCOME` = 2.94 (20.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 376608

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 19.42 (391.1x median), `CREDIT_TERM_MONTHS` = 1.96 (26.5x median), `PREV_APPROVAL_RATE` = -0.50 (25.8x median), `EXT_SOURCE_3` = 1.30 (10.7x median), `AMT_ANNUITY` = 1.04 (10.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 291361

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 11.92 (240.5x median), `EXT_SOURCE_1` = -0.78 (58.6x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 256226

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `POS_MONTHS_COUNT` = 2.78 (73.4x median), `CREDIT_TERM_MONTHS` = 1.78 (40.4x median), `YEARS_BIRTH` = 1.20 (38.1x median), `AMT_INCOME_TOTAL` = -2.31 (22.2x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (21.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 450171

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 17.24 (347.2x median), `EXT_SOURCE_1` = -2.12 (158.7x median), `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `CC_MONTHS_COUNT` = 3.45 (8.9x median), `YEARS_BIRTH` = 1.15 (8.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 386639

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = 1.66 (121.9x median), `POS_SK_DPD_MEAN` = 16.45 (86.1x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `EXT_SOURCE_3` = -1.82 (17.4x median), `AMT_ANNUITY` = 1.35 (13.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 214375

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 13.09 (68.3x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `EXT_SOURCE_3` = -2.03 (19.3x median), `PREV_APPROVAL_RATE` = -0.36 (18.6x median), `CREDIT_TERM_MONTHS` = -1.10 (13.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 450665

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -1.51 (75.5x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 2.62 (52.2x median), `POS_SK_DPD_MEAN` = 5.85 (30.0x median), `CREDIT_TERM_MONTHS` = 1.67 (22.8x median), `EXT_SOURCE_3` = -1.44 (14.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 412275

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 19.86 (104.2x median), `PREV_APPROVAL_RATE` = -1.02 (51.1x median), `EXT_SOURCE_1` = -0.34 (25.9x median), `EXT_SOURCE_3` = -2.17 (20.5x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.81 (10.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 182654

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 12.72 (249.4x median), `BUREAU_BB_DPD_RATIO_MEAN` = 11.22 (58.7x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `POS_MONTHS_COUNT` = 1.25 (32.4x median), `INST_DPD_MAX` = 2.63 (26.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 411819

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `POS_SK_DPD_MEAN` = 18.06 (94.7x median), `EXT_SOURCE_1` = -0.42 (32.4x median), `INST_DPD_MEAN` = 63.64 (22.2x median), `CREDIT_TERM_MONTHS` = -1.45 (17.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 156323

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = 1.59 (117.1x median), `YEARS_BIRTH` = -1.20 (36.0x median), `INST_SEVERE_LATE_RATIO` = 4.04 (25.0x median), `BUREAU_ACTIVE_RATIO` = 1.14 (20.3x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 2.43 (18.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 254747

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 6.11 (123.7x median), `EXT_SOURCE_1` = -1.09 (82.0x median), `PREV_APPROVAL_RATE` = -1.02 (51.1x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_COUNT` = 5.10 (29.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 108903

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 11.88 (239.6x median), `EXT_SOURCE_1` = 2.22 (163.7x median), `PREV_APPROVAL_RATE` = -1.40 (69.7x median), `CREDIT_TERM_MONTHS` = 2.17 (29.2x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 296918

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -1.51 (75.5x median), `POS_SK_DPD_MEAN` = 8.53 (44.2x median), `BUREAU_ACTIVE_RATIO` = 1.18 (20.9x median), `CREDIT_TERM_MONTHS` = -1.08 (13.1x median), `ANNUITY_TO_INCOME` = -0.94 (9.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 231799

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe B (Rare but Valid) |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = 1.67 (22.8x median), `POS_SK_DPD_MEAN` = 4.10 (20.7x median), `CC_AMT_BALANCE_MEAN` = 5.02 (17.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## SK_ID_CURR 290736

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 5.27 (103.9x median), `PREV_APPROVAL_RATE` = -1.68 (83.6x median), `POS_SK_DPD_MEAN` = 14.75 (77.1x median), `BUREAU_BB_DPD_RATIO_MEAN` = 3.36 (18.3x median), `EXT_SOURCE_3` = -1.57 (15.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 292180

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 15.18 (297.4x median), `BUREAU_BB_DPD_RATIO_MEAN` = 9.16 (48.1x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `POS_SK_DPD_MEAN` = 6.77 (34.8x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 292969

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 22.49 (118.1x median), `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `ANNUITY_TO_INCOME` = 7.43 (85.3x median), `AMT_ANNUITY` = 3.00 (31.9x median), `CREDIT_TO_INCOME` = 3.43 (23.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 356724

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `POS_MONTHS_COUNT` = 2.98 (78.8x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.68 (19.2x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `EXT_SOURCE_3` = -1.78 (16.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 431239

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | Tipe B (Rare but Valid) |
| Top Deviating Features | `POS_MONTHS_COUNT` = 1.77 (46.4x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `EXT_SOURCE_1` = 0.41 (29.2x median), `CREDIT_TERM_MONTHS` = -1.07 (22.7x median), `INST_DPD_MAX` = 2.07 (20.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## SK_ID_CURR 195505

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | Tipe B (Rare but Valid) |
| Top Deviating Features | `EXT_SOURCE_1` = 0.47 (33.7x median), `EXT_SOURCE_3` = -2.34 (22.0x median), `YEARS_BIRTH` = -0.64 (18.7x median), `INST_SEVERE_LATE_RATIO` = 2.82 (17.8x median), `POS_MONTHS_COUNT` = 0.68 (17.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## SK_ID_CURR 424314

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 19.46 (391.9x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `EXT_SOURCE_1` = 0.33 (23.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CREDIT_TERM_MONTHS` = 1.26 (17.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 450132

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 8.27 (167.0x median), `EXT_SOURCE_1` = -0.28 (21.4x median), `OWN_CAR_AGE` = 6.68 (15.7x median), `CREDIT_TERM_MONTHS` = 0.91 (12.9x median), `CC_MONTHS_COUNT` = 2.72 (7.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 225340

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 23.40 (122.9x median), `INST_DPD_MEAN` = 161.23 (57.7x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `CREDIT_TERM_MONTHS` = -1.50 (18.5x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 234533

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 17.68 (356.0x median), `EXT_SOURCE_1` = -2.74 (204.9x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `EXT_SOURCE_3` = -2.11 (20.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 449307

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 16.71 (327.3x median), `BUREAU_BB_DPD_RATIO_MEAN` = 7.79 (41.1x median), `POS_MONTHS_COUNT` = 1.57 (41.0x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 334205

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 11.82 (238.5x median), `EXT_SOURCE_1` = 0.89 (65.3x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `ANNUITY_TO_INCOME` = 1.12 (13.7x median), `CREDIT_TERM_MONTHS` = -1.08 (13.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 412526

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = 2.60 (192.3x median), `PREV_APPROVAL_RATE` = -1.51 (75.5x median), `POS_SK_DPD_MEAN` = 8.82 (45.7x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_COUNT` = 2.46 (14.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 122415

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 25.47 (512.5x median), `EXT_SOURCE_1` = -2.61 (194.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `AMT_ANNUITY` = -1.51 (17.5x median), `PREV_APPROVAL_RATE` = 0.30 (13.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 261692

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | Tipe B (Rare but Valid) |
| Top Deviating Features | `AMT_CREDIT` = -1.50 (39.3x median), `AMT_ANNUITY` = -1.93 (33.4x median), `BUREAU_ACTIVE_RATIO` = 1.51 (26.6x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.54 (11.5x median), `PREV_REFUSED_COUNT` = 7.90 (11.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## SK_ID_CURR 324234

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -1.58 (78.6x median), `POS_SK_DPD_MEAN` = 10.11 (52.6x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = 2.16 (29.1x median), `CREDIT_TO_INCOME` = 3.39 (23.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 104235

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 12.94 (260.9x median), `EXT_SOURCE_1` = 2.51 (185.7x median), `PREV_APPROVAL_RATE` = 0.49 (23.2x median), `BUREAU_COUNT` = 3.78 (22.0x median), `AMT_ANNUITY` = 1.88 (19.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 280523

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | Tipe B (Rare but Valid) |
| Top Deviating Features | `POS_MONTHS_COUNT` = 1.45 (37.8x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `CREDIT_TERM_MONTHS` = 1.28 (29.4x median), `OWN_CAR_AGE` = 6.68 (15.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## SK_ID_CURR 413132

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | Tipe B (Rare but Valid) |
| Top Deviating Features | `YEARS_BIRTH` = 1.35 (42.8x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `POS_MONTHS_COUNT` = -0.73 (20.5x median), `CREDIT_TERM_MONTHS` = 0.86 (20.0x median), `INST_SEVERE_LATE_RATIO` = 2.63 (16.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## SK_ID_CURR 237453

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 4.15 (84.4x median), `PREV_APPROVAL_RATE` = -1.02 (51.1x median), `AMT_ANNUITY` = -1.70 (19.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DAYS_CREDIT_MEAN` = -2.67 (15.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 237966

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 12.52 (252.4x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `YEARS_BIRTH` = 1.21 (8.8x median), `INST_DPD_MEAN` = 23.54 (7.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 321888

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = -2.36 (176.6x median), `INST_SEVERE_LATE_RATIO` = 8.24 (49.9x median), `AMT_CREDIT` = 0.70 (20.0x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `INST_DPD_MEAN` = 1.06 (12.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 358923

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 47.13 (921.2x median), `BUREAU_BB_DPD_RATIO_MEAN` = 25.25 (130.9x median), `POS_SK_DPD_MEAN` = 5.81 (29.8x median), `PREV_APPROVAL_RATE` = -0.45 (23.2x median), `CREDIT_TERM_MONTHS` = -1.51 (18.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 259353

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 16.16 (325.6x median), `PREV_APPROVAL_RATE` = -1.32 (66.1x median), `AMT_ANNUITY` = -1.27 (15.0x median), `BUREAU_ACTIVE_RATIO` = -0.88 (13.9x median), `BUREAU_COUNT` = 2.02 (12.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 334187

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 7.14 (144.4x median), `ANNUITY_TO_INCOME` = 3.27 (38.0x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CREDIT_TO_INCOME` = 2.39 (16.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 177797

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 27.47 (552.8x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `ANNUITY_TO_INCOME` = 1.51 (18.1x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `AMT_ANNUITY` = 1.11 (11.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 225367

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 20.15 (105.7x median), `EXT_SOURCE_1` = -1.41 (105.7x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `ANNUITY_TO_INCOME` = 1.37 (16.5x median), `EXT_SOURCE_3` = 1.48 (12.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 167948

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = 0.71 (51.6x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `POS_SK_DPD_MEAN` = 6.06 (31.1x median), `AMT_ANNUITY` = -2.30 (26.2x median), `ANNUITY_TO_INCOME` = -1.39 (14.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 218946

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `CC_SK_DPD_MEAN` = 2.06 (42.3x median), `AMT_ANNUITY` = -2.03 (23.3x median), `CREDIT_TERM_MONTHS` = 1.36 (18.7x median), `BUREAU_COUNT` = 1.80 (11.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 228944

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 14.93 (78.1x median), `PREV_APPROVAL_RATE` = -1.40 (69.7x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `EXT_SOURCE_3` = -1.85 (17.7x median), `AMT_ANNUITY` = -1.20 (14.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 195457

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 9.46 (191.1x median), `EXT_SOURCE_1` = 1.05 (76.8x median), `PREV_APPROVAL_RATE` = -1.31 (65.3x median), `CREDIT_TERM_MONTHS` = 1.43 (19.6x median), `BUREAU_COUNT` = 3.12 (18.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 453803

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 11.76 (230.6x median), `BUREAU_BB_DPD_RATIO_MEAN` = 5.98 (31.7x median), `AMT_ANNUITY` = 2.55 (26.9x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CREDIT_TERM_MONTHS` = -1.35 (16.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 110402

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 17.67 (355.9x median), `CREDIT_TERM_MONTHS` = -1.42 (30.4x median), `OWN_CAR_AGE` = 6.68 (15.7x median), `AMT_ANNUITY` = -2.06 (15.6x median), `INST_SEVERE_LATE_RATIO` = 2.42 (15.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 112061

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 13.62 (274.5x median), `EXT_SOURCE_1` = 2.11 (155.9x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `CREDIT_TERM_MONTHS` = 1.70 (23.0x median), `CREDIT_TO_INCOME` = 2.18 (15.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 203139

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = -2.49 (185.6x median), `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `POS_SK_DPD_MEAN` = 13.81 (72.1x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `INST_DPD_MEAN` = 40.72 (13.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 395055

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 10.53 (206.7x median), `BUREAU_BB_DPD_RATIO_MEAN` = 18.19 (94.5x median), `POS_SK_DPD_MEAN` = 10.50 (54.6x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `YEARS_BIRTH` = 1.56 (11.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 136525

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 2.76 (56.4x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (10.1x median), `CC_MONTHS_COUNT` = 3.41 (8.8x median), `CREDIT_TERM_MONTHS` = 0.54 (8.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 394566

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 13.83 (278.9x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `CREDIT_TERM_MONTHS` = 1.67 (22.8x median), `CREDIT_TO_INCOME` = 2.59 (17.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 284052

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `POS_SK_DPD_MEAN` = 7.42 (38.3x median), `EXT_SOURCE_1` = -0.39 (30.0x median), `CREDIT_TERM_MONTHS` = 1.67 (22.8x median), `CREDIT_TO_INCOME` = 2.76 (18.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 150958

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 9.02 (182.1x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `CREDIT_TERM_MONTHS` = 1.96 (26.5x median), `AMT_ANNUITY` = 1.15 (11.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 217805

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -1.51 (75.5x median), `POS_SK_DPD_MEAN` = 6.01 (30.9x median), `CREDIT_TERM_MONTHS` = 2.15 (29.0x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `DEF_30_CNT_SOCIAL_CIRCLE_BIN` = 4.63 (14.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 330023

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 10.61 (214.0x median), `PREV_APPROVAL_RATE` = 0.41 (19.4x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `AMT_ANNUITY` = -1.51 (17.6x median), `POS_SK_DPD_MEAN` = 2.46 (12.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 117570

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 10.83 (218.5x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `CREDIT_TERM_MONTHS` = 1.27 (17.5x median), `AMT_ANNUITY` = 1.22 (12.4x median), `AMT_INCOME_TOTAL` = 1.84 (9.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 273630

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = 1.37 (101.0x median), `PREV_APPROVAL_RATE` = -1.87 (92.9x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `POS_SK_DPD_MEAN` = 4.86 (24.7x median), `AMT_ANNUITY` = 1.93 (20.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 248989

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -1.02 (51.1x median), `POS_SK_DPD_MEAN` = 7.82 (40.4x median), `CREDIT_TERM_MONTHS` = 1.70 (23.0x median), `AMT_ANNUITY` = 0.86 (8.4x median), `AMT_CREDIT` = 1.44 (8.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 235746

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 3.07 (62.6x median), `PREV_APPROVAL_RATE` = -1.24 (62.0x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_1` = -0.27 (21.1x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 440789

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 5.24 (103.4x median), `EXT_SOURCE_1` = -1.06 (79.7x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `INST_SEVERE_LATE_RATIO` = 5.63 (34.4x median), `EXT_SOURCE_2` = -2.69 (34.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 199204

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 5.01 (101.6x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_ANNUITY` = 1.63 (16.9x median), `ANNUITY_TO_INCOME` = 0.82 (10.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 108900

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = 1.39 (102.0x median), `CREDIT_TERM_MONTHS` = 2.39 (53.7x median), `INST_SEVERE_LATE_RATIO` = 8.05 (48.8x median), `POS_MONTHS_COUNT` = 1.57 (41.0x median), `YEARS_BIRTH` = 1.17 (37.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 283004

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe B (Rare but Valid) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 2.48 (49.4x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_BB_DPD_RATIO_MEAN` = 6.44 (34.1x median), `ANNUITY_TO_INCOME` = 2.15 (25.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## SK_ID_CURR 371385

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 9.98 (201.5x median), `EXT_SOURCE_1` = -1.80 (134.3x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `AMT_ANNUITY` = -1.68 (19.4x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 208006

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 18.92 (380.9x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `POS_SK_DPD_MEAN` = 5.57 (28.5x median), `CREDIT_TERM_MONTHS` = 1.67 (22.7x median), `EXT_SOURCE_3` = 1.34 (11.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 104226

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 24.14 (485.8x median), `PREV_APPROVAL_RATE` = -1.40 (69.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DAYS_CREDIT_MEAN` = -2.75 (16.2x median), `ANNUITY_TO_INCOME` = 1.27 (15.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 172911

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe B (Rare but Valid) |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 9.38 (48.7x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CREDIT_TERM_MONTHS` = -0.94 (11.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## SK_ID_CURR 402036

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = 2.54 (187.9x median), `CC_SK_DPD_MEAN` = 6.67 (134.9x median), `AMT_ANNUITY` = -1.85 (21.3x median), `AMT_CREDIT` = -1.89 (13.3x median), `BUREAU_COUNT` = 2.02 (12.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 381225

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 9.75 (196.9x median), `EXT_SOURCE_1` = 2.32 (171.6x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `ANNUITY_TO_INCOME` = 2.71 (31.7x median), `BUREAU_COUNT` = 3.12 (18.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 186519

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | Tipe B (Rare but Valid) |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `CREDIT_TERM_MONTHS` = -1.08 (22.9x median), `OWN_CAR_AGE` = 6.79 (15.9x median), `AMT_INCOME_TOTAL` = 1.70 (14.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## SK_ID_CURR 270151

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = 2.56 (188.8x median), `POS_SK_DPD_MEAN` = 5.60 (28.7x median), `PREV_APPROVAL_RATE` = -0.45 (23.2x median), `CREDIT_TERM_MONTHS` = 1.26 (17.4x median), `YEARS_EMPLOYED` = 4.70 (15.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 238787

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 12.57 (253.5x median), `EXT_SOURCE_1` = -2.57 (191.6x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `AMT_ANNUITY` = 1.37 (14.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 108987

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 4.12 (83.7x median), `EXT_SOURCE_1` = -0.42 (31.9x median), `PREV_APPROVAL_RATE` = 0.55 (26.1x median), `AMT_ANNUITY` = -1.40 (16.3x median), `BUREAU_COUNT` = 2.24 (13.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 328061

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 3.16 (64.5x median), `INST_SEVERE_LATE_RATIO` = 4.43 (27.3x median), `YEARS_BIRTH` = -1.06 (14.5x median), `INST_DPD_MAX` = 1.64 (11.2x median), `AMT_INCOME_TOTAL` = -1.06 (10.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 349145

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 27.02 (543.8x median), `EXT_SOURCE_1` = 1.54 (113.2x median), `PREV_APPROVAL_RATE` = -1.02 (51.1x median), `ANNUITY_TO_INCOME` = 1.79 (21.3x median), `CREDIT_TO_INCOME` = 1.31 (9.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 122603

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 11.34 (59.1x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `CREDIT_TERM_MONTHS` = -1.62 (20.0x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CC_AMT_BALANCE_MEAN` = 3.40 (12.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 247700

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = 2.75 (202.9x median), `CC_SK_DPD_MEAN` = 7.40 (149.6x median), `PREV_APPROVAL_RATE` = -0.56 (28.6x median), `EXT_SOURCE_3` = -1.30 (12.7x median), `YEARS_BIRTH` = 1.57 (11.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 335860

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 30.33 (593.3x median), `BUREAU_BB_DPD_RATIO_MEAN` = 16.93 (88.1x median), `EXT_SOURCE_1` = -0.89 (66.8x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `POS_SK_DPD_MEAN` = 5.74 (29.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 185954

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 23.89 (467.5x median), `EXT_SOURCE_1` = -2.73 (203.8x median), `BUREAU_BB_DPD_RATIO_MEAN` = 18.07 (93.9x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 119905

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -1.24 (62.0x median), `EXT_SOURCE_1` = 0.50 (36.2x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `EXT_SOURCE_2` = -2.44 (13.0x median), `CC_UTILIZATION_MEAN` = 4.03 (10.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 311318

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | Tipe C (Risk Signal) |
| Top Deviating Features | `YEARS_BIRTH` = 1.37 (43.2x median), `CREDIT_TERM_MONTHS` = 1.67 (38.0x median), `CREDIT_TO_INCOME` = 5.82 (26.1x median), `AMT_INCOME_TOTAL` = -2.51 (24.0x median), `POS_MONTHS_COUNT` = -0.73 (20.5x median) |
| Justifikasi | Kombinasi finansial kontradiktif (mis. rasio cicilan/pendapatan ekstrem, income rendah + credit besar, atau skor eksternal tinggi di cluster bermasalah). |
| Business Impact | Underwriting: matikan auto-approve, wajibkan manual review oleh underwriter senior + verifikasi pendapatan fisik. |

---

## SK_ID_CURR 131396

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 11.44 (230.9x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `PREV_APPROVAL_RATE` = 0.49 (23.2x median), `EXT_SOURCE_3` = 1.26 (10.3x median), `YEARS_BIRTH` = 1.26 (9.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 441234

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = -1.47 (110.0x median), `POS_SK_DPD_MEAN` = 11.21 (58.4x median), `PREV_APPROVAL_RATE` = -1.02 (51.1x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 254119

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 37.90 (741.0x median), `EXT_SOURCE_1` = -1.92 (143.6x median), `BUREAU_BB_DPD_RATIO_MEAN` = 22.72 (117.8x median), `PREV_APPROVAL_RATE` = -1.58 (78.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 360926

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 6.26 (123.2x median), `EXT_SOURCE_1` = -1.63 (122.2x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_BB_DPD_RATIO_MEAN` = 3.94 (21.3x median), `POS_SK_DPD_MEAN` = 3.48 (17.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 183580

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = -2.14 (160.2x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 5.54 (109.1x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `POS_SK_DPD_MEAN` = 5.80 (29.7x median), `BUREAU_BB_DPD_RATIO_MEAN` = 3.02 (16.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 143730

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = 2.66 (196.9x median), `POS_SK_DPD_MEAN` = 8.03 (41.5x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_ANNUITY` = 2.74 (29.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 126237

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 14.88 (299.9x median), `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_ACTIVE_RATIO` = 1.25 (22.2x median), `ANNUITY_TO_INCOME` = 1.07 (13.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 320553

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `POS_MONTHS_COUNT` = 4.92 (130.6x median), `YEARS_BIRTH` = 1.11 (35.2x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (21.0x median), `CREDIT_TERM_MONTHS` = 0.90 (20.9x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 341594

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `POS_MONTHS_COUNT` = 2.94 (77.7x median), `INST_DPD_MAX` = 7.83 (76.2x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `POS_SK_DPD_MEAN` = 1.99 (29.4x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.80 (23.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 356129

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 11.71 (61.0x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `BUREAU_BB_DPD_RATIO_MEAN` = 4.54 (24.3x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `EXT_SOURCE_3` = -1.21 (11.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 398708

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `POS_SK_DPD_MEAN` = 17.89 (93.8x median), `CREDIT_TERM_MONTHS` = 1.27 (17.5x median), `DEF_30_CNT_SOCIAL_CIRCLE_BIN` = 4.63 (14.7x median), `CREDIT_TO_INCOME` = 1.79 (12.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 300913

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 19.41 (390.8x median), `EXT_SOURCE_1` = 0.71 (51.5x median), `EXT_SOURCE_3` = -2.28 (21.5x median), `PREV_APPROVAL_RATE` = 0.41 (19.4x median), `AMT_ANNUITY` = 1.48 (15.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 201006

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 9.77 (197.2x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `AMT_ANNUITY` = -1.09 (13.0x median), `EXT_SOURCE_3` = 1.40 (11.6x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.74 (9.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 309402

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 33.81 (661.3x median), `POS_MONTHS_COUNT` = 3.51 (92.8x median), `BUREAU_BB_DPD_RATIO_MEAN` = 15.95 (83.0x median), `YEARS_BIRTH` = -1.42 (42.9x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 410342

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 8.62 (174.1x median), `EXT_SOURCE_3` = -2.32 (21.9x median), `AMT_ANNUITY` = -1.39 (16.2x median), `ORGANIZATION_TYPE_FREQ` = 1.37 (8.9x median), `CC_MONTHS_COUNT` = 3.33 (8.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 198496

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 14.72 (296.7x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `AMT_ANNUITY` = -1.90 (21.8x median), `ANNUITY_TO_INCOME` = -1.26 (13.3x median), `AMT_CREDIT` = -1.40 (10.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 424523

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 22.52 (118.3x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `AMT_ANNUITY` = -2.20 (25.1x median), `INST_DPD_MEAN` = 53.49 (18.5x median), `AMT_CREDIT` = -2.61 (17.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 278250

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `BUREAU_BB_DPD_RATIO_MEAN` = 21.76 (112.9x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_3` = -1.29 (12.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 195760

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 21.41 (431.0x median), `CREDIT_TERM_MONTHS` = -1.62 (20.1x median), `BUREAU_ACTIVE_RATIO` = 0.61 (11.3x median), `BUREAU_COUNT` = 1.36 (8.6x median), `CC_MONTHS_COUNT` = 2.76 (7.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 388463

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe B (Rare but Valid) |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 7.79 (40.2x median), `EXT_SOURCE_1` = -0.51 (39.0x median), `EXT_SOURCE_3` = -2.55 (23.9x median), `CREDIT_TERM_MONTHS` = 1.28 (17.7x median), `PREV_APPROVAL_RATE` = -0.27 (14.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## SK_ID_CURR 191057

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 10.29 (207.6x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_ACTIVE_RATIO` = 1.25 (22.2x median), `EXT_SOURCE_3` = 1.67 (14.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 186834

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 9.30 (187.9x median), `EXT_SOURCE_1` = 0.50 (36.1x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `ANNUITY_TO_INCOME` = 2.15 (25.4x median), `CREDIT_TERM_MONTHS` = -1.52 (18.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 170056

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = 1.10 (81.0x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `POS_SK_DPD_MEAN` = 6.02 (30.9x median), `BUREAU_BB_DPD_RATIO_MEAN` = 4.53 (24.3x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 272890

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 16.93 (88.7x median), `ANNUITY_TO_INCOME` = 3.26 (38.0x median), `AMT_ANNUITY` = 1.86 (19.4x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CREDIT_TO_INCOME` = 2.12 (14.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 289506

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 15.31 (308.4x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `EXT_SOURCE_2` = -1.86 (10.2x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median), `CC_MONTHS_COUNT` = 3.37 (8.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 399075

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `EXT_SOURCE_1` = -1.43 (107.2x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `POS_SK_DPD_MEAN` = 6.72 (34.6x median), `EXT_SOURCE_3` = -1.10 (10.9x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 0.46 (10.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 135195

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 10.03 (202.4x median), `EXT_SOURCE_1` = -0.86 (64.9x median), `PREV_APPROVAL_RATE` = -0.81 (41.1x median), `ANNUITY_TO_INCOME` = 2.15 (25.4x median), `BUREAU_ACTIVE_RATIO` = 1.25 (22.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 234063

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | Tipe B (Rare but Valid) |
| Top Deviating Features | `POS_MONTHS_COUNT` = 1.41 (36.7x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.58 (27.8x median), `EXT_SOURCE_3` = -2.47 (23.2x median), `YEARS_BIRTH` = -0.71 (21.0x median), `AMT_ANNUITY` = -2.28 (17.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## SK_ID_CURR 419058

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | Tipe B (Rare but Valid) |
| Top Deviating Features | `INST_DPD_MAX` = 4.76 (46.8x median), `POS_MONTHS_COUNT` = 0.97 (24.8x median), `CREDIT_TERM_MONTHS` = -1.08 (22.8x median), `POS_SK_DPD_MEAN` = 1.47 (22.1x median), `AMT_INCOME_TOTAL` = 2.47 (21.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## SK_ID_CURR 138439

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 21.76 (114.2x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `CREDIT_TERM_MONTHS` = -1.57 (19.4x median), `INST_DPD_MEAN` = 36.04 (12.1x median), `AMT_CREDIT` = -1.64 (11.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## SK_ID_CURR 427621

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | Tipe A (Data Error) |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 7.82 (158.1x median), `ANNUITY_TO_INCOME` = 4.00 (46.4x median), `CREDIT_TO_INCOME` = 2.06 (14.3x median), `PREV_APPROVAL_RATE` = 0.30 (13.9x median), `YEARS_BIRTH` = 1.66 (12.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---
