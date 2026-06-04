# Phase 4 — Anomaly Investigation Log
**Dataset:** Home Credit Default Risk
**High-confidence anomalies investigated:** 1,412

---

## ROW_ID 85

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 1.37 (35.6x median), `EXT_SOURCE_1` = -0.40 (30.6x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.46 (18.8x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `OWN_CAR_AGE` = 6.79 (15.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 89

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.83 (134.6x median), `POS_SK_DPD_MEAN` = 16.97 (87.5x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `ANNUITY_TO_INCOME` = 1.69 (19.1x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 183

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 9.45 (185.5x median), `POS_SK_DPD_MEAN` = 15.15 (78.0x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_BB_DPD_RATIO_MEAN` = 8.06 (42.5x median), `ANNUITY_TO_INCOME` = 2.34 (26.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 270

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `ANNUITY_TO_INCOME` = 2.35 (26.3x median), `CREDIT_TO_INCOME` = 3.76 (24.8x median), `CREDIT_TERM_MONTHS` = 1.68 (23.1x median), `POS_SK_DPD_MEAN` = 3.24 (15.9x median), `YEARS_BIRTH` = 1.48 (10.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 991

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 2.66 (70.2x median), `CREDIT_TERM_MONTHS` = 1.68 (37.7x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_3` = -2.94 (27.5x median), `YEARS_BIRTH` = -0.90 (25.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 1188

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.51 (112.8x median), `INST_SEVERE_LATE_RATIO` = 6.54 (39.9x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `INST_DPD_MEAN` = 1.03 (10.0x median), `EXT_SOURCE_2` = 0.84 (8.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 1318

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.50 (184.4x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = -1.08 (22.6x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.32 (17.0x median), `BUREAU_ACTIVE_RATIO` = -0.58 (8.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 1570

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `AMT_CREDIT` = 1.87 (59.7x median), `AMT_ANNUITY` = 2.05 (30.1x median), `EXT_SOURCE_1` = -0.30 (23.3x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.59 (10.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 1727

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.67 (197.6x median), `BUREAU_DAYS_CREDIT_MEAN` = -3.00 (39.7x median), `CREDIT_TERM_MONTHS` = 1.17 (26.7x median), `YEARS_BIRTH` = 0.73 (22.8x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 1970

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.85 (62.2x median), `BUREAU_BB_DPD_RATIO_MEAN` = 7.84 (41.3x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `POS_MONTHS_COUNT` = -0.53 (15.1x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 1.85 (13.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 2202

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `CREDIT_TERM_MONTHS` = 2.17 (29.6x median), `EXT_SOURCE_3` = 1.68 (14.1x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 2368

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -3.24 (242.0x median), `EXT_SOURCE_3` = -2.07 (19.6x median), `YEARS_BIRTH` = -1.04 (14.5x median), `BUREAU_DAYS_CREDIT_MEAN` = 0.88 (7.4x median), `BUREAU_COUNT` = 0.92 (6.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 2494

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `YEARS_BIRTH` = 1.65 (50.2x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `CREDIT_TERM_MONTHS` = -1.62 (34.4x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 2.23 (25.1x median), `POS_MONTHS_COUNT` = -0.85 (23.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 2685

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 27.97 (144.8x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `EXT_SOURCE_3` = -1.40 (13.5x median), `CC_MONTHS_COUNT` = 3.41 (8.8x median), `AMT_ANNUITY` = -0.64 (8.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 2873

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 6.21 (37.9x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `INST_DPD_MEAN` = 1.22 (11.7x median), `INST_LATE_RATIO` = 4.69 (8.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 3620

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 24.14 (485.8x median), `PREV_APPROVAL_RATE` = -1.40 (69.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DAYS_CREDIT_MEAN` = -2.75 (16.1x median), `EXT_SOURCE_3` = 1.75 (14.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 4244

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_DAYS_CREDIT_MEAN` = -2.15 (28.2x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `YEARS_BIRTH` = -0.62 (17.6x median), `OWN_CAR_AGE` = 5.57 (13.2x median), `AMT_ANNUITY` = -1.01 (8.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 4734

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 3.71 (98.2x median), `YEARS_BIRTH` = 0.68 (21.4x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.59 (20.6x median), `CREDIT_TERM_MONTHS` = -0.94 (19.7x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 2.43 (18.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 5028

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `AMT_ANNUITY` = -3.10 (35.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `AMT_INCOME_TOTAL` = -3.26 (14.3x median), `AMT_CREDIT` = -1.98 (13.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 5206

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.25 (92.0x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `ANNUITY_TO_INCOME` = 1.88 (21.2x median), `CREDIT_TO_INCOME` = 1.74 (12.1x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 5223

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.53 (40.1x median), `INST_SEVERE_LATE_RATIO` = 3.19 (19.9x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `EXT_SOURCE_3` = -0.58 (6.2x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (4.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 5799

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 16.99 (243.7x median), `POS_MONTHS_COUNT` = 3.87 (102.5x median), `EXT_SOURCE_1` = 1.08 (79.2x median), `CREDIT_TERM_MONTHS` = 0.99 (22.6x median), `AMT_INCOME_TOTAL` = 1.79 (15.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 5815

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 14.38 (289.8x median), `PREV_APPROVAL_RATE` = -0.87 (43.9x median), `CREDIT_TERM_MONTHS` = 1.67 (23.0x median), `EXT_SOURCE_3` = -1.43 (13.8x median), `BUREAU_ACTIVE_RATIO` = -0.79 (12.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 5975

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.24 (93.3x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.60 (32.4x median), `BUREAU_BB_DPD_RATIO_MEAN` = 3.18 (17.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 6039

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 8.78 (177.3x median), `PREV_APPROVAL_RATE` = -1.24 (62.0x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `EXT_SOURCE_3` = -2.04 (19.4x median), `BUREAU_ACTIVE_RATIO` = 0.73 (13.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 6503

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `POS_SK_DPD_MEAN` = 5.01 (25.1x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `PREV_APPROVAL_RATE` = 0.30 (13.9x median), `CREDIT_TERM_MONTHS` = -1.05 (12.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 6655

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 15.55 (313.4x median), `EXT_SOURCE_1` = 1.45 (106.3x median), `CREDIT_TERM_MONTHS` = 1.67 (37.6x median), `YEARS_BIRTH` = 0.51 (16.3x median), `BUREAU_ACTIVE_RATIO` = -0.66 (10.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 7225

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.69 (124.8x median), `BUREAU_COUNT` = 4.66 (16.9x median), `AMT_CREDIT` = 0.48 (16.0x median), `YEARS_EMPLOYED` = 3.43 (11.7x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.48 (10.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 7614

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.36 (99.9x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_2` = -1.47 (18.1x median), `BUREAU_ACTIVE_RATIO` = -0.58 (8.9x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.85 (8.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 7745

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_CREDIT` = 1.32 (42.6x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.59 (10.5x median), `AMT_ANNUITY` = 0.72 (9.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 7916

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_CREDIT` = -0.88 (26.6x median), `BUREAU_COUNT` = 7.08 (26.2x median), `AMT_ANNUITY` = -1.64 (25.9x median), `EXT_SOURCE_3` = -2.44 (13.6x median), `PREV_REFUSED_COUNT` = 8.46 (11.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 8580

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.99 (74.8x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `INST_DPD_MAX` = 3.36 (21.9x median), `INST_DPD_MEAN` = 2.05 (19.0x median), `INST_SEVERE_LATE_RATIO` = 3.02 (18.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 8629

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.48 (35.0x median), `YEARS_BIRTH` = 0.97 (29.9x median), `POS_MONTHS_COUNT` = -0.85 (23.7x median), `YEARS_EMPLOYED` = 3.83 (19.3x median), `BUREAU_ACTIVE_RATIO` = 0.78 (14.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 8715

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 10.00 (196.4x median), `EXT_SOURCE_1` = -1.71 (127.8x median), `BUREAU_BB_DPD_RATIO_MEAN` = 5.63 (29.9x median), `EXT_SOURCE_3` = -2.94 (27.5x median), `POS_MONTHS_COUNT` = -0.77 (21.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 10392

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 1.96 (43.9x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.30 (16.6x median), `POS_MONTHS_COUNT` = -0.57 (16.2x median), `YEARS_EMPLOYED` = 2.62 (13.5x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.84 (10.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 10655

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 7.01 (137.8x median), `EXT_SOURCE_1` = 0.78 (56.6x median), `BUREAU_BB_DPD_RATIO_MEAN` = 4.64 (24.9x median), `EXT_SOURCE_3` = -1.26 (12.3x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.03 (6.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 10848

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 6.92 (42.1x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `YEARS_EMPLOYED` = 3.78 (17.6x median), `AMT_INCOME_TOTAL` = -0.85 (8.8x median), `INST_LATE_RATIO` = 4.29 (7.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 11873

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.35 (173.4x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_EMPLOYED` = 3.52 (16.5x median), `YEARS_BIRTH` = 1.14 (13.8x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (11.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 12007

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 4.11 (109.0x median), `CREDIT_TERM_MONTHS` = 1.96 (43.8x median), `YEARS_BIRTH` = 1.28 (39.1x median), `YEARS_EMPLOYED` = 5.35 (26.6x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.28 (16.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 12177

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `EXT_SOURCE_3` = -2.33 (21.9x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `CREDIT_TERM_MONTHS` = 1.26 (17.6x median), `PREV_REFUSED_COUNT` = 3.45 (8.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 12354

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.19 (161.5x median), `YEARS_BIRTH` = 1.35 (41.4x median), `CREDIT_TERM_MONTHS` = 1.27 (28.7x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.00 (23.2x median), `BUREAU_DAYS_CREDIT_MEAN` = 0.51 (7.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 12412

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 14.33 (73.7x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `ANNUITY_TO_INCOME` = 3.31 (36.6x median), `CREDIT_TERM_MONTHS` = -1.51 (18.9x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 12574

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_CREDIT` = 0.52 (17.3x median), `CC_MONTHS_COUNT` = 3.41 (8.8x median), `PREV_REFUSED_COUNT` = 6.23 (8.4x median), `AMT_ANNUITY` = 0.57 (7.7x median), `BUREAU_COUNT` = 2.02 (6.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 12638

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.28 (170.3x median), `YEARS_BIRTH` = -1.19 (34.4x median), `EXT_SOURCE_3` = -2.07 (19.6x median), `BUREAU_COUNT` = 2.46 (14.7x median), `EXT_SOURCE_2` = -2.48 (9.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 12861

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `CREDIT_TERM_MONTHS` = 1.28 (17.9x median), `BUREAU_COUNT` = 1.36 (8.6x median), `AMT_ANNUITY` = 0.69 (6.7x median), `AMT_CREDIT` = 1.17 (6.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 13090

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `POS_MONTHS_COUNT` = -1.13 (31.3x median), `EXT_SOURCE_1` = -0.39 (29.9x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.14 (14.5x median), `EXT_SOURCE_3` = -1.30 (12.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 13373

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `INST_SEVERE_LATE_RATIO` = 3.19 (19.9x median), `YEARS_BIRTH` = 1.54 (18.9x median), `INST_DPD_MAX` = 2.75 (18.1x median), `INST_DPD_MEAN` = 1.81 (16.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 13547

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `AMT_CREDIT` = 1.70 (54.5x median), `AMT_ANNUITY` = 1.81 (26.5x median), `BUREAU_ACTIVE_RATIO` = 0.73 (13.3x median), `YEARS_EMPLOYED` = 2.70 (9.4x median), `CC_MONTHS_COUNT` = 3.05 (8.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 13816

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.98 (222.3x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.08 (22.1x median), `AMT_CREDIT` = -0.72 (21.5x median), `OWN_CAR_AGE` = 6.79 (15.9x median), `EXT_SOURCE_3` = -2.08 (11.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 14182

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.38 (175.4x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `INST_SEVERE_LATE_RATIO` = 3.82 (23.7x median), `BUREAU_DAYS_CREDIT_MEAN` = -2.10 (14.2x median), `BUREAU_ACTIVE_RATIO` = 2.03 (13.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 14964

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.65 (49.6x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_ACTIVE_RATIO` = 0.69 (12.7x median), `AMT_CREDIT` = -0.43 (12.5x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.55 (11.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 15298

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 14.31 (288.4x median), `ANNUITY_TO_INCOME` = 3.15 (34.9x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `PREV_APPROVAL_RATE` = -0.27 (14.5x median), `AMT_INCOME_TOTAL` = -3.03 (13.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 15501

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.93 (67.9x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_EMPLOYED` = 4.62 (21.3x median), `ANNUITY_TO_INCOME` = 6.90 (16.3x median), `BUREAU_ACTIVE_RATIO` = 2.03 (13.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 15502

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.74 (54.0x median), `YEARS_BIRTH` = 1.22 (37.5x median), `YEARS_EMPLOYED` = 5.55 (27.5x median), `EXT_SOURCE_3` = -2.03 (19.3x median), `CREDIT_TERM_MONTHS` = 0.53 (12.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 15613

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 1.89 (49.7x median), `YEARS_EMPLOYED` = 3.52 (17.8x median), `OWN_CAR_AGE` = 6.68 (15.7x median), `AMT_INCOME_TOTAL` = -1.40 (13.8x median), `YEARS_BIRTH` = 0.33 (10.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 16306

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.72 (126.6x median), `POS_MONTHS_COUNT` = 3.06 (81.0x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.00 (23.2x median), `YEARS_BIRTH` = 0.63 (19.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 16973

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.70 (125.2x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.88 (37.8x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `INST_LATE_RATIO` = 3.20 (20.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 17008

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.43 (181.2x median), `POS_MONTHS_COUNT` = 1.53 (39.9x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 2.43 (18.5x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `YEARS_EMPLOYED` = 3.45 (17.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 17064

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -1.24 (62.0x median), `EXT_SOURCE_1` = 0.50 (36.2x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `EXT_SOURCE_2` = -2.44 (13.1x median), `CC_UTILIZATION_MEAN` = 4.03 (10.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 18575

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_BIRTH` = 0.76 (23.5x median), `YEARS_EMPLOYED` = 3.62 (18.3x median), `BUREAU_COUNT` = 2.68 (15.9x median), `AMT_INCOME_TOTAL` = 1.84 (15.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 19087

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 6.42 (32.5x median), `PREV_APPROVAL_RATE` = -0.27 (14.5x median), `EXT_SOURCE_3` = 1.34 (11.0x median), `BUREAU_ACTIVE_RATIO` = -0.48 (7.1x median), `ANNUITY_TO_INCOME` = 0.50 (6.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 19112

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.04 (152.2x median), `PREV_APPROVAL_RATE` = -2.06 (102.6x median), `POS_SK_DPD_MEAN` = 18.34 (94.6x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 4.06 (80.3x median), `CREDIT_TERM_MONTHS` = 1.68 (23.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 19213

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.52 (188.4x median), `BUREAU_BB_DPD_RATIO_MEAN` = 12.70 (66.3x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `AMT_ANNUITY` = 1.47 (15.4x median), `EXT_SOURCE_3` = -1.44 (13.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 19387

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 5.15 (31.6x median), `INST_LATE_RATIO` = 3.80 (24.5x median), `EXT_SOURCE_1` = 0.20 (14.0x median), `BUREAU_COUNT` = 3.34 (11.8x median), `BUREAU_ACTIVE_RATIO` = -0.63 (9.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 19818

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.58 (190.9x median), `AMT_CREDIT` = -1.55 (47.8x median), `AMT_ANNUITY` = -1.82 (28.6x median), `INST_LATE_RATIO` = 3.06 (19.9x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.64 (13.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 20232

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 19.32 (99.7x median), `EXT_SOURCE_1` = -0.59 (45.1x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CREDIT_TERM_MONTHS` = 1.18 (16.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 20362

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 3.27 (86.4x median), `YEARS_BIRTH` = 1.65 (50.2x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 1.85 (13.9x median), `PREV_COUNT` = 4.54 (13.7x median), `AMT_INCOME_TOTAL` = 1.56 (13.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 20727

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CREDIT_TO_INCOME` = 30.73 (56.3x median), `ANNUITY_TO_INCOME` = 17.93 (44.1x median), `AMT_INCOME_TOTAL` = -3.69 (34.8x median), `INST_SEVERE_LATE_RATIO` = 4.39 (27.1x median), `YEARS_BIRTH` = 1.26 (15.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 21061

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = -1.62 (20.4x median), `EXT_SOURCE_2` = -2.53 (13.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 21107

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.28 (94.4x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `INST_SEVERE_LATE_RATIO` = 5.63 (34.4x median), `INST_DPD_MEAN` = 1.55 (14.7x median), `EXT_SOURCE_3` = -1.17 (11.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 21892

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.98 (73.5x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `ANNUITY_TO_INCOME` = 1.08 (12.6x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (10.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 21901

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 0.88 (22.7x median), `INST_DPD_MAX` = 2.20 (22.2x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `INST_SEVERE_LATE_RATIO` = 2.63 (16.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 22058

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 3.58 (22.3x median), `INST_LATE_RATIO` = 4.58 (8.3x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.17 (7.5x median), `AMT_INCOME_TOTAL` = -0.59 (6.4x median), `YEARS_EMPLOYED` = 1.20 (6.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 22115

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 2.98 (78.8x median), `YEARS_BIRTH` = 1.30 (39.6x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_INCOME_TOTAL` = 2.08 (18.1x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 1.85 (13.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 22443

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `POS_MONTHS_COUNT` = 0.88 (22.7x median), `CREDIT_TERM_MONTHS` = 0.93 (21.3x median), `AMT_INCOME_TOTAL` = 2.08 (18.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 22983

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.76 (129.9x median), `POS_MONTHS_COUNT` = 3.27 (86.4x median), `YEARS_BIRTH` = 1.28 (39.1x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.00 (23.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 23018

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `OWN_CAR_AGE` = 6.68 (15.7x median), `EXT_SOURCE_2` = 0.87 (9.1x median), `YEARS_EMPLOYED` = 2.12 (6.1x median), `EXT_SOURCE_3` = -0.49 (5.4x median), `AMT_INCOME_TOTAL` = 0.86 (5.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 23019

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `YEARS_BIRTH` = -1.44 (41.8x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = -1.08 (22.7x median), `EXT_SOURCE_3` = -2.27 (21.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 23336

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 2.01 (52.9x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `YEARS_BIRTH` = 0.60 (18.8x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CREDIT_TERM_MONTHS` = 0.69 (16.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 23442

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 5.02 (101.8x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = 1.26 (17.6x median), `ANNUITY_TO_INCOME` = 1.27 (14.6x median), `CREDIT_TO_INCOME` = 2.06 (14.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 23528

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.82 (134.3x median), `YEARS_BIRTH` = 1.28 (39.1x median), `CREDIT_TERM_MONTHS` = 1.68 (37.7x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_INCOME_TOTAL` = 1.97 (17.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 23538

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.37 (100.8x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `AMT_ANNUITY` = -1.95 (30.6x median), `AMT_CREDIT` = -1.00 (30.3x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 23673

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `POS_SK_DPD_MEAN` = 4.32 (21.5x median), `PREV_APPROVAL_RATE` = 0.41 (19.4x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `EXT_SOURCE_2` = -2.48 (13.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 23692

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.93 (218.6x median), `BUREAU_COUNT` = 4.66 (16.9x median), `EXT_SOURCE_2` = -2.71 (11.7x median), `EXT_SOURCE_3` = -2.13 (11.7x median), `AMT_CREDIT` = 0.23 (8.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 23981

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 5.62 (110.8x median), `EXT_SOURCE_3` = -2.94 (27.5x median), `BUREAU_BB_DPD_RATIO_MEAN` = 4.23 (22.8x median), `YEARS_EMPLOYED` = 2.08 (10.1x median), `BUREAU_ACTIVE_RATIO` = 1.41 (9.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 24095

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.21 (164.9x median), `POS_MONTHS_COUNT` = 2.01 (52.9x median), `YEARS_BIRTH` = -1.13 (32.8x median), `CREDIT_TERM_MONTHS` = -1.38 (29.2x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 24661

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 1.97 (44.2x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_BIRTH` = -0.81 (23.1x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 24936

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -1.87 (92.9x median), `EXT_SOURCE_1` = 0.43 (30.6x median), `POS_SK_DPD_MEAN` = 5.92 (29.9x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CREDIT_TERM_MONTHS` = -0.74 (8.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 24969

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.89 (139.6x median), `POS_SK_DPD_MEAN` = 9.53 (48.7x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = 1.68 (23.1x median), `PREV_APPROVAL_RATE` = -0.14 (7.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 25129

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `EXT_SOURCE_1` = 0.18 (12.4x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (10.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 25228

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 7.85 (158.6x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `CREDIT_TERM_MONTHS` = 1.67 (23.1x median), `EXT_SOURCE_3` = 1.12 (9.1x median), `CC_MONTHS_COUNT` = 3.45 (8.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 25285

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.79 (57.8x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.66 (14.0x median), `PREV_REFUSED_COUNT` = 9.02 (12.7x median), `BUREAU_COUNT` = 2.68 (9.3x median), `EXT_SOURCE_3` = -1.71 (9.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 25568

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `OWN_CAR_AGE` = 4.01 (9.8x median), `ANNUITY_TO_INCOME` = -0.99 (9.6x median), `AMT_ANNUITY` = -0.75 (9.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 25625

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -1.68 (83.6x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `CREDIT_TERM_MONTHS` = 1.97 (27.0x median), `YEARS_EMPLOYED` = 4.64 (14.7x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 25686

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `POS_MONTHS_COUNT` = 0.93 (23.7x median), `AMT_INCOME_TOTAL` = 2.26 (19.7x median), `YEARS_EMPLOYED` = 3.21 (16.3x median), `BUREAU_COUNT` = 2.46 (14.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 25691

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 8.33 (50.5x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `EXT_SOURCE_3` = -2.26 (21.3x median), `INST_LATE_RATIO` = 4.69 (8.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 25868

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 1.68 (37.7x median), `POS_MONTHS_COUNT` = 1.17 (30.2x median), `INST_DPD_MAX` = 2.29 (23.0x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 1.85 (13.9x median), `PREV_COUNT` = 3.37 (9.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 26028

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.95 (144.0x median), `POS_SK_DPD_MEAN` = 13.87 (71.3x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `AMT_ANNUITY` = 1.89 (20.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 26043

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.70 (125.1x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `CREDIT_TERM_MONTHS` = 1.69 (23.4x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 26650

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `ANNUITY_TO_INCOME` = 1.45 (16.6x median), `EXT_SOURCE_3` = -1.44 (14.0x median), `CNT_CHILDREN` = 4.99 (9.7x median), `YEARS_BIRTH` = 1.05 (7.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 26702

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `EXT_SOURCE_1` = -0.40 (30.8x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.34 (27.2x median), `AMT_CREDIT` = 0.74 (24.3x median), `AMT_ANNUITY` = 1.61 (23.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 27012

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 11.44 (230.9x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `PREV_APPROVAL_RATE` = 0.49 (23.2x median), `EXT_SOURCE_3` = 1.26 (10.3x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 27075

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_ANNUITY` = -2.54 (39.4x median), `AMT_CREDIT` = -1.01 (30.8x median), `EXT_SOURCE_1` = 0.36 (25.9x median), `CREDIT_TERM_MONTHS` = 2.17 (12.1x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.37 (8.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 27207

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -3.04 (226.7x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `CREDIT_TERM_MONTHS` = -1.56 (19.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `EXT_SOURCE_2` = -2.32 (12.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 27913

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 5.99 (121.2x median), `EXT_SOURCE_1` = -0.75 (56.6x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_COUNT` = 3.56 (20.8x median), `CREDIT_TERM_MONTHS` = 0.69 (10.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 27942

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `YEARS_EMPLOYED` = 4.70 (21.6x median), `YEARS_BIRTH` = 1.23 (14.9x median), `EXT_SOURCE_3` = 1.42 (11.8x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.03 (6.5x median), `BUREAU_COUNT` = 0.48 (3.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 27991

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `YEARS_BIRTH` = 1.53 (46.5x median), `CREDIT_TERM_MONTHS` = 1.76 (39.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `PREV_REFUSED_COUNT` = 7.35 (17.2x median), `PREV_APPROVAL_RATE` = -1.99 (13.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 28231

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_2` = -1.96 (23.8x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `INST_SEVERE_LATE_RATIO` = 2.73 (17.2x median), `EXT_SOURCE_3` = -1.04 (10.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 28637

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 4.74 (29.1x median), `YEARS_BIRTH` = -0.96 (13.5x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (11.5x median), `BUREAU_ACTIVE_RATIO` = -1.11 (5.8x median), `INST_LATE_RATIO` = 2.78 (5.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 28658

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.12 (158.5x median), `YEARS_BIRTH` = -1.37 (39.8x median), `CREDIT_TERM_MONTHS` = 1.67 (37.7x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 28736

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_LATE_RATIO` = 3.26 (21.1x median), `AMT_ANNUITY` = 1.42 (20.5x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.56 (10.0x median), `BUREAU_ACTIVE_RATIO` = -0.58 (8.9x median), `EXT_SOURCE_2` = -1.60 (7.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 28967

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_CREDIT` = 1.17 (37.9x median), `EXT_SOURCE_1` = 0.22 (15.5x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.72 (15.2x median), `BUREAU_ACTIVE_RATIO` = 0.78 (14.2x median), `INST_LATE_RATIO` = 1.71 (11.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 29806

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 23.41 (458.2x median), `BUREAU_BB_DPD_RATIO_MEAN` = 10.99 (57.5x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median), `INST_LATE_RATIO` = 4.29 (7.8x median), `EXT_SOURCE_3` = -0.62 (6.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 29823

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.43 (105.0x median), `BUREAU_COUNT` = 3.34 (19.6x median), `EXT_SOURCE_3` = -2.07 (19.6x median), `OWN_CAR_AGE` = 6.79 (15.9x median), `AMT_INCOME_TOTAL` = 1.84 (15.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 29874

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.05 (151.3x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `ANNUITY_TO_INCOME` = 1.30 (14.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 30471

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 12.60 (247.0x median), `EXT_SOURCE_1` = -2.19 (163.5x median), `BUREAU_BB_DPD_RATIO_MEAN` = 7.64 (40.3x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `EXT_SOURCE_2` = 1.01 (10.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 30609

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_CREDIT` = -0.84 (25.4x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.01 (20.8x median), `AMT_ANNUITY` = -1.06 (17.1x median), `OWN_CAR_AGE` = 6.68 (15.7x median), `YEARS_EMPLOYED` = 3.97 (13.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 30645

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_CREDIT` = 0.92 (29.9x median), `AMT_ANNUITY` = 1.53 (22.2x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `INST_LATE_RATIO` = 2.62 (17.2x median), `YEARS_EMPLOYED` = 4.31 (14.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 31512

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 4.74 (93.5x median), `EXT_SOURCE_1` = -0.94 (70.6x median), `BUREAU_BB_DPD_RATIO_MEAN` = 2.09 (11.7x median), `BUREAU_ACTIVE_RATIO` = -0.66 (10.1x median), `EXT_SOURCE_3` = -0.60 (6.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 32058

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.98 (147.7x median), `YEARS_BIRTH` = -1.63 (47.6x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `CREDIT_TERM_MONTHS` = -1.51 (32.1x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.00 (23.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 32234

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 3.30 (20.6x median), `POS_MONTHS_COUNT` = -0.69 (19.4x median), `CREDIT_TERM_MONTHS` = 0.53 (12.6x median), `AMT_INCOME_TOTAL` = 1.40 (11.9x median), `YEARS_BIRTH` = 0.24 (8.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 32246

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_DPD_MAX` = 5.83 (37.3x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `INST_DPD_MEAN` = 1.80 (16.9x median), `INST_SEVERE_LATE_RATIO` = 1.43 (9.5x median), `EXT_SOURCE_2` = 0.74 (7.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 32249

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.06 (79.4x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `INST_SEVERE_LATE_RATIO` = 4.08 (25.3x median), `INST_DPD_MEAN` = 1.98 (18.4x median), `INST_DPD_MAX` = 1.83 (12.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 32561

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.65 (46.9x median), `AMT_CREDIT` = 0.59 (19.7x median), `AMT_ANNUITY` = 1.19 (17.0x median), `INST_DPD_MAX` = 1.78 (15.5x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.59 (10.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 32810

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 7.33 (144.2x median), `AMT_CREDIT` = -1.51 (46.5x median), `BUREAU_BB_DPD_RATIO_MEAN` = 8.31 (43.7x median), `AMT_ANNUITY` = -2.40 (37.3x median), `PREV_REFUSED_COUNT` = 12.92 (18.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 32998

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_BB_DPD_RATIO_MEAN` = 7.55 (39.8x median), `INST_SEVERE_LATE_RATIO` = 2.19 (14.0x median), `EXT_SOURCE_2` = -0.92 (11.7x median), `INST_DPD_MEAN` = 0.78 (7.9x median), `INST_LATE_RATIO` = 3.97 (7.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 33028

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.12 (158.5x median), `AMT_CREDIT` = 1.39 (44.6x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `AMT_ANNUITY` = 1.15 (16.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 33776

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.55 (115.8x median), `CC_SK_DPD_MEAN` = 4.25 (86.4x median), `INST_DPD_MAX` = 7.12 (69.4x median), `POS_MONTHS_COUNT` = 1.29 (33.5x median), `YEARS_BIRTH` = -1.06 (30.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 34246

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 8.97 (176.2x median), `POS_SK_DPD_MEAN` = 22.71 (117.4x median), `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `BUREAU_BB_DPD_RATIO_MEAN` = 8.78 (46.2x median), `ANNUITY_TO_INCOME` = 1.64 (18.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 34306

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.54 (113.2x median), `EXT_SOURCE_2` = 1.04 (11.1x median), `CC_MONTHS_COUNT` = 3.45 (8.9x median), `INST_LATE_RATIO` = 2.62 (5.2x median), `BUREAU_ACTIVE_RATIO` = -0.32 (4.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 34615

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 3.35 (66.4x median), `EXT_SOURCE_3` = -2.94 (16.6x median), `AMT_CREDIT` = -0.55 (16.4x median), `BUREAU_BB_DPD_RATIO_MEAN` = 2.49 (13.8x median), `BUREAU_ACTIVE_RATIO` = 0.61 (11.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 34633

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 2.98 (78.8x median), `EXT_SOURCE_1` = 0.97 (70.7x median), `CREDIT_TERM_MONTHS` = 1.68 (37.8x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 34878

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 2.42 (63.7x median), `INST_DPD_MAX` = 3.55 (35.2x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 1.19 (24.2x median), `BUREAU_BB_DPD_RATIO_MEAN` = 3.11 (17.0x median), `AMT_INCOME_TOTAL` = 1.56 (13.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 35065

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `INST_SEVERE_LATE_RATIO` = 4.74 (29.1x median), `BUREAU_ACTIVE_RATIO` = 1.25 (22.2x median), `INST_DPD_MEAN` = 1.10 (10.7x median), `EXT_SOURCE_2` = -0.74 (9.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 35651

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.03 (77.7x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_BIRTH` = -0.88 (25.1x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 35862

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 3.27 (86.4x median), `EXT_SOURCE_1` = 0.80 (58.5x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.07 (12.5x median), `BUREAU_ACTIVE_RATIO` = 0.64 (11.8x median), `EXT_SOURCE_3` = -1.15 (11.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 35877

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_DPD_MEAN` = 2.60 (23.9x median), `INST_SEVERE_LATE_RATIO` = 3.58 (22.3x median), `INST_DPD_MAX` = 3.33 (21.7x median), `POS_SK_DPD_MEAN` = 1.34 (20.1x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 35908

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.00 (73.5x median), `YEARS_BIRTH` = 1.24 (38.0x median), `POS_MONTHS_COUNT` = -0.77 (21.6x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 36657

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.01 (148.3x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.64 (21.2x median), `POS_MONTHS_COUNT` = -0.73 (20.5x median), `BUREAU_COUNT` = 3.34 (19.6x median), `CREDIT_TERM_MONTHS` = 0.53 (12.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 37284

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `YEARS_BIRTH` = -0.54 (15.0x median), `EXT_SOURCE_3` = -1.55 (14.9x median), `AMT_INCOME_TOTAL` = -1.06 (10.7x median), `BUREAU_DAYS_CREDIT_MEAN` = -0.86 (10.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 37528

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 3.14 (83.1x median), `EXT_SOURCE_1` = 0.54 (39.1x median), `CREDIT_TERM_MONTHS` = 1.66 (37.4x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 1.85 (13.9x median), `EXT_SOURCE_3` = -1.17 (11.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 37906

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 14.11 (284.3x median), `EXT_SOURCE_1` = 1.25 (91.7x median), `CREDIT_TERM_MONTHS` = 1.67 (23.0x median), `BUREAU_ACTIVE_RATIO` = 0.69 (12.7x median), `CREDIT_TO_INCOME` = 1.32 (9.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 38098

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.91 (140.7x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_3` = -1.56 (15.0x median), `INST_SEVERE_LATE_RATIO` = 1.31 (8.8x median), `EXT_SOURCE_2` = -0.66 (8.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 38385

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `AMT_ANNUITY` = 1.41 (14.7x median), `EXT_SOURCE_3` = 1.60 (13.3x median), `YEARS_EMPLOYED` = 4.00 (12.9x median), `POS_SK_DPD_MEAN` = 2.52 (12.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 38388

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_DPD_MAX` = 4.97 (41.4x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `AMT_CREDIT` = -0.42 (12.3x median), `EXT_SOURCE_2` = -2.67 (11.6x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.59 (10.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 38621

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.56 (115.0x median), `BUREAU_BB_DPD_RATIO_MEAN` = 7.18 (37.9x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `EXT_SOURCE_3` = -0.75 (7.8x median), `CNT_CHILDREN` = 3.60 (7.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 38750

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 4.39 (27.1x median), `EXT_SOURCE_3` = -2.32 (21.8x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median), `EXT_SOURCE_2` = 0.68 (6.9x median), `AMT_INCOME_TOTAL` = 1.24 (6.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 38873

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.80 (60.7x median), `POS_MONTHS_COUNT` = 1.33 (34.5x median), `YEARS_EMPLOYED` = 2.40 (12.5x median), `YEARS_BIRTH` = -0.32 (8.4x median), `CREDIT_TERM_MONTHS` = 0.32 (8.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 39028

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.84 (63.4x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_ACTIVE_RATIO` = -0.71 (11.1x median), `EXT_SOURCE_2` = 0.89 (9.4x median), `AMT_INCOME_TOTAL` = 1.56 (8.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 39040

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 17.50 (352.5x median), `PREV_APPROVAL_RATE` = -1.24 (62.0x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `YEARS_BIRTH` = 1.48 (10.4x median), `ANNUITY_TO_INCOME` = 0.79 (9.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 39180

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.40 (179.3x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CREDIT_TERM_MONTHS` = -0.93 (11.3x median), `YEARS_BIRTH` = -1.22 (10.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 39390

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 1.40 (28.3x median), `AMT_INCOME_TOTAL` = -2.51 (24.0x median), `EXT_SOURCE_3` = -1.67 (16.0x median), `YEARS_EMPLOYED` = 3.09 (14.6x median), `INST_SEVERE_LATE_RATIO` = 2.19 (14.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 39490

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 6.86 (182.4x median), `EXT_SOURCE_1` = 1.48 (108.8x median), `YEARS_BIRTH` = 1.57 (47.8x median), `BUREAU_BB_DPD_RATIO_MEAN` = 3.49 (18.9x median), `CREDIT_TERM_MONTHS` = 0.67 (15.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 39696

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.49 (37.5x median), `OWN_CAR_AGE` = 6.79 (15.9x median), `INST_SEVERE_LATE_RATIO` = 2.19 (14.0x median), `INST_DPD_MAX` = 1.50 (10.3x median), `INST_DPD_MEAN` = 1.04 (10.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 39810

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -1.51 (75.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_1` = 0.45 (32.8x median), `CREDIT_TERM_MONTHS` = 0.94 (13.4x median), `BUREAU_ACTIVE_RATIO` = 0.69 (12.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 40086

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `AMT_ANNUITY` = -1.86 (21.8x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `ANNUITY_TO_INCOME` = -1.06 (10.4x median), `CREDIT_TERM_MONTHS` = 0.66 (9.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 40329

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `YEARS_EMPLOYED` = 3.10 (15.8x median), `POS_MONTHS_COUNT` = 0.48 (11.9x median), `EXT_SOURCE_3` = 1.41 (11.7x median), `PREV_APPROVAL_RATE` = 0.96 (8.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 40432

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -0.50 (25.8x median), `EXT_SOURCE_3` = 1.34 (11.0x median), `CREDIT_TERM_MONTHS` = -0.79 (9.4x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median), `POS_SK_DPD_MEAN` = 1.68 (7.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 40598

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = 1.27 (28.7x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.58 (27.8x median), `YEARS_BIRTH` = -0.83 (23.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 40897

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = -1.09 (22.8x median), `AMT_INCOME_TOTAL` = 1.84 (15.8x median), `YEARS_BIRTH` = 0.48 (15.4x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 1.85 (13.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 41035

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_COUNT` = 5.76 (21.2x median), `AMT_ANNUITY` = 0.94 (13.3x median), `PREV_REFUSED_COUNT` = 7.90 (11.0x median), `CC_MONTHS_COUNT` = 3.13 (8.2x median), `AMT_CREDIT` = 0.23 (8.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 41395

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 1.96 (43.9x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `POS_MONTHS_COUNT` = -0.61 (17.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 41526

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.37 (102.8x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_INCOME_TOTAL` = 2.31 (20.1x median), `BUREAU_ACTIVE_RATIO` = 2.03 (13.4x median), `YEARS_BIRTH` = -0.78 (11.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 41650

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.91 (66.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_2` = -2.29 (27.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DAYS_CREDIT_MEAN` = -2.81 (11.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 41774

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 2.58 (68.0x median), `CREDIT_TERM_MONTHS` = 1.96 (43.9x median), `YEARS_BIRTH` = 1.16 (35.7x median), `CREDIT_TO_INCOME` = 5.27 (23.7x median), `ANNUITY_TO_INCOME` = 3.25 (13.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 42085

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `YEARS_EMPLOYED` = 5.35 (17.7x median), `BUREAU_COUNT` = 3.12 (11.0x median), `AMT_ANNUITY` = -0.30 (5.5x median), `AMT_CREDIT` = -0.19 (5.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 42203

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `AMT_CREDIT` = -0.76 (22.8x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.07 (22.0x median), `AMT_ANNUITY` = -1.04 (16.7x median), `OWN_CAR_AGE` = 6.68 (15.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 42557

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.96 (144.4x median), `AMT_CREDIT` = 1.35 (43.4x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.36 (27.5x median), `AMT_ANNUITY` = 1.42 (20.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 42623

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 2.86 (75.6x median), `YEARS_BIRTH` = 1.33 (40.7x median), `CREDIT_TERM_MONTHS` = 1.68 (37.7x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_COUNT` = 5.98 (34.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 42950

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 25.28 (508.7x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `EXT_SOURCE_1` = -0.22 (17.4x median), `EXT_SOURCE_3` = -1.74 (16.6x median), `AMT_ANNUITY` = -0.72 (9.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 43025

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 2.42 (63.7x median), `CREDIT_TO_INCOME` = 5.05 (22.7x median), `ANNUITY_TO_INCOME` = 5.79 (22.6x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 1.85 (13.9x median), `AMT_INCOME_TOTAL` = -1.40 (13.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 43112

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -1.51 (75.5x median), `BUREAU_COUNT` = 3.34 (19.6x median), `EXT_SOURCE_3` = 1.69 (14.2x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.13 (6.1x median), `YEARS_BIRTH` = -0.65 (6.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 43707

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_3` = -2.26 (21.3x median), `BUREAU_ACTIVE_RATIO` = -0.82 (12.9x median), `EXT_SOURCE_2` = 1.02 (10.8x median), `INST_LATE_RATIO` = 3.80 (7.1x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.37 (6.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 43949

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.75 (129.2x median), `YEARS_BIRTH` = 0.88 (27.2x median), `EXT_SOURCE_3` = -2.02 (19.2x median), `YEARS_EMPLOYED` = 3.65 (18.4x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 1.85 (13.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 44083

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `INST_DPD_MAX` = 5.01 (32.2x median), `INST_DPD_MEAN` = 2.19 (20.3x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `EXT_SOURCE_1` = -0.21 (16.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 44196

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.00 (23.2x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.80 (20.5x median), `POS_MONTHS_COUNT` = 0.76 (19.4x median), `BUREAU_DAYS_CREDIT_MEAN` = -0.93 (11.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 44264

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 57.79 (1161.7x median), `EXT_SOURCE_1` = 1.82 (134.4x median), `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `INST_DPD_MEAN` = 66.10 (22.9x median), `EXT_SOURCE_3` = 1.45 (12.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 44839

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 1.97 (27.0x median), `POS_SK_DPD_MEAN` = 4.82 (24.1x median), `BUREAU_COUNT` = 2.90 (17.1x median), `EXT_SOURCE_3` = -1.70 (16.3x median), `CREDIT_TO_INCOME` = 1.86 (12.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 45294

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.66 (122.3x median), `POS_MONTHS_COUNT` = 3.95 (104.7x median), `YEARS_BIRTH` = -0.56 (15.7x median), `EXT_SOURCE_3` = -1.51 (14.5x median), `BUREAU_COUNT` = 2.24 (13.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 45892

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 1.59 (32.1x median), `BUREAU_BB_DPD_RATIO_MEAN` = 5.83 (31.0x median), `INST_SEVERE_LATE_RATIO` = 2.80 (17.6x median), `INST_DPD_MEAN` = 1.83 (17.1x median), `EXT_SOURCE_2` = 1.42 (15.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 45939

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.72 (128.5x median), `CREDIT_TERM_MONTHS` = -1.56 (33.3x median), `YEARS_BIRTH` = -1.08 (31.1x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.58 (27.8x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.84 (23.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 46107

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.95 (145.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `EXT_SOURCE_2` = -1.00 (12.6x median), `AMT_INCOME_TOTAL` = -1.71 (7.0x median), `CNT_CHILDREN` = 2.21 (4.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 46393

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `CREDIT_TERM_MONTHS` = 1.27 (17.7x median), `CNT_CHILDREN` = 7.78 (14.5x median), `CREDIT_TO_INCOME` = 1.72 (11.9x median), `ANNUITY_TO_INCOME` = 0.95 (11.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 46396

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 3.77 (76.8x median), `ANNUITY_TO_INCOME` = 1.13 (13.2x median), `BUREAU_COUNT` = 2.02 (12.2x median), `EXT_SOURCE_1` = 0.13 (8.3x median), `CREDIT_TO_INCOME` = 1.12 (8.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 46762

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `AMT_ANNUITY` = 1.69 (17.9x median), `CREDIT_TERM_MONTHS` = 0.99 (14.0x median), `EXT_SOURCE_3` = -1.38 (13.4x median), `AMT_INCOME_TOTAL` = 2.08 (10.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 46953

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `INST_SEVERE_LATE_RATIO` = 4.74 (29.1x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (11.5x median), `INST_DPD_MEAN` = 1.06 (10.4x median), `INST_LATE_RATIO` = 3.46 (6.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 47532

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `EXT_SOURCE_2` = -2.43 (13.1x median), `ANNUITY_TO_INCOME` = 1.05 (12.3x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (10.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 47607

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 12.65 (255.0x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `CREDIT_TERM_MONTHS` = 1.67 (23.0x median), `CC_MONTHS_COUNT` = 3.41 (8.8x median), `YEARS_BIRTH` = 1.18 (8.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 47714

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.11 (155.8x median), `AMT_CREDIT` = 0.92 (30.0x median), `EXT_SOURCE_3` = -2.26 (12.5x median), `AMT_ANNUITY` = 0.86 (12.0x median), `YEARS_EMPLOYED` = 2.34 (8.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 48053

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟠 Tipe C — Risk Signal** |
| Top Deviating Features | `AMT_INCOME_TOTAL` = -2.33 (22.3x median), `YEARS_BIRTH` = 1.61 (19.9x median), `ANNUITY_TO_INCOME` = 5.94 (13.9x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (11.5x median), `INST_LATE_RATIO` = 4.82 (8.7x median) |
| Justifikasi | Kombinasi finansial kontradiktif (mis. rasio cicilan/pendapatan ekstrem, income rendah + credit besar, atau skor eksternal tinggi di cluster bermasalah). |
| Business Impact | Underwriting: matikan auto-approve, wajibkan manual review oleh underwriter senior + verifikasi pendapatan fisik. |

---

## ROW_ID 48646

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.03 (150.0x median), `AMT_CREDIT` = -0.71 (21.2x median), `BUREAU_COUNT` = 2.90 (10.2x median), `CC_MONTHS_COUNT` = 3.41 (8.8x median), `POS_MONTHS_COUNT` = 6.25 (7.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 48705

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 7.02 (142.1x median), `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `CREDIT_TERM_MONTHS` = 0.85 (12.2x median), `CC_MONTHS_COUNT` = 3.41 (8.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 49182

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 1.68 (37.7x median), `EXT_SOURCE_1` = 0.36 (25.4x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.26 (16.2x median), `CREDIT_TO_INCOME` = 2.93 (13.6x median), `EXT_SOURCE_3` = -1.30 (12.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 49329

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 5.08 (134.9x median), `CREDIT_TERM_MONTHS` = -1.10 (23.1x median), `EXT_SOURCE_3` = -2.02 (19.1x median), `AMT_ANNUITY` = -2.05 (15.5x median), `BUREAU_COUNT` = 2.24 (13.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 49343

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.37 (102.5x median), `YEARS_BIRTH` = 1.19 (36.5x median), `POS_MONTHS_COUNT` = 1.21 (31.3x median), `CREDIT_TERM_MONTHS` = 0.92 (21.1x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 49445

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.46 (107.2x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `AMT_CREDIT` = 0.78 (25.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.59 (10.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 49462

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `YEARS_EMPLOYED` = 4.60 (15.4x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.59 (10.5x median), `AMT_CREDIT` = -0.34 (9.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 49524

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_CREDIT` = 1.20 (38.6x median), `AMT_ANNUITY` = 1.67 (24.4x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `EXT_SOURCE_3` = -2.26 (12.5x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.57 (12.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 49598

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_INCOME_TOTAL` = 1.24 (10.3x median), `YEARS_BIRTH` = 0.86 (10.2x median), `CC_MONTHS_COUNT` = 3.45 (8.9x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.00 (8.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 49881

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `POS_MONTHS_COUNT` = 1.29 (33.5x median), `BUREAU_DAYS_CREDIT_MEAN` = -2.24 (29.3x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `AMT_INCOME_TOTAL` = 1.56 (13.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 49906

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_ANNUITY` = -2.33 (36.3x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `AMT_CREDIT` = -0.88 (26.6x median), `EXT_SOURCE_1` = -0.24 (19.1x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 50120

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.69 (52.3x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_2` = -2.33 (28.1x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CREDIT_TERM_MONTHS` = 2.13 (5.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 50675

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `POS_MONTHS_COUNT` = -1.13 (31.3x median), `YEARS_BIRTH` = 0.90 (27.9x median), `INST_SEVERE_LATE_RATIO` = 3.85 (23.9x median), `EXT_SOURCE_3` = -0.95 (9.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 50993

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.07 (80.8x median), `INST_DPD_MAX` = 6.39 (53.0x median), `POS_SK_DPD_MEAN` = 2.02 (29.9x median), `INST_DPD_MEAN` = 1.90 (21.2x median), `AMT_CREDIT` = -0.54 (16.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 51238

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 7.80 (47.4x median), `BUREAU_DAYS_CREDIT_MEAN` = -2.46 (16.9x median), `YEARS_BIRTH` = -0.98 (13.7x median), `INST_DPD_MEAN` = 0.71 (7.3x median), `BUREAU_ACTIVE_RATIO` = -1.11 (5.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 51775

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.44 (180.3x median), `POS_MONTHS_COUNT` = 1.85 (48.6x median), `YEARS_BIRTH` = 1.17 (35.8x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_EMPLOYED` = 3.74 (18.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 52246

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.49 (35.4x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (4.5x median), `AMT_INCOME_TOTAL` = 0.71 (4.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 52497

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.50 (37.9x median), `AMT_CREDIT` = -0.69 (20.6x median), `CC_AMT_BALANCE_MEAN` = 3.60 (12.7x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.59 (10.5x median), `PREV_REFUSED_COUNT` = 7.35 (10.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 52570

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟠 Tipe C — Risk Signal** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 3.82 (23.7x median), `AMT_INCOME_TOTAL` = -2.13 (20.5x median), `YEARS_BIRTH` = -0.93 (13.1x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (11.5x median), `ANNUITY_TO_INCOME` = 4.80 (11.1x median) |
| Justifikasi | Kombinasi finansial kontradiktif (mis. rasio cicilan/pendapatan ekstrem, income rendah + credit besar, atau skor eksternal tinggi di cluster bermasalah). |
| Business Impact | Underwriting: matikan auto-approve, wajibkan manual review oleh underwriter senior + verifikasi pendapatan fisik. |

---

## ROW_ID 52890

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 5.11 (100.7x median), `EXT_SOURCE_1` = -0.36 (28.0x median), `BUREAU_BB_DPD_RATIO_MEAN` = 3.49 (19.0x median), `INST_DPD_MAX` = 2.11 (18.1x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 53185

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `CNT_CHILDREN` = 3.60 (7.2x median), `AMT_INCOME_TOTAL` = 0.86 (5.0x median), `EXT_SOURCE_3` = 0.54 (3.8x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 0.70 (2.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 53408

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `AMT_ANNUITY` = 1.61 (17.1x median), `CREDIT_TERM_MONTHS` = -1.08 (13.2x median), `ANNUITY_TO_INCOME` = 1.09 (12.8x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 53935

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `EXT_SOURCE_1` = 1.26 (92.7x median), `BUREAU_ACTIVE_RATIO` = 0.61 (11.3x median), `INST_SEVERE_LATE_RATIO` = 39.69 (10.1x median), `BUREAU_COUNT` = 1.36 (8.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 54629

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 6.45 (126.9x median), `EXT_SOURCE_1` = 1.18 (87.0x median), `POS_MONTHS_COUNT` = 2.14 (56.1x median), `CREDIT_TERM_MONTHS` = -1.45 (30.7x median), `BUREAU_BB_DPD_RATIO_MEAN` = 4.45 (23.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 54853

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 3.02 (18.9x median), `INST_DPD_MAX` = 1.47 (10.1x median), `EXT_SOURCE_3` = 1.14 (9.3x median), `INST_DPD_MEAN` = 0.94 (9.2x median), `EXT_SOURCE_2` = 0.85 (8.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 54934

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.74 (202.3x median), `YEARS_BIRTH` = 1.67 (50.8x median), `CREDIT_TERM_MONTHS` = 1.67 (37.6x median), `YEARS_EMPLOYED` = 4.76 (23.7x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 2.43 (18.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 55376

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 24.23 (125.3x median), `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `EXT_SOURCE_1` = 1.19 (87.3x median), `INST_DPD_MEAN` = 111.40 (39.4x median), `CREDIT_TERM_MONTHS` = 1.26 (17.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 56040

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.70 (50.9x median), `POS_MONTHS_COUNT` = 1.49 (38.9x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.00 (23.2x median), `BUREAU_COUNT` = 2.90 (17.1x median), `EXT_SOURCE_3` = -1.59 (15.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 56139

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `AMT_CREDIT` = -0.65 (19.3x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `AMT_ANNUITY` = -0.89 (14.5x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.48 (10.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 56286

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.67 (197.1x median), `AMT_CREDIT` = -1.01 (30.8x median), `AMT_ANNUITY` = -1.37 (21.7x median), `BUREAU_COUNT` = 5.32 (19.5x median), `EXT_SOURCE_3` = -2.17 (12.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 57073

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_3` = -2.17 (20.5x median), `BUREAU_ACTIVE_RATIO` = 2.03 (13.4x median), `AMT_INCOME_TOTAL` = 1.56 (13.3x median), `INST_LATE_RATIO` = 5.57 (9.9x median), `YEARS_EMPLOYED` = 1.74 (8.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 57346

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.84 (61.5x median), `CREDIT_TERM_MONTHS` = 2.16 (48.3x median), `YEARS_BIRTH` = -1.09 (31.4x median), `POS_MONTHS_COUNT` = 1.13 (29.1x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 57528

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `POS_MONTHS_COUNT` = -0.69 (19.4x median), `EXT_SOURCE_3` = -1.25 (12.3x median), `AMT_ANNUITY` = -1.22 (9.7x median), `BUREAU_COUNT` = 1.36 (8.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 58729

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.87 (214.3x median), `AMT_CREDIT` = -0.72 (21.7x median), `INST_SEVERE_LATE_RATIO` = 3.31 (20.7x median), `INST_LATE_RATIO` = 2.75 (18.0x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 59689

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_2` = -1.69 (20.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `AMT_INCOME_TOTAL` = -1.66 (6.8x median), `EXT_SOURCE_3` = 0.82 (6.4x median), `ANNUITY_TO_INCOME` = 1.83 (4.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 59743

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 15.69 (316.2x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `EXT_SOURCE_3` = 1.79 (15.0x median), `CREDIT_TERM_MONTHS` = 0.86 (12.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 60057

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.53 (40.2x median), `INST_SEVERE_LATE_RATIO` = 3.82 (23.7x median), `INST_DPD_MEAN` = 1.92 (17.9x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `INST_DPD_MAX` = 1.78 (12.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 60284

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_DPD_MAX` = 2.99 (19.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `INST_DPD_MEAN` = 1.43 (13.6x median), `INST_SEVERE_LATE_RATIO` = 2.07 (13.3x median), `EXT_SOURCE_2` = -0.56 (7.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 61091

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `YEARS_BIRTH` = -1.59 (46.4x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.32 (18.9x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.63 (18.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 61199

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 5.00 (132.8x median), `EXT_SOURCE_1` = 1.61 (118.9x median), `CREDIT_TERM_MONTHS` = -1.63 (34.8x median), `EXT_SOURCE_3` = -2.13 (20.1x median), `AMT_ANNUITY` = -1.96 (14.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 61413

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 5.68 (112.0x median), `YEARS_BIRTH` = 1.41 (43.1x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_BB_DPD_RATIO_MEAN` = 5.94 (31.6x median), `POS_MONTHS_COUNT` = 1.17 (30.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 61449

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `INST_SEVERE_LATE_RATIO` = 5.63 (34.4x median), `BUREAU_DAYS_CREDIT_MEAN` = -2.27 (15.4x median), `EXT_SOURCE_3` = 1.14 (9.2x median), `INST_DPD_MEAN` = 0.70 (7.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 61604

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 1.27 (28.7x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.58 (27.8x median), `YEARS_BIRTH` = 0.72 (22.5x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.22 (17.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 61643

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `POS_MONTHS_COUNT` = 1.33 (34.5x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `OWN_CAR_AGE` = 6.79 (15.9x median), `EXT_SOURCE_3` = 1.16 (9.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 61777

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.31 (98.3x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_2` = -2.65 (31.8x median), `EXT_SOURCE_3` = -1.72 (16.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 61832

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.00 (23.2x median), `CREDIT_TERM_MONTHS` = -0.89 (18.5x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.36 (15.7x median), `BUREAU_DAYS_CREDIT_MEAN` = 0.99 (14.4x median), `PREV_APPROVAL_RATE` = -1.44 (9.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 62194

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.47 (35.6x median), `INST_SEVERE_LATE_RATIO` = 5.15 (31.6x median), `YEARS_BIRTH` = -1.16 (16.1x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (11.5x median), `INST_DPD_MEAN` = 1.04 (10.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 62333

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `CC_MONTHS_COUNT` = 3.45 (8.9x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.34 (7.7x median), `BUREAU_COUNT` = 2.02 (6.8x median), `CC_UTILIZATION_MAX` = 2.26 (5.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 63288

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.05 (76.8x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_BIRTH` = 1.07 (32.7x median), `CREDIT_TERM_MONTHS` = 0.87 (20.0x median), `BUREAU_ACTIVE_RATIO` = 0.78 (14.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 63739

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.26 (168.8x median), `PREV_REFUSED_COUNT` = 13.47 (19.4x median), `BUREAU_ACTIVE_RATIO` = 0.61 (11.3x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.48 (10.4x median), `AMT_ANNUITY` = 0.72 (10.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 63779

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_1` = 0.47 (33.8x median), `AMT_CREDIT` = -1.01 (30.6x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.32 (26.9x median), `AMT_ANNUITY` = -1.19 (19.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 63905

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.93 (142.1x median), `POS_SK_DPD_MEAN` = 13.09 (67.2x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `PREV_APPROVAL_RATE` = -0.36 (18.6x median), `EXT_SOURCE_2` = -2.33 (12.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 64818

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `EXT_SOURCE_2` = 0.58 (5.7x median), `YEARS_EMPLOYED` = 1.48 (4.5x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (4.5x median), `AMT_INCOME_TOTAL` = -1.06 (4.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 66485

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `EXT_SOURCE_1` = 0.41 (29.8x median), `ANNUITY_TO_INCOME` = 1.83 (20.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `AMT_ANNUITY` = 1.65 (17.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 67161

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.61 (120.5x median), `CREDIT_TERM_MONTHS` = 0.86 (19.9x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.52 (19.6x median), `INST_SEVERE_LATE_RATIO` = 2.23 (14.2x median), `BUREAU_COUNT` = 2.24 (13.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 67275

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.91 (140.8x median), `CREDIT_TERM_MONTHS` = -1.48 (31.5x median), `YEARS_BIRTH` = 0.92 (28.5x median), `EXT_SOURCE_3` = -1.51 (14.6x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 0.43 (9.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 67339

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.54 (113.7x median), `YEARS_EMPLOYED` = 4.18 (19.4x median), `YEARS_BIRTH` = 0.58 (6.5x median), `BUREAU_ACTIVE_RATIO` = 0.78 (5.8x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 1.27 (3.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 67362

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.67 (125.2x median), `POS_MONTHS_COUNT` = 2.38 (62.6x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `YEARS_BIRTH` = -1.04 (30.1x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.49 (17.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 67398

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 20.69 (296.6x median), `EXT_SOURCE_1` = -1.79 (134.2x median), `EXT_SOURCE_2` = -1.64 (20.1x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median), `OWN_CAR_AGE` = 3.00 (7.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 67646

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `YEARS_BIRTH` = -0.82 (23.4x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.73 (19.7x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 2.43 (18.5x median), `EXT_SOURCE_1` = 0.26 (18.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 67925

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `AMT_CREDIT` = -0.55 (16.2x median), `AMT_ANNUITY` = -0.97 (15.8x median), `OWN_CAR_AGE` = 6.68 (15.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 67939

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = -1.21 (25.4x median), `BUREAU_ACTIVE_RATIO` = 0.78 (14.2x median), `YEARS_BIRTH` = -0.46 (12.6x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.74 (9.0x median), `AMT_CREDIT` = -1.19 (6.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 68119

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 9.83 (50.2x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = 1.69 (23.4x median), `EXT_SOURCE_2` = -2.62 (14.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 68341

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `AMT_CREDIT` = 1.89 (60.3x median), `AMT_ANNUITY` = 1.34 (19.3x median), `PREV_REFUSED_COUNT` = 12.92 (18.6x median), `INST_DPD_MAX` = 1.39 (12.3x median), `CREDIT_TERM_MONTHS` = 1.96 (11.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 68425

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_BB_DPD_RATIO_MEAN` = 5.25 (28.0x median), `AMT_ANNUITY` = 1.48 (21.4x median), `AMT_CREDIT` = 0.60 (19.9x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.64 (8.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 68854

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 8.53 (51.7x median), `BUREAU_ACTIVE_RATIO` = 2.03 (13.4x median), `AMT_INCOME_TOTAL` = -1.28 (12.7x median), `YEARS_EMPLOYED` = 2.00 (9.8x median), `INST_DPD_MEAN` = 0.86 (8.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 68953

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 12.30 (241.2x median), `BUREAU_BB_DPD_RATIO_MEAN` = 7.36 (38.9x median), `EXT_SOURCE_2` = -1.86 (22.6x median), `INST_SEVERE_LATE_RATIO` = 3.28 (20.5x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 69085

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 7.40 (145.5x median), `EXT_SOURCE_1` = -0.50 (38.3x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `AMT_CREDIT` = -1.04 (31.7x median), `INST_DPD_MAX` = 3.13 (26.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 69276

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.79 (134.3x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `AMT_CREDIT` = -1.01 (30.8x median), `AMT_ANNUITY` = -1.92 (30.0x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.59 (10.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 69332

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `YEARS_BIRTH` = -1.66 (48.3x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.00 (23.2x median), `CREDIT_TERM_MONTHS` = -0.78 (16.2x median), `BUREAU_DAYS_CREDIT_MEAN` = 0.89 (13.1x median), `BUREAU_COUNT` = 2.02 (12.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 69361

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_CREDIT` = -1.01 (30.8x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `AMT_ANNUITY` = -1.02 (16.5x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.59 (10.5x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (9.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 69422

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.26 (94.4x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.58 (27.8x median), `YEARS_BIRTH` = -0.83 (23.7x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.84 (20.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 69768

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.88 (140.7x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `YEARS_BIRTH` = -1.09 (31.6x median), `CREDIT_TERM_MONTHS` = -0.74 (15.1x median), `POS_MONTHS_COUNT` = -0.49 (14.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 70188

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.05 (151.5x median), `POS_MONTHS_COUNT` = 1.25 (32.4x median), `INST_PAYMENT_RATIO_MEAN` = 0.16 (15.4x median), `YEARS_BIRTH` = 0.44 (14.0x median), `EXT_SOURCE_3` = -1.37 (13.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 70303

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.39 (102.3x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `PREV_APPROVAL_RATE` = -0.36 (18.6x median), `CREDIT_TERM_MONTHS` = -1.39 (17.4x median), `AMT_ANNUITY` = -1.28 (15.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 70347

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `YEARS_BIRTH` = 1.31 (40.2x median), `CREDIT_TERM_MONTHS` = 1.17 (26.6x median), `YEARS_EMPLOYED` = 4.56 (22.8x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.42 (18.3x median), `OWN_CAR_AGE` = 6.68 (15.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 70374

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.65 (195.8x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `CREDIT_TERM_MONTHS` = -1.48 (31.3x median), `BUREAU_BB_DPD_RATIO_MEAN` = 5.44 (29.0x median), `YEARS_BIRTH` = 0.94 (28.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 70591

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `POS_SK_DPD_MEAN` = 6.75 (34.2x median), `EXT_SOURCE_1` = 0.44 (31.6x median), `YEARS_EMPLOYED` = 4.68 (14.9x median), `EXT_SOURCE_3` = -0.88 (8.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 70902

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_DPD_RATIO_MEAN` = 12.07 (63.1x median), `PREV_APPROVAL_RATE` = -0.92 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_1` = 0.44 (31.8x median), `EXT_SOURCE_3` = -1.96 (18.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 71024

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 32.45 (168.1x median), `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `AMT_ANNUITY` = 1.52 (16.0x median), `ANNUITY_TO_INCOME` = 1.31 (15.0x median), `YEARS_BIRTH` = 1.56 (11.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 71987

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 12.46 (251.3x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_ACTIVE_RATIO` = 1.25 (22.2x median), `AMT_ANNUITY` = 1.05 (10.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 72023

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 1.41 (36.7x median), `YEARS_BIRTH` = 0.79 (24.6x median), `CREDIT_TERM_MONTHS` = -1.08 (22.6x median), `BUREAU_COUNT` = 3.78 (22.0x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 2.43 (18.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 72211

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_2` = -2.62 (31.5x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `OWN_CAR_AGE` = 6.68 (15.7x median), `YEARS_BIRTH` = -1.91 (4.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 72625

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.38 (103.1x median), `YEARS_BIRTH` = -1.46 (42.4x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_3` = -2.12 (20.1x median), `POS_MONTHS_COUNT` = 0.68 (17.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 72750

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (10.1x median), `BUREAU_COUNT` = -1.06 (4.9x median), `INST_SEVERE_LATE_RATIO` = 19.45 (4.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 72804

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.09 (80.3x median), `YEARS_BIRTH` = 0.72 (22.5x median), `POS_MONTHS_COUNT` = 0.60 (15.1x median), `AMT_INCOME_TOTAL` = 1.40 (11.9x median), `EXT_SOURCE_3` = 1.12 (9.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 72853

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_MONTHS_COUNT` = -1.13 (31.3x median), `CREDIT_TERM_MONTHS` = 1.19 (27.0x median), `EXT_SOURCE_1` = -0.32 (24.5x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 73377

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `ANNUITY_TO_INCOME` = 1.16 (13.5x median), `YEARS_BIRTH` = -1.31 (11.1x median), `AMT_ANNUITY` = 0.92 (9.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 74122

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 23.89 (467.5x median), `EXT_SOURCE_1` = -2.73 (203.8x median), `BUREAU_BB_DPD_RATIO_MEAN` = 18.07 (93.9x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 74413

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `ANNUITY_TO_INCOME` = 1.08 (12.6x median), `EXT_SOURCE_2` = -1.86 (10.3x median), `CREDIT_TERM_MONTHS` = -0.79 (9.4x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 74475

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `POS_MONTHS_COUNT` = -0.93 (25.9x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CREDIT_TERM_MONTHS` = 0.69 (16.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 74508

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.09 (79.6x median), `POS_MONTHS_COUNT` = 1.77 (46.4x median), `YEARS_EMPLOYED` = 3.01 (15.4x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 0.59 (12.4x median), `BUREAU_BB_DPD_RATIO_MEAN` = 2.17 (12.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 74634

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.43 (179.5x median), `AMT_CREDIT` = 0.93 (30.3x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `PREV_REFUSED_COUNT` = 7.90 (11.0x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.59 (10.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 74873

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 9.30 (187.9x median), `EXT_SOURCE_1` = 0.50 (36.1x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `ANNUITY_TO_INCOME` = 2.15 (24.1x median), `CREDIT_TERM_MONTHS` = -1.52 (19.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 75806

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.49 (37.2x median), `BUREAU_ACTIVE_RATIO` = 1.51 (26.6x median), `CREDIT_TERM_MONTHS` = -0.92 (19.2x median), `AMT_ANNUITY` = -2.04 (15.5x median), `YEARS_EMPLOYED` = 2.35 (12.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 76232

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 9.07 (178.1x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_BB_DPD_RATIO_MEAN` = 6.02 (31.9x median), `INST_SEVERE_LATE_RATIO` = 4.39 (27.1x median), `INST_DPD_MEAN` = 2.21 (20.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 76282

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 1.78 (36.8x median), `EXT_SOURCE_1` = -0.33 (25.5x median), `AMT_ANNUITY` = -1.64 (19.3x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median), `CC_MONTHS_COUNT` = 3.37 (8.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 76480

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 3.31 (87.4x median), `CREDIT_TERM_MONTHS` = 1.67 (37.6x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_COUNT` = 3.78 (22.0x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.62 (21.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 76560

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 7.60 (149.3x median), `BUREAU_BB_DPD_RATIO_MEAN` = 6.40 (33.9x median), `BUREAU_DAYS_CREDIT_MEAN` = -2.25 (29.5x median), `YEARS_BIRTH` = -0.84 (24.2x median), `CREDIT_TERM_MONTHS` = -0.89 (18.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 76587

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.99 (146.8x median), `POS_MONTHS_COUNT` = 3.35 (88.5x median), `YEARS_BIRTH` = 1.16 (35.6x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.58 (27.8x median), `BUREAU_ACTIVE_RATIO` = 1.41 (24.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 76732

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_CREDIT` = -0.76 (22.8x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `AMT_ANNUITY` = -1.04 (16.7x median), `INST_LATE_RATIO` = 2.01 (13.4x median), `INST_DPD_MAX` = 1.26 (11.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 76734

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.72 (126.9x median), `INST_SEVERE_LATE_RATIO` = 8.06 (48.9x median), `INST_LATE_RATIO` = 5.09 (32.4x median), `INST_DPD_MEAN` = 1.40 (15.9x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.52 (9.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 76846

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟠 Tipe C — Risk Signal** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `YEARS_BIRTH` = -1.06 (30.6x median), `CREDIT_TERM_MONTHS` = 1.18 (26.8x median), `CREDIT_TO_INCOME` = 4.43 (20.0x median) |
| Justifikasi | Kombinasi finansial kontradiktif (mis. rasio cicilan/pendapatan ekstrem, income rendah + credit besar, atau skor eksternal tinggi di cluster bermasalah). |
| Business Impact | Underwriting: matikan auto-approve, wajibkan manual review oleh underwriter senior + verifikasi pendapatan fisik. |

---

## ROW_ID 76932

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `AMT_CREDIT` = -2.29 (71.0x median), `EXT_SOURCE_1` = -0.82 (61.7x median), `AMT_ANNUITY` = -1.67 (26.3x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.59 (10.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 77142

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_2` = -2.33 (28.1x median), `INST_SEVERE_LATE_RATIO` = 3.37 (21.0x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `INST_DPD_MEAN` = 0.68 (7.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 77165

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -3.23 (240.9x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.46 (8.1x median), `BUREAU_ACTIVE_RATIO` = -0.48 (7.1x median), `YEARS_BIRTH` = -1.35 (6.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 77387

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_CREDIT` = -0.63 (18.8x median), `AMT_ANNUITY` = -0.81 (13.3x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.31 (7.1x median), `EXT_SOURCE_3` = -1.34 (7.0x median), `BUREAU_COUNT` = 2.02 (6.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 77589

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 7.33 (44.6x median), `INST_LATE_RATIO` = 5.63 (10.0x median), `BUREAU_COUNT` = 1.58 (9.8x median), `INST_DPD_MEAN` = 0.96 (9.4x median), `BUREAU_DAYS_CREDIT_MEAN` = -0.75 (4.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 77738

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 1.97 (44.2x median), `BUREAU_COUNT` = 5.10 (29.3x median), `YEARS_BIRTH` = -0.93 (26.8x median), `BUREAU_ACTIVE_RATIO` = -0.66 (10.1x median), `POS_MONTHS_COUNT` = 0.40 (9.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 77976

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_BIRTH` = 1.07 (33.0x median), `POS_MONTHS_COUNT` = -0.73 (20.5x median), `EXT_SOURCE_3` = -1.62 (15.6x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.20 (15.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 78255

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `EXT_SOURCE_3` = -2.94 (27.5x median), `CREDIT_TERM_MONTHS` = -0.74 (8.7x median), `ANNUITY_TO_INCOME` = -0.81 (7.7x median), `YEARS_BIRTH` = -0.80 (7.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 78366

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 5.30 (32.5x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `INST_DPD_MEAN` = 1.02 (11.9x median), `INST_LATE_RATIO` = 1.65 (11.2x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.59 (10.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 78998

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.71 (53.9x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `INST_DPD_MAX` = 2.73 (23.2x median), `INST_SEVERE_LATE_RATIO` = 3.02 (18.9x median), `INST_DPD_MEAN` = 1.66 (18.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 79170

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 1.89 (49.7x median), `YEARS_BIRTH` = 1.33 (40.7x median), `EXT_SOURCE_3` = -1.75 (16.7x median), `BUREAU_DAYS_CREDIT_MEAN` = 0.68 (10.2x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = -1.03 (9.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 79868

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 7.87 (40.0x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `EXT_SOURCE_3` = -1.93 (18.4x median), `EXT_SOURCE_2` = -2.71 (14.5x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.97 (3.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 79901

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `AMT_CREDIT` = 0.44 (15.0x median), `INST_SEVERE_LATE_RATIO` = 2.14 (13.7x median), `BUREAU_COUNT` = 3.56 (12.7x median), `AMT_ANNUITY` = 0.58 (7.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 80441

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `POS_SK_DPD_MEAN` = 7.89 (40.1x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CREDIT_TERM_MONTHS` = 1.26 (17.6x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (10.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 80943

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_CREDIT` = 1.35 (43.4x median), `AMT_ANNUITY` = 1.30 (18.7x median), `BUREAU_ACTIVE_RATIO` = -0.62 (9.5x median), `BUREAU_COUNT` = 1.80 (5.9x median), `CC_UTILIZATION_MAX` = 2.28 (5.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 81043

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 6.96 (140.8x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `AMT_ANNUITY` = -1.93 (22.5x median), `BUREAU_COUNT` = 3.34 (19.6x median), `PREV_APPROVAL_RATE` = 0.41 (19.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 81225

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `AMT_CREDIT` = -1.01 (30.8x median), `AMT_ANNUITY` = -1.10 (17.7x median), `EXT_SOURCE_2` = -2.08 (9.2x median), `EXT_SOURCE_3` = 1.11 (7.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 81615

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_ANNUITY` = 1.66 (24.2x median), `INST_LATE_RATIO` = 3.69 (23.8x median), `BUREAU_BB_DPD_RATIO_MEAN` = 3.28 (17.9x median), `INST_DPD_MAX` = 1.46 (12.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 82130

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 19.62 (395.0x median), `EXT_SOURCE_1` = 1.19 (87.0x median), `YEARS_BIRTH` = 1.14 (34.9x median), `POS_MONTHS_COUNT` = -0.97 (27.0x median), `YEARS_EMPLOYED` = 1.73 (9.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 82211

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 1.21 (31.3x median), `YEARS_BIRTH` = 0.83 (25.6x median), `BUREAU_ACTIVE_RATIO` = 1.41 (24.8x median), `EXT_SOURCE_3` = -2.26 (21.3x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.29 (14.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 82258

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.65 (121.7x median), `POS_MONTHS_COUNT` = 1.85 (48.6x median), `CREDIT_TERM_MONTHS` = 1.70 (38.1x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_BIRTH` = -0.91 (26.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 82484

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.10 (80.4x median), `POS_MONTHS_COUNT` = 1.57 (41.0x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_DAYS_CREDIT_MEAN` = -2.01 (26.3x median), `YEARS_BIRTH` = 0.66 (20.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 83120

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 1.29 (33.5x median), `BUREAU_ACTIVE_RATIO` = 1.14 (20.3x median), `YEARS_BIRTH` = 0.51 (16.2x median), `CREDIT_TERM_MONTHS` = -0.58 (11.7x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.92 (11.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 83659

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.87 (12.6x median), `YEARS_BIRTH` = -0.89 (12.5x median), `EXT_SOURCE_3` = -0.96 (9.7x median), `PREV_REFUSED_COUNT` = 3.45 (8.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 83871

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 11.16 (160.4x median), `YEARS_BIRTH` = 1.53 (46.5x median), `POS_MONTHS_COUNT` = 1.49 (38.9x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 84069

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.47 (36.2x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `CREDIT_TERM_MONTHS` = -1.48 (31.5x median), `YEARS_BIRTH` = -0.89 (25.5x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 84164

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.79 (134.0x median), `YEARS_BIRTH` = -1.08 (31.1x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `POS_MONTHS_COUNT` = 0.68 (17.3x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 1.85 (13.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 84223

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.11 (83.5x median), `BUREAU_BB_DPD_RATIO_MEAN` = 3.99 (21.5x median), `INST_LATE_RATIO` = 2.45 (16.1x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.58 (12.5x median), `AMT_CREDIT` = 0.34 (11.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 84473

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 25.23 (507.6x median), `EXT_SOURCE_1` = 1.16 (84.8x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `YEARS_BIRTH` = 1.01 (31.0x median), `POS_MONTHS_COUNT` = -0.93 (25.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 84632

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 37.66 (736.4x median), `BUREAU_BB_DPD_RATIO_MEAN` = 23.77 (123.3x median), `POS_SK_DPD_MEAN` = 21.74 (112.4x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 84642

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -1.76 (87.5x median), `POS_SK_DPD_MEAN` = 8.25 (42.0x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CC_UTILIZATION_MEAN` = 3.56 (9.8x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 84781

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `YEARS_BIRTH` = 1.35 (41.2x median), `CREDIT_TERM_MONTHS` = 1.70 (38.1x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 84898

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 14.72 (296.7x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `AMT_ANNUITY` = -1.90 (22.2x median), `ANNUITY_TO_INCOME` = -1.26 (12.5x median), `AMT_CREDIT` = -1.40 (9.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 85610

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.39 (29.6x median), `AMT_ANNUITY` = -1.94 (22.7x median), `CREDIT_TERM_MONTHS` = -1.51 (18.9x median), `AMT_CREDIT` = -2.52 (17.0x median), `ANNUITY_TO_INCOME` = -1.27 (12.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 85886

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 1.65 (43.2x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CREDIT_TERM_MONTHS` = 0.53 (12.6x median), `AMT_INCOME_TOTAL` = 1.40 (11.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 87344

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 1.26 (28.7x median), `POS_MONTHS_COUNT` = 0.97 (24.8x median), `EXT_SOURCE_3` = -1.90 (18.1x median), `INST_DPD_MAX` = 1.77 (18.0x median), `BUREAU_ACTIVE_RATIO` = 0.89 (16.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 87435

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_CREDIT` = -1.12 (34.2x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.87 (18.0x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `EXT_SOURCE_3` = -2.48 (13.8x median), `AMT_ANNUITY` = -0.39 (6.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 87665

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_CREDIT` = 1.17 (37.9x median), `BUREAU_ACTIVE_RATIO` = 1.14 (20.3x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.74 (15.5x median), `EXT_SOURCE_3` = -2.08 (11.4x median), `CREDIT_TERM_MONTHS` = 1.70 (9.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 87741

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.88 (138.8x median), `POS_SK_DPD_MEAN` = 7.93 (40.3x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `CREDIT_TERM_MONTHS` = 1.26 (17.6x median), `BUREAU_COUNT` = 2.24 (13.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 87912

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.09 (82.2x median), `BUREAU_BB_DPD_RATIO_MEAN` = 2.60 (14.4x median), `AMT_CREDIT` = 0.42 (14.2x median), `BUREAU_ACTIVE_RATIO` = -0.84 (13.3x median), `CC_UTILIZATION_MEAN` = 3.98 (10.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 87976

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.67 (125.2x median), `INST_SEVERE_LATE_RATIO` = 3.02 (18.9x median), `INST_DPD_MEAN` = 1.04 (10.2x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.18 (7.6x median), `INST_LATE_RATIO` = 3.80 (7.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 88867

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 4.23 (112.3x median), `EXT_SOURCE_1` = -1.03 (77.2x median), `EXT_SOURCE_3` = -2.54 (23.8x median), `CREDIT_TERM_MONTHS` = -1.05 (21.9x median), `YEARS_BIRTH` = -0.41 (11.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 90046

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.52 (37.7x median), `CREDIT_TERM_MONTHS` = -1.09 (22.8x median), `YEARS_BIRTH` = -0.53 (14.7x median), `BUREAU_COUNT` = 2.24 (13.4x median), `INST_LATE_RATIO` = 2.90 (11.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 90071

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.54 (38.9x median), `BUREAU_ACTIVE_RATIO` = 1.51 (26.6x median), `INST_DPD_MAX` = 3.12 (26.4x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.01 (20.7x median), `EXT_SOURCE_3` = -2.03 (11.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 91369

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.23 (90.0x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.29 (26.4x median), `AMT_ANNUITY` = 0.79 (11.0x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median), `YEARS_EMPLOYED` = 2.12 (7.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 92160

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.82 (62.1x median), `AMT_CREDIT` = -0.85 (25.8x median), `BUREAU_ACTIVE_RATIO` = 0.86 (15.5x median), `CNT_CHILDREN` = 3.60 (7.2x median), `CREDIT_TERM_MONTHS` = -1.48 (6.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 92181

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.67 (197.3x median), `YEARS_EMPLOYED` = 4.25 (19.7x median), `YEARS_BIRTH` = 0.93 (11.0x median), `AMT_INCOME_TOTAL` = 0.86 (6.8x median), `BUREAU_DAYS_CREDIT_MEAN` = -0.73 (4.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 92355

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_ANNUITY` = 1.42 (14.9x median), `EXT_SOURCE_3` = -1.31 (12.8x median), `BUREAU_COUNT` = 1.58 (9.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 92642

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 6.21 (37.9x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `AMT_INCOME_TOTAL` = -1.96 (19.0x median), `INST_DPD_MEAN` = 1.12 (10.9x median), `YEARS_BIRTH` = -0.42 (6.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 93013

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 18.92 (380.9x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `POS_SK_DPD_MEAN` = 5.57 (28.0x median), `CREDIT_TERM_MONTHS` = 1.67 (23.1x median), `EXT_SOURCE_3` = 1.34 (11.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 93056

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.92 (143.3x median), `YEARS_BIRTH` = -1.06 (30.7x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `AMT_ANNUITY` = -1.40 (10.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 93076

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.61 (120.3x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `OWN_CAR_AGE` = 6.68 (15.7x median), `CNT_CHILDREN` = 3.60 (7.2x median), `PREV_REFUSED_COUNT` = 2.33 (6.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 93305

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 1.96 (43.8x median), `POS_MONTHS_COUNT` = 1.01 (25.9x median), `YEARS_BIRTH` = 0.55 (17.3x median), `EXT_SOURCE_3` = 1.40 (11.6x median), `AMT_INCOME_TOTAL` = 1.05 (8.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 94006

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.08 (79.5x median), `EXT_SOURCE_3` = 1.29 (10.6x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.20 (7.7x median), `CREDIT_TO_INCOME` = 4.20 (6.8x median), `BUREAU_COUNT` = 0.70 (4.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 94414

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `YEARS_BIRTH` = -1.23 (17.0x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (11.5x median), `AMT_INCOME_TOTAL` = -1.06 (10.7x median), `OWN_CAR_AGE` = 3.11 (7.8x median), `BUREAU_ACTIVE_RATIO` = -1.11 (5.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 94812

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.66 (47.8x median), `CREDIT_TERM_MONTHS` = 1.67 (37.6x median), `POS_MONTHS_COUNT` = -0.81 (22.7x median), `YEARS_BIRTH` = 0.55 (17.5x median), `BUREAU_DAYS_CREDIT_MEAN` = -0.87 (10.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 94915

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 24.22 (125.3x median), `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `INST_DPD_MEAN` = 110.97 (39.2x median), `AMT_ANNUITY` = 2.18 (23.4x median), `ANNUITY_TO_INCOME` = 1.16 (13.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 95252

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.11 (157.4x median), `YEARS_BIRTH` = -1.21 (35.1x median), `POS_MONTHS_COUNT` = -0.65 (18.4x median), `CREDIT_TERM_MONTHS` = -0.80 (16.4x median), `AMT_INCOME_TOTAL` = -1.53 (15.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 95409

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.42 (106.4x median), `CREDIT_TERM_MONTHS` = 1.96 (43.8x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.18 (15.0x median), `CREDIT_TO_INCOME` = 3.11 (14.4x median), `POS_MONTHS_COUNT` = 0.56 (14.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 95510

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.79 (59.7x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.39 (28.2x median), `AMT_CREDIT` = 0.74 (24.4x median), `AMT_ANNUITY` = 1.08 (15.4x median), `CC_MONTHS_COUNT` = 3.13 (8.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 95592

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.36 (25.9x median), `POS_SK_DPD_MEAN` = 4.86 (24.4x median), `PREV_APPROVAL_RATE` = 0.41 (19.4x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `ANNUITY_TO_INCOME` = 0.96 (11.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 95813

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 1.79 (31.4x median), `POS_MONTHS_COUNT` = -1.13 (31.3x median), `YEARS_BIRTH` = -0.74 (21.0x median), `EXT_SOURCE_3` = -2.13 (20.2x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.47 (16.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 96315

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (10.1x median), `EXT_SOURCE_2` = -1.78 (9.8x median), `YEARS_BIRTH` = -0.72 (6.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 96734

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.08 (155.4x median), `YEARS_BIRTH` = -1.74 (50.7x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `CREDIT_TERM_MONTHS` = -1.30 (27.4x median), `EXT_SOURCE_3` = -1.51 (14.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 97127

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 1.95 (26.7x median), `PREV_APPROVAL_RATE` = -0.45 (23.2x median), `CREDIT_TO_INCOME` = 1.14 (8.2x median), `AMT_CREDIT` = 1.18 (6.5x median), `BUREAU_COUNT` = 0.70 (4.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 97161

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 2.63 (52.4x median), `EXT_SOURCE_1` = -0.48 (36.4x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = 1.28 (29.1x median), `YEARS_BIRTH` = 0.82 (25.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 97618

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.65 (121.2x median), `AMT_CREDIT` = 1.15 (37.0x median), `AMT_ANNUITY` = 1.50 (21.7x median), `BUREAU_ACTIVE_RATIO` = 0.86 (15.5x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.54 (11.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 97627

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.37 (100.4x median), `AMT_CREDIT` = 1.23 (39.7x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_COUNT` = 5.76 (21.2x median), `INST_LATE_RATIO` = 1.59 (10.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 97966

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 11.37 (229.3x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `ANNUITY_TO_INCOME` = 2.20 (24.7x median), `YEARS_EMPLOYED` = 4.57 (14.5x median), `BUREAU_ACTIVE_RATIO` = 0.78 (14.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 98187

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `EXT_SOURCE_2` = -1.41 (17.4x median), `OWN_CAR_AGE` = 6.68 (15.7x median), `AMT_INCOME_TOTAL` = -1.06 (4.0x median), `YEARS_BIRTH` = -1.76 (3.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 98450

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 3.13 (62.1x median), `YEARS_BIRTH` = 1.75 (53.0x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `POS_MONTHS_COUNT` = 1.33 (34.5x median), `BUREAU_BB_DPD_RATIO_MEAN` = 3.07 (16.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 98546

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.34 (174.4x median), `EXT_SOURCE_3` = -2.38 (22.4x median), `PREV_REFUSED_COUNT` = 9.57 (22.1x median), `POS_MONTHS_COUNT` = 0.76 (19.4x median), `PREV_COUNT` = 4.31 (13.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 99866

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `POS_SK_DPD_MEAN` = 5.66 (28.5x median), `AMT_ANNUITY` = -1.13 (13.6x median), `EXT_SOURCE_2` = -1.84 (10.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 99993

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `EXT_SOURCE_2` = 1.14 (12.2x median), `INST_LATE_RATIO` = 2.32 (4.7x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (4.5x median), `AMT_INCOME_TOTAL` = -1.06 (4.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 100321

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 2.42 (63.7x median), `YEARS_BIRTH` = 1.30 (39.6x median), `BUREAU_BB_DPD_RATIO_MEAN` = 5.34 (28.4x median), `EXT_SOURCE_3` = -2.53 (23.7x median), `AMT_INCOME_TOTAL` = 1.24 (10.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 100412

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟠 Tipe C — Risk Signal** |
| Top Deviating Features | `YEARS_BIRTH` = 1.69 (20.9x median), `AMT_INCOME_TOTAL` = -2.13 (20.5x median), `BUREAU_ACTIVE_RATIO` = 2.03 (13.4x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.27 (10.2x median), `ANNUITY_TO_INCOME` = 3.22 (7.1x median) |
| Justifikasi | Kombinasi finansial kontradiktif (mis. rasio cicilan/pendapatan ekstrem, income rendah + credit besar, atau skor eksternal tinggi di cluster bermasalah). |
| Business Impact | Underwriting: matikan auto-approve, wajibkan manual review oleh underwriter senior + verifikasi pendapatan fisik. |

---

## ROW_ID 100446

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 21.12 (413.4x median), `BUREAU_BB_DPD_RATIO_MEAN` = 28.40 (147.0x median), `POS_SK_DPD_MEAN` = 5.98 (30.2x median), `PREV_APPROVAL_RATE` = -0.45 (23.2x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 100469

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 4.56 (120.9x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `YEARS_EMPLOYED` = 4.17 (20.9x median), `YEARS_BIRTH` = 0.55 (17.4x median), `BUREAU_DAYS_CREDIT_MEAN` = -0.78 (9.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 100557

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.38 (103.7x median), `POS_SK_DPD_MEAN` = 4.35 (63.2x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `EXT_SOURCE_3` = -2.61 (24.4x median), `POS_MONTHS_COUNT` = 0.84 (21.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 100862

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.91 (216.8x median), `AMT_CREDIT` = 1.46 (46.9x median), `AMT_ANNUITY` = 0.89 (12.5x median), `CREDIT_TERM_MONTHS` = 1.68 (9.6x median), `CC_MONTHS_COUNT` = 3.37 (8.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 100953

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.81 (59.0x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.41 (28.6x median), `AMT_ANNUITY` = 1.72 (25.0x median), `BUREAU_ACTIVE_RATIO` = 0.78 (14.2x median), `PREV_REFUSED_COUNT` = 8.46 (11.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 101138

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.76 (131.6x median), `BUREAU_BB_DPD_RATIO_MEAN` = 13.28 (69.3x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 101289

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 1.89 (49.7x median), `YEARS_BIRTH` = 1.62 (49.4x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.58 (27.8x median), `BUREAU_COUNT` = 3.34 (19.6x median), `EXT_SOURCE_3` = -1.71 (16.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 101658

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.42 (179.0x median), `YEARS_BIRTH` = -1.04 (30.0x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 1.85 (13.9x median), `PREV_APPROVAL_RATE` = -1.44 (9.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 101687

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.74 (128.5x median), `POS_MONTHS_COUNT` = 3.75 (99.3x median), `INST_DPD_MAX` = 5.13 (50.3x median), `YEARS_BIRTH` = 1.46 (44.5x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 101816

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.70 (126.9x median), `POS_SK_DPD_MEAN` = 6.97 (35.3x median), `BUREAU_ACTIVE_RATIO` = 1.25 (22.2x median), `PREV_APPROVAL_RATE` = 0.41 (19.4x median), `AMT_ANNUITY` = -1.18 (14.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 102066

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_CREDIT` = -0.76 (22.8x median), `INST_LATE_RATIO` = 3.17 (20.6x median), `AMT_ANNUITY` = -1.04 (16.7x median), `BUREAU_COUNT` = 3.78 (13.5x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.23 (5.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 102177

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_REQ_CREDIT_BUREAU_YEAR` = 2.43 (18.5x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `YEARS_BIRTH` = 0.41 (13.2x median), `POS_MONTHS_COUNT` = -0.45 (13.0x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.91 (10.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 102983

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.83 (60.3x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = 0.87 (20.0x median), `OWN_CAR_AGE` = 6.68 (15.7x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 1.85 (13.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 103085

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 5.71 (28.8x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CREDIT_TERM_MONTHS` = 1.26 (17.6x median), `EXT_SOURCE_2` = -2.16 (11.7x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (10.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 103362

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `INST_PAYMENT_RATIO_MEAN` = 1.46 (138.1x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_2` = -2.52 (30.4x median), `EXT_SOURCE_1` = -0.37 (28.5x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 103479

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.95 (143.9x median), `YEARS_BIRTH` = 0.87 (27.1x median), `INST_DPD_MAX` = 2.46 (24.6x median), `YEARS_EMPLOYED` = 4.44 (22.2x median), `EXT_SOURCE_3` = -1.44 (13.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 103641

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_CREDIT` = 0.80 (26.1x median), `BUREAU_COUNT` = 3.34 (11.8x median), `AMT_ANNUITY` = 0.78 (10.8x median), `BUREAU_BB_DPD_RATIO_MEAN` = 1.15 (6.9x median), `EXT_SOURCE_3` = -1.30 (6.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 103774

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.02 (77.1x median), `INST_SEVERE_LATE_RATIO` = 6.21 (37.9x median), `EXT_SOURCE_3` = -1.79 (17.1x median), `BUREAU_BB_DPD_RATIO_MEAN` = 2.20 (12.3x median), `INST_DPD_MEAN` = 0.91 (9.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 103832

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `YEARS_BIRTH` = -0.71 (20.3x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 2.43 (18.5x median), `CREDIT_TERM_MONTHS` = -0.59 (11.9x median), `PREV_APPROVAL_RATE` = -1.64 (11.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 104075

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `EXT_SOURCE_2` = -1.29 (16.0x median), `OWN_CAR_AGE` = 6.68 (15.7x median), `CNT_CHILDREN` = 3.60 (7.2x median), `AMT_INCOME_TOTAL` = -1.66 (6.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 104229

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 3.82 (23.7x median), `YEARS_BIRTH` = 1.35 (16.5x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (11.5x median), `POS_MONTHS_COUNT` = 3.10 (7.9x median), `INST_DPD_MEAN` = 0.78 (7.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 104311

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `POS_SK_DPD_MEAN` = 4.44 (22.2x median), `CREDIT_TERM_MONTHS` = -1.51 (18.9x median), `AMT_CREDIT` = -0.96 (7.1x median), `CREDIT_TO_INCOME` = -0.93 (4.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 105081

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.04 (78.0x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = 1.28 (29.1x median), `AMT_INCOME_TOTAL` = -2.51 (24.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 105144

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 23.91 (481.2x median), `EXT_SOURCE_1` = -0.55 (42.0x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `POS_MONTHS_COUNT` = -1.01 (28.1x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 105220

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `YEARS_BIRTH` = -1.36 (11.4x median), `EXT_SOURCE_2` = -1.74 (9.7x median), `OWN_CAR_AGE` = 3.45 (8.6x median), `ANNUITY_TO_INCOME` = 0.56 (7.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 105455

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -1.24 (62.0x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `ANNUITY_TO_INCOME` = 0.90 (10.6x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.33 (9.3x median), `AMT_ANNUITY` = 0.75 (7.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 105551

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `YEARS_BIRTH` = -1.31 (37.9x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `CREDIT_TERM_MONTHS` = 0.60 (14.2x median), `POS_MONTHS_COUNT` = 0.52 (13.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 105754

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.80 (58.3x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `AMT_CREDIT` = -0.45 (13.1x median), `AMT_ANNUITY` = -0.63 (10.5x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.59 (10.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 105788

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.51 (111.3x median), `POS_MONTHS_COUNT` = 1.29 (33.5x median), `YEARS_BIRTH` = 1.01 (31.2x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `AMT_ANNUITY` = -2.06 (15.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 105807

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.87 (137.8x median), `PREV_APPROVAL_RATE` = -1.97 (98.1x median), `POS_SK_DPD_MEAN` = 6.22 (31.4x median), `EXT_SOURCE_3` = -2.45 (23.0x median), `ANNUITY_TO_INCOME` = 1.08 (12.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 106129

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.78 (56.9x median), `CREDIT_TERM_MONTHS` = 1.88 (42.1x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `POS_MONTHS_COUNT` = 0.72 (18.4x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 106248

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = -1.21 (25.4x median), `POS_MONTHS_COUNT` = 0.72 (18.4x median), `AMT_INCOME_TOTAL` = 1.84 (15.8x median), `YEARS_EMPLOYED` = 2.28 (11.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 106510

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 12.90 (66.3x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_ACTIVE_RATIO` = 1.51 (26.6x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 3.82 (12.5x median), `YEARS_BIRTH` = 1.23 (8.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 106902

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.00 (23.2x median), `POS_MONTHS_COUNT` = -0.61 (17.3x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.35 (15.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 107064

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -1.02 (51.1x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `POS_SK_DPD_MEAN` = 3.65 (18.0x median), `YEARS_BIRTH` = 1.14 (7.7x median), `EXT_SOURCE_3` = 0.94 (7.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 107225

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_CREDIT` = -0.97 (29.4x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.59 (10.5x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (9.2x median), `YEARS_BIRTH` = -1.63 (7.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 107485

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 2.86 (75.6x median), `CREDIT_TERM_MONTHS` = 3.12 (69.3x median), `CREDIT_TO_INCOME` = 9.32 (41.1x median), `YEARS_BIRTH` = 1.31 (40.2x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 107699

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.23 (90.5x median), `CREDIT_TERM_MONTHS` = 1.69 (38.1x median), `YEARS_BIRTH` = 1.01 (31.1x median), `POS_MONTHS_COUNT` = -0.89 (24.8x median), `YEARS_EMPLOYED` = 2.58 (13.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 107728

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.11 (83.3x median), `AMT_CREDIT` = -1.51 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `AMT_ANNUITY` = -2.02 (31.6x median), `EXT_SOURCE_3` = -1.75 (9.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 107925

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.01 (150.6x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.14 (23.3x median), `BUREAU_COUNT` = 4.88 (17.8x median), `EXT_SOURCE_3` = -2.60 (14.5x median), `AMT_CREDIT` = -0.36 (10.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 107990

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.08 (153.7x median), `CREDIT_TERM_MONTHS` = 1.68 (37.8x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_BIRTH` = 0.85 (26.4x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 108158

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.14 (85.7x median), `PREV_APPROVAL_RATE` = -1.24 (62.0x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = -1.07 (13.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 108379

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.72 (126.8x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_CREDIT` = 0.74 (24.1x median), `BUREAU_ACTIVE_RATIO` = 1.25 (22.2x median), `AMT_ANNUITY` = 1.21 (17.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 108397

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `ANNUITY_TO_INCOME` = 1.94 (21.9x median), `OWN_CAR_AGE` = 6.79 (15.9x median), `YEARS_BIRTH` = -1.24 (10.5x median), `AMT_ANNUITY` = 1.00 (10.1x median), `EXT_SOURCE_3` = -0.87 (8.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 108436

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `INST_SEVERE_LATE_RATIO` = 3.82 (23.7x median), `EXT_SOURCE_2` = -1.13 (14.1x median), `INST_DPD_MEAN` = 1.43 (13.6x median), `INST_DPD_MAX` = 1.73 (11.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 108528

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.29 (168.9x median), `CREDIT_TERM_MONTHS` = 1.16 (16.3x median), `BUREAU_ACTIVE_RATIO` = 0.86 (15.5x median), `EXT_SOURCE_3` = -0.98 (9.8x median), `YEARS_EMPLOYED` = 1.97 (6.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 109324

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `INST_SEVERE_LATE_RATIO` = 4.74 (29.1x median), `EXT_SOURCE_3` = -1.94 (18.4x median), `INST_DPD_MEAN` = 1.56 (14.7x median), `INST_LATE_RATIO` = 4.14 (7.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 109409

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟠 Tipe C — Risk Signal** |
| Top Deviating Features | `YEARS_BIRTH` = 1.68 (20.7x median), `AMT_INCOME_TOTAL` = -1.40 (13.8x median), `EXT_SOURCE_3` = 1.33 (11.0x median), `CC_MONTHS_COUNT` = 3.45 (8.9x median), `ANNUITY_TO_INCOME` = 3.51 (7.8x median) |
| Justifikasi | Kombinasi finansial kontradiktif (mis. rasio cicilan/pendapatan ekstrem, income rendah + credit besar, atau skor eksternal tinggi di cluster bermasalah). |
| Business Impact | Underwriting: matikan auto-approve, wajibkan manual review oleh underwriter senior + verifikasi pendapatan fisik. |

---

## ROW_ID 109624

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.58 (42.0x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `POS_MONTHS_COUNT` = 0.52 (13.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 110051

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -1.35 (67.4x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 3.04 (60.4x median), `BUREAU_COUNT` = 4.44 (25.7x median), `POS_SK_DPD_MEAN` = 3.56 (17.6x median), `BUREAU_BB_DPD_RATIO_MEAN` = 2.16 (12.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 110231

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_MONTHS_COUNT` = -1.13 (31.3x median), `YEARS_BIRTH` = 0.70 (21.8x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `CREDIT_TERM_MONTHS` = -0.90 (18.8x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 110259

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.91 (66.5x median), `AMT_CREDIT` = 0.32 (11.1x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median), `PREV_REFUSED_COUNT` = 5.12 (6.8x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.31 (5.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 110413

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `EXT_SOURCE_2` = -2.23 (27.0x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `INST_LATE_RATIO` = 3.40 (6.4x median), `INST_DPD_MEAN` = 0.58 (6.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 110460

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.43 (107.3x median), `POS_SK_DPD_MEAN` = 11.81 (60.6x median), `PREV_APPROVAL_RATE` = -1.10 (55.2x median), `YEARS_BIRTH` = -1.21 (10.3x median), `AMT_ANNUITY` = -0.73 (9.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 110514

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.06 (151.7x median), `POS_MONTHS_COUNT` = 0.64 (16.2x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.27 (14.7x median), `YEARS_EMPLOYED` = 2.52 (13.1x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.00 (12.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 110622

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_CREDIT` = -1.40 (43.0x median), `AMT_ANNUITY` = -2.39 (37.2x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.60 (12.7x median), `BUREAU_ACTIVE_RATIO` = -0.66 (10.1x median), `CC_MONTHS_COUNT` = 2.40 (6.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 110745

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.84 (63.4x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_BIRTH` = -1.23 (16.9x median), `BUREAU_DAYS_CREDIT_MEAN` = 0.68 (5.9x median), `EXT_SOURCE_3` = -0.45 (5.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 110841

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_LATE_RATIO` = 2.47 (16.3x median), `BUREAU_COUNT` = 4.44 (16.1x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.58 (10.3x median), `EXT_SOURCE_3` = 1.27 (8.6x median), `AMT_ANNUITY` = 0.50 (6.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 110863

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.52 (112.0x median), `CREDIT_TERM_MONTHS` = 1.96 (43.9x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_BIRTH` = 0.84 (25.9x median), `YEARS_EMPLOYED` = 4.14 (20.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 110951

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 4.67 (94.8x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `ANNUITY_TO_INCOME` = 1.51 (17.3x median), `CREDIT_TO_INCOME` = 1.43 (10.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 110960

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.30 (170.0x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `AMT_CREDIT` = -0.54 (16.1x median), `AMT_ANNUITY` = -0.97 (15.7x median), `BUREAU_ACTIVE_RATIO` = -0.62 (9.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 111309

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 3.94 (80.1x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `ANNUITY_TO_INCOME` = 2.05 (23.0x median), `CREDIT_TERM_MONTHS` = 1.66 (22.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 111471

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 3.18 (84.2x median), `CREDIT_TERM_MONTHS` = 2.15 (48.2x median), `YEARS_BIRTH` = -0.51 (14.2x median), `PREV_REFUSED_COUNT` = 5.67 (13.5x median), `EXT_SOURCE_3` = -1.17 (11.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 111535

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `YEARS_EMPLOYED` = 4.20 (19.5x median), `YEARS_BIRTH` = 1.42 (17.4x median), `OWN_CAR_AGE` = 6.79 (15.9x median), `AMT_INCOME_TOTAL` = 1.40 (11.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 112058

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.12 (83.9x median), `YEARS_BIRTH` = -0.93 (26.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `OWN_CAR_AGE` = 6.68 (15.7x median), `ANNUITY_TO_INCOME` = 2.75 (11.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 112072

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `YEARS_BIRTH` = -1.63 (47.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = -0.92 (19.2x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `AMT_INCOME_TOTAL` = 1.97 (17.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 112249

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 23.78 (123.0x median), `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `INST_DPD_MEAN` = 163.15 (58.1x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `INST_SEVERE_LATE_RATIO` = 31.72 (7.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 112344

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.92 (141.7x median), `POS_SK_DPD_MEAN` = 10.61 (54.3x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `CREDIT_TERM_MONTHS` = -1.62 (20.3x median), `EXT_SOURCE_3` = -1.58 (15.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 113086

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.61 (118.5x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.75 (35.4x median), `AMT_ANNUITY` = -1.25 (20.0x median), `CREDIT_TERM_MONTHS` = 2.12 (11.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 113274

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 1.70 (38.1x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_COUNT` = 4.88 (28.1x median), `INST_SEVERE_LATE_RATIO` = 4.30 (26.5x median), `EXT_SOURCE_1` = -0.30 (23.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 113465

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 18.30 (368.6x median), `ANNUITY_TO_INCOME` = 4.35 (47.8x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `CREDIT_TO_INCOME` = 3.85 (25.4x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 113710

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.62 (119.5x median), `INST_LATE_RATIO` = 2.44 (16.1x median), `YEARS_EMPLOYED` = 2.82 (9.8x median), `BUREAU_ACTIVE_RATIO` = -0.32 (4.4x median), `BUREAU_DAYS_CREDIT_MEAN` = -0.94 (4.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 113732

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.38 (27.3x median), `POS_MONTHS_COUNT` = -0.77 (21.6x median), `EXT_SOURCE_3` = -1.71 (16.3x median), `BUREAU_DAYS_CREDIT_MEAN` = 0.91 (13.3x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 1.27 (9.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 113739

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 6.21 (37.9x median), `AMT_INCOME_TOTAL` = -3.42 (15.0x median), `INST_DPD_MEAN` = 1.33 (12.7x median), `BUREAU_ACTIVE_RATIO` = 0.61 (11.3x median), `EXT_SOURCE_2` = 0.87 (9.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 113877

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.58 (190.8x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_EMPLOYED` = 4.39 (20.3x median), `AMT_INCOME_TOTAL` = 2.31 (20.1x median), `YEARS_BIRTH` = 1.06 (12.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 113957

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 20.13 (405.2x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_EMPLOYED` = 4.17 (13.4x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 114071

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 11.00 (215.9x median), `EXT_SOURCE_1` = 1.17 (86.2x median), `BUREAU_BB_DPD_RATIO_MEAN` = 8.32 (43.8x median), `EXT_SOURCE_3` = -2.25 (12.4x median), `AMT_ANNUITY` = -0.69 (11.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 114216

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.54 (31.1x median), `AMT_CREDIT` = -1.01 (30.8x median), `EXT_SOURCE_1` = 0.27 (18.7x median), `EXT_SOURCE_3` = -2.19 (12.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 114231

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.19 (87.1x median), `CREDIT_TERM_MONTHS` = 2.17 (48.6x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `YEARS_EMPLOYED` = 4.20 (21.1x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.59 (20.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 114668

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟠 Tipe C — Risk Signal** |
| Top Deviating Features | `ANNUITY_TO_INCOME` = 4.26 (46.8x median), `CREDIT_TO_INCOME` = 4.70 (30.8x median), `PREV_APPROVAL_RATE` = -0.45 (23.2x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `EXT_SOURCE_2` = -2.71 (14.5x median) |
| Justifikasi | Kombinasi finansial kontradiktif (mis. rasio cicilan/pendapatan ekstrem, income rendah + credit besar, atau skor eksternal tinggi di cluster bermasalah). |
| Business Impact | Underwriting: matikan auto-approve, wajibkan manual review oleh underwriter senior + verifikasi pendapatan fisik. |

---

## ROW_ID 114975

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `YEARS_BIRTH` = -1.81 (53.0x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `EXT_SOURCE_3` = -2.48 (23.3x median), `CREDIT_TERM_MONTHS` = -1.08 (22.6x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.32 (15.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 115348

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.36 (102.2x median), `CC_SK_DPD_MEAN` = 2.47 (50.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CREDIT_TERM_MONTHS` = -1.41 (17.6x median), `BUREAU_DAYS_CREDIT_MEAN` = -2.07 (11.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 115670

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.23 (90.0x median), `YEARS_BIRTH` = 0.75 (23.3x median), `CREDIT_TERM_MONTHS` = 0.88 (20.2x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.03 (13.0x median), `POS_MONTHS_COUNT` = 0.44 (10.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 115828

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -1.24 (62.0x median), `AMT_ANNUITY` = 1.56 (16.5x median), `AMT_INCOME_TOTAL` = 1.84 (9.6x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median), `AMT_CREDIT` = 1.20 (6.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 115885

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 3.14 (83.1x median), `EXT_SOURCE_1` = -0.92 (69.7x median), `CREDIT_TERM_MONTHS` = 1.97 (44.2x median), `YEARS_BIRTH` = -0.63 (17.7x median), `AMT_INCOME_TOTAL` = 1.84 (15.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 115970

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.11 (81.4x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `CREDIT_TERM_MONTHS` = 1.68 (23.1x median), `CREDIT_TO_INCOME` = 3.09 (20.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 116078

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.49 (111.7x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `EXT_SOURCE_3` = -2.40 (22.6x median), `OWN_CAR_AGE` = 6.68 (15.7x median), `INST_SEVERE_LATE_RATIO` = 2.28 (14.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 116338

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.94 (143.2x median), `POS_MONTHS_COUNT` = -0.93 (25.9x median), `BUREAU_ACTIVE_RATIO` = 0.86 (15.5x median), `YEARS_BIRTH` = -0.43 (11.8x median), `CREDIT_TERM_MONTHS` = 0.32 (8.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 116439

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `ANNUITY_TO_INCOME` = 1.70 (19.3x median), `CREDIT_TO_INCOME` = 2.46 (16.6x median), `CREDIT_TERM_MONTHS` = 1.18 (16.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 116514

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.75 (54.9x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `EXT_SOURCE_3` = -1.23 (12.0x median), `AMT_INCOME_TOTAL` = -2.13 (9.0x median), `INST_LATE_RATIO` = 3.98 (7.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 116791

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_3` = -2.37 (22.3x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `YEARS_BIRTH` = 1.35 (9.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 116973

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.61 (118.9x median), `AMT_CREDIT` = -0.87 (26.4x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `EXT_SOURCE_2` = -2.62 (11.4x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.59 (10.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 116979

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.08 (155.1x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_COUNT` = 5.32 (30.6x median), `YEARS_BIRTH` = -0.60 (16.9x median), `BUREAU_DAYS_CREDIT_MEAN` = -0.98 (12.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 117154

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.18 (160.9x median), `YEARS_BIRTH` = 1.60 (48.7x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 1.85 (13.9x median), `AMT_INCOME_TOTAL` = 1.40 (11.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 117386

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.04 (76.0x median), `BUREAU_ACTIVE_RATIO` = 1.14 (20.3x median), `EXT_SOURCE_3` = -1.88 (17.9x median), `YEARS_BIRTH` = -0.50 (13.8x median), `CREDIT_TERM_MONTHS` = 0.53 (12.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 118260

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.46 (109.6x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_2` = -2.04 (24.7x median), `INST_LATE_RATIO` = 3.34 (6.3x median), `BUREAU_ACTIVE_RATIO` = 0.15 (3.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 118814

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 0.99 (20.3x median), `CREDIT_TERM_MONTHS` = -1.39 (17.3x median), `EXT_SOURCE_3` = -1.17 (11.5x median), `YEARS_BIRTH` = 1.51 (10.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 119108

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.61 (46.4x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `CREDIT_TERM_MONTHS` = -1.57 (33.4x median), `POS_MONTHS_COUNT` = 1.17 (30.2x median), `YEARS_BIRTH` = -0.68 (19.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 119664

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 2.90 (57.6x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_BB_DPD_RATIO_MEAN` = 5.86 (31.1x median), `BUREAU_ACTIVE_RATIO` = 1.41 (24.8x median), `EXT_SOURCE_3` = -1.28 (12.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 119990

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 5.15 (31.6x median), `EXT_SOURCE_3` = -2.94 (27.5x median), `EXT_SOURCE_1` = -0.20 (15.7x median), `EXT_SOURCE_2` = 0.91 (9.6x median), `INST_LATE_RATIO` = 3.06 (5.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 120530

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 1.67 (37.7x median), `POS_MONTHS_COUNT` = -1.13 (31.3x median), `YEARS_EMPLOYED` = 3.83 (19.3x median), `YEARS_BIRTH` = 0.58 (18.2x median), `INST_DPD_MAX` = 1.68 (17.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 120733

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `CREDIT_TERM_MONTHS` = -1.31 (27.6x median), `YEARS_BIRTH` = -0.94 (27.0x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.29 (18.5x median), `POS_MONTHS_COUNT` = -0.57 (16.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 121009

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.73 (53.2x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `CNT_CHILDREN` = 3.60 (7.2x median), `AMT_INCOME_TOTAL` = -1.66 (6.8x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.74 (5.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 121235

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 7.05 (142.5x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CREDIT_TERM_MONTHS` = -1.40 (17.5x median), `EXT_SOURCE_2` = -2.36 (12.7x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (10.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 121538

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.63 (47.6x median), `CREDIT_TERM_MONTHS` = 1.68 (37.7x median), `YEARS_BIRTH` = -0.98 (28.4x median), `POS_MONTHS_COUNT` = -1.01 (28.1x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 121777

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 7.47 (107.8x median), `CC_SK_DPD_MEAN` = 4.02 (81.7x median), `EXT_SOURCE_1` = 0.58 (42.3x median), `YEARS_BIRTH` = 0.80 (9.4x median), `CC_UTILIZATION_MAX` = 1.39 (4.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 122244

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 15.18 (78.1x median), `EXT_SOURCE_1` = 0.95 (69.9x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `CREDIT_TERM_MONTHS` = -1.51 (18.9x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 122621

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 18.61 (374.8x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `CREDIT_TERM_MONTHS` = 1.70 (23.4x median), `CREDIT_TO_INCOME` = 1.28 (9.1x median), `EXT_SOURCE_3` = 1.10 (8.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 122885

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.32 (99.3x median), `CREDIT_TERM_MONTHS` = 1.68 (37.7x median), `POS_MONTHS_COUNT` = -0.69 (19.4x median), `YEARS_BIRTH` = -0.42 (11.4x median), `YEARS_EMPLOYED` = 2.06 (10.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 123283

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟠 Tipe C — Risk Signal** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_BIRTH` = -1.07 (30.9x median), `CREDIT_TERM_MONTHS` = -1.38 (29.3x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Kombinasi finansial kontradiktif (mis. rasio cicilan/pendapatan ekstrem, income rendah + credit besar, atau skor eksternal tinggi di cluster bermasalah). |
| Business Impact | Underwriting: matikan auto-approve, wajibkan manual review oleh underwriter senior + verifikasi pendapatan fisik. |

---

## ROW_ID 123340

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.62 (193.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `POS_MONTHS_COUNT` = -1.13 (31.3x median), `YEARS_BIRTH` = 0.95 (29.2x median), `PREV_APPROVAL_RATE` = -2.34 (16.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 123501

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_BB_DPD_RATIO_MEAN` = 8.79 (46.2x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `CREDIT_TERM_MONTHS` = 1.96 (26.8x median), `AMT_ANNUITY` = 1.06 (10.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 123827

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.26 (25.7x median), `AMT_ANNUITY` = -0.89 (14.4x median), `BUREAU_ACTIVE_RATIO` = 0.78 (14.2x median), `EXT_SOURCE_2` = -2.59 (11.3x median), `EXT_SOURCE_3` = -1.87 (10.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 124284

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `AMT_CREDIT` = -1.87 (57.8x median), `INST_SEVERE_LATE_RATIO` = 6.32 (38.5x median), `AMT_ANNUITY` = -1.86 (29.2x median), `INST_LATE_RATIO` = 3.58 (23.1x median), `BUREAU_COUNT` = 4.66 (16.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 124356

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 24.41 (491.2x median), `YEARS_BIRTH` = 0.83 (25.7x median), `POS_MONTHS_COUNT` = -0.73 (20.5x median), `YEARS_EMPLOYED` = 2.73 (14.0x median), `CREDIT_TERM_MONTHS` = 0.54 (12.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 124520

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -1.24 (62.0x median), `EXT_SOURCE_1` = 0.68 (49.7x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = -1.49 (18.7x median), `YEARS_BIRTH` = -1.47 (12.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 124545

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.35 (101.5x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `EXT_SOURCE_2` = -0.86 (11.0x median), `EXT_SOURCE_3` = -0.78 (8.0x median), `AMT_INCOME_TOTAL` = 1.24 (6.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 124744

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 6.21 (37.9x median), `INST_DPD_MEAN` = 1.70 (15.9x median), `YEARS_BIRTH` = -0.84 (11.9x median), `AMT_INCOME_TOTAL` = -1.06 (10.7x median), `INST_LATE_RATIO` = 4.69 (8.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 124919

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 4.15 (110.1x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_COUNT` = 5.54 (31.8x median), `EXT_SOURCE_3` = -2.75 (25.7x median), `YEARS_BIRTH` = -0.82 (23.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 125469

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.54 (38.9x median), `CREDIT_TERM_MONTHS` = 1.67 (37.6x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `YEARS_BIRTH` = -0.91 (26.1x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.01 (12.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 125705

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.65 (49.2x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.23 (25.1x median), `BUREAU_ACTIVE_RATIO` = 1.14 (20.3x median), `BUREAU_BB_DPD_RATIO_MEAN` = 2.50 (13.9x median), `CC_SK_DPD_MEAN` = 0.41 (9.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 125769

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.92 (143.2x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_3` = -2.65 (24.8x median), `INST_SEVERE_LATE_RATIO` = 2.97 (18.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 125782

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.79 (132.2x median), `INST_SEVERE_LATE_RATIO` = 6.66 (40.6x median), `BUREAU_BB_DPD_RATIO_MEAN` = 3.35 (18.2x median), `EXT_SOURCE_2` = -1.20 (14.9x median), `INST_DPD_MEAN` = 1.47 (13.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 125982

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.86 (64.6x median), `CREDIT_TERM_MONTHS` = -1.52 (32.3x median), `YEARS_BIRTH` = -0.93 (26.8x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.79 (23.3x median), `AMT_ANNUITY` = -1.62 (12.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 125992

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.42 (31.9x median), `INST_SEVERE_LATE_RATIO` = 4.83 (29.7x median), `YEARS_EMPLOYED` = 3.91 (18.2x median), `YEARS_BIRTH` = 0.74 (8.6x median), `AMT_INCOME_TOTAL` = -0.77 (8.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 126139

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 4.58 (22.9x median), `AMT_ANNUITY` = -1.32 (15.8x median), `YEARS_EMPLOYED` = 4.62 (14.7x median), `EXT_SOURCE_3` = 1.03 (8.3x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.25 (6.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 126168

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.76 (129.6x median), `CREDIT_TERM_MONTHS` = 1.52 (21.0x median), `BUREAU_BB_DPD_RATIO_MEAN` = 3.11 (17.0x median), `YEARS_BIRTH` = 1.64 (11.6x median), `YEARS_EMPLOYED` = 2.53 (8.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 126449

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 6.92 (42.1x median), `EXT_SOURCE_3` = -2.73 (25.6x median), `BUREAU_ACTIVE_RATIO` = 2.03 (13.4x median), `INST_DPD_MEAN` = 1.34 (12.8x median), `YEARS_BIRTH` = -0.84 (11.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 126727

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.83 (136.7x median), `POS_SK_DPD_MEAN` = 9.56 (48.8x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `CREDIT_TERM_MONTHS` = -1.21 (14.9x median), `YEARS_BIRTH` = -1.07 (9.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 126916

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -3.22 (239.8x median), `POS_MONTHS_COUNT` = 1.17 (30.2x median), `EXT_SOURCE_3` = -2.17 (20.5x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `AMT_ANNUITY` = -2.34 (17.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 127007

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.77 (130.6x median), `YEARS_BIRTH` = 1.13 (34.7x median), `POS_MONTHS_COUNT` = -0.81 (22.7x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 127074

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `POS_SK_DPD_MEAN` = 4.81 (24.1x median), `CREDIT_TERM_MONTHS` = -1.39 (17.4x median), `YEARS_BIRTH` = 1.97 (14.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 127517

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_DAYS_CREDIT_MEAN` = -2.21 (29.0x median), `YEARS_BIRTH` = -0.97 (27.8x median), `CREDIT_TERM_MONTHS` = 1.19 (27.0x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `POS_MONTHS_COUNT` = 0.36 (8.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 127883

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.64 (33.2x median), `PREV_REFUSED_COUNT` = 6.23 (8.4x median), `AMT_CREDIT` = -0.27 (7.6x median), `BUREAU_DAYS_CREDIT_MEAN` = 0.94 (6.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 128147

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟠 Tipe C — Risk Signal** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.46 (33.0x median), `ANNUITY_TO_INCOME` = 7.43 (17.7x median), `AMT_INCOME_TOTAL` = -1.73 (16.9x median), `BUREAU_COUNT` = 2.68 (15.9x median), `EXT_SOURCE_3` = -1.34 (13.0x median) |
| Justifikasi | Kombinasi finansial kontradiktif (mis. rasio cicilan/pendapatan ekstrem, income rendah + credit besar, atau skor eksternal tinggi di cluster bermasalah). |
| Business Impact | Underwriting: matikan auto-approve, wajibkan manual review oleh underwriter senior + verifikasi pendapatan fisik. |

---

## ROW_ID 129047

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 6.38 (125.6x median), `BUREAU_BB_DPD_RATIO_MEAN` = 6.95 (36.7x median), `PREV_APPROVAL_RATE` = -0.36 (18.6x median), `CREDIT_TERM_MONTHS` = -1.07 (13.1x median), `YEARS_BIRTH` = -0.84 (7.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 130106

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_DPD_RATIO_MEAN` = 13.12 (68.5x median), `EXT_SOURCE_1` = 0.76 (55.7x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `CREDIT_TERM_MONTHS` = -1.08 (22.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 130267

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 5.15 (31.6x median), `EXT_SOURCE_1` = -0.30 (23.3x median), `EXT_SOURCE_3` = 1.37 (11.3x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.26 (8.2x median), `YEARS_BIRTH` = -0.54 (8.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 130489

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 3.75 (99.3x median), `EXT_SOURCE_1` = -1.09 (81.8x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 130642

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.58 (27.8x median), `AMT_ANNUITY` = -2.51 (18.9x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.47 (16.9x median), `YEARS_BIRTH` = 0.48 (15.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 130649

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.95 (71.6x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_CREDIT` = 0.52 (17.3x median), `YEARS_BIRTH` = -1.05 (5.2x median), `CNT_CHILDREN` = 2.21 (4.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 130968

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.04 (150.7x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `POS_SK_DPD_MEAN` = 7.46 (37.9x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `CREDIT_TERM_MONTHS` = 1.69 (23.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 131205

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 16.96 (87.4x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `AMT_ANNUITY` = -0.94 (11.5x median), `YEARS_BIRTH` = 1.57 (11.0x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.86 (10.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 131212

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `PREV_APPROVAL_RATE` = 0.30 (13.9x median), `POS_SK_DPD_MEAN` = 2.76 (13.4x median), `ANNUITY_TO_INCOME` = -0.56 (5.0x median), `AMT_ANNUITY` = -0.35 (4.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 131321

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `POS_SK_DPD_MEAN` = 6.24 (31.5x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `CREDIT_TERM_MONTHS` = 0.53 (8.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 131841

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.25 (91.7x median), `POS_MONTHS_COUNT` = 1.41 (36.7x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_BIRTH` = 0.68 (21.4x median), `BUREAU_ACTIVE_RATIO` = 1.14 (20.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 131979

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 24.54 (126.9x median), `EXT_SOURCE_1` = 1.05 (77.0x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `AMT_ANNUITY` = 1.95 (20.8x median), `CREDIT_TERM_MONTHS` = -1.48 (18.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 132958

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_COUNT` = 8.40 (31.3x median), `AMT_CREDIT` = 0.58 (19.1x median), `EXT_SOURCE_3` = -2.21 (12.2x median), `CREDIT_TERM_MONTHS` = 1.28 (7.6x median), `POS_MONTHS_COUNT` = 6.17 (7.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 133081

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.41 (19.4x median), `CC_SK_DPD_MEAN` = 0.90 (19.0x median), `CREDIT_TERM_MONTHS` = 1.26 (17.7x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median), `CC_MONTHS_COUNT` = 3.17 (8.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 133796

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.87 (214.1x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 3.45 (68.3x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_BB_DPD_RATIO_MEAN` = 4.48 (24.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 134317

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `INST_LATE_RATIO` = 2.39 (15.8x median), `AMT_ANNUITY` = -0.72 (11.9x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.59 (10.5x median), `CREDIT_TERM_MONTHS` = 1.66 (9.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 134380

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.37 (177.3x median), `POS_MONTHS_COUNT` = 2.30 (60.4x median), `YEARS_BIRTH` = -1.16 (33.7x median), `EXT_SOURCE_3` = -1.46 (14.1x median), `BUREAU_COUNT` = 1.58 (9.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 134552

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_CREDIT` = 1.45 (46.5x median), `AMT_ANNUITY` = 0.88 (12.3x median), `CREDIT_TERM_MONTHS` = 1.68 (9.6x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.54 (9.6x median), `PREV_REFUSED_COUNT` = 6.23 (8.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 134783

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 5.26 (76.2x median), `AMT_CREDIT` = -0.91 (27.6x median), `INST_LATE_RATIO` = 3.80 (24.5x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.59 (10.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 135297

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.80 (134.7x median), `AMT_CREDIT` = -0.79 (23.9x median), `EXT_SOURCE_3` = -1.93 (10.5x median), `BUREAU_COUNT` = 2.46 (8.5x median), `CREDIT_TERM_MONTHS` = -1.37 (6.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 135446

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 2.03 (13.1x median), `EXT_SOURCE_2` = -0.58 (7.7x median), `BUREAU_ACTIVE_RATIO` = -0.32 (4.4x median), `AMT_INCOME_TOTAL` = 0.49 (3.3x median), `EXT_SOURCE_3` = 0.47 (3.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 135471

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `ANNUITY_TO_INCOME` = 2.82 (31.4x median), `CREDIT_TO_INCOME` = 4.33 (28.4x median), `CREDIT_TERM_MONTHS` = 1.67 (23.0x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 135625

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.16 (85.2x median), `POS_MONTHS_COUNT` = 1.73 (45.3x median), `YEARS_BIRTH` = 0.82 (25.5x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.00 (23.2x median), `YEARS_EMPLOYED` = 4.19 (21.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 135863

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 10.53 (212.6x median), `PREV_APPROVAL_RATE` = -0.92 (46.5x median), `EXT_SOURCE_1` = 0.55 (39.9x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CREDIT_TERM_MONTHS` = 1.26 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 136114

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_1` = -0.41 (31.4x median), `AMT_INCOME_TOTAL` = -2.51 (24.0x median), `YEARS_BIRTH` = -0.73 (20.7x median), `POS_MONTHS_COUNT` = -0.69 (19.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 136507

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.65 (121.6x median), `CREDIT_TERM_MONTHS` = 2.16 (48.2x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.29 (14.9x median), `YEARS_BIRTH` = -0.52 (14.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 136651

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.24 (92.9x median), `AMT_CREDIT` = 0.68 (22.3x median), `AMT_ANNUITY` = 0.78 (10.8x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.45 (9.8x median), `CC_UTILIZATION_MAX` = 2.38 (6.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 136908

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.93 (144.5x median), `YEARS_BIRTH` = -1.32 (38.2x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_ACTIVE_RATIO` = 1.41 (24.8x median), `EXT_SOURCE_3` = -2.64 (24.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 137125

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_2` = -1.89 (23.0x median), `INST_SEVERE_LATE_RATIO` = 3.37 (21.0x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `INST_DPD_MEAN` = 0.92 (9.1x median), `AMT_INCOME_TOTAL` = -1.66 (6.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 137600

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 13.42 (69.0x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `AMT_ANNUITY` = -1.85 (21.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 137832

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `YEARS_BIRTH` = 0.91 (28.3x median), `POS_MONTHS_COUNT` = -0.85 (23.7x median), `YEARS_EMPLOYED` = 4.28 (21.4x median), `CREDIT_TERM_MONTHS` = 0.88 (20.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 138008

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.63 (194.0x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `EXT_SOURCE_3` = 1.78 (15.0x median), `POS_SK_DPD_MEAN` = 2.91 (14.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 138325

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.03 (77.6x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `INST_SEVERE_LATE_RATIO` = 3.58 (22.3x median), `YEARS_BIRTH` = -1.09 (15.1x median), `AMT_INCOME_TOTAL` = 1.70 (14.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 138366

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.18 (88.3x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_BIRTH` = -1.03 (29.7x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.92 (21.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 138619

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 1.66 (37.3x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_3` = -1.15 (11.3x median), `POS_MONTHS_COUNT` = -0.37 (10.8x median), `PREV_APPROVAL_RATE` = 0.96 (8.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 139183

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_CREDIT` = 1.42 (45.7x median), `AMT_ANNUITY` = 1.02 (14.4x median), `YEARS_EMPLOYED` = 2.38 (8.4x median), `CREDIT_TERM_MONTHS` = 1.28 (7.6x median), `CNT_CHILDREN` = 3.60 (7.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 139238

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.61 (44.3x median), `CREDIT_TERM_MONTHS` = 1.68 (37.7x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `YEARS_BIRTH` = -1.03 (29.6x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.58 (27.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 139699

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `YEARS_BIRTH` = 1.46 (44.4x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_INCOME_TOTAL` = 1.70 (14.6x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 1.85 (13.9x median), `CREDIT_TERM_MONTHS` = 0.54 (12.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 140173

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `INST_SEVERE_LATE_RATIO` = 4.23 (26.1x median), `YEARS_EMPLOYED` = 5.43 (24.8x median), `INST_DPD_MAX` = 2.80 (18.4x median), `INST_DPD_MEAN` = 1.96 (18.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 140210

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 3.47 (91.8x median), `EXT_SOURCE_1` = 0.93 (68.0x median), `CREDIT_TERM_MONTHS` = 1.68 (37.8x median), `YEARS_EMPLOYED` = 2.59 (13.4x median), `CREDIT_TO_INCOME` = 2.78 (13.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 140277

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.84 (135.6x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_INCOME_TOTAL` = 1.56 (13.3x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 1.27 (9.3x median), `EXT_SOURCE_3` = 0.95 (7.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 140491

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.95 (146.2x median), `CREDIT_TERM_MONTHS` = -1.41 (29.8x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 1.85 (13.9x median), `YEARS_BIRTH` = -0.40 (11.0x median), `POS_MONTHS_COUNT` = 0.44 (10.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 140644

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.34 (173.0x median), `POS_MONTHS_COUNT` = 1.45 (37.8x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.00 (23.2x median), `YEARS_BIRTH` = 0.71 (22.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 140645

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 4.27 (113.3x median), `EXT_SOURCE_1` = -0.70 (52.9x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `INST_DPD_MAX` = 3.44 (34.1x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.70 (19.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 140756

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 1.70 (38.1x median), `POS_MONTHS_COUNT` = -1.13 (31.3x median), `YEARS_BIRTH` = 0.83 (25.8x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `YEARS_EMPLOYED` = 3.97 (20.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 140761

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 16.49 (85.0x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `ANNUITY_TO_INCOME` = 1.42 (16.2x median), `CREDIT_TERM_MONTHS` = -1.10 (13.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 140794

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.90 (142.0x median), `INST_SEVERE_LATE_RATIO` = 4.39 (27.1x median), `EXT_SOURCE_2` = 0.68 (6.9x median), `EXT_SOURCE_3` = -0.49 (5.4x median), `CNT_CHILDREN` = 2.21 (4.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 140897

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.88 (212.9x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_EMPLOYED` = 3.58 (16.7x median), `BUREAU_DAYS_CREDIT_MEAN` = -2.24 (15.3x median), `YEARS_BIRTH` = 1.06 (12.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 140954

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.46 (182.1x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `PREV_APPROVAL_RATE` = -0.45 (23.2x median), `CREDIT_TERM_MONTHS` = -1.38 (17.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 140955

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 18.92 (381.0x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `AMT_ANNUITY` = -1.52 (18.0x median), `CREDIT_TERM_MONTHS` = 0.83 (12.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 141197

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `POS_MONTHS_COUNT` = 1.09 (28.1x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 2.43 (18.5x median), `EXT_SOURCE_1` = 0.26 (18.4x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 141343

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `YEARS_BIRTH` = -1.29 (37.5x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `PREV_APPROVAL_RATE` = -1.35 (8.8x median), `EXT_SOURCE_2` = -1.70 (7.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 141371

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.50 (36.4x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_INCOME_TOTAL` = 2.47 (21.6x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (11.5x median), `CNT_CHILDREN` = 3.60 (7.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 141382

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 1.25 (32.4x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `YEARS_BIRTH` = -0.36 (9.6x median), `AMT_ANNUITY` = -0.87 (7.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 141692

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 2.26 (59.4x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.58 (27.8x median), `YEARS_BIRTH` = 0.72 (22.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 141799

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `AMT_INCOME_TOTAL` = 0.86 (6.8x median), `POS_MONTHS_COUNT` = 0.28 (6.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 141982

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.15 (84.3x median), `YEARS_BIRTH` = 1.70 (51.5x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `POS_MONTHS_COUNT` = 1.29 (33.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 141993

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 22.22 (447.2x median), `EXT_SOURCE_1` = 1.82 (133.9x median), `CREDIT_TERM_MONTHS` = 1.96 (43.9x median), `YEARS_BIRTH` = 0.90 (27.7x median), `CREDIT_TO_INCOME` = 2.92 (13.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 142260

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 12.29 (176.6x median), `EXT_SOURCE_1` = 2.04 (150.8x median), `POS_MONTHS_COUNT` = 3.14 (83.1x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `AMT_INCOME_TOTAL` = 2.08 (18.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 142470

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 1.69 (44.3x median), `YEARS_BIRTH` = 0.55 (17.3x median), `EXT_SOURCE_3` = -1.53 (14.7x median), `AMT_INCOME_TOTAL` = 1.56 (13.3x median), `BUREAU_COUNT` = 1.58 (9.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 142795

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 1.33 (34.5x median), `INST_DPD_MAX` = 3.32 (32.9x median), `CREDIT_TERM_MONTHS` = -1.06 (22.3x median), `BUREAU_COUNT` = 2.24 (13.4x median), `PREV_REFUSED_COUNT` = 4.56 (11.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 143258

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_MONTHS_COUNT` = -0.93 (25.9x median), `CREDIT_TERM_MONTHS` = -0.88 (18.2x median), `AMT_ANNUITY` = -1.68 (12.9x median), `BUREAU_COUNT` = 1.58 (9.8x median), `AMT_CREDIT` = -1.73 (9.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 143273

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.79 (57.5x median), `EXT_SOURCE_2` = -1.42 (17.5x median), `BUREAU_ACTIVE_RATIO` = -0.48 (7.1x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.45 (4.7x median), `YEARS_BIRTH` = -1.39 (2.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 143298

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟠 Tipe C — Risk Signal** |
| Top Deviating Features | `INST_DPD_MAX` = 3.20 (31.8x median), `YEARS_BIRTH` = 1.02 (31.5x median), `AMT_INCOME_TOTAL` = -2.98 (28.3x median), `INST_SEVERE_LATE_RATIO` = 4.59 (28.3x median), `CREDIT_TO_INCOME` = 4.85 (21.9x median) |
| Justifikasi | Kombinasi finansial kontradiktif (mis. rasio cicilan/pendapatan ekstrem, income rendah + credit besar, atau skor eksternal tinggi di cluster bermasalah). |
| Business Impact | Underwriting: matikan auto-approve, wajibkan manual review oleh underwriter senior + verifikasi pendapatan fisik. |

---

## ROW_ID 143610

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = -1.08 (22.7x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `PREV_REFUSED_COUNT` = 5.12 (12.3x median), `PREV_APPROVAL_RATE` = -1.68 (11.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 143664

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.94 (217.7x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_EMPLOYED` = 4.22 (19.5x median), `YEARS_BIRTH` = 1.31 (15.9x median), `EXT_SOURCE_3` = 1.24 (10.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 143726

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 32.34 (632.5x median), `BUREAU_BB_DPD_RATIO_MEAN` = 18.04 (93.8x median), `EXT_SOURCE_1` = -0.76 (57.5x median), `YEARS_BIRTH` = -0.91 (26.1x median), `CREDIT_TERM_MONTHS` = -1.08 (22.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 143873

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 21.04 (423.7x median), `CREDIT_TERM_MONTHS` = -1.48 (18.5x median), `PREV_APPROVAL_RATE` = -0.27 (14.5x median), `BUREAU_ACTIVE_RATIO` = 0.78 (14.2x median), `EXT_SOURCE_1` = 0.14 (9.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 144153

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.88 (64.6x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `INST_DPD_MAX` = 2.95 (19.3x median), `BUREAU_ACTIVE_RATIO` = 2.03 (13.4x median), `INST_SEVERE_LATE_RATIO` = 1.65 (10.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 144284

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -3.01 (224.9x median), `POS_MONTHS_COUNT` = 1.69 (44.3x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `YEARS_BIRTH` = -1.14 (32.9x median), `BUREAU_ACTIVE_RATIO` = 1.25 (22.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 144397

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 26.83 (525.0x median), `BUREAU_BB_DPD_RATIO_MEAN` = 15.05 (78.4x median), `PREV_APPROVAL_RATE` = -1.24 (62.0x median), `POS_SK_DPD_MEAN` = 4.04 (20.1x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 144495

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.60 (43.9x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `EXT_SOURCE_2` = -1.27 (15.8x median), `OWN_CAR_AGE` = 6.68 (15.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 144747

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `AMT_CREDIT` = -2.89 (89.9x median), `AMT_ANNUITY` = -4.04 (62.2x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `INST_DPD_MAX` = 1.38 (12.2x median), `EXT_SOURCE_3` = 1.69 (11.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 144863

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 4.98 (98.2x median), `BUREAU_BB_DPD_RATIO_MEAN` = 6.20 (32.9x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.55 (31.3x median), `BUREAU_ACTIVE_RATIO` = 0.86 (15.5x median), `EXT_SOURCE_3` = -2.65 (14.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 144879

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 3.19 (19.9x median), `INST_DPD_MEAN` = 1.43 (13.5x median), `INST_LATE_RATIO` = 6.83 (11.9x median), `EXT_SOURCE_3` = -1.14 (11.2x median), `EXT_SOURCE_2` = 0.94 (9.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 145041

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.15 (86.2x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_3` = 1.87 (15.8x median), `BUREAU_DAYS_CREDIT_MEAN` = -2.03 (13.8x median), `YEARS_BIRTH` = -0.56 (8.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 145895

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.78 (57.1x median), `INST_SEVERE_LATE_RATIO` = 5.15 (31.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CNT_CHILDREN` = 3.60 (7.2x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.41 (6.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 146193

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.75 (205.6x median), `INST_SEVERE_LATE_RATIO` = 6.21 (37.9x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `BUREAU_BB_DPD_RATIO_MEAN` = 4.09 (22.0x median), `INST_LATE_RATIO` = 2.92 (19.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 146197

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_DAYS_CREDIT_MEAN` = -2.73 (36.1x median), `CREDIT_TERM_MONTHS` = -1.57 (33.3x median), `BUREAU_BB_DPD_RATIO_MEAN` = 6.20 (32.9x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `YEARS_BIRTH` = -0.58 (16.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 146377

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_INCOME_TOTAL` = 2.47 (21.6x median), `YEARS_EMPLOYED` = 2.19 (10.6x median), `BUREAU_ACTIVE_RATIO` = 1.25 (8.6x median), `YEARS_BIRTH` = -0.54 (8.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 146413

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.13 (157.5x median), `POS_MONTHS_COUNT` = 4.19 (111.2x median), `CREDIT_TERM_MONTHS` = 1.67 (37.5x median), `YEARS_BIRTH` = 1.11 (34.0x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 146573

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `POS_MONTHS_COUNT` = -1.13 (31.3x median), `YEARS_BIRTH` = 0.83 (25.8x median), `CREDIT_TERM_MONTHS` = 0.86 (19.8x median), `PREV_APPROVAL_RATE` = -2.34 (16.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 146592

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.60 (43.5x median), `INST_DPD_MAX` = 3.96 (25.6x median), `INST_DPD_MEAN` = 2.09 (19.4x median), `INST_SEVERE_LATE_RATIO` = 2.60 (16.5x median), `YEARS_BIRTH` = -0.58 (8.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 146923

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 25.09 (129.8x median), `EXT_SOURCE_1` = 0.70 (51.0x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `AMT_ANNUITY` = 1.18 (12.2x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.65 (9.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 147327

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 1.26 (28.6x median), `POS_MONTHS_COUNT` = 0.48 (11.9x median), `YEARS_BIRTH` = 0.36 (11.8x median), `BUREAU_DAYS_CREDIT_MEAN` = -0.87 (10.9x median), `BUREAU_COUNT` = 1.58 (9.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 147494

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.80 (58.1x median), `EXT_SOURCE_3` = -1.90 (18.1x median), `BUREAU_ACTIVE_RATIO` = -0.82 (12.9x median), `INST_LATE_RATIO` = 3.51 (6.6x median), `CNT_CHILDREN` = 2.21 (4.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 147499

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.90 (65.8x median), `BUREAU_DAYS_CREDIT_MEAN` = -2.26 (29.7x median), `CREDIT_TERM_MONTHS` = 1.00 (22.8x median), `BUREAU_COUNT` = 2.24 (13.4x median), `YEARS_EMPLOYED` = 2.59 (13.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 147638

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 18.19 (366.4x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `EXT_SOURCE_3` = 2.11 (18.0x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 147685

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 12.45 (178.8x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.72 (11.5x median), `YEARS_EMPLOYED` = 2.00 (9.8x median), `AMT_INCOME_TOTAL` = 0.94 (7.6x median), `POS_MONTHS_COUNT` = 2.50 (6.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 147885

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.75 (205.4x median), `INST_SEVERE_LATE_RATIO` = 5.15 (31.6x median), `EXT_SOURCE_2` = -1.57 (19.3x median), `INST_DPD_MEAN` = 1.00 (9.8x median), `EXT_SOURCE_3` = -0.77 (8.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 148062

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟠 Tipe C — Risk Signal** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `YEARS_BIRTH` = 1.12 (34.3x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `AMT_INCOME_TOTAL` = -2.04 (19.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Kombinasi finansial kontradiktif (mis. rasio cicilan/pendapatan ekstrem, income rendah + credit besar, atau skor eksternal tinggi di cluster bermasalah). |
| Business Impact | Underwriting: matikan auto-approve, wajibkan manual review oleh underwriter senior + verifikasi pendapatan fisik. |

---

## ROW_ID 148068

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 22.82 (459.3x median), `YEARS_BIRTH` = 1.52 (46.2x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `POS_MONTHS_COUNT` = -1.13 (31.3x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 148097

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.84 (135.4x median), `INST_SEVERE_LATE_RATIO` = 5.76 (35.2x median), `YEARS_EMPLOYED` = 4.05 (10.7x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median), `EXT_SOURCE_2` = -0.60 (8.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 148277

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_CREDIT` = 1.35 (43.4x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_ANNUITY` = 1.42 (20.6x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.79 (16.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 148458

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 2.26 (46.3x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `AMT_ANNUITY` = -1.25 (14.9x median), `EXT_SOURCE_3` = -1.10 (10.9x median), `YEARS_BIRTH` = -1.15 (9.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 148718

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 2.49 (15.8x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median), `EXT_SOURCE_3` = -0.32 (3.9x median), `YEARS_BIRTH` = -1.36 (2.5x median), `BUREAU_DAYS_CREDIT_MEAN` = 0.90 (2.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 148863

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.87 (65.8x median), `YEARS_BIRTH` = -0.96 (27.5x median), `BUREAU_ACTIVE_RATIO` = 0.78 (14.2x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.14 (13.3x median), `CREDIT_TERM_MONTHS` = 0.41 (10.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 148895

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 7.39 (37.5x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `CREDIT_TERM_MONTHS` = 1.68 (23.1x median), `EXT_SOURCE_3` = -1.50 (14.5x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.61 (9.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 149033

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 1.97 (51.8x median), `CREDIT_TERM_MONTHS` = 1.96 (43.8x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `YEARS_BIRTH` = -0.81 (23.1x median), `BUREAU_COUNT` = 3.12 (18.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 149169

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_COUNT` = 5.10 (29.3x median), `YEARS_BIRTH` = -0.54 (15.2x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.17 (14.9x median), `PREV_COUNT` = 3.37 (9.9x median), `PREV_APPROVAL_RATE` = -1.47 (9.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 149402

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.10 (80.9x median), `AMT_INCOME_TOTAL` = -1.40 (13.8x median), `YEARS_BIRTH` = 1.09 (13.1x median), `CREDIT_TO_INCOME` = 7.12 (12.3x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (11.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 149880

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 15.95 (312.4x median), `BUREAU_BB_DPD_RATIO_MEAN` = 9.25 (48.6x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `POS_SK_DPD_MEAN` = 5.60 (28.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 150102

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `AMT_CREDIT` = -1.70 (52.4x median), `AMT_ANNUITY` = -2.74 (42.5x median), `PREV_REFUSED_COUNT` = 14.03 (20.3x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.94 (19.5x median), `OWN_CAR_AGE` = 1.78 (4.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 150258

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 1.67 (37.6x median), `POS_MONTHS_COUNT` = -1.13 (31.3x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.65 (21.5x median), `EXT_SOURCE_1` = 0.26 (18.5x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 150500

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.29 (169.3x median), `CC_SK_DPD_MEAN` = 6.93 (140.2x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = -1.39 (17.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 150520

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.80 (58.5x median), `CREDIT_TERM_MONTHS` = -1.51 (32.0x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 2.43 (18.5x median), `POS_MONTHS_COUNT` = -0.61 (17.3x median), `PREV_APPROVAL_RATE` = -1.97 (13.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 150846

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.52 (186.3x median), `BUREAU_COUNT` = 3.56 (12.7x median), `YEARS_EMPLOYED` = 3.53 (12.0x median), `CC_MONTHS_COUNT` = 3.25 (8.4x median), `EXT_SOURCE_3` = -1.22 (6.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 151125

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 1.25 (32.4x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 2.43 (18.5x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.37 (15.8x median), `BUREAU_BB_DPD_RATIO_MEAN` = 2.28 (12.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 151430

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.16 (161.6x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `POS_MONTHS_COUNT` = -0.85 (23.7x median), `YEARS_BIRTH` = -0.75 (21.4x median), `CREDIT_TERM_MONTHS` = -0.93 (19.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 151495

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.36 (17.4x median), `POS_MONTHS_COUNT` = -0.61 (17.3x median), `CREDIT_TERM_MONTHS` = 0.71 (16.5x median), `AMT_INCOME_TOTAL` = -1.66 (16.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 151548

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 14.19 (203.8x median), `EXT_SOURCE_1` = -2.61 (195.2x median), `POS_MONTHS_COUNT` = 1.97 (51.8x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_BIRTH` = -0.82 (23.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 151605

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 6.73 (136.2x median), `CREDIT_TERM_MONTHS` = 1.70 (38.1x median), `YEARS_BIRTH` = 1.19 (36.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.75 (22.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 151677

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 3.28 (20.5x median), `AMT_INCOME_TOTAL` = 0.86 (6.8x median), `BUREAU_ACTIVE_RATIO` = -1.11 (5.8x median), `YEARS_EMPLOYED` = 1.03 (5.5x median), `INST_LATE_RATIO` = 2.48 (5.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 152034

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 4.60 (122.0x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.58 (27.8x median), `BUREAU_ACTIVE_RATIO` = 1.41 (24.8x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.44 (16.6x median), `YEARS_BIRTH` = 0.35 (11.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 152649

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_2` = -1.42 (17.5x median), `OWN_CAR_AGE` = 6.68 (15.7x median), `EXT_SOURCE_1` = 0.19 (13.1x median), `EXT_SOURCE_3` = 1.42 (11.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 153304

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 18.13 (260.0x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 5.74 (113.0x median), `POS_MONTHS_COUNT` = 3.79 (100.4x median), `YEARS_BIRTH` = 1.43 (43.5x median), `BUREAU_BB_DPD_RATIO_MEAN` = 4.84 (25.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 154651

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 15.62 (80.4x median), `BUREAU_ACTIVE_RATIO` = 0.78 (14.2x median), `YEARS_BIRTH` = 1.77 (12.6x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.51 (8.4x median), `PREV_APPROVAL_RATE` = -0.14 (7.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 154770

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.87 (63.9x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `INST_PAYMENT_RATIO_MEAN` = 0.23 (22.4x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.60 (12.7x median), `AMT_CREDIT` = 0.32 (11.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 154771

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.84 (136.0x median), `BUREAU_COUNT` = 3.12 (18.3x median), `AMT_ANNUITY` = -1.78 (13.6x median), `YEARS_EMPLOYED` = 2.20 (11.5x median), `BUREAU_DAYS_CREDIT_MEAN` = -0.66 (8.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 154839

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `YEARS_BIRTH` = 0.92 (28.6x median), `CREDIT_TERM_MONTHS` = -1.30 (27.4x median), `YEARS_EMPLOYED` = 4.63 (23.1x median), `POS_MONTHS_COUNT` = -0.61 (17.3x median), `BUREAU_BB_DPD_RATIO_MEAN` = 1.38 (8.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 155274

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.87 (63.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `POS_MONTHS_COUNT` = -1.13 (31.3x median), `CREDIT_TERM_MONTHS` = -1.40 (29.6x median), `YEARS_BIRTH` = -0.81 (23.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 155335

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.53 (112.5x median), `AMT_CREDIT` = 0.74 (24.1x median), `INST_LATE_RATIO` = 2.69 (17.6x median), `EXT_SOURCE_3` = -1.76 (9.5x median), `CREDIT_TERM_MONTHS` = 1.17 (7.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 155568

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 5.38 (32.9x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `EXT_SOURCE_2` = -1.28 (15.9x median), `INST_DPD_MEAN` = 0.86 (8.6x median), `INST_LATE_RATIO` = 3.61 (6.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 156315

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_COUNT` = 4.22 (24.5x median), `CREDIT_TERM_MONTHS` = -1.08 (22.7x median), `EXT_SOURCE_1` = 0.29 (20.9x median), `YEARS_BIRTH` = 0.64 (20.0x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 1.85 (13.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 156327

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 63.21 (1235.4x median), `BUREAU_BB_DPD_RATIO_MEAN` = 31.31 (162.0x median), `EXT_SOURCE_1` = -0.69 (52.2x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.90 (10.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 156540

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_3` = -1.83 (17.4x median), `AMT_ANNUITY` = -2.30 (17.4x median), `EXT_SOURCE_1` = 0.19 (13.5x median), `BUREAU_DAYS_CREDIT_MEAN` = 0.61 (9.3x median), `AMT_CREDIT` = -1.73 (9.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 156567

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.92 (141.8x median), `POS_MONTHS_COUNT` = -0.65 (18.4x median), `YEARS_BIRTH` = -0.63 (17.9x median), `AMT_INCOME_TOTAL` = -1.28 (12.7x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 156736

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_ACTIVE_RATIO` = 1.41 (24.8x median), `POS_MONTHS_COUNT` = 0.84 (21.6x median), `CREDIT_TERM_MONTHS` = -0.58 (11.7x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.96 (11.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 158137

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.94 (145.0x median), `YEARS_BIRTH` = -1.40 (40.8x median), `POS_MONTHS_COUNT` = -0.77 (21.6x median), `CREDIT_TERM_MONTHS` = -0.94 (19.5x median), `EXT_SOURCE_3` = -1.69 (16.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 158171

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.45 (183.1x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_CREDIT` = -0.92 (28.0x median), `PREV_REFUSED_COUNT` = 11.25 (16.0x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.59 (10.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 159365

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -1.87 (92.9x median), `POS_SK_DPD_MEAN` = 17.99 (92.8x median), `CREDIT_TERM_MONTHS` = 1.73 (23.9x median), `AMT_ANNUITY` = -1.31 (15.7x median), `ANNUITY_TO_INCOME` = -0.95 (9.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 159559

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.61 (46.5x median), `CREDIT_TERM_MONTHS` = 1.97 (44.2x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `POS_MONTHS_COUNT` = 1.05 (27.0x median), `YEARS_BIRTH` = -0.62 (17.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 159685

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `ANNUITY_TO_INCOME` = 1.60 (18.2x median), `AMT_ANNUITY` = 1.68 (17.8x median), `AMT_CREDIT` = 1.23 (6.8x median), `CREDIT_TO_INCOME` = 0.91 (6.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 160179

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.63 (120.4x median), `CREDIT_TERM_MONTHS` = 1.67 (37.6x median), `BUREAU_ACTIVE_RATIO` = 1.25 (22.2x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.09 (12.8x median), `BUREAU_DAYS_CREDIT_MEAN` = 0.86 (12.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 160242

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_ACTIVE_RATIO` = 2.03 (13.4x median), `AMT_INCOME_TOTAL` = -1.28 (12.7x median), `CNT_CHILDREN` = 3.60 (7.2x median), `CC_UTILIZATION_MAX` = 2.40 (6.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 160503

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `CREDIT_TERM_MONTHS` = 1.70 (23.4x median), `CREDIT_TO_INCOME` = 2.36 (16.0x median), `ANNUITY_TO_INCOME` = 1.19 (13.8x median), `BUREAU_COUNT` = 2.02 (12.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 160661

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 26.15 (511.6x median), `BUREAU_BB_DPD_RATIO_MEAN` = 16.33 (85.0x median), `AMT_CREDIT` = -1.33 (40.6x median), `AMT_ANNUITY` = -1.23 (19.6x median), `BUREAU_DAYS_CREDIT_MEAN` = -2.79 (14.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 160697

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 16.32 (234.2x median), `AMT_CREDIT` = -1.51 (46.5x median), `AMT_ANNUITY` = -2.02 (31.6x median), `YEARS_EMPLOYED` = 3.60 (12.2x median), `BUREAU_ACTIVE_RATIO` = -0.71 (11.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 161133

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `EXT_SOURCE_2` = -2.51 (30.2x median), `YEARS_EMPLOYED` = 4.41 (11.5x median), `EXT_SOURCE_3` = 0.83 (6.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 161169

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.06 (80.0x median), `YEARS_BIRTH` = -1.58 (46.0x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `CREDIT_TERM_MONTHS` = -1.62 (34.4x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.00 (23.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 161770

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `INST_DPD_MAX` = 6.36 (62.1x median), `CREDIT_TERM_MONTHS` = 1.67 (37.6x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `YEARS_BIRTH` = -0.86 (24.7x median), `BUREAU_ACTIVE_RATIO` = 0.91 (16.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 161986

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.47 (182.3x median), `AMT_CREDIT` = 1.55 (49.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_ANNUITY` = 0.89 (12.5x median), `CREDIT_TERM_MONTHS` = 1.96 (11.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 162579

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.45 (108.8x median), `POS_MONTHS_COUNT` = 3.31 (87.4x median), `YEARS_BIRTH` = -1.11 (32.1x median), `EXT_SOURCE_3` = -2.53 (23.7x median), `CREDIT_TERM_MONTHS` = -1.08 (22.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 162585

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.19 (163.8x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `PREV_REFUSED_COUNT` = 12.92 (18.6x median), `BUREAU_ACTIVE_RATIO` = 0.64 (11.8x median), `CC_UTILIZATION_MEAN` = 3.96 (10.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 162830

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `YEARS_BIRTH` = 1.48 (45.1x median), `BUREAU_BB_DPD_RATIO_MEAN` = 4.74 (25.4x median), `BUREAU_ACTIVE_RATIO` = 1.41 (24.8x median), `EXT_SOURCE_3` = -2.42 (22.8x median), `INST_SEVERE_LATE_RATIO` = 3.14 (19.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 163134

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_LATE_RATIO` = 2.48 (16.3x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.66 (8.3x median), `AMT_CREDIT` = -0.27 (7.6x median), `AMT_ANNUITY` = -0.40 (7.1x median), `YEARS_EMPLOYED` = 1.53 (5.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 163158

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.55 (116.5x median), `AMT_CREDIT` = -0.73 (21.8x median), `INST_LATE_RATIO` = 2.15 (14.3x median), `EXT_SOURCE_3` = -2.20 (12.1x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 163319

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_1` = 0.26 (18.1x median), `BUREAU_ACTIVE_RATIO` = 0.69 (12.7x median), `YEARS_EMPLOYED` = 2.89 (10.0x median), `EXT_SOURCE_3` = 1.12 (7.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 163583

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 17.44 (351.2x median), `EXT_SOURCE_1` = -1.34 (100.2x median), `PREV_APPROVAL_RATE` = -1.44 (71.8x median), `BUREAU_COUNT` = 2.90 (17.1x median), `PREV_REFUSED_COUNT` = 3.45 (8.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 164352

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.50 (184.8x median), `CREDIT_TERM_MONTHS` = 2.17 (48.5x median), `YEARS_BIRTH` = 0.82 (25.3x median), `AMT_INCOME_TOTAL` = 2.47 (21.6x median), `YEARS_EMPLOYED` = 3.48 (17.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 164391

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 3.40 (67.4x median), `INST_SEVERE_LATE_RATIO` = 3.82 (23.7x median), `INST_DPD_MEAN` = 1.91 (17.8x median), `BUREAU_BB_DPD_RATIO_MEAN` = 2.85 (15.7x median), `INST_DPD_MAX` = 2.01 (13.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 164681

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.54 (115.5x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `AMT_CREDIT` = -0.96 (29.1x median), `AMT_ANNUITY` = -1.33 (21.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 164994

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `CREDIT_TERM_MONTHS` = 2.17 (29.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CREDIT_TO_INCOME` = 2.31 (15.7x median), `AMT_ANNUITY` = 1.46 (15.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 165357

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 22.13 (114.4x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `YEARS_BIRTH` = -1.24 (10.5x median), `AMT_ANNUITY` = -0.68 (8.6x median), `CC_MONTHS_COUNT` = 3.05 (8.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 165385

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 1.28 (29.1x median), `EXT_SOURCE_3` = -2.10 (19.9x median), `POS_MONTHS_COUNT` = -0.69 (19.4x median), `YEARS_BIRTH` = -0.67 (19.1x median), `OWN_CAR_AGE` = 6.68 (15.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 165526

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `CREDIT_TERM_MONTHS` = -1.62 (34.5x median), `POS_MONTHS_COUNT` = 1.29 (33.5x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.58 (27.8x median), `YEARS_BIRTH` = 0.63 (19.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 165729

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.07 (78.4x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (11.5x median), `AMT_INCOME_TOTAL` = 1.24 (10.3x median), `CNT_CHILDREN` = 3.60 (7.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 166364

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `CREDIT_TERM_MONTHS` = 1.26 (17.7x median), `ANNUITY_TO_INCOME` = -0.69 (6.4x median), `EXT_SOURCE_3` = -0.48 (5.3x median), `AMT_INCOME_TOTAL` = 0.86 (5.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 166388

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.79 (59.7x median), `EXT_SOURCE_3` = 1.04 (8.4x median), `EXT_SOURCE_2` = 0.64 (6.5x median), `INST_LATE_RATIO` = 2.56 (5.1x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.46 (4.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 166617

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `POS_MONTHS_COUNT` = 0.93 (23.7x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `CREDIT_TERM_MONTHS` = 0.85 (19.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 166766

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `CREDIT_TERM_MONTHS` = 1.26 (17.7x median), `CREDIT_TO_INCOME` = 1.06 (7.7x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.32 (7.3x median), `EXT_SOURCE_3` = 0.88 (6.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 166984

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.47 (109.9x median), `POS_MONTHS_COUNT` = 3.91 (103.6x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_BIRTH` = -0.76 (21.6x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 2.43 (18.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 166993

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.67 (125.4x median), `CREDIT_TERM_MONTHS` = 1.68 (37.7x median), `BUREAU_COUNT` = 3.56 (20.8x median), `PREV_APPROVAL_RATE` = -1.24 (8.0x median), `CREDIT_TO_INCOME` = 1.57 (7.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 167112

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -0.50 (25.8x median), `POS_SK_DPD_MEAN` = 2.95 (14.4x median), `YEARS_BIRTH` = 1.76 (12.6x median), `CREDIT_TERM_MONTHS` = 0.86 (12.3x median), `BUREAU_COUNT` = 1.36 (8.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 167277

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.26 (92.6x median), `BUREAU_COUNT` = 5.98 (34.2x median), `AMT_ANNUITY` = -1.63 (12.6x median), `POS_MONTHS_COUNT` = -0.37 (10.8x median), `EXT_SOURCE_3` = -1.07 (10.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 167648

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.52 (37.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `POS_MONTHS_COUNT` = -0.61 (17.3x median), `AMT_ANNUITY` = -1.93 (14.7x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.03 (13.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 167939

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_CREDIT` = 1.37 (44.1x median), `INST_SEVERE_LATE_RATIO` = 3.14 (19.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `YEARS_EMPLOYED` = 4.45 (14.9x median), `AMT_ANNUITY` = 0.95 (13.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 168296

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 6.92 (136.2x median), `BUREAU_BB_DPD_RATIO_MEAN` = 5.85 (31.1x median), `BUREAU_DAYS_CREDIT_MEAN` = -2.19 (28.7x median), `YEARS_BIRTH` = -0.99 (28.6x median), `CREDIT_TERM_MONTHS` = -1.30 (27.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 168320

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `POS_MONTHS_COUNT` = -0.57 (16.2x median), `YEARS_BIRTH` = 0.36 (11.8x median), `YEARS_EMPLOYED` = 1.91 (10.1x median), `AMT_ANNUITY` = -1.04 (8.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 168466

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `CREDIT_TERM_MONTHS` = 1.30 (18.1x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DAYS_CREDIT_MEAN` = -2.91 (17.2x median), `POS_SK_DPD_MEAN` = 2.53 (12.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 168826

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_DPD_MAX` = 3.86 (38.1x median), `CREDIT_TERM_MONTHS` = 1.68 (37.7x median), `POS_MONTHS_COUNT` = 0.80 (20.5x median), `EXT_SOURCE_3` = -2.05 (19.5x median), `POS_SK_DPD_MEAN` = 0.98 (15.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 169184

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 1.67 (37.7x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `YEARS_BIRTH` = 0.90 (27.9x median), `YEARS_EMPLOYED` = 4.55 (22.7x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 169548

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 6.21 (37.9x median), `EXT_SOURCE_2` = -2.40 (28.9x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `INST_DPD_MEAN` = 1.40 (13.3x median), `INST_LATE_RATIO` = 3.80 (7.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 169763

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `EXT_SOURCE_1` = -0.59 (45.0x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_ACTIVE_RATIO` = 1.25 (22.2x median), `CREDIT_TERM_MONTHS` = 0.88 (12.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 169818

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 0.97 (24.8x median), `OWN_CAR_AGE` = 6.79 (15.9x median), `BUREAU_COUNT` = 1.36 (8.6x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.64 (7.9x median), `CREDIT_TERM_MONTHS` = 0.21 (5.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 169860

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 2.78 (56.9x median), `INST_DPD_MAX` = 4.75 (46.6x median), `CREDIT_TERM_MONTHS` = 1.69 (38.1x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `INST_DPD_MEAN` = 1.86 (20.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 170233

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_DPD_RATIO_MEAN` = 26.43 (136.9x median), `INST_SEVERE_LATE_RATIO` = 7.05 (42.9x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.98 (39.7x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 170328

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -1.74 (86.6x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 2.46 (49.1x median), `BUREAU_BB_DPD_RATIO_MEAN` = 6.59 (34.9x median), `EXT_SOURCE_3` = -1.62 (15.6x median), `BUREAU_ACTIVE_RATIO` = 0.86 (15.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 170339

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_CREDIT` = -1.01 (30.8x median), `BUREAU_ACTIVE_RATIO` = 0.73 (13.3x median), `AMT_ANNUITY` = -0.53 (9.1x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.38 (8.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 170394

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -1.24 (62.0x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `ANNUITY_TO_INCOME` = 1.37 (15.7x median), `YEARS_BIRTH` = -1.21 (10.3x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (10.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 171154

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 7.59 (149.3x median), `BUREAU_BB_DPD_RATIO_MEAN` = 8.85 (46.5x median), `POS_MONTHS_COUNT` = -1.13 (31.3x median), `EXT_SOURCE_3` = -2.14 (20.2x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 171381

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 3.23 (64.0x median), `BUREAU_BB_DPD_RATIO_MEAN` = 4.79 (25.7x median), `EXT_SOURCE_3` = -2.31 (21.7x median), `INST_SEVERE_LATE_RATIO` = 3.19 (19.9x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 171981

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.04 (150.6x median), `EXT_SOURCE_3` = 1.40 (11.6x median), `AMT_INCOME_TOTAL` = -1.06 (10.7x median), `YEARS_EMPLOYED` = 1.80 (8.9x median), `YEARS_BIRTH` = -0.54 (7.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 172356

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_CREDIT` = 1.16 (37.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_EMPLOYED` = 4.18 (14.1x median), `EXT_SOURCE_3` = -2.27 (12.6x median), `CREDIT_TERM_MONTHS` = 2.15 (12.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 172683

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.37 (102.5x median), `INST_SEVERE_LATE_RATIO` = 5.00 (30.7x median), `POS_MONTHS_COUNT` = -0.81 (22.7x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 172726

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.03 (149.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_CREDIT` = 0.52 (17.3x median), `OWN_CAR_AGE` = 6.68 (15.7x median), `AMT_ANNUITY` = 0.64 (8.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 172970

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.88 (64.6x median), `EXT_SOURCE_3` = -2.94 (27.5x median), `POS_SK_DPD_MEAN` = 3.92 (19.4x median), `BUREAU_BB_DPD_RATIO_MEAN` = 2.57 (14.2x median), `CREDIT_TERM_MONTHS` = -0.78 (9.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 173166

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.26 (20.3x median), `AMT_ANNUITY` = 1.64 (17.3x median), `ANNUITY_TO_INCOME` = 1.13 (13.1x median), `EXT_SOURCE_3` = 1.51 (12.6x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.56 (8.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 173274

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.97 (70.8x median), `YEARS_BIRTH` = -1.12 (32.4x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 1.85 (13.9x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.96 (11.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 173635

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 9.32 (183.0x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_BB_DPD_RATIO_MEAN` = 5.47 (29.2x median), `POS_MONTHS_COUNT` = -0.97 (27.0x median), `YEARS_BIRTH` = -0.85 (24.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 173907

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.70 (201.4x median), `YEARS_BIRTH` = -1.28 (37.1x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `CREDIT_TERM_MONTHS` = -1.08 (22.7x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 174773

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.90 (65.7x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_ANNUITY` = 1.02 (14.5x median), `EXT_SOURCE_3` = -1.76 (9.5x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.47 (8.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 174937

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 15.89 (311.4x median), `BUREAU_BB_DPD_RATIO_MEAN` = 15.71 (81.8x median), `EXT_SOURCE_1` = 0.39 (27.9x median), `INST_SEVERE_LATE_RATIO` = 3.82 (23.7x median), `INST_LATE_RATIO` = 3.52 (22.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 175250

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 3.95 (78.2x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CREDIT_TERM_MONTHS` = 1.17 (16.5x median), `PREV_APPROVAL_RATE` = 0.30 (13.9x median), `POS_SK_DPD_MEAN` = 2.41 (11.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 175475

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 16.23 (327.0x median), `POS_MONTHS_COUNT` = -1.01 (28.1x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `YEARS_EMPLOYED` = 3.75 (18.9x median), `CREDIT_TERM_MONTHS` = -0.90 (18.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 175681

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 1.68 (37.7x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_BIRTH` = 1.09 (33.5x median), `AMT_INCOME_TOTAL` = 2.47 (21.6x median), `POS_MONTHS_COUNT` = -0.65 (18.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 175797

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 3.87 (102.5x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.58 (27.8x median), `AMT_ANNUITY` = -3.60 (26.6x median), `EXT_SOURCE_3` = -1.97 (18.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 176058

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.46 (109.5x median), `YEARS_BIRTH` = -1.52 (44.2x median), `CREDIT_TERM_MONTHS` = 0.92 (21.0x median), `BUREAU_BB_DPD_RATIO_MEAN` = 3.87 (20.9x median), `AMT_INCOME_TOTAL` = 2.31 (20.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 176132

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 7.05 (35.7x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = -1.45 (18.1x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `ANNUITY_TO_INCOME` = 1.29 (14.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 176511

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `POS_SK_DPD_MEAN` = 5.78 (29.1x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `ANNUITY_TO_INCOME` = 1.08 (12.7x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (10.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 176727

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.12 (156.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `AMT_INCOME_TOTAL` = 2.31 (20.1x median), `EXT_SOURCE_3` = 1.64 (13.7x median), `YEARS_BIRTH` = -0.43 (6.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 177078

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 19.09 (384.4x median), `PREV_APPROVAL_RATE` = -1.74 (86.6x median), `EXT_SOURCE_1` = -0.60 (45.5x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CREDIT_TERM_MONTHS` = -1.08 (13.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 177341

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.45 (108.4x median), `YEARS_BIRTH` = -1.68 (49.1x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = -1.62 (34.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 177439

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.71 (200.6x median), `INST_LATE_RATIO` = 2.82 (18.4x median), `BUREAU_COUNT` = 3.34 (11.8x median), `EXT_SOURCE_3` = -2.09 (11.5x median), `YEARS_EMPLOYED` = 3.17 (10.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 177447

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `YEARS_BIRTH` = -1.08 (31.2x median), `EXT_SOURCE_1` = -0.29 (22.3x median), `AMT_ANNUITY` = 1.68 (11.0x median), `CREDIT_TERM_MONTHS` = 0.45 (10.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 177542

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `CREDIT_TERM_MONTHS` = -0.94 (19.7x median), `POS_MONTHS_COUNT` = 0.72 (18.4x median), `YEARS_BIRTH` = 0.41 (13.3x median), `EXT_SOURCE_3` = -1.19 (11.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 177790

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = 1.67 (23.0x median), `EXT_SOURCE_1` = -0.29 (22.3x median), `BUREAU_COUNT` = 1.80 (11.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 178300

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.78 (56.6x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `EXT_SOURCE_3` = -2.03 (19.2x median), `BUREAU_ACTIVE_RATIO` = 0.89 (16.1x median), `EXT_SOURCE_2` = -1.60 (8.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 178837

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `AMT_CREDIT` = -0.73 (21.8x median), `EXT_SOURCE_1` = 0.24 (16.7x median), `AMT_ANNUITY` = -0.83 (13.6x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.59 (10.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 179673

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 7.96 (161.0x median), `PREV_APPROVAL_RATE` = -1.02 (51.1x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_BB_DPD_RATIO_MEAN` = 2.80 (15.4x median), `EXT_SOURCE_3` = -0.88 (8.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 179692

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.41 (177.7x median), `YEARS_BIRTH` = 0.89 (27.5x median), `POS_MONTHS_COUNT` = 0.72 (18.4x median), `BUREAU_COUNT` = 2.02 (12.2x median), `YEARS_EMPLOYED` = 1.89 (10.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 179847

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.26 (94.6x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `YEARS_BIRTH` = -1.07 (14.9x median), `BUREAU_ACTIVE_RATIO` = 1.41 (9.6x median), `CNT_CHILDREN` = 3.60 (7.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 179888

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 2.46 (64.8x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 2.43 (18.5x median), `CREDIT_TERM_MONTHS` = 0.52 (12.4x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.01 (11.9x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 180228

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_3` = -1.89 (18.0x median), `OWN_CAR_AGE` = 6.68 (15.7x median), `INST_LATE_RATIO` = 8.23 (14.1x median), `AMT_INCOME_TOTAL` = -1.66 (6.8x median), `EXT_SOURCE_2` = 0.55 (5.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 180398

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.40 (28.7x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.72 (7.5x median), `EXT_SOURCE_3` = 0.81 (6.2x median), `BUREAU_ACTIVE_RATIO` = -0.41 (5.9x median), `POS_MONTHS_COUNT` = 1.69 (4.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 180575

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.00 (147.6x median), `POS_MONTHS_COUNT` = 1.93 (50.7x median), `CREDIT_TERM_MONTHS` = 1.88 (42.1x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_COUNT` = 4.66 (26.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 180690

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 33.81 (661.3x median), `POS_MONTHS_COUNT` = 3.51 (92.8x median), `BUREAU_BB_DPD_RATIO_MEAN` = 15.95 (83.0x median), `YEARS_BIRTH` = -1.42 (41.4x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 181203

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.95 (71.7x median), `POS_MONTHS_COUNT` = 2.42 (63.7x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.23 (17.7x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.53 (17.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 181342

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -1.02 (51.1x median), `POS_SK_DPD_MEAN` = 9.56 (48.9x median), `AMT_ANNUITY` = 2.39 (25.7x median), `EXT_SOURCE_3` = 1.29 (10.6x median), `AMT_INCOME_TOTAL` = 2.01 (10.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 181464

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 4.31 (114.4x median), `EXT_SOURCE_1` = 1.39 (102.4x median), `BUREAU_COUNT` = 5.76 (33.0x median), `YEARS_BIRTH` = 0.95 (29.2x median), `AMT_INCOME_TOTAL` = 1.59 (13.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 181554

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟠 Tipe C — Risk Signal** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `AMT_INCOME_TOTAL` = -1.96 (19.0x median), `BUREAU_COUNT` = 1.58 (9.8x median), `ANNUITY_TO_INCOME` = 3.60 (8.1x median), `CREDIT_TO_INCOME` = 4.66 (7.7x median) |
| Justifikasi | Kombinasi finansial kontradiktif (mis. rasio cicilan/pendapatan ekstrem, income rendah + credit besar, atau skor eksternal tinggi di cluster bermasalah). |
| Business Impact | Underwriting: matikan auto-approve, wajibkan manual review oleh underwriter senior + verifikasi pendapatan fisik. |

---

## ROW_ID 181658

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.49 (23.2x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DAYS_CREDIT_MEAN` = -2.45 (14.3x median), `EXT_SOURCE_3` = 1.66 (13.9x median), `CC_UTILIZATION_MEAN` = 3.83 (10.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 181982

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.15 (158.9x median), `AMT_CREDIT` = -1.85 (57.0x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_ANNUITY` = -1.83 (28.7x median), `YEARS_BIRTH` = 1.86 (6.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 182191

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `EXT_SOURCE_3` = -2.47 (23.2x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `OWN_CAR_AGE` = 6.68 (15.7x median), `EXT_SOURCE_2` = -1.05 (13.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 182246

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 15.45 (311.3x median), `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = 0.84 (12.1x median), `AMT_ANNUITY` = -0.99 (12.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 182380

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_BIRTH` = 0.78 (24.3x median), `EXT_SOURCE_3` = -2.33 (21.9x median), `BUREAU_ACTIVE_RATIO` = 1.09 (19.5x median), `AMT_INCOME_TOTAL` = 2.08 (18.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 182753

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 11.12 (218.2x median), `POS_SK_DPD_MEAN` = 24.16 (125.0x median), `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `BUREAU_BB_DPD_RATIO_MEAN` = 8.33 (43.8x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 182895

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -1.60 (80.0x median), `CREDIT_TERM_MONTHS` = 2.17 (29.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DAYS_CREDIT_MEAN` = -2.57 (15.1x median), `AMT_ANNUITY` = -1.24 (14.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 183092

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.03 (77.5x median), `INST_SEVERE_LATE_RATIO` = 4.97 (30.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `AMT_INCOME_TOTAL` = -1.66 (6.8x median), `INST_DPD_MEAN` = 0.65 (6.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 183100

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 8.04 (162.4x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CREDIT_TERM_MONTHS` = -1.38 (17.2x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (10.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 183782

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 1.68 (37.8x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 1.85 (13.9x median), `PREV_APPROVAL_RATE` = -1.56 (10.4x median), `PREV_COUNT` = 2.90 (8.4x median), `EXT_SOURCE_3` = 1.03 (8.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 183918

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.23 (90.1x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `POS_MONTHS_COUNT` = 1.21 (31.3x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 1.85 (13.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 184010

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.03 (77.5x median), `PREV_APPROVAL_RATE` = -1.40 (69.7x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `ANNUITY_TO_INCOME` = 1.36 (15.6x median), `BUREAU_BB_DPD_RATIO_MEAN` = 2.47 (13.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 184014

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 11.51 (225.7x median), `BUREAU_BB_DPD_RATIO_MEAN` = 9.24 (48.5x median), `YEARS_EMPLOYED` = 3.68 (12.5x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.59 (10.5x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 184253

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.85 (136.7x median), `AMT_CREDIT` = 0.52 (17.3x median), `INST_LATE_RATIO` = 2.64 (17.3x median), `BUREAU_ACTIVE_RATIO` = 0.69 (12.7x median), `PREV_REFUSED_COUNT` = 6.23 (8.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 184730

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_BB_DPD_RATIO_MEAN` = 5.64 (30.0x median), `YEARS_BIRTH` = -0.92 (26.3x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 1.85 (13.9x median), `EXT_SOURCE_3` = -0.79 (8.1x median), `PREV_APPROVAL_RATE` = -1.24 (8.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 185509

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.53 (38.4x median), `CREDIT_TERM_MONTHS` = 1.70 (38.1x median), `YEARS_BIRTH` = -0.95 (27.4x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DAYS_CREDIT_MEAN` = 0.96 (14.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 185767

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CC_SK_DPD_MEAN` = 0.88 (18.7x median), `CC_MONTHS_COUNT` = 3.41 (8.8x median), `ANNUITY_TO_INCOME` = 0.69 (8.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 185927

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 4.74 (93.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `CREDIT_TERM_MONTHS` = -1.62 (34.5x median), `EXT_SOURCE_3` = -2.23 (21.1x median), `BUREAU_BB_DPD_RATIO_MEAN` = 3.75 (20.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 186204

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `YEARS_EMPLOYED` = 4.59 (12.0x median), `AMT_INCOME_TOTAL` = 1.56 (8.3x median), `EXT_SOURCE_2` = 0.71 (7.2x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (4.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 186214

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 14.73 (296.9x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `CREDIT_TERM_MONTHS` = 1.66 (22.9x median), `BUREAU_COUNT` = 2.68 (15.9x median), `EXT_SOURCE_2` = -2.35 (12.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 186318

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_DPD_MAX` = 3.10 (20.3x median), `YEARS_EMPLOYED` = 3.60 (16.8x median), `INST_SEVERE_LATE_RATIO` = 2.43 (15.5x median), `INST_DPD_MEAN` = 1.60 (15.0x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (11.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 186394

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 24.59 (127.2x median), `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `CREDIT_TERM_MONTHS` = -1.38 (17.2x median), `BUREAU_ACTIVE_RATIO` = -0.66 (10.1x median), `EXT_SOURCE_3` = 1.19 (9.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 186408

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.73 (34.9x median), `YEARS_EMPLOYED` = 2.68 (9.4x median), `CC_MONTHS_COUNT` = 3.53 (9.1x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median), `AMT_CREDIT` = 0.21 (7.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 186558

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `POS_SK_DPD_MEAN` = 7.59 (38.6x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = -1.51 (18.9x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 187053

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `CREDIT_TERM_MONTHS` = -1.07 (22.5x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `POS_MONTHS_COUNT` = 0.80 (20.5x median), `YEARS_BIRTH` = -0.72 (20.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 187456

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.86 (17.8x median), `AMT_CREDIT` = 0.52 (17.3x median), `BUREAU_ACTIVE_RATIO` = 0.86 (15.5x median), `EXT_SOURCE_3` = -2.39 (13.3x median), `CREDIT_TERM_MONTHS` = 1.97 (11.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 188002

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 9.73 (196.4x median), `EXT_SOURCE_1` = -2.07 (155.0x median), `CREDIT_TERM_MONTHS` = 1.68 (37.7x median), `POS_MONTHS_COUNT` = 1.01 (25.9x median), `YEARS_BIRTH` = -0.90 (25.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 188157

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.48 (36.9x median), `YEARS_BIRTH` = -0.94 (27.0x median), `BUREAU_DAYS_CREDIT_MEAN` = -0.92 (11.5x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median), `AMT_INCOME_TOTAL` = 0.86 (6.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 188184

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `YEARS_BIRTH` = -1.18 (34.1x median), `CREDIT_TERM_MONTHS` = -1.56 (33.2x median), `POS_MONTHS_COUNT` = 1.25 (32.4x median), `AMT_INCOME_TOTAL` = 2.47 (21.6x median), `BUREAU_COUNT` = 2.46 (14.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 188427

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.00 (147.2x median), `INST_DPD_MAX` = 5.75 (56.2x median), `POS_MONTHS_COUNT` = 1.77 (46.4x median), `YEARS_BIRTH` = 0.84 (26.0x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.50 (19.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 188477

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `AMT_CREDIT` = -2.24 (69.2x median), `AMT_ANNUITY` = -1.59 (25.1x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.59 (10.5x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (9.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 188627

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 7.55 (152.7x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = 1.68 (23.1x median), `BUREAU_ACTIVE_RATIO` = 0.64 (11.8x median), `PREV_APPROVAL_RATE` = -0.14 (7.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 189049

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.76 (129.7x median), `EXT_SOURCE_3` = -2.41 (22.6x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.20 (9.7x median), `BUREAU_ACTIVE_RATIO` = 1.25 (8.6x median), `ANNUITY_TO_INCOME` = 3.37 (7.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 189092

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 15.71 (80.9x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `AMT_ANNUITY` = -1.37 (16.3x median), `YEARS_BIRTH` = 1.96 (14.1x median), `EXT_SOURCE_3` = -1.16 (11.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 189094

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 1.28 (29.1x median), `INST_SEVERE_LATE_RATIO` = 3.82 (23.7x median), `INST_DPD_MAX` = 1.35 (14.0x median), `BUREAU_COUNT` = 1.80 (11.0x median), `INST_DPD_MEAN` = 0.83 (9.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 189184

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -1.02 (51.1x median), `POS_SK_DPD_MEAN` = 9.91 (50.7x median), `EXT_SOURCE_1` = 0.46 (33.4x median), `BUREAU_COUNT` = 3.12 (18.3x median), `EXT_SOURCE_3` = 1.39 (11.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 189261

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.93 (142.6x median), `POS_SK_DPD_MEAN` = 5.57 (28.1x median), `AMT_ANNUITY` = -2.22 (25.9x median), `PREV_APPROVAL_RATE` = 0.30 (13.9x median), `BUREAU_COUNT` = 1.80 (11.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 189304

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.31 (170.6x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.49 (17.1x median), `YEARS_BIRTH` = -0.46 (12.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 189409

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟠 Tipe C — Risk Signal** |
| Top Deviating Features | `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `AMT_INCOME_TOTAL` = -2.13 (20.5x median), `YEARS_BIRTH` = -0.70 (19.8x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `POS_MONTHS_COUNT` = -0.61 (17.3x median) |
| Justifikasi | Kombinasi finansial kontradiktif (mis. rasio cicilan/pendapatan ekstrem, income rendah + credit besar, atau skor eksternal tinggi di cluster bermasalah). |
| Business Impact | Underwriting: matikan auto-approve, wajibkan manual review oleh underwriter senior + verifikasi pendapatan fisik. |

---

## ROW_ID 189641

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -1.24 (62.0x median), `EXT_SOURCE_1` = -0.70 (52.9x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `YEARS_BIRTH` = -1.23 (10.4x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (10.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 190004

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `EXT_SOURCE_3` = -1.01 (10.1x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.36 (9.5x median), `POS_SK_DPD_MEAN` = 1.96 (9.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 190053

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.66 (122.4x median), `POS_MONTHS_COUNT` = 1.81 (47.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_BIRTH` = 0.94 (29.0x median), `AMT_INCOME_TOTAL` = 2.31 (20.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 190254

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.45 (180.8x median), `YEARS_BIRTH` = 1.38 (16.9x median), `YEARS_EMPLOYED` = 3.25 (15.3x median), `AMT_INCOME_TOTAL` = 1.56 (13.3x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.08 (3.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 190357

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.97 (71.3x median), `AMT_CREDIT` = 1.99 (63.4x median), `AMT_ANNUITY` = 2.06 (30.2x median), `BUREAU_ACTIVE_RATIO` = -0.58 (8.9x median), `EXT_SOURCE_3` = -1.51 (8.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 190647

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.82 (17.1x median), `AMT_CREDIT` = -0.47 (13.8x median), `AMT_ANNUITY` = -0.50 (8.5x median), `YEARS_EMPLOYED` = 2.26 (8.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 191009

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `POS_MONTHS_COUNT` = -0.97 (27.0x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `CREDIT_TERM_MONTHS` = 0.86 (19.9x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 191256

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 8.30 (167.8x median), `EXT_SOURCE_1` = 2.09 (154.3x median), `AMT_ANNUITY` = -2.95 (33.9x median), `AMT_CREDIT` = -3.26 (21.7x median), `CREDIT_TERM_MONTHS` = -1.48 (18.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 191401

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 2.14 (47.8x median), `POS_MONTHS_COUNT` = 1.41 (36.7x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `INST_DPD_MAX` = 2.30 (23.1x median), `EXT_SOURCE_3` = -1.87 (17.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 191864

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 17.82 (91.9x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `ANNUITY_TO_INCOME` = 2.85 (31.6x median), `CREDIT_TO_INCOME` = 3.69 (24.4x median), `CREDIT_TERM_MONTHS` = 1.17 (16.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 192005

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.22 (165.9x median), `CREDIT_TERM_MONTHS` = 2.15 (48.1x median), `YEARS_BIRTH` = -1.43 (41.6x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.00 (23.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 192426

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.83 (136.7x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `POS_SK_DPD_MEAN` = 2.43 (11.7x median), `AMT_ANNUITY` = -0.84 (10.4x median), `EXT_SOURCE_3` = -1.02 (10.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 192531

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.65 (121.4x median), `AMT_CREDIT` = 2.10 (66.8x median), `AMT_ANNUITY` = 2.03 (29.8x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.81 (16.9x median), `EXT_SOURCE_3` = -2.10 (11.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 193089

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 2.50 (65.8x median), `INST_SEVERE_LATE_RATIO` = 5.24 (32.1x median), `CREDIT_TERM_MONTHS` = 1.30 (29.5x median), `CC_SK_DPD_MEAN` = 0.99 (20.9x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 193211

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.04 (76.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_ACTIVE_RATIO` = 2.03 (13.4x median), `ANNUITY_TO_INCOME` = 5.23 (12.2x median), `CREDIT_TO_INCOME` = 5.91 (10.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 193517

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_CREDIT` = -1.19 (36.4x median), `INST_SEVERE_LATE_RATIO` = 4.39 (27.1x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.94 (19.5x median), `AMT_ANNUITY` = -1.05 (16.9x median), `EXT_SOURCE_3` = -2.57 (14.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 194100

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 8.51 (167.1x median), `BUREAU_BB_DPD_RATIO_MEAN` = 7.49 (39.5x median), `PREV_APPROVAL_RATE` = -0.41 (21.3x median), `POS_SK_DPD_MEAN` = 3.36 (16.5x median), `ANNUITY_TO_INCOME` = -1.28 (12.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 194133

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -3.25 (242.0x median), `INST_SEVERE_LATE_RATIO` = 6.00 (36.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `INST_DPD_MEAN` = 1.05 (10.2x median), `INST_LATE_RATIO` = 3.94 (7.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 194170

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 1.68 (37.8x median), `POS_MONTHS_COUNT` = 1.33 (34.5x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.58 (27.8x median), `EXT_SOURCE_3` = -2.36 (22.2x median), `AMT_INCOME_TOTAL` = 2.20 (19.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 194559

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `YEARS_BIRTH` = 1.75 (12.5x median), `EXT_SOURCE_3` = 1.40 (11.6x median), `CREDIT_TERM_MONTHS` = -0.87 (10.4x median), `POS_SK_DPD_MEAN` = 1.54 (7.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 194611

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.34 (173.0x median), `AMT_CREDIT` = -1.01 (30.8x median), `AMT_ANNUITY` = -1.37 (21.7x median), `YEARS_EMPLOYED` = 3.68 (12.5x median), `BUREAU_COUNT` = 2.90 (10.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 194744

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 3.02 (18.9x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (11.5x median), `AMT_INCOME_TOTAL` = 1.24 (10.3x median), `YEARS_EMPLOYED` = 1.12 (5.9x median), `BUREAU_ACTIVE_RATIO` = -1.11 (5.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 195575

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.83 (211.5x median), `POS_MONTHS_COUNT` = 2.66 (70.2x median), `BUREAU_COUNT` = 4.88 (28.1x median), `EXT_SOURCE_3` = -1.30 (12.6x median), `YEARS_BIRTH` = 0.37 (12.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 195943

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 4.50 (27.7x median), `YEARS_BIRTH` = -1.13 (15.6x median), `EXT_SOURCE_3` = -1.57 (15.1x median), `INST_LATE_RATIO` = 3.48 (6.5x median), `BUREAU_DAYS_CREDIT_MEAN` = 0.69 (6.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 195949

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 1.67 (37.6x median), `INST_SEVERE_LATE_RATIO` = 3.48 (21.6x median), `EXT_SOURCE_3` = -1.68 (16.1x median), `YEARS_EMPLOYED` = 2.63 (13.6x median), `YEARS_BIRTH` = 0.42 (13.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 196091

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.29 (97.1x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `POS_MONTHS_COUNT` = -1.13 (31.3x median), `CREDIT_TERM_MONTHS` = -1.31 (27.6x median), `YEARS_BIRTH` = -0.93 (26.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 196668

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 4.80 (24.0x median), `CREDIT_TERM_MONTHS` = 1.69 (23.4x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `EXT_SOURCE_3` = 0.99 (7.9x median), `CREDIT_TO_INCOME` = 1.07 (7.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 196866

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `INST_LATE_RATIO` = 8.23 (14.1x median), `EXT_SOURCE_3` = 1.60 (13.3x median), `EXT_SOURCE_2` = -0.97 (12.2x median), `INST_DPD_MEAN` = 1.24 (11.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 196962

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_ANNUITY` = -1.78 (20.9x median), `POS_SK_DPD_MEAN` = 3.95 (19.6x median), `PREV_APPROVAL_RATE` = -0.36 (18.6x median), `AMT_CREDIT` = -1.33 (9.4x median), `ANNUITY_TO_INCOME` = -0.86 (8.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 197079

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.84 (137.4x median), `BUREAU_COUNT` = 3.34 (19.6x median), `YEARS_BIRTH` = -1.12 (15.5x median), `PREV_COUNT` = 2.19 (6.5x median), `CREDIT_TO_INCOME` = 3.60 (5.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 197824

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.39 (30.1x median), `ANNUITY_TO_INCOME` = 2.16 (24.2x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DAYS_CREDIT_MEAN` = -2.71 (15.9x median), `AMT_INCOME_TOTAL` = -2.51 (10.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 198036

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.52 (17.5x median), `CREDIT_TERM_MONTHS` = -0.70 (14.3x median), `YEARS_BIRTH` = -0.44 (12.0x median), `BUREAU_DAYS_CREDIT_MEAN` = 0.81 (12.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 198165

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟠 Tipe C — Risk Signal** |
| Top Deviating Features | `YEARS_EMPLOYED` = 4.11 (19.1x median), `EXT_SOURCE_3` = -1.92 (18.3x median), `AMT_INCOME_TOTAL` = -1.73 (16.9x median), `INST_SEVERE_LATE_RATIO` = 2.60 (16.5x median), `INST_DPD_MEAN` = 0.92 (9.1x median) |
| Justifikasi | Kombinasi finansial kontradiktif (mis. rasio cicilan/pendapatan ekstrem, income rendah + credit besar, atau skor eksternal tinggi di cluster bermasalah). |
| Business Impact | Underwriting: matikan auto-approve, wajibkan manual review oleh underwriter senior + verifikasi pendapatan fisik. |

---

## ROW_ID 198501

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 4.11 (109.0x median), `EXT_SOURCE_1` = -1.41 (105.8x median), `YEARS_BIRTH` = -1.38 (40.1x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.00 (23.2x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 198696

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.88 (64.6x median), `PREV_REFUSED_COUNT` = 19.60 (28.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `INST_LATE_RATIO` = 1.54 (10.5x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.59 (10.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 199089

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.17 (85.7x median), `POS_MONTHS_COUNT` = 2.10 (55.1x median), `YEARS_BIRTH` = 1.39 (42.6x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.58 (27.8x median), `CREDIT_TERM_MONTHS` = 1.17 (26.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 199155

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -1.51 (75.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `ANNUITY_TO_INCOME` = 1.83 (20.7x median), `CREDIT_TERM_MONTHS` = -1.48 (18.5x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 199557

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 6.14 (124.4x median), `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `BUREAU_ACTIVE_RATIO` = 1.18 (20.9x median), `CREDIT_TERM_MONTHS` = 1.26 (17.6x median), `EXT_SOURCE_3` = -1.83 (17.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 199872

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `POS_SK_DPD_MEAN` = 5.57 (28.1x median), `AMT_ANNUITY` = -2.30 (26.7x median), `BUREAU_COUNT` = 2.68 (15.9x median), `EXT_SOURCE_3` = -1.40 (13.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 200163

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 3.14 (83.1x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_INCOME_TOTAL` = -0.68 (7.2x median), `BUREAU_ACTIVE_RATIO` = -0.48 (7.1x median), `PREV_APPROVAL_RATE` = 0.63 (5.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 200183

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.63 (121.9x median), `INST_SEVERE_LATE_RATIO` = 3.28 (20.5x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `INST_DPD_MEAN` = 1.17 (11.3x median), `INST_DPD_MAX` = 1.22 (8.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 200356

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.91 (217.4x median), `POS_MONTHS_COUNT` = 1.41 (36.7x median), `YEARS_BIRTH` = -1.25 (36.2x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.00 (23.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 200563

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 7.12 (43.3x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `INST_DPD_MEAN` = 0.67 (6.9x median), `INST_LATE_RATIO` = 3.17 (6.0x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.31 (6.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 200767

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.74 (55.7x median), `BUREAU_ACTIVE_RATIO` = 1.34 (23.6x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.00 (23.2x median), `CREDIT_TERM_MONTHS` = -0.95 (19.8x median), `YEARS_BIRTH` = -0.70 (19.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 200786

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_CREDIT` = -1.51 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `AMT_ANNUITY` = -2.02 (31.6x median), `BUREAU_COUNT` = 5.76 (21.2x median), `EXT_SOURCE_1` = 0.24 (16.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 200956

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.00 (72.9x median), `INST_SEVERE_LATE_RATIO` = 8.33 (50.5x median), `YEARS_BIRTH` = -1.08 (15.0x median), `EXT_SOURCE_3` = -1.01 (10.1x median), `INST_DPD_MEAN` = 0.92 (9.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 201389

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.65 (47.3x median), `INST_SEVERE_LATE_RATIO` = 3.02 (18.9x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `INST_DPD_MAX` = 1.30 (9.1x median), `EXT_SOURCE_2` = 0.80 (8.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 201812

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 1.68 (37.7x median), `POS_MONTHS_COUNT` = 1.33 (34.5x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.58 (27.8x median), `YEARS_BIRTH` = 0.71 (22.2x median), `BUREAU_ACTIVE_RATIO` = 1.25 (22.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 202489

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.82 (136.4x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `YEARS_BIRTH` = -1.15 (33.2x median), `POS_MONTHS_COUNT` = 1.09 (28.1x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.73 (19.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 202495

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.47 (110.4x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.00 (23.2x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.42 (18.2x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `POS_MONTHS_COUNT` = 0.68 (17.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 203192

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.21 (89.1x median), `YEARS_BIRTH` = 1.44 (43.9x median), `POS_MONTHS_COUNT` = 1.33 (34.5x median), `CREDIT_TERM_MONTHS` = 1.26 (28.6x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.43 (16.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 203542

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 1.68 (37.8x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TO_INCOME` = 3.51 (16.1x median), `YEARS_BIRTH` = -0.56 (15.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 203701

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_CREDIT` = 1.43 (45.9x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.09 (22.3x median), `CREDIT_TERM_MONTHS` = 1.96 (11.0x median), `AMT_ANNUITY` = 0.74 (10.2x median), `INST_LATE_RATIO` = 1.23 (8.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 203768

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.00 (73.4x median), `PREV_APPROVAL_RATE` = -0.87 (43.9x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CREDIT_TERM_MONTHS` = 1.27 (17.7x median), `CREDIT_TO_INCOME` = 1.56 (10.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 204143

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.75 (203.5x median), `YEARS_EMPLOYED` = 4.07 (18.9x median), `EXT_SOURCE_3` = 1.33 (11.0x median), `YEARS_BIRTH` = 0.84 (9.8x median), `CREDIT_TO_INCOME` = 3.26 (5.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 204172

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 4.74 (29.1x median), `YEARS_BIRTH` = 1.26 (15.4x median), `BUREAU_ACTIVE_RATIO` = 2.03 (13.4x median), `EXT_SOURCE_3` = 1.48 (12.3x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.17 (9.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 204202

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_1` = 0.40 (28.9x median), `YEARS_BIRTH` = -0.93 (26.7x median), `BUREAU_COUNT` = 4.00 (23.2x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.00 (23.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 204419

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.12 (83.9x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `POS_MONTHS_COUNT` = 0.88 (22.7x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 2.43 (18.5x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 204477

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_ACTIVE_RATIO` = 1.41 (24.8x median), `YEARS_EMPLOYED` = 3.62 (18.3x median), `YEARS_BIRTH` = 0.52 (16.5x median), `AMT_INCOME_TOTAL` = 1.24 (10.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 204699

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.36 (102.3x median), `AMT_CREDIT` = 1.42 (45.7x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `INST_DPD_MAX` = 3.63 (30.5x median), `INST_SEVERE_LATE_RATIO` = 3.70 (23.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 204943

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.59 (117.0x median), `YEARS_BIRTH` = 1.42 (43.3x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.85 (24.0x median), `POS_MONTHS_COUNT` = -0.85 (23.7x median), `EXT_SOURCE_3` = 1.42 (11.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 204990

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.24 (167.5x median), `YEARS_BIRTH` = -1.11 (32.2x median), `POS_MONTHS_COUNT` = 0.52 (13.0x median), `BUREAU_DAYS_CREDIT_MEAN` = 0.79 (11.7x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 205153

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.71 (51.8x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `AMT_CREDIT` = 0.78 (25.3x median), `AMT_ANNUITY` = 0.97 (13.7x median), `INST_LATE_RATIO` = 1.46 (10.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 205665

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 1.69 (38.1x median), `EXT_SOURCE_1` = 0.50 (35.8x median), `BUREAU_DAYS_CREDIT_MEAN` = -2.14 (28.1x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `POS_MONTHS_COUNT` = -0.61 (17.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 206099

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 2.82 (74.5x median), `CREDIT_TERM_MONTHS` = 1.69 (38.1x median), `YEARS_BIRTH` = -0.76 (21.8x median), `EXT_SOURCE_3` = -2.24 (21.1x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.46 (18.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 206109

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.90 (68.1x median), `CREDIT_TERM_MONTHS` = -0.79 (16.3x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.82 (9.9x median), `YEARS_BIRTH` = -0.30 (8.1x median), `PREV_APPROVAL_RATE` = 0.96 (8.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 206162

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟠 Tipe C — Risk Signal** |
| Top Deviating Features | `AMT_INCOME_TOTAL` = -2.31 (22.2x median), `EXT_SOURCE_3` = -1.73 (16.6x median), `ANNUITY_TO_INCOME` = 6.84 (16.2x median), `POS_MONTHS_COUNT` = 3.31 (8.4x median), `INST_DPD_MAX` = 1.11 (7.9x median) |
| Justifikasi | Kombinasi finansial kontradiktif (mis. rasio cicilan/pendapatan ekstrem, income rendah + credit besar, atau skor eksternal tinggi di cluster bermasalah). |
| Business Impact | Underwriting: matikan auto-approve, wajibkan manual review oleh underwriter senior + verifikasi pendapatan fisik. |

---

## ROW_ID 206540

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `YEARS_BIRTH` = -1.25 (36.2x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_INCOME_TOTAL` = 2.31 (20.1x median), `POS_MONTHS_COUNT` = -0.61 (17.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 207021

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.38 (101.5x median), `AMT_CREDIT` = 1.89 (60.3x median), `AMT_ANNUITY` = 1.76 (25.7x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.91 (18.8x median), `CREDIT_TERM_MONTHS` = 1.00 (6.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 207066

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.03 (77.7x median), `EXT_SOURCE_2` = -2.65 (31.8x median), `EXT_SOURCE_3` = -1.95 (18.5x median), `CNT_CHILDREN` = 2.21 (4.8x median), `BUREAU_ACTIVE_RATIO` = -0.32 (4.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 207359

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.55 (114.1x median), `CREDIT_TERM_MONTHS` = 1.68 (37.7x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.58 (27.8x median), `POS_MONTHS_COUNT` = -0.65 (18.4x median), `BUREAU_ACTIVE_RATIO` = 0.78 (14.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 207437

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.23 (90.6x median), `AMT_CREDIT` = 1.38 (44.4x median), `AMT_ANNUITY` = 1.42 (20.5x median), `BUREAU_COUNT` = 4.22 (15.2x median), `EXT_SOURCE_3` = -2.21 (12.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 207735

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `AMT_ANNUITY` = -1.25 (15.0x median), `EXT_SOURCE_3` = 1.48 (12.3x median), `AMT_CREDIT` = -1.34 (9.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 208114

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_CREDIT` = 1.39 (44.8x median), `INST_SEVERE_LATE_RATIO` = 5.72 (35.0x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_BB_DPD_RATIO_MEAN` = 2.63 (14.5x median), `AMT_ANNUITY` = 0.98 (13.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 208193

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.38 (176.1x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `EXT_SOURCE_2` = 1.21 (13.1x median), `EXT_SOURCE_3` = 1.39 (11.4x median), `BUREAU_ACTIVE_RATIO` = -0.58 (8.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 208646

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.30 (169.9x median), `AMT_CREDIT` = -0.55 (16.4x median), `INST_LATE_RATIO` = 2.10 (14.0x median), `EXT_SOURCE_3` = -2.01 (11.0x median), `BUREAU_ACTIVE_RATIO` = 0.34 (6.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 208663

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.16 (159.5x median), `INST_SEVERE_LATE_RATIO` = 5.91 (36.1x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `EXT_SOURCE_2` = -0.93 (11.8x median), `INST_DPD_MEAN` = 0.95 (9.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 208712

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.75 (56.6x median), `INST_SEVERE_LATE_RATIO` = 5.91 (36.1x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_COUNT` = 2.90 (17.1x median), `YEARS_BIRTH` = -0.98 (13.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 208751

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 5.54 (109.1x median), `EXT_SOURCE_1` = -0.67 (50.5x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.35 (27.5x median), `BUREAU_BB_DPD_RATIO_MEAN` = 5.13 (27.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 209003

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.44 (108.1x median), `CREDIT_TERM_MONTHS` = 2.13 (29.1x median), `PREV_APPROVAL_RATE` = 0.30 (13.9x median), `EXT_SOURCE_2` = -2.48 (13.3x median), `YEARS_BIRTH` = -1.28 (10.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 209110

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 31.29 (629.5x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `ANNUITY_TO_INCOME` = 3.04 (33.7x median), `CREDIT_TO_INCOME` = 3.33 (22.1x median), `AMT_ANNUITY` = 1.30 (13.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 209267

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `INST_LATE_RATIO` = 1.96 (13.1x median), `INST_SEVERE_LATE_RATIO` = 1.70 (11.1x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.36 (8.1x median), `BUREAU_COUNT` = 2.02 (6.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 210214

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.07 (78.8x median), `CREDIT_TERM_MONTHS` = 1.25 (28.4x median), `YEARS_BIRTH` = -0.95 (27.2x median), `BUREAU_ACTIVE_RATIO` = 1.41 (24.8x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 2.43 (18.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 210469

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.16 (85.3x median), `POS_MONTHS_COUNT` = 2.46 (64.8x median), `YEARS_BIRTH` = 1.23 (37.7x median), `CREDIT_TERM_MONTHS` = 1.28 (29.1x median), `BUREAU_COUNT` = 3.12 (18.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 210631

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.35 (99.6x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 3.10 (61.6x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `POS_SK_DPD_MEAN` = 4.23 (21.1x median), `AMT_ANNUITY` = 1.93 (20.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 211267

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.72 (52.5x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 1.29 (26.2x median), `CREDIT_TERM_MONTHS` = 1.67 (23.1x median), `BUREAU_COUNT` = 3.78 (22.0x median), `EXT_SOURCE_3` = -2.22 (20.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 211400

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `EXT_SOURCE_2` = 1.36 (14.9x median), `AMT_INCOME_TOTAL` = 2.47 (12.6x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (4.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 211479

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.01 (73.8x median), `OWN_CAR_AGE` = 6.68 (15.7x median), `EXT_SOURCE_2` = 1.07 (11.5x median), `CNT_CHILDREN` = 2.21 (4.8x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.45 (4.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 211510

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 12.55 (253.1x median), `POS_SK_DPD_MEAN` = 26.57 (137.5x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `BUREAU_ACTIVE_RATIO` = 1.25 (22.2x median), `CREDIT_TERM_MONTHS` = 1.27 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 211652

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 7.37 (149.0x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = 1.67 (23.1x median), `EXT_SOURCE_2` = -2.30 (12.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 211892

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.87 (137.8x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `INST_LATE_RATIO` = 0.97 (7.0x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.36 (6.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 211981

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.25 (168.3x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `OWN_CAR_AGE` = 6.68 (15.7x median), `EXT_SOURCE_2` = -0.72 (9.4x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (4.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 212446

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 21.98 (442.4x median), `EXT_SOURCE_1` = 1.52 (111.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_BIRTH` = -0.48 (13.4x median), `BUREAU_ACTIVE_RATIO` = 0.69 (12.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 212863

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.43 (105.6x median), `POS_MONTHS_COUNT` = 1.93 (50.7x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.63 (18.6x median), `AMT_INCOME_TOTAL` = -1.66 (16.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 212993

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (10.1x median), `AMT_ANNUITY` = -0.80 (10.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 213250

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `OWN_CAR_AGE` = 6.68 (15.7x median), `EXT_SOURCE_2` = 0.87 (9.2x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (4.5x median), `AMT_INCOME_TOTAL` = 0.73 (4.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 214109

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `CREDIT_TERM_MONTHS` = -1.62 (20.3x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `AMT_CREDIT` = -1.73 (12.0x median), `EXT_SOURCE_2` = -2.03 (11.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 214674

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.27 (167.4x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `EXT_SOURCE_2` = 1.24 (13.4x median), `EXT_SOURCE_3` = 0.93 (7.3x median), `AMT_INCOME_TOTAL` = 1.17 (6.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 214684

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.80 (206.8x median), `CREDIT_TERM_MONTHS` = 1.97 (44.2x median), `YEARS_BIRTH` = 1.40 (42.7x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.30 (15.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 214945

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `OWN_CAR_AGE` = 6.68 (15.7x median), `YEARS_BIRTH` = -0.53 (7.9x median), `CNT_CHILDREN` = 3.60 (7.2x median), `CC_UTILIZATION_MAX` = 1.50 (4.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 215228

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `EXT_SOURCE_2` = 0.76 (7.8x median), `YEARS_BIRTH` = -1.31 (2.4x median), `BUREAU_DAYS_CREDIT_MEAN` = 0.90 (2.4x median), `AMT_INCOME_TOTAL` = -0.59 (1.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 215381

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.21 (88.6x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `YEARS_BIRTH` = -0.93 (26.8x median), `POS_MONTHS_COUNT` = -0.85 (23.7x median), `CREDIT_TERM_MONTHS` = -1.10 (23.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 215748

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_CREDIT` = 0.72 (23.5x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DAYS_CREDIT_MEAN` = -2.51 (13.1x median), `AMT_ANNUITY` = 0.93 (13.1x median), `YEARS_EMPLOYED` = 3.17 (10.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 215866

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 1.53 (39.9x median), `EXT_SOURCE_1` = 0.54 (39.2x median), `YEARS_BIRTH` = 1.17 (35.8x median), `CREDIT_TERM_MONTHS` = 1.30 (29.5x median), `BUREAU_DAYS_CREDIT_MEAN` = 0.62 (9.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 216791

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.63 (120.4x median), `BUREAU_DAYS_CREDIT_MEAN` = -2.80 (19.3x median), `YEARS_EMPLOYED` = 3.96 (18.4x median), `EXT_SOURCE_3` = -1.13 (11.1x median), `YEARS_BIRTH` = 0.85 (10.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 217159

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `EXT_SOURCE_1` = 0.46 (33.4x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `EXT_SOURCE_2` = 0.66 (6.6x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (4.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 217233

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.41 (19.4x median), `BUREAU_ACTIVE_RATIO` = 0.78 (14.2x median), `EXT_SOURCE_3` = 1.48 (12.3x median), `YEARS_BIRTH` = -1.27 (10.8x median), `ANNUITY_TO_INCOME` = -1.08 (10.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 217235

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_2` = 1.17 (12.7x median), `BUREAU_DAYS_CREDIT_MEAN` = -2.31 (9.8x median), `AMT_INCOME_TOTAL` = 1.24 (6.8x median), `CNT_CHILDREN` = 2.21 (4.8x median), `EXT_SOURCE_3` = 0.54 (3.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 217638

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `YEARS_EMPLOYED` = 3.83 (10.1x median), `OWN_CAR_AGE` = 1.66 (4.7x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (4.5x median), `AMT_INCOME_TOTAL` = -1.17 (4.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 217835

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.15 (86.4x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 2.43 (18.5x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.59 (18.1x median), `BUREAU_DAYS_CREDIT_MEAN` = 0.72 (10.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 218263

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_BB_DPD_RATIO_MEAN` = 3.61 (19.6x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 2.43 (18.5x median), `CREDIT_TERM_MONTHS` = 0.71 (16.5x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.82 (9.9x median), `BUREAU_DAYS_CREDIT_MEAN` = 0.65 (9.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 218420

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.84 (61.3x median), `INST_DPD_MAX` = 4.28 (42.1x median), `INST_SEVERE_LATE_RATIO` = 3.72 (23.1x median), `POS_MONTHS_COUNT` = 0.80 (20.5x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 218649

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_CREDIT` = -0.56 (16.5x median), `AMT_ANNUITY` = -0.72 (11.9x median), `BUREAU_COUNT` = 3.34 (11.8x median), `CC_MONTHS_COUNT` = 3.37 (8.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 218779

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `INST_SEVERE_LATE_RATIO` = 3.37 (21.0x median), `YEARS_BIRTH` = -0.74 (10.6x median), `BUREAU_COUNT` = 1.36 (8.6x median), `INST_LATE_RATIO` = 3.80 (7.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 219141

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.70 (52.9x median), `CREDIT_TERM_MONTHS` = 1.27 (28.8x median), `POS_MONTHS_COUNT` = 0.72 (18.4x median), `BUREAU_COUNT` = 3.12 (18.3x median), `BUREAU_ACTIVE_RATIO` = 0.88 (15.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 219260

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_INCOME_TOTAL` = 1.84 (15.8x median), `OWN_CAR_AGE` = 6.68 (15.7x median), `YEARS_BIRTH` = -0.63 (9.1x median), `YEARS_EMPLOYED` = 1.46 (7.4x median), `BUREAU_DAYS_CREDIT_MEAN` = -0.94 (5.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 219615

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.89 (139.1x median), `POS_MONTHS_COUNT` = 1.53 (39.9x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `CREDIT_TERM_MONTHS` = -0.94 (19.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 219650

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.98 (146.3x median), `POS_MONTHS_COUNT` = 3.43 (90.7x median), `YEARS_BIRTH` = 0.89 (27.5x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.00 (23.2x median), `INST_DPD_MAX` = 1.96 (19.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 220062

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_2` = -2.18 (26.3x median), `INST_SEVERE_LATE_RATIO` = 3.82 (23.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `INST_LATE_RATIO` = 7.12 (12.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 220092

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_DPD_MAX` = 5.13 (32.9x median), `POS_SK_DPD_MEAN` = 1.79 (26.6x median), `INST_DPD_MEAN` = 2.13 (19.8x median), `EXT_SOURCE_3` = 1.69 (14.2x median), `BUREAU_ACTIVE_RATIO` = -0.63 (9.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 221109

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `POS_MONTHS_COUNT` = -0.45 (13.0x median), `YEARS_BIRTH` = 0.36 (11.8x median), `BUREAU_DAYS_CREDIT_MEAN` = -0.92 (11.4x median), `PREV_APPROVAL_RATE` = -1.68 (11.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 221168

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 6.84 (134.5x median), `EXT_SOURCE_1` = 1.53 (112.7x median), `BUREAU_BB_DPD_RATIO_MEAN` = 3.89 (21.0x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.62 (21.0x median), `POS_MONTHS_COUNT` = -0.69 (19.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 221792

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.97 (145.5x median), `AMT_INCOME_TOTAL` = -1.66 (16.2x median), `YEARS_EMPLOYED` = 3.26 (15.3x median), `ANNUITY_TO_INCOME` = 3.74 (8.4x median), `BUREAU_COUNT` = 0.92 (6.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 222023

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 6.94 (140.4x median), `EXT_SOURCE_1` = 1.09 (79.9x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_COUNT` = 2.68 (15.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 222136

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 9.74 (49.8x median), `ANNUITY_TO_INCOME` = 1.24 (14.4x median), `EXT_SOURCE_1` = 0.20 (13.9x median), `CREDIT_TO_INCOME` = 1.38 (9.8x median), `CREDIT_TERM_MONTHS` = 0.52 (7.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 222258

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 4.20 (85.3x median), `EXT_SOURCE_1` = 0.83 (60.7x median), `CREDIT_TERM_MONTHS` = 1.27 (17.7x median), `ANNUITY_TO_INCOME` = 1.34 (15.4x median), `CREDIT_TO_INCOME` = 2.15 (14.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 222410

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.82 (134.3x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 1.37 (27.7x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 5.87 (18.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 222587

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.07 (80.7x median), `BUREAU_BB_DPD_RATIO_MEAN` = 12.09 (63.2x median), `INST_DPD_MAX` = 2.99 (19.6x median), `EXT_SOURCE_2` = -1.40 (17.3x median), `INST_DPD_MEAN` = 1.59 (15.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 222816

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 2.82 (57.6x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = 1.67 (23.0x median), `EXT_SOURCE_1` = 0.26 (18.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 223331

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 9.05 (177.8x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `BUREAU_BB_DPD_RATIO_MEAN` = 5.33 (28.4x median), `BUREAU_DAYS_CREDIT_MEAN` = -2.37 (12.3x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.59 (10.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 223708

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 8.29 (167.6x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `CREDIT_TERM_MONTHS` = 1.27 (17.7x median), `CC_MONTHS_COUNT` = 3.45 (8.9x median), `PREV_APPROVAL_RATE` = -0.14 (7.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 223735

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.47 (184.1x median), `CC_SK_DPD_MEAN` = 6.23 (126.1x median), `CREDIT_TERM_MONTHS` = 1.70 (23.4x median), `CREDIT_TO_INCOME` = 1.64 (11.4x median), `YEARS_BIRTH` = -1.04 (9.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 224138

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `AMT_ANNUITY` = -1.43 (17.0x median), `EXT_SOURCE_3` = 1.80 (15.2x median), `YEARS_EMPLOYED` = 4.04 (13.0x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 224386

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.66 (124.3x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `INST_SEVERE_LATE_RATIO` = 5.15 (31.6x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `EXT_SOURCE_2` = -0.94 (12.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 224754

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.44 (108.0x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_CREDIT` = 0.47 (15.9x median), `PREV_REFUSED_COUNT` = 9.02 (12.7x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.59 (10.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 224921

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 2.06 (54.0x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_EMPLOYED` = 3.62 (18.3x median), `YEARS_BIRTH` = 0.47 (15.0x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 1.85 (13.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 225339

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 22.95 (118.6x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_ANNUITY` = 2.54 (27.4x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 225382

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.63 (194.1x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `CREDIT_TERM_MONTHS` = 0.85 (19.7x median), `POS_MONTHS_COUNT` = -0.69 (19.4x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 225762

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.30 (95.9x median), `INST_SEVERE_LATE_RATIO` = 3.37 (21.0x median), `CREDIT_TERM_MONTHS` = 0.85 (19.7x median), `YEARS_BIRTH` = -0.62 (17.5x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 1.85 (13.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 226243

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.90 (140.0x median), `POS_MONTHS_COUNT` = 2.54 (66.9x median), `YEARS_BIRTH` = 1.44 (43.9x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `BUREAU_BB_DPD_RATIO_MEAN` = 6.53 (34.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 226910

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `EXT_SOURCE_3` = -2.03 (19.3x median), `AMT_INCOME_TOTAL` = 2.20 (19.1x median), `POS_MONTHS_COUNT` = 0.60 (15.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 226977

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 9.87 (199.2x median), `EXT_SOURCE_1` = -0.81 (61.4x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CREDIT_TERM_MONTHS` = 1.19 (16.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 227023

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.43 (181.6x median), `YEARS_BIRTH` = -1.21 (35.0x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = -0.96 (20.0x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 227113

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.88 (140.6x median), `ANNUITY_TO_INCOME` = 4.12 (11.4x median), `AMT_INCOME_TOTAL` = -2.51 (9.9x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.12 (7.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 227173

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.84 (61.4x median), `POS_MONTHS_COUNT` = 0.93 (23.7x median), `EXT_SOURCE_3` = -2.42 (22.7x median), `CREDIT_TERM_MONTHS` = -1.08 (22.6x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.12 (13.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 227347

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.84 (61.5x median), `BUREAU_COUNT` = 2.90 (17.1x median), `OWN_CAR_AGE` = 6.68 (15.7x median), `AMT_INCOME_TOTAL` = -1.59 (15.6x median), `EXT_SOURCE_3` = -1.40 (13.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 227382

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 4.74 (29.1x median), `AMT_INCOME_TOTAL` = 1.72 (14.8x median), `INST_DPD_MAX` = 2.19 (14.6x median), `YEARS_BIRTH` = -0.93 (13.1x median), `INST_DPD_MEAN` = 1.22 (11.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 227460

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 1.61 (42.1x median), `INST_DPD_MAX` = 3.59 (35.5x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `CREDIT_TERM_MONTHS` = -0.94 (19.5x median), `YEARS_BIRTH` = -0.58 (16.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 228439

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.04 (152.6x median), `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CREDIT_TERM_MONTHS` = -1.31 (16.3x median), `AMT_ANNUITY` = 1.21 (12.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 228719

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.31 (170.7x median), `CREDIT_TERM_MONTHS` = 1.96 (43.9x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 229227

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.46 (107.3x median), `YEARS_BIRTH` = 1.63 (49.5x median), `INST_DPD_MAX` = 3.72 (36.7x median), `POS_MONTHS_COUNT` = 1.29 (33.5x median), `EXT_SOURCE_3` = -2.22 (21.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 229247

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.20 (164.3x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `EXT_SOURCE_3` = -1.77 (16.9x median), `BUREAU_BB_DPD_RATIO_MEAN` = 0.87 (5.5x median), `AMT_INCOME_TOTAL` = 0.86 (5.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 229467

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.71 (52.1x median), `AMT_CREDIT` = -1.01 (30.8x median), `AMT_ANNUITY` = -1.37 (21.7x median), `INST_LATE_RATIO` = 1.39 (9.6x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.50 (8.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 229574

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -1.02 (51.1x median), `POS_SK_DPD_MEAN` = 6.81 (34.5x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `EXT_SOURCE_3` = -1.85 (17.6x median), `CREDIT_TERM_MONTHS` = -1.09 (13.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 229850

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.12 (156.4x median), `YEARS_BIRTH` = -1.23 (35.7x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `CREDIT_TERM_MONTHS` = -1.10 (23.0x median), `AMT_INCOME_TOTAL` = 2.47 (21.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 230161

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 10.88 (213.4x median), `EXT_SOURCE_1` = 1.99 (146.7x median), `BUREAU_BB_DPD_RATIO_MEAN` = 6.40 (33.9x median), `POS_SK_DPD_MEAN` = 4.86 (24.3x median), `CREDIT_TERM_MONTHS` = -1.62 (20.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 230220

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 2.16 (48.2x median), `AMT_INCOME_TOTAL` = 2.31 (20.1x median), `BUREAU_COUNT` = 2.68 (15.9x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.21 (15.4x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 1.85 (13.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 230322

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.32 (173.0x median), `AMT_CREDIT` = 1.14 (36.9x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.85 (17.7x median), `BUREAU_COUNT` = 3.78 (13.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 230412

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_INCOME_TOTAL` = 2.31 (20.1x median), `YEARS_EMPLOYED` = 3.20 (15.0x median), `BUREAU_COUNT` = 2.24 (13.4x median), `ANNUITY_TO_INCOME` = -1.29 (4.2x median), `BUREAU_ACTIVE_RATIO` = 0.36 (3.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 230483

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.84 (209.8x median), `YEARS_BIRTH` = 1.12 (34.3x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `AMT_INCOME_TOTAL` = 1.24 (10.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 230491

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 8.29 (167.4x median), `PREV_APPROVAL_RATE` = 0.30 (13.9x median), `AMT_ANNUITY` = 1.00 (10.1x median), `CC_MONTHS_COUNT` = 3.37 (8.7x median), `YEARS_BIRTH` = -0.86 (7.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 230495

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `EXT_SOURCE_1` = -0.50 (38.5x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `EXT_SOURCE_3` = 1.81 (15.3x median), `CREDIT_TERM_MONTHS` = 0.78 (11.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 231025

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 12.33 (177.1x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 3.14 (62.3x median), `AMT_CREDIT` = -0.83 (24.9x median), `BUREAU_BB_DPD_RATIO_MEAN` = 1.38 (8.1x median), `BUREAU_COUNT` = 2.02 (6.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 231136

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median), `CREDIT_TERM_MONTHS` = 0.56 (8.4x median), `YEARS_BIRTH` = 1.18 (8.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 231559

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 1.70 (38.1x median), `YEARS_BIRTH` = -0.85 (24.2x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.59 (5.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 232399

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.07 (154.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_ACTIVE_RATIO` = 1.25 (22.2x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.97 (20.0x median), `EXT_SOURCE_3` = -1.80 (9.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 232868

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_1` = -0.39 (30.2x median), `CREDIT_TERM_MONTHS` = 1.28 (17.9x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.99 (11.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 233785

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `INST_PAYMENT_RATIO_MEAN` = 6.76 (611.2x median), `BUREAU_DAYS_CREDIT_MEAN` = -0.94 (11.8x median), `PREV_REFUSED_COUNT` = 4.56 (11.0x median), `AMT_INCOME_TOTAL` = 1.24 (10.3x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 1.27 (9.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 234097

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `INST_DPD_MAX` = 7.03 (68.6x median), `POS_MONTHS_COUNT` = 1.81 (47.5x median), `POS_SK_DPD_MEAN` = 2.25 (33.2x median), `YEARS_BIRTH` = 1.07 (32.8x median), `CREDIT_TERM_MONTHS` = 0.85 (19.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 234122

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.04 (150.8x median), `BUREAU_COUNT` = 4.66 (26.9x median), `YEARS_EMPLOYED` = 4.50 (20.8x median), `YEARS_BIRTH` = 0.88 (10.4x median), `INST_SEVERE_LATE_RATIO` = 1.28 (8.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 234197

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.02 (149.2x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `YEARS_EMPLOYED` = 3.73 (17.4x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (11.5x median), `AMT_INCOME_TOTAL` = -1.06 (10.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 234905

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `EXT_SOURCE_1` = -0.56 (42.7x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_ANNUITY` = -1.78 (20.9x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 234972

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 2.62 (69.1x median), `EXT_SOURCE_1` = 0.70 (50.9x median), `YEARS_BIRTH` = -1.34 (38.8x median), `CREDIT_TERM_MONTHS` = -1.30 (27.4x median), `PREV_COUNT` = 7.60 (23.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 234973

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.90 (66.1x median), `POS_MONTHS_COUNT` = -0.69 (19.4x median), `INST_DPD_MAX` = 1.67 (17.1x median), `POS_SK_DPD_MEAN` = 0.93 (14.2x median), `BUREAU_COUNT` = 1.80 (11.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 235000

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_PAYMENT_RATIO_MEAN` = 0.39 (37.7x median), `EXT_SOURCE_3` = -1.62 (15.6x median), `EXT_SOURCE_2` = 1.01 (10.8x median), `AMT_INCOME_TOTAL` = -1.28 (5.0x median), `BUREAU_ACTIVE_RATIO` = -0.32 (4.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 235438

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.15 (84.3x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_3` = -1.71 (16.3x median), `BUREAU_ACTIVE_RATIO` = -0.82 (12.9x median), `BUREAU_COUNT` = 3.78 (10.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 235562

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.21 (89.0x median), `POS_MONTHS_COUNT` = 1.85 (48.6x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `YEARS_BIRTH` = -0.51 (14.1x median), `YEARS_EMPLOYED` = 2.24 (11.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 236061

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `CC_AMT_BALANCE_MEAN` = 5.88 (20.1x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CREDIT_TERM_MONTHS` = 0.87 (12.4x median), `AMT_ANNUITY` = 0.75 (7.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 236321

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.95 (69.5x median), `POS_MONTHS_COUNT` = 2.42 (63.7x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_BIRTH` = -0.99 (28.6x median), `CREDIT_TERM_MONTHS` = -1.32 (28.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 236423

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.07 (80.6x median), `POS_SK_DPD_MEAN` = 4.33 (21.6x median), `AMT_ANNUITY` = 1.27 (13.2x median), `BUREAU_COUNT` = 1.36 (8.6x median), `ANNUITY_TO_INCOME` = 0.58 (7.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 236631

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `INST_DPD_MAX` = 7.69 (74.8x median), `POS_SK_DPD_MEAN` = 3.87 (56.2x median), `CREDIT_TERM_MONTHS` = 2.16 (48.3x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `POS_MONTHS_COUNT` = 0.80 (20.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 237119

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.97 (221.6x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `EXT_SOURCE_3` = -2.65 (24.8x median), `EXT_SOURCE_2` = -1.71 (20.9x median), `OWN_CAR_AGE` = 6.68 (15.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 237132

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.64 (48.4x median), `CREDIT_TERM_MONTHS` = -1.62 (20.4x median), `POS_SK_DPD_MEAN` = 3.65 (18.0x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `EXT_SOURCE_3` = 1.68 (14.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 237205

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.58 (27.8x median), `AMT_ANNUITY` = -2.35 (17.7x median), `BUREAU_ACTIVE_RATIO` = 0.78 (14.2x median), `YEARS_BIRTH` = -0.49 (13.5x median), `PREV_REFUSED_COUNT` = 5.67 (13.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 237599

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.74 (54.0x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_ACTIVE_RATIO` = 0.69 (12.7x median), `EXT_SOURCE_3` = -1.04 (10.3x median), `CNT_CHILDREN` = 3.60 (7.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 238686

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `YEARS_BIRTH` = 1.29 (39.5x median), `POS_MONTHS_COUNT` = 0.93 (23.7x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.78 (23.2x median), `YEARS_EMPLOYED` = 3.91 (19.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 238749

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.11 (155.6x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.38 (17.8x median), `INST_DPD_MAX` = 1.68 (17.2x median), `CREDIT_TERM_MONTHS` = 0.54 (12.8x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 1.27 (9.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 238870

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (10.1x median), `ANNUITY_TO_INCOME` = -0.62 (5.7x median), `CREDIT_TERM_MONTHS` = 0.33 (5.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 238955

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 10.80 (217.9x median), `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `ANNUITY_TO_INCOME` = 2.68 (29.8x median), `AMT_ANNUITY` = 2.43 (26.1x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 239019

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.01 (73.7x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CC_MONTHS_COUNT` = 3.41 (8.8x median), `BUREAU_COUNT` = 1.36 (8.6x median), `YEARS_BIRTH` = 0.64 (7.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 239257

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.14 (83.8x median), `CREDIT_TERM_MONTHS` = 2.16 (48.3x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_INCOME_TOTAL` = 2.20 (19.1x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 240107

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `POS_MONTHS_COUNT` = -1.13 (31.3x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `AMT_INCOME_TOTAL` = 2.31 (20.1x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 240206

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `YEARS_BIRTH` = -1.24 (35.8x median), `POS_MONTHS_COUNT` = -0.69 (19.4x median), `EXT_SOURCE_3` = -1.38 (13.4x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.85 (10.1x median), `BUREAU_COUNT` = 1.58 (9.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 240211

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `POS_SK_DPD_MEAN` = 8.70 (44.4x median), `AMT_ANNUITY` = -2.84 (32.8x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `AMT_CREDIT` = -2.29 (15.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 240255

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 6.37 (38.9x median), `YEARS_BIRTH` = 1.32 (16.1x median), `INST_DPD_MEAN` = 1.45 (13.7x median), `BUREAU_ACTIVE_RATIO` = 2.03 (13.4x median), `INST_DPD_MAX` = 1.62 (11.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 240698

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.94 (68.8x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_EMPLOYED` = 1.98 (9.7x median), `EXT_SOURCE_3` = 0.98 (7.8x median), `CNT_CHILDREN` = 2.21 (4.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 240701

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.12 (84.3x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `AMT_ANNUITY` = -1.56 (18.5x median), `AMT_CREDIT` = -1.16 (8.4x median), `PREV_APPROVAL_RATE` = -0.14 (7.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 240723

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `YEARS_BIRTH` = 1.67 (50.8x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_INCOME_TOTAL` = 2.47 (21.6x median), `BUREAU_COUNT` = 2.90 (17.1x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 1.85 (13.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 241346

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.97 (145.6x median), `PREV_APPROVAL_RATE` = -1.51 (75.5x median), `EXT_SOURCE_3` = -1.97 (18.7x median), `BUREAU_ACTIVE_RATIO` = 0.86 (15.5x median), `EXT_SOURCE_2` = -2.69 (14.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 241410

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.87 (139.6x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `POS_MONTHS_COUNT` = -1.13 (31.3x median), `YEARS_BIRTH` = -1.00 (28.8x median), `AMT_INCOME_TOTAL` = 2.08 (18.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 241437

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_3` = -1.63 (15.6x median), `BUREAU_BB_DPD_RATIO_MEAN` = 1.55 (9.0x median), `BUREAU_COUNT` = 3.12 (8.8x median), `INST_SEVERE_LATE_RATIO` = 1.08 (7.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 241444

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟠 Tipe C — Risk Signal** |
| Top Deviating Features | `YEARS_EMPLOYED` = 6.36 (29.0x median), `YEARS_BIRTH` = 1.70 (21.0x median), `EXT_SOURCE_3` = 0.93 (7.3x median), `ANNUITY_TO_INCOME` = 3.11 (6.8x median), `CREDIT_TO_INCOME` = 2.02 (2.8x median) |
| Justifikasi | Kombinasi finansial kontradiktif (mis. rasio cicilan/pendapatan ekstrem, income rendah + credit besar, atau skor eksternal tinggi di cluster bermasalah). |
| Business Impact | Underwriting: matikan auto-approve, wajibkan manual review oleh underwriter senior + verifikasi pendapatan fisik. |

---

## ROW_ID 241945

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 23.06 (464.2x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_ACTIVE_RATIO` = 1.41 (24.8x median), `ANNUITY_TO_INCOME` = 1.21 (14.0x median), `EXT_SOURCE_3` = -1.44 (13.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 242028

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = -1.31 (27.6x median), `POS_MONTHS_COUNT` = 1.05 (27.0x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.00 (23.2x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.53 (17.6x median), `YEARS_EMPLOYED` = 2.16 (11.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 242296

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_ACTIVE_RATIO` = 1.14 (20.3x median), `EXT_SOURCE_3` = -1.91 (18.2x median), `AMT_INCOME_TOTAL` = -2.13 (9.0x median), `INST_LATE_RATIO` = 2.32 (4.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 242343

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.61 (118.3x median), `EXT_SOURCE_2` = -1.44 (17.8x median), `EXT_SOURCE_3` = -1.18 (11.6x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median), `CNT_CHILDREN` = 2.21 (4.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 242799

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.11 (157.7x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `EXT_SOURCE_3` = -1.75 (16.7x median), `AMT_INCOME_TOTAL` = 1.84 (15.8x median), `YEARS_BIRTH` = -1.10 (15.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 242962

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `YEARS_BIRTH` = 0.78 (24.3x median), `POS_MONTHS_COUNT` = -0.85 (23.7x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 2.43 (18.5x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.04 (15.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 243093

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.43 (181.1x median), `CREDIT_TERM_MONTHS` = 1.68 (37.7x median), `YEARS_BIRTH` = -1.13 (32.6x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.82 (20.7x median), `BUREAU_DAYS_CREDIT_MEAN` = -0.63 (7.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 243535

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.86 (63.2x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_BB_DPD_RATIO_MEAN` = 3.10 (17.0x median), `AMT_ANNUITY` = -1.10 (13.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 244163

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 22.93 (448.8x median), `BUREAU_BB_DPD_RATIO_MEAN` = 12.13 (63.4x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `AMT_ANNUITY` = 2.21 (32.6x median), `EXT_SOURCE_1` = -0.32 (24.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 244523

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.74 (53.6x median), `CREDIT_TERM_MONTHS` = -1.07 (22.4x median), `POS_MONTHS_COUNT` = -0.41 (11.9x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median), `ANNUITY_TO_INCOME` = 1.94 (8.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 244641

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟠 Tipe C — Risk Signal** |
| Top Deviating Features | `AMT_INCOME_TOTAL` = -3.11 (29.5x median), `YEARS_BIRTH` = 1.34 (16.3x median), `ANNUITY_TO_INCOME` = 5.64 (13.2x median), `CREDIT_TO_INCOME` = 6.75 (11.6x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (11.5x median) |
| Justifikasi | Kombinasi finansial kontradiktif (mis. rasio cicilan/pendapatan ekstrem, income rendah + credit besar, atau skor eksternal tinggi di cluster bermasalah). |
| Business Impact | Underwriting: matikan auto-approve, wajibkan manual review oleh underwriter senior + verifikasi pendapatan fisik. |

---

## ROW_ID 244857

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.28 (96.1x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 3.54 (70.1x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.00 (23.2x median), `CREDIT_TERM_MONTHS` = -0.93 (19.4x median), `BUREAU_BB_DPD_RATIO_MEAN` = 3.23 (17.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 244957

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 27.41 (551.6x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 7.93 (155.8x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `AMT_ANNUITY` = -2.32 (27.0x median), `BUREAU_BB_DPD_RATIO_MEAN` = 4.78 (25.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 245201

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 2.54 (66.9x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_ACTIVE_RATIO` = 1.68 (29.5x median), `YEARS_BIRTH` = 0.78 (24.3x median), `EXT_SOURCE_3` = -2.46 (23.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 245648

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.65 (121.9x median), `POS_MONTHS_COUNT` = 3.51 (92.8x median), `CREDIT_TERM_MONTHS` = 0.99 (22.6x median), `YEARS_BIRTH` = -0.68 (19.4x median), `EXT_SOURCE_3` = -1.80 (17.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 245842

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 6.98 (137.4x median), `EXT_SOURCE_1` = 1.28 (93.8x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_BB_DPD_RATIO_MEAN` = 5.08 (27.1x median), `AMT_ANNUITY` = -1.48 (17.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 246369

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 8.24 (42.0x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `CC_AMT_BALANCE_MEAN` = 3.43 (12.1x median), `AMT_ANNUITY` = 1.11 (11.4x median), `CC_UTILIZATION_MEAN` = 3.63 (9.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 247049

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.49 (111.8x median), `POS_SK_DPD_MEAN` = 11.89 (61.0x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `CREDIT_TERM_MONTHS` = -1.40 (17.5x median), `EXT_SOURCE_3` = 1.64 (13.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 247128

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `POS_SK_DPD_MEAN` = 8.13 (41.4x median), `AMT_ANNUITY` = -1.78 (20.9x median), `ANNUITY_TO_INCOME` = -1.07 (10.5x median), `AMT_CREDIT` = -1.33 (9.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 247167

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `OWN_CAR_AGE` = 6.68 (15.7x median), `EXT_SOURCE_3` = -1.45 (14.0x median), `EXT_SOURCE_2` = -1.05 (13.2x median), `AMT_INCOME_TOTAL` = -1.06 (4.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 248306

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 17.03 (343.1x median), `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `EXT_SOURCE_3` = -2.22 (20.9x median), `CREDIT_TERM_MONTHS` = 0.88 (12.6x median), `CC_MONTHS_COUNT` = 3.41 (8.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 249514

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.58 (116.4x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_3` = -1.76 (16.8x median), `BUREAU_ACTIVE_RATIO` = -0.58 (8.9x median), `BUREAU_COUNT` = 1.58 (5.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 249923

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CREDIT_TERM_MONTHS` = -1.39 (17.3x median), `BUREAU_DAYS_CREDIT_MEAN` = -2.33 (13.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 250381

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `POS_SK_DPD_MEAN` = 5.55 (27.9x median), `EXT_SOURCE_3` = -1.36 (13.2x median), `ANNUITY_TO_INCOME` = -1.12 (11.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 250415

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `POS_SK_DPD_MEAN` = 5.84 (29.4x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CREDIT_TERM_MONTHS` = -1.06 (13.0x median), `EXT_SOURCE_3` = 1.47 (12.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 250512

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 9.89 (199.7x median), `EXT_SOURCE_1` = 1.60 (118.1x median), `CREDIT_TERM_MONTHS` = -1.12 (23.5x median), `POS_MONTHS_COUNT` = -0.77 (21.6x median), `INST_LATE_RATIO` = 4.45 (17.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 251046

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 3.31 (87.4x median), `YEARS_BIRTH` = 1.64 (49.8x median), `EXT_SOURCE_1` = 0.67 (48.7x median), `PREV_COUNT` = 7.37 (22.9x median), `EXT_SOURCE_3` = -1.41 (13.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 251078

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_LATE_RATIO` = 2.82 (18.4x median), `AMT_CREDIT` = 0.42 (14.3x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median), `YEARS_EMPLOYED` = 2.51 (8.8x median), `BUREAU_COUNT` = 2.46 (8.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 251193

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.23 (164.5x median), `CREDIT_TERM_MONTHS` = 1.97 (44.2x median), `POS_MONTHS_COUNT` = -0.73 (20.5x median), `YEARS_EMPLOYED` = 3.11 (15.9x median), `BUREAU_COUNT` = 1.36 (8.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 251752

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `YEARS_BIRTH` = 0.97 (29.8x median), `YEARS_EMPLOYED` = 4.97 (24.7x median), `CREDIT_TERM_MONTHS` = 0.60 (14.2x median), `BUREAU_COUNT` = 1.58 (9.8x median), `PREV_APPROVAL_RATE` = -1.10 (7.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 252045

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `EXT_SOURCE_2` = -2.59 (31.1x median), `EXT_SOURCE_3` = -2.94 (27.5x median), `AMT_INCOME_TOTAL` = -1.96 (8.2x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.91 (5.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 252352

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 9.29 (182.5x median), `BUREAU_BB_DPD_RATIO_MEAN` = 7.82 (41.2x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.02 (12.8x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.70 (8.5x median), `BUREAU_ACTIVE_RATIO` = -0.48 (7.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 252686

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.89 (65.0x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `INST_DPD_MAX` = 3.05 (25.8x median), `INST_DPD_MEAN` = 2.08 (23.1x median), `INST_LATE_RATIO` = 3.50 (22.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 253077

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 7.63 (150.0x median), `EXT_SOURCE_1` = 0.61 (44.4x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_BIRTH` = 0.98 (30.1x median), `CREDIT_TERM_MONTHS` = 0.88 (20.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 253942

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 0.85 (19.7x median), `OWN_CAR_AGE` = 6.68 (15.7x median), `EXT_SOURCE_3` = -1.50 (14.5x median), `YEARS_BIRTH` = 0.42 (13.6x median), `POS_MONTHS_COUNT` = -0.45 (13.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 254019

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.02 (76.7x median), `POS_MONTHS_COUNT` = 1.93 (50.7x median), `CREDIT_TERM_MONTHS` = 1.70 (38.1x median), `YEARS_BIRTH` = -1.21 (35.1x median), `CREDIT_TO_INCOME` = 5.10 (22.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 254119

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 1.95 (43.8x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 2.43 (18.5x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.41 (18.1x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `EXT_SOURCE_3` = 1.66 (13.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 254365

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.74 (53.9x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.00 (23.2x median), `YEARS_BIRTH` = -0.65 (18.4x median), `AMT_INCOME_TOTAL` = 1.40 (11.9x median), `EXT_SOURCE_3` = -1.08 (10.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 254980

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 6.92 (42.1x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_BB_DPD_RATIO_MEAN` = 5.62 (29.9x median), `EXT_SOURCE_2` = 0.88 (9.3x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 255578

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 49.39 (965.5x median), `BUREAU_BB_DPD_RATIO_MEAN` = 28.62 (148.2x median), `EXT_SOURCE_1` = 1.41 (103.7x median), `YEARS_BIRTH` = -0.86 (12.2x median), `AMT_INCOME_TOTAL` = -0.68 (7.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 255787

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 4.64 (28.6x median), `INST_DPD_MEAN` = 1.98 (22.0x median), `AMT_CREDIT` = -0.69 (20.8x median), `INST_LATE_RATIO` = 3.05 (19.8x median), `INST_DPD_MAX` = 2.17 (18.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 255832

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `POS_MONTHS_COUNT` = 0.76 (19.4x median), `BUREAU_COUNT` = 2.24 (13.4x median), `YEARS_BIRTH` = 0.30 (9.9x median), `EXT_SOURCE_3` = -0.89 (9.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 256567

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `POS_SK_DPD_MEAN` = 7.04 (35.7x median), `CREDIT_TERM_MONTHS` = 1.88 (25.7x median), `YEARS_EMPLOYED` = 4.63 (14.7x median), `YEARS_BIRTH` = 1.60 (11.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 256627

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `EXT_SOURCE_2` = -1.35 (16.8x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (4.5x median), `AMT_INCOME_TOTAL` = -1.06 (4.0x median), `INST_LATE_RATIO` = 1.34 (3.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 256690

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 1.73 (34.7x median), `INST_DPD_MAX` = 2.43 (24.3x median), `EXT_SOURCE_1` = -0.29 (22.9x median), `YEARS_EMPLOYED` = 2.65 (13.6x median), `POS_MONTHS_COUNT` = 0.52 (13.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 257026

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.81 (133.7x median), `EXT_SOURCE_3` = -2.75 (25.7x median), `CREDIT_TERM_MONTHS` = -1.08 (22.7x median), `YEARS_BIRTH` = 0.61 (19.2x median), `POS_MONTHS_COUNT` = -0.65 (18.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 257118

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.76 (55.3x median), `CNT_CHILDREN` = 3.60 (7.2x median), `EXT_SOURCE_3` = 0.80 (6.2x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.10 (5.2x median), `POS_MONTHS_COUNT` = 1.01 (3.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 257148

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_CREDIT` = -1.59 (49.0x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.23 (25.0x median), `AMT_ANNUITY` = -1.44 (22.9x median), `EXT_SOURCE_3` = -1.93 (10.5x median), `CC_MONTHS_COUNT` = 3.45 (8.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 257751

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 19.90 (400.7x median), `BUREAU_DAYS_CREDIT_MEAN` = -2.51 (33.0x median), `POS_MONTHS_COUNT` = -1.05 (29.1x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `YEARS_BIRTH` = -0.59 (16.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 257821

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 5.63 (34.4x median), `YEARS_BIRTH` = -1.29 (17.7x median), `INST_DPD_MEAN` = 0.90 (8.9x median), `INST_LATE_RATIO` = 3.40 (6.4x median), `BUREAU_COUNT` = 0.92 (6.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 257958

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.05 (76.9x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_BIRTH` = -1.06 (14.8x median), `BUREAU_ACTIVE_RATIO` = 2.03 (13.4x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.28 (10.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 258101

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.79 (208.4x median), `AMT_INCOME_TOTAL` = -3.26 (30.8x median), `YEARS_BIRTH` = 1.13 (13.6x median), `ANNUITY_TO_INCOME` = 5.62 (13.1x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (11.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 258127

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `POS_SK_DPD_MEAN` = 17.89 (92.3x median), `CREDIT_TERM_MONTHS` = 1.27 (17.7x median), `CREDIT_TO_INCOME` = 1.79 (12.3x median), `ANNUITY_TO_INCOME` = 1.01 (11.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 258128

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `POS_MONTHS_COUNT` = -0.69 (19.4x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 2.43 (18.5x median), `AMT_ANNUITY` = -2.30 (17.4x median), `BUREAU_ACTIVE_RATIO` = 0.78 (14.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 258315

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.74 (128.4x median), `INST_SEVERE_LATE_RATIO` = 4.08 (25.3x median), `EXT_SOURCE_2` = 0.98 (10.4x median), `EXT_SOURCE_3` = 1.12 (9.1x median), `CC_MONTHS_COUNT` = 3.41 (8.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 258892

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.27 (93.1x median), `CREDIT_TERM_MONTHS` = -1.37 (28.9x median), `POS_MONTHS_COUNT` = -1.01 (28.1x median), `YEARS_EMPLOYED` = 2.93 (15.0x median), `PREV_APPROVAL_RATE` = 0.96 (8.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 259147

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.91 (140.6x median), `POS_MONTHS_COUNT` = 3.55 (93.9x median), `YEARS_BIRTH` = 0.43 (13.7x median), `PREV_COUNT` = 3.60 (10.7x median), `AMT_INCOME_TOTAL` = 1.08 (8.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 259266

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `CREDIT_TERM_MONTHS` = 1.67 (23.0x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.49 (8.3x median), `EXT_SOURCE_3` = -0.59 (6.3x median), `CREDIT_TO_INCOME` = 0.81 (6.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 259398

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CREDIT_TERM_MONTHS` = -1.41 (17.6x median), `EXT_SOURCE_1` = 0.21 (14.6x median), `AMT_ANNUITY` = -1.14 (13.8x median), `AMT_CREDIT` = -1.81 (12.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 259523

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `AMT_CREDIT` = 1.58 (50.6x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 2.19 (43.8x median), `AMT_ANNUITY` = 1.42 (20.6x median), `PREV_REFUSED_COUNT` = 6.79 (9.3x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.58 (7.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 259786

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.53 (30.9x median), `EXT_SOURCE_3` = -2.20 (12.1x median), `EXT_SOURCE_2` = -2.22 (9.8x median), `CC_UTILIZATION_MEAN` = 3.03 (8.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 259834

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 1.68 (37.7x median), `BUREAU_ACTIVE_RATIO` = 1.41 (24.8x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.00 (23.2x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.38 (16.0x median), `PREV_APPROVAL_RATE` = -1.37 (9.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 259912

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 7.01 (141.7x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `CREDIT_TERM_MONTHS` = 1.67 (23.0x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `ANNUITY_TO_INCOME` = -1.06 (10.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 260255

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.01 (74.1x median), `POS_MONTHS_COUNT` = 2.10 (55.1x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = 0.87 (20.0x median), `YEARS_EMPLOYED` = 2.65 (13.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 260470

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.07 (153.0x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `POS_MONTHS_COUNT` = 1.17 (30.2x median), `CREDIT_TERM_MONTHS` = 1.17 (26.7x median), `YEARS_BIRTH` = -0.53 (14.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 260796

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 3.08 (227.4x median), `POS_MONTHS_COUNT` = 2.14 (56.1x median), `YEARS_BIRTH` = 0.79 (24.6x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.09 (13.8x median), `BUREAU_COUNT` = 1.80 (11.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 260797

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.28 (168.0x median), `POS_SK_DPD_MEAN` = 3.83 (19.0x median), `CREDIT_TERM_MONTHS` = -1.35 (16.8x median), `ANNUITY_TO_INCOME` = 1.37 (15.8x median), `AMT_ANNUITY` = 1.26 (13.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 260982

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.61 (192.5x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 5.31 (104.7x median), `INST_DPD_MAX` = 3.54 (23.0x median), `INST_DPD_MEAN` = 2.05 (19.0x median), `BUREAU_BB_DPD_RATIO_MEAN` = 3.46 (18.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 261156

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_BB_DPD_RATIO_MEAN` = 6.76 (35.8x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_1` = 0.38 (27.5x median), `AMT_CREDIT` = 0.63 (20.8x median), `AMT_ANNUITY` = 0.93 (13.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 261507

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `EXT_SOURCE_2` = 1.53 (16.9x median), `AMT_INCOME_TOTAL` = 1.84 (9.6x median), `CNT_CHILDREN` = 2.21 (4.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 261560

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.70 (53.3x median), `POS_MONTHS_COUNT` = 0.97 (24.8x median), `EXT_SOURCE_3` = -2.35 (22.1x median), `INST_DPD_MAX` = 2.12 (21.3x median), `BUREAU_COUNT` = 3.34 (19.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 261683

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `INST_SEVERE_LATE_RATIO` = 3.28 (20.5x median), `EXT_SOURCE_3` = -1.72 (16.5x median), `INST_DPD_MEAN` = 0.93 (9.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 261763

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.14 (86.0x median), `INST_SEVERE_LATE_RATIO` = 7.80 (47.4x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `EXT_SOURCE_3` = -2.55 (23.9x median), `OWN_CAR_AGE` = 6.68 (15.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 262551

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_DPD_MAX` = 2.40 (20.5x median), `EXT_SOURCE_1` = 0.24 (17.1x median), `AMT_CREDIT` = -0.44 (12.7x median), `EXT_SOURCE_3` = 1.29 (8.7x median), `POS_MONTHS_COUNT` = 4.48 (4.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 262644

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.01 (148.4x median), `POS_MONTHS_COUNT` = 1.13 (29.1x median), `BUREAU_ACTIVE_RATIO` = 1.49 (26.2x median), `EXT_SOURCE_3` = -2.54 (23.8x median), `BUREAU_COUNT` = 4.00 (23.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 262939

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `CC_SK_DPD_MEAN` = 1.57 (32.4x median), `AMT_ANNUITY` = -1.51 (17.9x median), `BUREAU_COUNT` = 2.02 (12.2x median), `EXT_SOURCE_3` = 1.34 (11.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 262996

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 18.10 (364.5x median), `EXT_SOURCE_1` = 1.98 (146.0x median), `POS_MONTHS_COUNT` = -1.13 (31.3x median), `CREDIT_TERM_MONTHS` = 1.26 (28.7x median), `BUREAU_ACTIVE_RATIO` = 0.89 (16.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 263212

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `INST_DPD_MAX` = 3.15 (26.6x median), `AMT_CREDIT` = 0.41 (13.8x median), `EXT_SOURCE_2` = -2.54 (11.1x median), `INST_LATE_RATIO` = 1.57 (10.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 263351

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.26 (94.4x median), `POS_MONTHS_COUNT` = 1.93 (50.7x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.58 (27.8x median), `AMT_INCOME_TOTAL` = 2.47 (21.6x median), `PREV_COUNT` = 4.54 (13.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 263363

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `AMT_CREDIT` = -2.52 (78.1x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `AMT_ANNUITY` = -2.20 (34.3x median), `PREV_REFUSED_COUNT` = 22.39 (32.9x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.39 (28.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 263428

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 15.40 (221.0x median), `EXT_SOURCE_1` = -0.59 (44.7x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `OWN_CAR_AGE` = 6.68 (15.7x median), `POS_MONTHS_COUNT` = 2.70 (6.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 264125

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.48 (36.9x median), `AMT_CREDIT` = -1.13 (34.4x median), `AMT_ANNUITY` = -1.35 (21.4x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 0.56 (11.9x median), `BUREAU_BB_DPD_RATIO_MEAN` = 1.97 (11.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 264328

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `ANNUITY_TO_INCOME` = 0.90 (10.7x median), `CREDIT_TERM_MONTHS` = 0.53 (8.0x median), `CREDIT_TO_INCOME` = 1.08 (7.9x median), `AMT_ANNUITY` = 0.75 (7.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 264787

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 6.26 (126.7x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = 1.28 (29.1x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `YEARS_BIRTH` = 0.50 (15.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 264911

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.57 (115.7x median), `CREDIT_TERM_MONTHS` = 1.69 (38.1x median), `YEARS_BIRTH` = 1.11 (34.1x median), `POS_MONTHS_COUNT` = 0.80 (20.5x median), `AMT_INCOME_TOTAL` = 1.70 (14.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 264974

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.75 (128.7x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 1.49 (30.0x median), `BUREAU_BB_DPD_RATIO_MEAN` = 3.37 (18.3x median), `EXT_SOURCE_3` = -1.57 (15.1x median), `YEARS_EMPLOYED` = 1.52 (7.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 265813

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `YEARS_BIRTH` = 1.37 (41.8x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.58 (27.8x median), `POS_MONTHS_COUNT` = -0.53 (15.1x median), `PREV_APPROVAL_RATE` = -1.93 (13.1x median), `AMT_ANNUITY` = 1.59 (10.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 265843

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_DPD_MAX` = 3.85 (38.0x median), `CREDIT_TERM_MONTHS` = 1.68 (37.7x median), `CC_SK_DPD_MEAN` = 1.16 (24.3x median), `POS_MONTHS_COUNT` = -0.85 (23.7x median), `YEARS_EMPLOYED` = 3.61 (18.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 265854

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.42 (180.4x median), `INST_SEVERE_LATE_RATIO` = 6.92 (42.1x median), `BUREAU_BB_DPD_RATIO_MEAN` = 7.67 (40.4x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_3` = -1.71 (16.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 265925

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 8.94 (54.1x median), `EXT_SOURCE_1` = 0.64 (46.7x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_3` = -1.62 (15.6x median), `BUREAU_ACTIVE_RATIO` = 0.61 (11.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 266703

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 2.46 (64.8x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = 1.27 (28.8x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.58 (27.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 266807

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.09 (156.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `CREDIT_TERM_MONTHS` = -1.56 (33.2x median), `POS_MONTHS_COUNT` = 0.93 (23.7x median), `YEARS_BIRTH` = -0.65 (18.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 266955

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `AMT_INCOME_TOTAL` = 2.47 (21.6x median), `YEARS_BIRTH` = -1.03 (14.4x median), `YEARS_EMPLOYED` = 0.79 (4.4x median), `PREV_APPROVAL_RATE` = -2.34 (3.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 266980

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.69 (50.2x median), `YEARS_BIRTH` = -1.08 (31.3x median), `BUREAU_ACTIVE_RATIO` = 0.86 (15.5x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.02 (12.0x median), `EXT_SOURCE_3` = -1.17 (11.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 267306

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.54 (189.7x median), `INST_SEVERE_LATE_RATIO` = 6.92 (42.1x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `INST_DPD_MEAN` = 1.10 (10.7x median), `INST_DPD_MAX` = 0.73 (5.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 267663

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.24 (91.1x median), `POS_MONTHS_COUNT` = 1.09 (28.1x median), `YEARS_BIRTH` = -0.70 (19.8x median), `BUREAU_ACTIVE_RATIO` = 0.64 (11.8x median), `BUREAU_DAYS_CREDIT_MEAN` = -0.90 (11.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 267953

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.31 (96.2x median), `CREDIT_TERM_MONTHS` = 1.68 (37.7x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `YEARS_BIRTH` = 0.67 (21.1x median), `POS_MONTHS_COUNT` = 0.76 (19.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 268034

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 3.31 (87.4x median), `YEARS_BIRTH` = 1.07 (33.0x median), `EXT_SOURCE_3` = 1.39 (11.4x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median), `AMT_INCOME_TOTAL` = 1.05 (8.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 268072

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.87 (21.2x median), `POS_MONTHS_COUNT` = 0.80 (20.5x median), `EXT_SOURCE_3` = -1.89 (18.0x median), `YEARS_BIRTH` = -0.60 (16.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 268167

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `INST_LATE_RATIO` = 4.30 (27.6x median), `AMT_CREDIT` = 0.82 (26.7x median), `BUREAU_BB_DPD_RATIO_MEAN` = 4.88 (26.1x median), `INST_SEVERE_LATE_RATIO` = 3.12 (19.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 268345

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.84 (61.5x median), `AMT_INCOME_TOTAL` = -2.73 (11.8x median), `EXT_SOURCE_3` = 1.01 (8.1x median), `EXT_SOURCE_2` = 0.73 (7.5x median), `YEARS_EMPLOYED` = 2.26 (6.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 268476

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `BUREAU_ACTIVE_RATIO` = 1.25 (22.2x median), `CREDIT_TERM_MONTHS` = -1.49 (18.7x median), `EXT_SOURCE_3` = -1.04 (10.3x median), `AMT_CREDIT` = -0.79 (6.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 268691

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 1.33 (34.5x median), `YEARS_BIRTH` = -1.12 (32.3x median), `BUREAU_ACTIVE_RATIO` = 1.64 (28.8x median), `EXT_SOURCE_3` = -2.62 (24.5x median), `EXT_SOURCE_1` = -0.29 (22.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 268739

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.79 (59.8x median), `CREDIT_TERM_MONTHS` = -1.51 (32.1x median), `BUREAU_DAYS_CREDIT_MEAN` = -2.05 (26.8x median), `YEARS_BIRTH` = -0.90 (25.9x median), `EXT_SOURCE_3` = 1.35 (11.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 268950

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 3.35 (88.5x median), `EXT_SOURCE_1` = 0.78 (57.1x median), `CREDIT_TERM_MONTHS` = -1.62 (34.5x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.58 (27.8x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 268991

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -1.24 (62.0x median), `EXT_SOURCE_1` = 0.71 (51.8x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CREDIT_TERM_MONTHS` = -1.39 (17.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 269019

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 22.28 (448.4x median), `CREDIT_TERM_MONTHS` = -1.22 (25.7x median), `YEARS_BIRTH` = 0.47 (14.9x median), `AMT_ANNUITY` = -1.30 (10.2x median), `AMT_CREDIT` = -1.73 (9.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 269154

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.41 (105.7x median), `POS_SK_DPD_MEAN` = 16.46 (84.8x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `CREDIT_TERM_MONTHS` = 1.42 (19.8x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 269331

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.57 (117.9x median), `POS_MONTHS_COUNT` = 1.53 (39.9x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `YEARS_BIRTH` = -0.91 (26.2x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.00 (14.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 269459

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 19.86 (102.5x median), `PREV_APPROVAL_RATE` = -1.02 (51.1x median), `EXT_SOURCE_1` = -0.34 (25.9x median), `EXT_SOURCE_3` = -2.17 (20.5x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.81 (10.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 269909

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.74 (130.3x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `EXT_SOURCE_2` = -2.46 (29.6x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.30 (4.3x median), `AMT_INCOME_TOTAL` = -1.07 (4.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 269910

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 4.50 (27.7x median), `YEARS_BIRTH` = -1.13 (15.7x median), `AMT_INCOME_TOTAL` = -1.40 (13.8x median), `INST_DPD_MEAN` = 0.78 (7.8x median), `INST_DPD_MAX` = 0.89 (6.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 270453

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 5.88 (115.8x median), `EXT_SOURCE_1` = -0.86 (64.7x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_BB_DPD_RATIO_MEAN` = 3.04 (16.6x median), `POS_SK_DPD_MEAN` = 2.20 (10.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 270592

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `POS_SK_DPD_MEAN` = 21.68 (112.0x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = -1.41 (17.5x median), `BUREAU_ACTIVE_RATIO` = -0.48 (7.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 270771

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_INCOME_TOTAL` = 2.47 (21.6x median), `BUREAU_DAYS_CREDIT_MEAN` = 0.80 (6.8x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.29 (4.2x median), `BUREAU_ACTIVE_RATIO` = 0.46 (3.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 270986

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `YEARS_BIRTH` = -1.31 (37.9x median), `CREDIT_TERM_MONTHS` = 1.67 (37.7x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.58 (27.8x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.64 (18.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 271748

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.91 (141.1x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `POS_MONTHS_COUNT` = -0.81 (22.7x median), `YEARS_BIRTH` = 0.63 (19.8x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 272072

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟠 Tipe C — Risk Signal** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 1.81 (47.5x median), `YEARS_BIRTH` = 1.48 (45.1x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `AMT_INCOME_TOTAL` = -1.95 (18.9x median) |
| Justifikasi | Kombinasi finansial kontradiktif (mis. rasio cicilan/pendapatan ekstrem, income rendah + credit besar, atau skor eksternal tinggi di cluster bermasalah). |
| Business Impact | Underwriting: matikan auto-approve, wajibkan manual review oleh underwriter senior + verifikasi pendapatan fisik. |

---

## ROW_ID 272341

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.59 (44.5x median), `YEARS_BIRTH` = -1.24 (35.8x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = -0.75 (15.4x median), `BUREAU_DAYS_CREDIT_MEAN` = 0.91 (13.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 272484

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 1.77 (46.4x median), `YEARS_BIRTH` = 1.26 (38.6x median), `CREDIT_TERM_MONTHS` = -1.40 (29.7x median), `AMT_INCOME_TOTAL` = -1.66 (16.2x median), `AMT_ANNUITY` = -2.09 (15.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 272850

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_BIRTH` = -0.84 (24.1x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CREDIT_TERM_MONTHS` = 0.32 (8.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 273411

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 3.19 (19.9x median), `EXT_SOURCE_2` = -1.48 (18.3x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `OWN_CAR_AGE` = 6.68 (15.7x median), `INST_DPD_MEAN` = 0.55 (5.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 273683

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.96 (144.8x median), `INST_SEVERE_LATE_RATIO` = 2.22 (14.2x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.53 (9.4x median), `EXT_SOURCE_3` = -1.71 (9.2x median), `INST_LATE_RATIO` = 1.25 (8.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 273701

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.29 (94.8x median), `INST_SEVERE_LATE_RATIO` = 6.92 (42.1x median), `EXT_SOURCE_2` = -2.35 (28.3x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `EXT_SOURCE_3` = 1.55 (13.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 273829

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 15.21 (306.5x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `EXT_SOURCE_3` = 1.48 (12.3x median), `YEARS_BIRTH` = 1.42 (9.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 273990

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.48 (108.9x median), `YEARS_BIRTH` = -1.16 (33.5x median), `CREDIT_TERM_MONTHS` = -1.45 (30.7x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 274209

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 1.81 (47.5x median), `YEARS_BIRTH` = 0.74 (23.2x median), `CREDIT_TERM_MONTHS` = -1.08 (22.6x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 2.43 (18.5x median), `EXT_SOURCE_3` = -1.51 (14.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 274225

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.06 (154.0x median), `EXT_SOURCE_3` = -2.47 (23.2x median), `BUREAU_COUNT` = 2.90 (8.3x median), `EXT_SOURCE_2` = -0.54 (7.3x median), `BUREAU_ACTIVE_RATIO` = 0.29 (5.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 274235

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 19.12 (384.9x median), `EXT_SOURCE_1` = -1.59 (119.1x median), `POS_MONTHS_COUNT` = -1.13 (31.3x median), `YEARS_BIRTH` = -0.86 (24.6x median), `PREV_APPROVAL_RATE` = -2.34 (16.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 274248

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.89 (139.6x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_DAYS_CREDIT_MEAN` = -2.48 (17.0x median), `EXT_SOURCE_3` = 1.09 (8.8x median), `AMT_INCOME_TOTAL` = 0.86 (6.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 274430

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.27 (167.4x median), `POS_MONTHS_COUNT` = 1.73 (45.3x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.58 (27.8x median), `CREDIT_TERM_MONTHS` = 0.86 (19.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 275005

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 6.04 (30.5x median), `CREDIT_TERM_MONTHS` = 1.70 (23.4x median), `PREV_APPROVAL_RATE` = -0.27 (14.5x median), `CREDIT_TO_INCOME` = 1.93 (13.3x median), `ANNUITY_TO_INCOME` = 0.85 (10.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 275112

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.82 (134.4x median), `PREV_APPROVAL_RATE` = 0.41 (19.4x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `CREDIT_TERM_MONTHS` = 1.19 (16.7x median), `POS_SK_DPD_MEAN` = 2.76 (13.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 275594

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_CREDIT` = 1.35 (43.4x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `AMT_ANNUITY` = 1.42 (20.6x median), `YEARS_EMPLOYED` = 2.98 (10.3x median), `CC_MONTHS_COUNT` = 3.09 (8.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 276010

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.83 (62.6x median), `YEARS_BIRTH` = -1.24 (35.9x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 2.43 (18.5x median), `EXT_SOURCE_3` = -1.56 (15.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 276528

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.55 (41.7x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.49 (30.2x median), `AMT_CREDIT` = 0.78 (25.3x median), `CREDIT_TERM_MONTHS` = 1.97 (11.1x median), `PREV_REFUSED_COUNT` = 6.23 (8.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 277231

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.92 (69.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DAYS_CREDIT_MEAN` = -2.90 (15.3x median), `EXT_SOURCE_3` = 1.67 (11.0x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.59 (10.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 277733

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 31.78 (621.5x median), `BUREAU_BB_DPD_RATIO_MEAN` = 17.87 (92.9x median), `POS_SK_DPD_MEAN` = 9.29 (47.4x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `CREDIT_TERM_MONTHS` = 1.68 (23.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 278158

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 7.90 (155.3x median), `BUREAU_BB_DPD_RATIO_MEAN` = 13.89 (72.4x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `EXT_SOURCE_2` = -1.07 (13.4x median), `INST_LATE_RATIO` = 3.19 (6.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 278490

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 4.72 (125.2x median), `EXT_SOURCE_1` = 1.51 (111.2x median), `CREDIT_TERM_MONTHS` = -1.41 (29.9x median), `YEARS_BIRTH` = 0.91 (28.2x median), `BUREAU_COUNT` = 3.56 (20.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 278521

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `CREDIT_TERM_MONTHS` = -1.08 (22.7x median), `YEARS_BIRTH` = -0.63 (17.8x median), `PREV_REFUSED_COUNT` = 4.00 (9.8x median), `POS_MONTHS_COUNT` = 0.40 (9.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 278762

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.44 (108.2x median), `CREDIT_TERM_MONTHS` = 1.26 (28.7x median), `YEARS_BIRTH` = -0.74 (21.0x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.42 (18.2x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.37 (15.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 278804

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 1.25 (22.2x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.74 (15.4x median), `EXT_SOURCE_3` = 1.29 (8.7x median), `YEARS_BIRTH` = -1.81 (8.3x median), `OWN_CAR_AGE` = 2.67 (6.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 278825

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.53 (186.8x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `INST_SEVERE_LATE_RATIO` = 5.63 (34.4x median), `AMT_INCOME_TOTAL` = 1.47 (12.4x median), `EXT_SOURCE_3` = 1.26 (10.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 279293

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 18.35 (94.6x median), `CREDIT_TERM_MONTHS` = -1.41 (17.5x median), `EXT_SOURCE_3` = 1.75 (14.7x median), `YEARS_BIRTH` = 1.47 (10.3x median), `ANNUITY_TO_INCOME` = 0.63 (7.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 279725

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = -1.63 (34.6x median), `POS_MONTHS_COUNT` = 1.01 (25.9x median), `YEARS_BIRTH` = 0.82 (25.4x median), `BUREAU_COUNT` = 3.34 (19.6x median), `AMT_CREDIT` = -2.20 (11.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 279769

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 6.92 (42.1x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_ACTIVE_RATIO` = 1.25 (22.2x median), `EXT_SOURCE_3` = -2.22 (21.0x median), `INST_LATE_RATIO` = 5.28 (9.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 279841

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.58 (27.8x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `CREDIT_TERM_MONTHS` = -0.75 (15.4x median), `AMT_ANNUITY` = -1.29 (10.2x median), `PREV_APPROVAL_RATE` = -1.37 (9.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 279896

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.88 (138.5x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `POS_SK_DPD_MEAN` = 3.06 (14.9x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (10.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 279910

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 19.46 (391.9x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `EXT_SOURCE_1` = 0.33 (23.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CREDIT_TERM_MONTHS` = 1.26 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 279917

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.91 (141.0x median), `POS_MONTHS_COUNT` = 1.85 (48.6x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `CREDIT_TERM_MONTHS` = 1.19 (27.0x median), `YEARS_BIRTH` = 0.63 (19.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 279963

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_COUNT` = 3.78 (13.5x median), `AMT_CREDIT` = 0.32 (11.1x median), `CC_MONTHS_COUNT` = 3.21 (8.3x median), `AMT_ANNUITY` = 0.50 (6.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 280239

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.47 (184.1x median), `POS_SK_DPD_MEAN` = 14.92 (76.8x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `CREDIT_TERM_MONTHS` = 1.69 (23.4x median), `CREDIT_TO_INCOME` = 2.05 (14.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 280908

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = 1.27 (28.7x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.49 (19.2x median), `BUREAU_COUNT` = 2.90 (17.1x median), `YEARS_EMPLOYED` = 2.63 (13.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 280935

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.79 (208.4x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `PREV_REFUSED_COUNT` = 2.33 (6.1x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (4.5x median), `PREV_COUNT` = 1.25 (4.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 281083

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 5.87 (35.9x median), `EXT_SOURCE_2` = -1.55 (19.0x median), `INST_DPD_MEAN` = 1.36 (12.9x median), `INST_DPD_MAX` = 1.37 (9.5x median), `AMT_INCOME_TOTAL` = 1.24 (6.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 281242

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 7.79 (39.6x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = -1.62 (20.4x median), `ANNUITY_TO_INCOME` = 1.62 (18.4x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 281341

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.51 (110.8x median), `AMT_CREDIT` = -1.53 (46.9x median), `BUREAU_ACTIVE_RATIO` = 1.54 (27.1x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.16 (23.6x median), `AMT_ANNUITY` = -0.91 (14.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 281438

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 1.97 (44.2x median), `EXT_SOURCE_1` = -0.53 (40.3x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `POS_MONTHS_COUNT` = 0.88 (22.7x median), `YEARS_BIRTH` = -0.71 (20.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 281500

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.49 (183.9x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.08 (12.7x median), `YEARS_BIRTH` = 0.35 (11.3x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 1.27 (9.3x median), `CREDIT_TERM_MONTHS` = 0.32 (7.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 281637

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 10.10 (51.7x median), `CREDIT_TERM_MONTHS` = -1.38 (17.2x median), `PREV_APPROVAL_RATE` = 0.30 (13.9x median), `AMT_CREDIT` = -1.33 (9.4x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 281694

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.56 (40.8x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `EXT_SOURCE_3` = -2.12 (20.0x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.44 (16.6x median), `POS_MONTHS_COUNT` = 0.56 (14.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 281939

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 23.35 (456.9x median), `BUREAU_BB_DPD_RATIO_MEAN` = 11.76 (61.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `YEARS_EMPLOYED` = 3.95 (18.3x median), `AMT_INCOME_TOTAL` = -0.77 (8.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 282265

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 5.15 (31.6x median), `EXT_SOURCE_2` = -1.47 (18.1x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `INST_DPD_MEAN` = 1.40 (13.3x median), `INST_LATE_RATIO` = 5.28 (9.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 282824

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `YEARS_BIRTH` = 1.08 (33.2x median), `BUREAU_COUNT` = 3.78 (22.0x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 2.43 (18.5x median), `POS_MONTHS_COUNT` = -0.41 (11.9x median), `PREV_APPROVAL_RATE` = -1.44 (9.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 283171

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 2.98 (78.8x median), `BUREAU_COUNT` = 4.22 (24.5x median), `AMT_INCOME_TOTAL` = 1.84 (15.8x median), `EXT_SOURCE_3` = -1.64 (15.8x median), `PREV_REFUSED_COUNT` = 4.56 (11.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 284077

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.48 (36.3x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_3` = 1.14 (9.3x median), `BUREAU_ACTIVE_RATIO` = -0.41 (5.9x median), `BUREAU_COUNT` = 0.92 (3.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 284415

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 1.68 (23.1x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `POS_SK_DPD_MEAN` = 3.33 (16.3x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (10.1x median), `EXT_SOURCE_1` = 0.13 (8.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 284628

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 1.68 (37.8x median), `EXT_SOURCE_3` = -1.58 (15.2x median), `BUREAU_COUNT` = 2.02 (12.2x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median), `AMT_INCOME_TOTAL` = 0.86 (6.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 284786

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 1.25 (22.2x median), `OWN_CAR_AGE` = 6.68 (15.7x median), `EXT_SOURCE_3` = -0.94 (9.4x median), `AMT_INCOME_TOTAL` = -1.66 (6.8x median), `INST_LATE_RATIO` = 2.32 (4.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 284858

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.92 (218.0x median), `YEARS_BIRTH` = -1.28 (37.0x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_COUNT` = 4.44 (25.7x median), `EXT_SOURCE_3` = -2.28 (21.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 284893

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -1.10 (55.2x median), `AMT_ANNUITY` = 1.21 (12.5x median), `EXT_SOURCE_2` = -2.15 (11.7x median), `EXT_SOURCE_3` = -1.10 (10.9x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 284960

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `YEARS_BIRTH` = 1.66 (50.4x median), `CREDIT_TERM_MONTHS` = 1.86 (41.7x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.48 (19.0x median), `POS_MONTHS_COUNT` = 0.56 (14.0x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 1.85 (13.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 285080

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_DPD_MAX` = 5.17 (43.0x median), `AMT_ANNUITY` = -1.18 (18.9x median), `AMT_CREDIT` = -0.42 (12.2x median), `INST_DPD_MEAN` = 0.97 (11.3x median), `EXT_SOURCE_2` = -1.93 (8.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 285624

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.91 (142.7x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_ACTIVE_RATIO` = 0.78 (14.2x median), `EXT_SOURCE_3` = 0.85 (6.7x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.26 (4.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 286750

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -1.14 (57.0x median), `POS_SK_DPD_MEAN` = 6.68 (33.8x median), `EXT_SOURCE_3` = -2.03 (19.3x median), `CREDIT_TERM_MONTHS` = -1.51 (18.9x median), `AMT_ANNUITY` = 1.39 (14.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 286991

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 1.96 (43.9x median), `POS_MONTHS_COUNT` = 1.65 (43.2x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.79 (23.3x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.01 (11.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 287101

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_DPD_RATIO_MEAN` = 13.79 (71.9x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `YEARS_BIRTH` = 1.43 (10.0x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median), `ANNUITY_TO_INCOME` = 0.70 (8.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 287429

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.86 (62.7x median), `CREDIT_TERM_MONTHS` = 1.96 (43.8x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `POS_MONTHS_COUNT` = -1.05 (29.1x median), `BUREAU_COUNT` = 2.90 (17.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 288878

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.77 (130.8x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median), `EXT_SOURCE_3` = -1.56 (8.3x median), `AMT_INCOME_TOTAL` = 2.31 (7.2x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.03 (6.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 289165

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_BIRTH` = -1.47 (20.1x median), `AMT_INCOME_TOTAL` = 1.24 (10.3x median), `BUREAU_ACTIVE_RATIO` = -1.11 (5.8x median), `BUREAU_DAYS_CREDIT_MEAN` = 0.42 (4.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 289494

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 1.49 (38.9x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `AMT_INCOME_TOTAL` = -1.96 (19.0x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `YEARS_EMPLOYED` = 2.46 (12.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 289778

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.24 (18.8x median), `AMT_INCOME_TOTAL` = 1.56 (13.3x median), `YEARS_BIRTH` = -0.94 (13.2x median), `EXT_SOURCE_3` = 0.93 (7.4x median), `BUREAU_COUNT` = 0.92 (6.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 290366

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 3.28 (20.5x median), `EXT_SOURCE_2` = -1.27 (15.8x median), `INST_DPD_MEAN` = 1.40 (13.3x median), `INST_DPD_MAX` = 1.63 (11.1x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 290570

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 2.34 (61.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `CREDIT_TERM_MONTHS` = 1.28 (29.1x median), `YEARS_BIRTH` = -0.98 (28.1x median), `EXT_SOURCE_1` = 0.38 (27.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 290686

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `YEARS_BIRTH` = 1.36 (41.4x median), `BUREAU_DAYS_CREDIT_MEAN` = -3.04 (40.2x median), `POS_MONTHS_COUNT` = -1.13 (31.3x median), `BUREAU_BB_DPD_RATIO_MEAN` = 5.86 (31.1x median), `INST_SEVERE_LATE_RATIO` = 4.60 (28.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 290719

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 2.26 (59.4x median), `YEARS_BIRTH` = -1.17 (33.8x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.73 (22.5x median), `AMT_ANNUITY` = -2.55 (19.1x median), `EXT_SOURCE_1` = -0.19 (15.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 290925

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.44 (182.4x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_2` = -1.65 (20.2x median), `EXT_SOURCE_3` = -1.39 (13.5x median), `YEARS_EMPLOYED` = 1.87 (5.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 290973

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_ANNUITY` = -0.99 (12.1x median), `POS_SK_DPD_MEAN` = 2.18 (10.4x median), `AMT_CREDIT` = -0.93 (6.9x median), `PREV_APPROVAL_RATE` = 0.14 (5.8x median), `EXT_SOURCE_3` = 0.72 (5.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 291014

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 3.95 (24.4x median), `OWN_CAR_AGE` = 6.79 (15.9x median), `INST_DPD_MEAN` = 1.04 (10.1x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median), `EXT_SOURCE_2` = 0.67 (6.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 291360

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.05 (151.4x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_BB_DPD_RATIO_MEAN` = 6.20 (32.9x median), `INST_SEVERE_LATE_RATIO` = 3.19 (19.9x median), `EXT_SOURCE_3` = -1.99 (18.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 291390

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `POS_MONTHS_COUNT` = -1.13 (31.3x median), `CREDIT_TERM_MONTHS` = 1.27 (28.8x median), `YEARS_BIRTH` = -0.78 (22.1x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 291639

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 22.12 (445.3x median), `CREDIT_TERM_MONTHS` = 1.67 (37.6x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `POS_MONTHS_COUNT` = -1.13 (31.3x median), `YEARS_EMPLOYED` = 3.11 (15.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 291942

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `YEARS_BIRTH` = -1.03 (29.7x median), `PREV_REFUSED_COUNT` = 5.12 (12.3x median), `PREV_COUNT` = 3.84 (11.4x median), `BUREAU_COUNT` = 1.80 (11.0x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 1.27 (9.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 292028

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 0.76 (19.4x median), `BUREAU_ACTIVE_RATIO` = -0.71 (11.1x median), `BUREAU_DAYS_CREDIT_MEAN` = -0.79 (9.7x median), `YEARS_BIRTH` = -0.34 (9.1x median), `AMT_ANNUITY` = -0.89 (7.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 292100

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `AMT_INCOME_TOTAL` = -1.66 (6.8x median), `INST_LATE_RATIO` = 3.17 (6.0x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (4.5x median), `EXT_SOURCE_2` = -0.19 (3.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 292114

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.45 (107.0x median), `POS_SK_DPD_MEAN` = 15.59 (80.3x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `EXT_SOURCE_3` = 1.83 (15.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 292179

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 9.03 (177.3x median), `INST_PAYMENT_RATIO_MEAN` = 0.48 (46.2x median), `BUREAU_BB_DPD_RATIO_MEAN` = 4.71 (25.2x median), `AMT_CREDIT` = -0.66 (19.9x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 292754

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.06 (77.4x median), `POS_SK_DPD_MEAN` = 11.74 (60.2x median), `EXT_SOURCE_3` = -1.89 (17.9x median), `AMT_ANNUITY` = 1.07 (10.9x median), `BUREAU_ACTIVE_RATIO` = -0.66 (10.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 292929

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.04 (76.0x median), `BUREAU_DAYS_CREDIT_MEAN` = -2.46 (32.4x median), `POS_MONTHS_COUNT` = 1.09 (28.1x median), `CREDIT_TERM_MONTHS` = -1.07 (22.5x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 292952

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.74 (129.9x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = 1.28 (17.9x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 293039

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `YEARS_EMPLOYED` = 4.22 (11.1x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median), `EXT_SOURCE_2` = 0.78 (8.1x median), `YEARS_BIRTH` = 1.40 (4.7x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.87 (3.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 293131

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_MONTHS_COUNT` = -1.13 (31.3x median), `CREDIT_TERM_MONTHS` = -1.07 (22.5x median), `YEARS_BIRTH` = -0.72 (20.4x median), `AMT_ANNUITY` = -1.47 (11.4x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.95 (11.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 293141

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 8.54 (172.6x median), `PREV_APPROVAL_RATE` = -1.02 (51.1x median), `CREDIT_TERM_MONTHS` = 1.25 (17.5x median), `YEARS_EMPLOYED` = 3.98 (12.8x median), `BUREAU_ACTIVE_RATIO` = -0.71 (11.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 293147

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.70 (201.6x median), `YEARS_BIRTH` = -1.22 (35.5x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `POS_MONTHS_COUNT` = 1.21 (31.3x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.58 (27.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 293244

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.31 (172.7x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `INST_SEVERE_LATE_RATIO` = 3.02 (18.9x median), `EXT_SOURCE_2` = -1.27 (15.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 294156

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.21 (89.0x median), `AMT_CREDIT` = 0.92 (30.0x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.59 (10.5x median), `CC_MONTHS_COUNT` = 3.41 (8.8x median), `EXT_SOURCE_3` = -1.41 (7.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 294357

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 3.59 (95.0x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_BIRTH` = 0.85 (26.3x median), `YEARS_EMPLOYED` = 4.78 (23.8x median), `AMT_INCOME_TOTAL` = 2.47 (21.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 294825

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = -1.51 (32.1x median), `YEARS_BIRTH` = 0.79 (24.6x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 1.85 (13.9x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.12 (13.1x median), `EXT_SOURCE_3` = -1.30 (12.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 295165

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.58 (27.8x median), `POS_MONTHS_COUNT` = 1.05 (27.0x median), `BUREAU_COUNT` = 3.78 (22.0x median), `AMT_ANNUITY` = -2.76 (20.6x median), `YEARS_BIRTH` = -0.56 (15.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 295210

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_2` = -2.65 (31.8x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (4.5x median), `PREV_APPROVAL_RATE` = -2.34 (3.4x median), `INST_PAYMENT_RATIO_MEAN` = -0.05 (3.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 295639

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.96 (144.6x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_BIRTH` = -0.96 (27.5x median), `CREDIT_TERM_MONTHS` = -1.09 (22.8x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.45 (16.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 296041

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.29 (96.8x median), `YEARS_BIRTH` = -1.17 (34.0x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 2.43 (18.5x median), `EXT_SOURCE_3` = -1.94 (18.4x median), `BUREAU_COUNT` = 2.68 (15.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 296068

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.95 (69.5x median), `YEARS_EMPLOYED` = 3.49 (16.3x median), `AMT_INCOME_TOTAL` = -1.28 (12.7x median), `EXT_SOURCE_3` = 1.40 (11.6x median), `INST_DPD_MEAN` = 0.87 (8.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 296551

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 1.28 (29.1x median), `BUREAU_ACTIVE_RATIO` = 1.41 (24.8x median), `YEARS_BIRTH` = -0.63 (17.6x median), `EXT_SOURCE_3` = -1.71 (16.3x median), `EXT_SOURCE_2` = -2.20 (8.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 296590

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `EXT_SOURCE_3` = -1.99 (18.9x median), `BUREAU_ACTIVE_RATIO` = 0.78 (14.2x median), `BUREAU_COUNT` = 2.24 (13.4x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 0.63 (13.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 296745

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 2.39 (47.7x median), `EXT_SOURCE_1` = -0.39 (29.7x median), `BUREAU_COUNT` = 4.22 (24.5x median), `YEARS_BIRTH` = -0.78 (22.1x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.40 (18.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 297514

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `YEARS_BIRTH` = 0.86 (26.7x median), `PREV_COUNT` = 7.84 (24.4x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.00 (23.2x median), `EXT_SOURCE_3` = -2.30 (21.6x median), `PREV_REFUSED_COUNT` = 7.90 (18.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 297551

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `YEARS_BIRTH` = -1.42 (41.2x median), `INST_DPD_MAX` = 2.35 (23.6x median), `EXT_SOURCE_3` = -1.29 (12.6x median), `POS_SK_DPD_MEAN` = 0.64 (10.2x median), `BUREAU_DAYS_CREDIT_MEAN` = 0.54 (8.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 297593

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.69 (124.6x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = 1.67 (23.1x median), `POS_SK_DPD_MEAN` = 4.33 (21.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 297748

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 7.37 (148.9x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `EXT_SOURCE_1` = 0.47 (34.0x median), `YEARS_BIRTH` = -1.24 (10.5x median), `CREDIT_TERM_MONTHS` = 0.62 (9.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 297987

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.92 (216.2x median), `POS_MONTHS_COUNT` = 2.10 (55.1x median), `YEARS_BIRTH` = 1.35 (41.3x median), `CREDIT_TERM_MONTHS` = -1.40 (29.7x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.63 (21.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 298226

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 1.70 (38.1x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `YEARS_EMPLOYED` = 2.98 (15.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 298320

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 5.15 (31.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `INST_LATE_RATIO` = 3.06 (5.9x median), `INST_DPD_MEAN` = 0.42 (4.7x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (4.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 298349

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.70 (50.8x median), `AMT_CREDIT` = -0.88 (26.6x median), `AMT_ANNUITY` = -1.20 (19.1x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `OWN_CAR_AGE` = 6.68 (15.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 298408

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.79 (131.9x median), `CREDIT_TERM_MONTHS` = 1.68 (37.7x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_BIRTH` = 1.03 (31.6x median), `CREDIT_TO_INCOME` = 4.63 (20.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 298587

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CC_MONTHS_COUNT` = 2.68 (7.1x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.40 (6.8x median), `EXT_SOURCE_2` = -1.36 (6.4x median), `CC_UTILIZATION_MAX` = 2.31 (5.9x median), `CC_UTILIZATION_MEAN` = 1.67 (5.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 298922

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.92 (67.5x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `EXT_SOURCE_2` = 0.52 (5.1x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (4.5x median), `PREV_APPROVAL_RATE` = -2.34 (3.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 298949

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_ANNUITY` = 1.25 (18.0x median), `BUREAU_ACTIVE_RATIO` = 0.78 (14.2x median), `INST_LATE_RATIO` = 1.96 (13.1x median), `EXT_SOURCE_3` = 1.68 (11.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 299008

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.32 (25.0x median), `AMT_CREDIT` = -0.78 (23.4x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.84 (17.4x median), `AMT_ANNUITY` = -0.89 (14.6x median), `PREV_REFUSED_COUNT` = 7.90 (11.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 299032

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.34 (98.4x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `POS_SK_DPD_MEAN` = 5.03 (25.2x median), `CREDIT_TERM_MONTHS` = 0.69 (10.1x median), `YEARS_EMPLOYED` = 2.79 (9.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 299430

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `ANNUITY_TO_INCOME` = 8.42 (91.5x median), `CREDIT_TO_INCOME` = 8.97 (57.9x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 299618

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 1.57 (41.0x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `YEARS_BIRTH` = -0.89 (25.6x median), `CREDIT_TERM_MONTHS` = -1.07 (22.5x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.59 (18.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 299834

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.77 (56.0x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `EXT_SOURCE_2` = 1.18 (12.7x median), `OWN_CAR_AGE` = 2.78 (7.1x median), `INST_LATE_RATIO` = 3.31 (6.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 300066

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 2.86 (75.6x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_3` = -2.68 (25.1x median), `BUREAU_COUNT` = 3.56 (20.8x median), `CREDIT_TERM_MONTHS` = 0.87 (20.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 300639

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `AMT_CREDIT` = 1.70 (54.5x median), `YEARS_EMPLOYED` = 5.00 (16.6x median), `AMT_ANNUITY` = 1.09 (15.5x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.55 (11.8x median), `CREDIT_TERM_MONTHS` = 1.97 (11.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 300740

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.32 (98.8x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `YEARS_BIRTH` = -1.18 (34.1x median), `CREDIT_TERM_MONTHS` = 1.17 (26.5x median), `POS_MONTHS_COUNT` = -0.49 (14.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 301012

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.87 (137.9x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `YEARS_BIRTH` = 0.85 (26.3x median), `YEARS_EMPLOYED` = 4.62 (23.1x median), `POS_MONTHS_COUNT` = -0.81 (22.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 301018

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `INST_DPD_MAX` = 3.78 (24.5x median), `INST_SEVERE_LATE_RATIO` = 3.82 (23.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `INST_DPD_MEAN` = 1.84 (17.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 301712

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟠 Tipe C — Risk Signal** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.47 (33.7x median), `AMT_INCOME_TOTAL` = 2.20 (19.1x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (11.5x median), `YEARS_EMPLOYED` = 2.07 (10.1x median), `ANNUITY_TO_INCOME` = 3.44 (7.6x median) |
| Justifikasi | Kombinasi finansial kontradiktif (mis. rasio cicilan/pendapatan ekstrem, income rendah + credit besar, atau skor eksternal tinggi di cluster bermasalah). |
| Business Impact | Underwriting: matikan auto-approve, wajibkan manual review oleh underwriter senior + verifikasi pendapatan fisik. |

---

## ROW_ID 301810

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.75 (205.3x median), `YEARS_BIRTH` = -1.76 (51.5x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `EXT_SOURCE_3` = -2.81 (26.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 301900

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `YEARS_BIRTH` = -1.20 (34.7x median), `CREDIT_TERM_MONTHS` = -1.40 (29.7x median), `AMT_INCOME_TOTAL` = 1.47 (12.4x median), `EXT_SOURCE_2` = -2.54 (10.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 302078

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.87 (137.7x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_3` = 1.14 (9.3x median), `YEARS_EMPLOYED` = 3.36 (9.0x median), `EXT_SOURCE_2` = -0.59 (7.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 302655

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = 2.16 (48.3x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_DAYS_CREDIT_MEAN` = -2.45 (32.2x median), `YEARS_BIRTH` = 0.66 (20.5x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 2.43 (18.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 302842

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.79 (132.1x median), `AMT_CREDIT` = 1.61 (51.4x median), `AMT_ANNUITY` = 1.56 (22.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DAYS_CREDIT_MEAN` = -2.25 (11.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 303010

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 19.80 (398.6x median), `POS_MONTHS_COUNT` = -1.13 (31.3x median), `CREDIT_TERM_MONTHS` = -1.41 (29.9x median), `YEARS_BIRTH` = 0.86 (26.5x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 303108

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 21.18 (109.4x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `EXT_SOURCE_1` = 0.35 (25.2x median), `CREDIT_TERM_MONTHS` = 1.67 (23.0x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 303109

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟠 Tipe C — Risk Signal** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `YEARS_BIRTH` = 0.80 (24.8x median), `CREDIT_TERM_MONTHS` = 0.87 (20.0x median), `INST_SEVERE_LATE_RATIO` = 3.11 (19.5x median), `CREDIT_TO_INCOME` = 4.27 (19.4x median) |
| Justifikasi | Kombinasi finansial kontradiktif (mis. rasio cicilan/pendapatan ekstrem, income rendah + credit besar, atau skor eksternal tinggi di cluster bermasalah). |
| Business Impact | Underwriting: matikan auto-approve, wajibkan manual review oleh underwriter senior + verifikasi pendapatan fisik. |

---

## ROW_ID 303245

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_3` = -1.48 (14.3x median), `EXT_SOURCE_2` = 1.02 (10.8x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.23 (3.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 303386

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `INST_SEVERE_LATE_RATIO` = 3.90 (24.2x median), `INST_DPD_MAX` = 2.96 (19.4x median), `INST_DPD_MEAN` = 2.01 (18.7x median), `EXT_SOURCE_3` = -1.10 (10.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 303401

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -1.35 (67.4x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 2.78 (55.4x median), `BUREAU_BB_DPD_RATIO_MEAN` = 4.77 (25.5x median), `EXT_SOURCE_1` = 0.35 (25.1x median), `EXT_SOURCE_3` = -1.83 (17.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 303530

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.57 (41.2x median), `YEARS_BIRTH` = -1.12 (15.5x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (11.5x median), `AMT_INCOME_TOTAL` = -1.06 (10.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (5.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 304450

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.67 (49.0x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_CREDIT` = 0.84 (27.4x median), `AMT_ANNUITY` = 1.26 (18.1x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.59 (10.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 304919

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 1.53 (39.9x median), `AMT_INCOME_TOTAL` = 2.47 (21.6x median), `CREDIT_TERM_MONTHS` = 0.60 (14.1x median), `EXT_SOURCE_3` = 1.27 (10.4x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 304931

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.69 (126.6x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `POS_SK_DPD_MEAN` = 4.82 (24.1x median), `EXT_SOURCE_3` = 1.53 (12.7x median), `CREDIT_TERM_MONTHS` = 0.86 (12.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 305235

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -1.51 (75.5x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `BUREAU_BB_DPD_RATIO_MEAN` = 2.47 (13.7x median), `EXT_SOURCE_1` = -0.12 (9.9x median), `PREV_REFUSED_COUNT` = 3.45 (8.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 305355

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `YEARS_BIRTH` = 1.07 (32.8x median), `YEARS_EMPLOYED` = 4.72 (23.6x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `AMT_INCOME_TOTAL` = -1.06 (10.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 305456

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 14.94 (301.1x median), `EXT_SOURCE_1` = 0.71 (51.9x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `AMT_ANNUITY` = -1.05 (12.8x median), `BUREAU_COUNT` = 1.36 (8.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 305662

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `OWN_CAR_AGE` = 6.68 (15.7x median), `BUREAU_ACTIVE_RATIO` = -0.79 (12.4x median), `EXT_SOURCE_2` = 1.03 (11.0x median), `INST_LATE_RATIO` = 3.17 (6.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 305890

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.28 (94.0x median), `AMT_CREDIT` = 1.42 (45.6x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.10 (22.6x median), `AMT_ANNUITY` = 1.52 (22.0x median), `BUREAU_ACTIVE_RATIO` = 0.78 (14.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 305967

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `INST_PAYMENT_RATIO_MEAN` = 7.04 (659.9x median), `AMT_CREDIT` = 1.42 (45.7x median), `EXT_SOURCE_1` = 0.46 (33.0x median), `INST_LATE_RATIO` = 2.02 (13.5x median), `YEARS_EMPLOYED` = 3.72 (12.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 306062

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_CREDIT` = -1.51 (46.5x median), `AMT_ANNUITY` = -1.45 (22.9x median), `BUREAU_COUNT` = 4.00 (14.4x median), `EXT_SOURCE_3` = -1.95 (10.6x median), `PREV_REFUSED_COUNT` = 6.79 (9.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 306181

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.12 (156.3x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `AMT_INCOME_TOTAL` = 2.31 (11.8x median), `EXT_SOURCE_2` = 0.85 (8.9x median), `EXT_SOURCE_3` = -0.34 (4.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 306814

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.33 (172.4x median), `POS_MONTHS_COUNT` = -1.13 (31.3x median), `YEARS_BIRTH` = 0.70 (21.9x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `PREV_APPROVAL_RATE` = -2.34 (16.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 306957

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.88 (64.3x median), `BUREAU_BB_DPD_RATIO_MEAN` = 4.18 (22.5x median), `CREDIT_TERM_MONTHS` = -0.95 (19.7x median), `YEARS_BIRTH` = -0.52 (14.6x median), `EXT_SOURCE_3` = -1.51 (14.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 307477

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 4.64 (123.1x median), `YEARS_BIRTH` = 0.56 (17.6x median), `AMT_INCOME_TOTAL` = 1.84 (15.8x median), `BUREAU_DAYS_CREDIT_MEAN` = -0.71 (8.6x median), `EXT_SOURCE_3` = 0.88 (6.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 309006

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.31 (170.2x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `CREDIT_TERM_MONTHS` = 0.87 (12.4x median), `AMT_ANNUITY` = 0.97 (9.9x median), `EXT_SOURCE_3` = 0.92 (7.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 309365

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = -1.56 (33.2x median), `YEARS_BIRTH` = 0.73 (22.7x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 2.43 (18.5x median), `PREV_APPROVAL_RATE` = -1.35 (8.8x median), `POS_MONTHS_COUNT` = -0.29 (8.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 309599

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.43 (179.5x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.65 (33.3x median), `AMT_CREDIT` = 0.93 (30.3x median), `OWN_CAR_AGE` = 6.79 (15.9x median), `BUREAU_ACTIVE_RATIO` = 0.73 (13.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 309699

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.99 (74.5x median), `INST_DPD_MEAN` = 2.87 (26.3x median), `INST_SEVERE_LATE_RATIO` = 4.08 (25.3x median), `INST_DPD_MAX` = 3.48 (22.6x median), `POS_SK_DPD_MEAN` = 1.31 (19.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 309845

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.58 (118.4x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.46 (29.5x median), `AMT_CREDIT` = 0.84 (27.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 309858

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.14 (83.7x median), `INST_SEVERE_LATE_RATIO` = 6.92 (42.1x median), `INST_DPD_MEAN` = 0.69 (7.1x median), `POS_MONTHS_COUNT` = 2.70 (7.0x median), `BUREAU_ACTIVE_RATIO` = 0.99 (7.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 310620

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_CREDIT` = 1.13 (36.4x median), `BUREAU_COUNT` = 4.88 (17.8x median), `AMT_ANNUITY` = 0.63 (8.6x median), `CC_MONTHS_COUNT` = 3.05 (8.0x median), `BUREAU_ACTIVE_RATIO` = -0.52 (7.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 310981

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.73 (55.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `INST_SEVERE_LATE_RATIO` = 3.10 (19.4x median), `AMT_CREDIT` = 0.52 (17.3x median), `INST_LATE_RATIO` = 2.32 (15.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 311120

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.58 (118.1x median), `YEARS_BIRTH` = -1.82 (53.2x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `CREDIT_TERM_MONTHS` = -1.63 (34.6x median), `EXT_SOURCE_3` = -2.58 (24.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 311512

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_CREDIT` = -0.75 (22.4x median), `AMT_ANNUITY` = -0.75 (12.4x median), `YEARS_EMPLOYED` = 3.26 (11.2x median), `BUREAU_ACTIVE_RATIO` = -0.69 (10.6x median), `PREV_REFUSED_COUNT` = 6.23 (8.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 311593

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.52 (37.8x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_3` = -0.90 (9.1x median), `BUREAU_ACTIVE_RATIO` = 1.25 (8.6x median), `YEARS_BIRTH` = -0.55 (8.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 312220

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.24 (93.4x median), `INST_SEVERE_LATE_RATIO` = 7.80 (47.4x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.50 (30.3x median), `INST_LATE_RATIO` = 3.52 (22.8x median), `AMT_ANNUITY` = 1.11 (15.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 312429

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = -1.08 (22.7x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.28 (16.4x median), `YEARS_BIRTH` = -0.45 (12.4x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 1.27 (9.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 312667

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.82 (62.2x median), `AMT_CREDIT` = 1.49 (47.7x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `INST_DPD_MAX` = 2.16 (18.6x median), `AMT_ANNUITY` = 1.10 (15.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 312692

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.58 (41.9x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `EXT_SOURCE_2` = 1.50 (16.4x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.40 (4.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 313017

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 3.14 (83.1x median), `EXT_SOURCE_1` = 0.74 (54.2x median), `YEARS_BIRTH` = 0.54 (17.1x median), `PREV_COUNT` = 4.54 (13.7x median), `BUREAU_COUNT` = 1.58 (9.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 313200

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.23 (90.4x median), `AMT_CREDIT` = -0.63 (18.8x median), `AMT_ANNUITY` = -0.92 (15.0x median), `BUREAU_COUNT` = 3.78 (13.5x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.54 (11.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 313414

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.96 (72.4x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `POS_MONTHS_COUNT` = -1.13 (31.3x median), `PREV_APPROVAL_RATE` = -2.34 (16.1x median), `YEARS_BIRTH` = 0.43 (13.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 314014

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `EXT_SOURCE_3` = 1.83 (15.4x median), `EXT_SOURCE_2` = 0.85 (8.9x median), `PREV_COUNT` = 1.96 (5.9x median), `CNT_CHILDREN` = 2.21 (4.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 314510

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.56 (42.2x median), `AMT_CREDIT` = 0.73 (23.9x median), `AMT_ANNUITY` = 0.95 (13.4x median), `EXT_SOURCE_3` = -2.19 (12.1x median), `PREV_REFUSED_COUNT` = 7.90 (11.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 314987

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 3.91 (103.6x median), `EXT_SOURCE_1` = 0.64 (46.5x median), `YEARS_BIRTH` = 1.29 (39.4x median), `BUREAU_ACTIVE_RATIO` = 1.41 (24.8x median), `CREDIT_TERM_MONTHS` = -1.08 (22.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 315075

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.42 (104.5x median), `CREDIT_TERM_MONTHS` = 1.43 (32.3x median), `POS_MONTHS_COUNT` = 1.05 (27.0x median), `BUREAU_ACTIVE_RATIO` = 1.51 (26.6x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 2.43 (18.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 315114

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.74 (204.5x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.59 (10.5x median), `AMT_ANNUITY` = 0.74 (10.2x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (9.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 315174

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.94 (143.3x median), `AMT_INCOME_TOTAL` = 2.31 (20.1x median), `YEARS_EMPLOYED` = 3.59 (16.7x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 0.36 (7.9x median), `CNT_CHILDREN` = 2.21 (4.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 315225

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟠 Tipe C — Risk Signal** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_1` = -0.42 (32.1x median), `CREDIT_TERM_MONTHS` = -1.08 (22.6x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `AMT_INCOME_TOTAL` = -2.13 (20.5x median) |
| Justifikasi | Kombinasi finansial kontradiktif (mis. rasio cicilan/pendapatan ekstrem, income rendah + credit besar, atau skor eksternal tinggi di cluster bermasalah). |
| Business Impact | Underwriting: matikan auto-approve, wajibkan manual review oleh underwriter senior + verifikasi pendapatan fisik. |

---

## ROW_ID 315307

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `INST_SEVERE_LATE_RATIO` = 5.63 (34.4x median), `INST_DPD_MEAN` = 1.14 (11.0x median), `EXT_SOURCE_2` = -0.69 (9.0x median), `INST_LATE_RATIO` = 3.40 (6.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 315810

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.58 (44.1x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_CREDIT` = 0.89 (28.8x median), `AMT_ANNUITY` = 1.16 (16.5x median), `YEARS_EMPLOYED` = 3.30 (11.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 315967

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.33 (174.4x median), `POS_MONTHS_COUNT` = 1.65 (43.2x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = 1.27 (28.7x median), `BUREAU_COUNT` = 4.00 (23.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 316022

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -1.24 (62.0x median), `ANNUITY_TO_INCOME` = 1.88 (21.2x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `YEARS_BIRTH` = -1.71 (14.2x median), `CREDIT_TERM_MONTHS` = -1.08 (13.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 316419

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `YEARS_BIRTH` = 2.09 (63.3x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `CREDIT_TERM_MONTHS` = -1.46 (30.9x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.58 (27.8x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.66 (19.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 316468

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.38 (101.3x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_COUNT` = 5.32 (19.5x median), `EXT_SOURCE_3` = -2.40 (13.3x median), `YEARS_EMPLOYED` = 2.64 (9.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 316495

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.10 (82.7x median), `AMT_CREDIT` = 1.87 (59.6x median), `AMT_ANNUITY` = 1.53 (22.2x median), `CREDIT_TERM_MONTHS` = 1.43 (8.3x median), `EXT_SOURCE_3` = 1.14 (7.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 316640

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 3.55 (93.9x median), `EXT_SOURCE_1` = 0.96 (70.2x median), `YEARS_BIRTH` = 1.08 (33.1x median), `AMT_INCOME_TOTAL` = 2.47 (21.6x median), `AMT_ANNUITY` = 1.78 (11.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 316804

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.23 (90.0x median), `BUREAU_DAYS_CREDIT_MEAN` = -2.25 (29.6x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.58 (27.8x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `POS_MONTHS_COUNT` = -0.37 (10.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 317025

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.86 (62.6x median), `AMT_CREDIT` = -0.50 (14.6x median), `PREV_REFUSED_COUNT` = 8.46 (11.8x median), `AMT_ANNUITY` = 0.66 (9.0x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.38 (8.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 317227

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `INST_SEVERE_LATE_RATIO` = 5.15 (31.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `EXT_SOURCE_1` = -0.17 (13.8x median), `EXT_SOURCE_2` = -1.08 (13.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 317356

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.04 (150.9x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_INCOME_TOTAL` = 2.08 (18.1x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.17 (7.5x median), `CNT_CHILDREN` = 3.60 (7.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 317468

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟠 Tipe C — Risk Signal** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `YEARS_BIRTH` = -0.94 (13.2x median), `ANNUITY_TO_INCOME` = 5.48 (12.8x median), `AMT_INCOME_TOTAL` = -1.06 (10.7x median), `EXT_SOURCE_3` = -0.77 (8.0x median) |
| Justifikasi | Kombinasi finansial kontradiktif (mis. rasio cicilan/pendapatan ekstrem, income rendah + credit besar, atau skor eksternal tinggi di cluster bermasalah). |
| Business Impact | Underwriting: matikan auto-approve, wajibkan manual review oleh underwriter senior + verifikasi pendapatan fisik. |

---

## ROW_ID 317587

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.03 (149.9x median), `YEARS_BIRTH` = 1.38 (42.1x median), `CREDIT_TERM_MONTHS` = 1.25 (28.3x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.16 (14.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 317674

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.49 (184.3x median), `AMT_CREDIT` = 1.05 (34.0x median), `AMT_ANNUITY` = 1.53 (22.2x median), `YEARS_EMPLOYED` = 5.14 (17.0x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.59 (10.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 317833

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_CREDIT` = 0.92 (30.0x median), `AMT_ANNUITY` = 1.61 (23.5x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.02 (21.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 317909

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.46 (181.7x median), `POS_MONTHS_COUNT` = 1.21 (31.3x median), `YEARS_EMPLOYED` = 4.34 (21.7x median), `YEARS_BIRTH` = 0.68 (21.2x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = -1.03 (9.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 318181

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_CREDIT` = -0.53 (15.6x median), `INST_DPD_MAX` = 1.68 (14.7x median), `BUREAU_COUNT` = 3.78 (13.5x median), `CC_MONTHS_COUNT` = 3.33 (8.6x median), `EXT_SOURCE_3` = -1.40 (7.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 318586

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.87 (138.0x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_COUNT` = 2.46 (14.7x median), `AMT_INCOME_TOTAL` = 1.24 (10.3x median), `CC_MONTHS_COUNT` = 3.25 (8.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 318621

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.17 (159.9x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `AMT_CREDIT` = 0.35 (12.1x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.59 (10.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 318741

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 2.34 (46.8x median), `EXT_SOURCE_1` = -0.34 (26.6x median), `AMT_ANNUITY` = 1.47 (21.3x median), `PREV_REFUSED_COUNT` = 9.02 (12.7x median), `EXT_SOURCE_3` = -1.85 (10.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 318812

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.93 (69.9x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.92 (19.1x median), `AMT_ANNUITY` = 0.96 (13.6x median), `INST_LATE_RATIO` = 1.28 (8.9x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 319404

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.80 (58.1x median), `PREV_APPROVAL_RATE` = -0.45 (23.2x median), `BUREAU_COUNT` = 2.90 (17.1x median), `POS_SK_DPD_MEAN` = 2.06 (9.8x median), `BUREAU_ACTIVE_RATIO` = -0.58 (8.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 319901

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 8.21 (161.4x median), `EXT_SOURCE_1` = -0.57 (43.7x median), `AMT_CREDIT` = -1.33 (40.6x median), `BUREAU_BB_DPD_RATIO_MEAN` = 6.64 (35.2x median), `INST_LATE_RATIO` = 2.47 (16.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 319928

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.78 (207.7x median), `YEARS_BIRTH` = -1.37 (39.7x median), `EXT_SOURCE_3` = -1.69 (16.1x median), `AMT_ANNUITY` = -2.02 (15.4x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 1.85 (13.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 320050

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.76 (55.1x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `YEARS_EMPLOYED` = 2.28 (11.0x median), `INST_DPD_MEAN` = 1.05 (10.2x median), `AMT_INCOME_TOTAL` = -0.96 (9.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 320344

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.55 (188.7x median), `AMT_CREDIT` = -3.06 (94.9x median), `AMT_ANNUITY` = -2.75 (42.7x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.10 (22.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 320483

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -1.10 (55.2x median), `POS_SK_DPD_MEAN` = 9.74 (49.8x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `EXT_SOURCE_3` = 1.83 (15.4x median), `CREDIT_TERM_MONTHS` = 0.85 (12.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 320549

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.41 (105.7x median), `PREV_APPROVAL_RATE` = -1.24 (62.0x median), `CREDIT_TERM_MONTHS` = -1.45 (18.2x median), `EXT_SOURCE_3` = 1.48 (12.3x median), `AMT_CREDIT` = -1.52 (10.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 320782

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 33.38 (671.4x median), `EXT_SOURCE_1` = 1.35 (99.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `CREDIT_TERM_MONTHS` = -1.44 (18.1x median), `CC_MONTHS_COUNT` = 2.76 (7.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 320849

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.67 (198.9x median), `AMT_CREDIT` = -1.51 (46.5x median), `AMT_ANNUITY` = -1.17 (18.7x median), `PREV_REFUSED_COUNT` = 9.02 (12.7x median), `EXT_SOURCE_3` = -1.85 (10.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 321941

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 4.67 (92.1x median), `EXT_SOURCE_1` = 0.85 (62.4x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `AMT_CREDIT` = -0.78 (23.6x median), `BUREAU_BB_DPD_RATIO_MEAN` = 3.03 (16.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 322013

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.86 (64.7x median), `INST_SEVERE_LATE_RATIO` = 5.76 (35.2x median), `BUREAU_ACTIVE_RATIO` = 1.51 (26.6x median), `BUREAU_BB_DPD_RATIO_MEAN` = 3.56 (19.3x median), `EXT_SOURCE_3` = -1.70 (16.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 322941

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.52 (112.2x median), `POS_MONTHS_COUNT` = 1.09 (28.1x median), `CREDIT_TERM_MONTHS` = 1.04 (23.8x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.77 (23.0x median), `BUREAU_BB_DPD_RATIO_MEAN` = 2.18 (12.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 323177

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `AMT_CREDIT` = -1.06 (32.2x median), `BUREAU_COUNT` = 5.54 (20.3x median), `AMT_ANNUITY` = -1.18 (18.8x median), `BUREAU_ACTIVE_RATIO` = -0.58 (8.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 323183

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 2.50 (65.8x median), `EXT_SOURCE_1` = -0.53 (40.3x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = 1.43 (32.3x median), `YEARS_EMPLOYED` = 3.22 (16.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 324504

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `POS_SK_DPD_MEAN` = 3.33 (16.4x median), `CREDIT_TERM_MONTHS` = -1.08 (13.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 324655

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `YEARS_BIRTH` = 1.32 (40.4x median), `INST_DPD_MAX` = 2.38 (23.9x median), `INST_SEVERE_LATE_RATIO` = 2.24 (14.3x median), `EXT_SOURCE_3` = -1.33 (12.9x median), `CC_SK_DPD_MEAN` = 0.52 (11.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 325251

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `AMT_ANNUITY` = 1.17 (12.0x median), `CREDIT_TERM_MONTHS` = -0.78 (9.2x median), `EXT_SOURCE_3` = -0.88 (8.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 325348

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `POS_SK_DPD_MEAN` = 5.92 (29.8x median), `AMT_ANNUITY` = -1.69 (19.9x median), `CREDIT_TERM_MONTHS` = -1.47 (18.5x median), `AMT_CREDIT` = -2.29 (15.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 325357

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.51 (113.5x median), `AMT_CREDIT` = -1.78 (54.8x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_COUNT` = 3.78 (13.5x median), `AMT_ANNUITY` = -0.77 (12.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 325445

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.72 (126.7x median), `AMT_CREDIT` = 1.41 (45.1x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_ANNUITY` = 1.00 (14.1x median), `CC_UTILIZATION_MEAN` = 2.81 (7.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 325615

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `AMT_CREDIT` = -3.26 (101.4x median), `AMT_ANNUITY` = -2.73 (42.4x median), `EXT_SOURCE_1` = 0.50 (36.1x median), `BUREAU_COUNT` = 3.56 (12.7x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.54 (11.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 325713

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_ANNUITY` = 2.04 (30.0x median), `AMT_CREDIT` = 0.59 (19.6x median), `YEARS_EMPLOYED` = 4.54 (15.2x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.92 (9.8x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.51 (9.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 325888

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.75 (131.0x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_COUNT` = 4.00 (14.4x median), `EXT_SOURCE_3` = -2.48 (13.8x median), `INST_LATE_RATIO` = 1.66 (11.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 327006

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `CREDIT_TERM_MONTHS` = -1.50 (31.9x median), `AMT_ANNUITY` = -2.64 (19.8x median), `YEARS_BIRTH` = -0.65 (18.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 327219

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.51 (111.2x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.59 (10.5x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (9.2x median), `AMT_CREDIT` = -0.27 (7.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 327262

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_2` = -2.00 (24.2x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 0.61 (12.8x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median), `YEARS_EMPLOYED` = 3.08 (8.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 328355

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.40 (28.8x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 1.35 (27.3x median), `BUREAU_BB_DPD_RATIO_MEAN` = 3.45 (18.8x median), `EXT_SOURCE_3` = -1.71 (16.4x median), `CREDIT_TERM_MONTHS` = -1.08 (13.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 328531

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.69 (124.8x median), `INST_SEVERE_LATE_RATIO` = 3.82 (23.7x median), `EXT_SOURCE_3` = 1.30 (10.7x median), `INST_DPD_MEAN` = 1.05 (10.3x median), `INST_DPD_MAX` = 1.27 (8.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 329860

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 2.82 (74.5x median), `CREDIT_TERM_MONTHS` = 1.26 (28.6x median), `BUREAU_ACTIVE_RATIO` = 1.25 (22.2x median), `YEARS_BIRTH` = 0.65 (20.4x median), `EXT_SOURCE_3` = -1.07 (10.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 330291

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 3.14 (83.1x median), `YEARS_BIRTH` = 1.74 (52.7x median), `CREDIT_TERM_MONTHS` = 0.69 (16.1x median), `BUREAU_COUNT` = 2.24 (13.4x median), `AMT_INCOME_TOTAL` = 1.40 (11.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 330474

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.73 (55.5x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `POS_SK_DPD_MEAN` = 7.91 (40.2x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 1.55 (31.3x median), `CREDIT_TERM_MONTHS` = -1.48 (18.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 330687

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `CREDIT_TERM_MONTHS` = -1.09 (22.8x median), `POS_MONTHS_COUNT` = -0.77 (21.6x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.76 (20.1x median), `YEARS_BIRTH` = -0.62 (17.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 330750

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.08 (81.0x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `CREDIT_TERM_MONTHS` = -1.08 (13.3x median), `YEARS_BIRTH` = -1.12 (9.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 331428

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_MONTHS_COUNT` = -0.85 (23.7x median), `CREDIT_TERM_MONTHS` = -1.08 (22.7x median), `YEARS_EMPLOYED` = 3.87 (19.5x median), `EXT_SOURCE_3` = -1.85 (17.6x median), `YEARS_BIRTH` = 0.56 (17.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 331509

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -3.03 (226.2x median), `POS_MONTHS_COUNT` = 1.61 (42.1x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_COUNT` = 4.88 (28.1x median), `AMT_INCOME_TOTAL` = 1.56 (13.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 331545

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.34 (98.4x median), `CC_SK_DPD_MEAN` = 4.81 (97.5x median), `INST_DPD_MAX` = 7.53 (73.4x median), `YEARS_BIRTH` = 1.38 (42.0x median), `POS_MONTHS_COUNT` = 0.72 (18.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 331597

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 14.54 (208.8x median), `EXT_SOURCE_1` = 1.84 (135.4x median), `POS_MONTHS_COUNT` = 3.31 (87.4x median), `BUREAU_ACTIVE_RATIO` = 0.78 (14.2x median), `EXT_SOURCE_3` = -0.99 (9.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 331852

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.05 (78.9x median), `YEARS_BIRTH` = -1.21 (35.1x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `POS_MONTHS_COUNT` = -1.05 (29.1x median), `BUREAU_COUNT` = 4.22 (24.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 331903

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.54 (39.2x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `EXT_SOURCE_3` = -2.68 (25.0x median), `YEARS_BIRTH` = 0.65 (20.5x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 332061

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_BIRTH` = -1.02 (29.3x median), `POS_MONTHS_COUNT` = -0.89 (24.8x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `AMT_INCOME_TOTAL` = 2.31 (20.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 332112

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 12.77 (257.4x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CC_MONTHS_COUNT` = 3.37 (8.7x median), `CREDIT_TERM_MONTHS` = -0.70 (8.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 332538

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `AMT_CREDIT` = -1.73 (53.2x median), `AMT_ANNUITY` = -2.30 (35.9x median), `YEARS_EMPLOYED` = 4.33 (14.5x median), `INST_PAYMENT_RATIO_MEAN` = 0.09 (9.3x median), `AMT_INCOME_TOTAL` = 2.47 (7.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 332810

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `YEARS_BIRTH` = -1.14 (32.8x median), `CREDIT_TERM_MONTHS` = -1.48 (31.4x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `POS_MONTHS_COUNT` = -0.69 (19.4x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 332851

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 3.96 (80.6x median), `EXT_SOURCE_1` = 0.88 (64.2x median), `AMT_CREDIT` = 2.00 (63.7x median), `AMT_ANNUITY` = 2.73 (40.4x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 333133

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 3.74 (23.2x median), `BUREAU_ACTIVE_RATIO` = 2.03 (13.4x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.11 (9.0x median), `EXT_SOURCE_2` = -2.57 (7.1x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.80 (5.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 333206

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.41 (103.4x median), `CC_SK_DPD_MEAN` = 2.91 (59.4x median), `INST_DPD_MAX` = 5.32 (52.1x median), `POS_MONTHS_COUNT` = 1.21 (31.3x median), `CREDIT_TERM_MONTHS` = 0.50 (12.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 333500

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.36 (99.8x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `POS_MONTHS_COUNT` = -1.01 (28.1x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.29 (15.0x median), `YEARS_EMPLOYED` = 2.44 (12.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 333628

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 9.29 (187.6x median), `PREV_APPROVAL_RATE` = -1.79 (89.1x median), `EXT_SOURCE_1` = 0.85 (62.2x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 334187

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `YEARS_BIRTH` = 1.17 (36.0x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.18 (17.0x median), `EXT_SOURCE_1` = -0.20 (15.8x median), `PREV_REFUSED_COUNT` = 5.67 (13.5x median), `PREV_COUNT` = 4.31 (13.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 334590

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 3.18 (84.2x median), `YEARS_BIRTH` = 1.59 (48.3x median), `CREDIT_TERM_MONTHS` = -1.06 (22.2x median), `AMT_ANNUITY` = -1.70 (13.1x median), `BUREAU_COUNT` = 2.02 (12.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 334869

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.15 (86.4x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `POS_SK_DPD_MEAN` = 6.76 (34.3x median), `CREDIT_TERM_MONTHS` = 0.69 (10.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 335092

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.35 (101.4x median), `POS_SK_DPD_MEAN` = 4.69 (23.4x median), `CREDIT_TERM_MONTHS` = -1.57 (19.6x median), `PREV_APPROVAL_RATE` = -0.36 (18.6x median), `AMT_ANNUITY` = 1.56 (16.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 335192

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 20.84 (419.6x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `AMT_ANNUITY` = -1.39 (16.6x median), `EXT_SOURCE_3` = -1.69 (16.1x median), `ANNUITY_TO_INCOME` = -1.05 (10.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 335419

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.00 (73.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `YEARS_BIRTH` = -0.68 (9.8x median), `ANNUITY_TO_INCOME` = 3.92 (8.9x median), `CREDIT_TO_INCOME` = 5.28 (8.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 336014

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.74 (128.3x median), `YEARS_BIRTH` = 1.58 (48.1x median), `POS_MONTHS_COUNT` = 1.73 (45.3x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = -1.03 (9.3x median), `BUREAU_BB_DPD_RATIO_MEAN` = 1.58 (9.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 336262

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.74 (53.8x median), `CREDIT_TERM_MONTHS` = -1.44 (30.6x median), `OWN_CAR_AGE` = 6.79 (15.9x median), `BUREAU_DAYS_CREDIT_MEAN` = -0.95 (11.9x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = -1.03 (9.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 336525

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = -2.34 (116.2x median), `POS_SK_DPD_MEAN` = 15.09 (77.7x median), `CREDIT_TERM_MONTHS` = -1.48 (18.5x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (10.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 336665

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟠 Tipe C — Risk Signal** |
| Top Deviating Features | `INST_SEVERE_LATE_RATIO` = 4.08 (25.3x median), `INST_DPD_MEAN` = 1.99 (18.5x median), `AMT_INCOME_TOTAL` = -1.66 (16.2x median), `INST_DPD_MAX` = 2.41 (16.0x median), `BUREAU_ACTIVE_RATIO` = 2.03 (13.4x median) |
| Justifikasi | Kombinasi finansial kontradiktif (mis. rasio cicilan/pendapatan ekstrem, income rendah + credit besar, atau skor eksternal tinggi di cluster bermasalah). |
| Business Impact | Underwriting: matikan auto-approve, wajibkan manual review oleh underwriter senior + verifikasi pendapatan fisik. |

---

## ROW_ID 337004

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.89 (67.0x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.60 (12.7x median), `AMT_ANNUITY` = 0.77 (10.7x median), `ANNUITY_TO_INCOME` = 2.36 (7.0x median), `YEARS_BIRTH` = -1.10 (5.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 337296

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.27 (167.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `ANNUITY_TO_INCOME` = 6.28 (14.8x median), `YEARS_EMPLOYED` = 2.92 (13.8x median), `YEARS_BIRTH` = 0.78 (9.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 337319

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `YEARS_BIRTH` = -1.56 (45.5x median), `EXT_SOURCE_1` = -0.49 (37.7x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `POS_MONTHS_COUNT` = -1.05 (29.1x median), `CREDIT_TERM_MONTHS` = 1.27 (28.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 337340

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 2.09 (41.8x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.64 (21.2x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `YEARS_BIRTH` = -0.55 (15.5x median), `AMT_ANNUITY` = 1.91 (12.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 337479

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.36 (102.4x median), `POS_MONTHS_COUNT` = 2.54 (66.9x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `CREDIT_TERM_MONTHS` = 1.04 (23.7x median), `AMT_INCOME_TOTAL` = 1.84 (15.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 337553

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.44 (180.1x median), `AMT_INCOME_TOTAL` = 2.47 (21.6x median), `YEARS_EMPLOYED` = 4.42 (20.4x median), `EXT_SOURCE_3` = -1.85 (17.7x median), `BUREAU_ACTIVE_RATIO` = 2.03 (13.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 338148

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 1.01 (25.9x median), `YEARS_BIRTH` = 0.81 (25.1x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 1.85 (13.9x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.87 (10.4x median), `AMT_INCOME_TOTAL` = 1.24 (10.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 338377

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.69 (50.4x median), `AMT_CREDIT` = 1.16 (37.4x median), `INST_SEVERE_LATE_RATIO` = 4.39 (27.1x median), `INST_LATE_RATIO` = 3.80 (24.5x median), `INST_DPD_MEAN` = 1.35 (15.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 338535

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.51 (187.8x median), `YEARS_BIRTH` = -1.55 (45.2x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `CREDIT_TERM_MONTHS` = -1.47 (31.3x median), `POS_MONTHS_COUNT` = -0.53 (15.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 338553

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_CREDIT` = -0.76 (22.8x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.59 (10.5x median), `AMT_ANNUITY` = -0.39 (7.0x median), `PREV_REFUSED_COUNT` = 5.12 (6.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 338649

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `YEARS_BIRTH` = 0.99 (30.6x median), `POS_MONTHS_COUNT` = 0.84 (21.6x median), `CREDIT_TERM_MONTHS` = -0.95 (19.7x median), `AMT_INCOME_TOTAL` = -1.00 (10.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 339745

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.30 (95.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_EMPLOYED` = 4.15 (19.2x median), `YEARS_BIRTH` = 1.14 (13.8x median), `AMT_INCOME_TOTAL` = 1.24 (10.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 341227

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 20.10 (103.8x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `EXT_SOURCE_1` = -0.49 (37.2x median), `CREDIT_TERM_MONTHS` = -1.51 (18.9x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 341611

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.01 (148.2x median), `POS_MONTHS_COUNT` = 2.18 (57.2x median), `EXT_SOURCE_3` = -2.12 (20.1x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.71 (19.5x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 341792

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.39 (104.2x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 3.82 (75.5x median), `CREDIT_TERM_MONTHS` = 1.28 (29.1x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `POS_MONTHS_COUNT` = -0.53 (15.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 342037

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_REFUSED_COUNT` = 18.49 (27.0x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CC_AMT_BALANCE_MEAN` = 3.11 (11.1x median), `CC_UTILIZATION_MEAN` = 4.02 (10.9x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = -0.59 (10.5x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 342201

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `YEARS_BIRTH` = 1.29 (39.3x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 3.58 (27.8x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.36 (17.5x median), `POS_MONTHS_COUNT` = 0.64 (16.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 342262

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_INCOME_TOTAL` = 2.47 (12.6x median), `EXT_SOURCE_2` = 1.00 (10.6x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median), `CC_MONTHS_COUNT` = 3.33 (8.6x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 342874

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 6.50 (131.6x median), `EXT_SOURCE_1` = 1.72 (127.1x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.37 (27.9x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `CC_MONTHS_COUNT` = 3.45 (8.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 343018

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 1.37 (27.7x median), `CREDIT_TERM_MONTHS` = -1.08 (13.3x median), `BUREAU_DAYS_CREDIT_MEAN` = -2.18 (12.6x median), `BUREAU_BB_DPD_RATIO_MEAN` = 2.02 (11.4x median), `ANNUITY_TO_INCOME` = 0.85 (10.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 343116

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 23.24 (454.7x median), `INST_PAYMENT_RATIO_MEAN` = 1.32 (125.0x median), `BUREAU_BB_DPD_RATIO_MEAN` = 12.25 (64.0x median), `AMT_ANNUITY` = 1.51 (21.9x median), `AMT_CREDIT` = 0.66 (21.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 343509

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 4.03 (106.9x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `YEARS_BIRTH` = 1.07 (33.0x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.22 (14.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 343832

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `AMT_INCOME_TOTAL` = 1.84 (15.8x median), `BUREAU_DAYS_CREDIT_MEAN` = -2.17 (14.8x median), `EXT_SOURCE_1` = -0.07 (6.6x median), `INST_LATE_RATIO` = 3.25 (6.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 343979

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 1.45 (37.8x median), `CREDIT_TERM_MONTHS` = -1.62 (34.5x median), `EXT_SOURCE_1` = -0.17 (14.0x median), `YEARS_BIRTH` = 0.25 (8.5x median), `ANNUITY_TO_INCOME` = 1.86 (7.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 344095

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.57 (191.7x median), `INST_DPD_MAX` = 7.33 (71.4x median), `POS_MONTHS_COUNT` = 1.45 (37.8x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_3` = -2.19 (20.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 344096

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.56 (40.8x median), `INST_SEVERE_LATE_RATIO` = 4.08 (25.3x median), `AMT_INCOME_TOTAL` = 1.84 (15.8x median), `YEARS_EMPLOYED` = 1.82 (9.0x median), `EXT_SOURCE_3` = 0.69 (5.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 344216

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.73 (129.4x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `OWN_CAR_AGE` = 3.67 (9.1x median), `EXT_SOURCE_3` = 1.12 (9.1x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.14 (3.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 344845

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.27 (19.0x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `EXT_SOURCE_2` = -0.42 (5.9x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (4.5x median), `PREV_APPROVAL_RATE` = -2.34 (3.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 345106

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.10 (83.0x median), `EXT_SOURCE_3` = -1.87 (17.8x median), `BUREAU_COUNT` = 2.02 (12.2x median), `POS_MONTHS_COUNT` = -0.41 (11.9x median), `YEARS_BIRTH` = -0.40 (10.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 345320

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.46 (109.3x median), `BUREAU_BB_DPD_RATIO_MEAN` = 10.33 (54.1x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `POS_MONTHS_COUNT` = -0.93 (25.9x median), `CREDIT_TERM_MONTHS` = -0.94 (19.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 345332

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.04 (75.9x median), `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `CREDIT_TERM_MONTHS` = -1.48 (18.5x median), `BUREAU_ACTIVE_RATIO` = 0.86 (15.5x median), `ANNUITY_TO_INCOME` = 1.25 (14.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 345345

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_DAYS_CREDIT_MEAN` = -3.09 (40.9x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_1` = -0.43 (32.9x median), `CREDIT_TERM_MONTHS` = -1.38 (29.2x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 345731

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 3.05 (62.3x median), `INST_DPD_MAX` = 5.80 (56.8x median), `POS_MONTHS_COUNT` = 1.21 (31.3x median), `INST_DPD_MEAN` = 1.84 (20.7x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.41 (16.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 345803

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_SK_DPD_MEAN` = 7.94 (114.4x median), `EXT_SOURCE_1` = 0.51 (36.7x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `AMT_INCOME_TOTAL` = 1.84 (15.8x median), `BUREAU_ACTIVE_RATIO` = 2.03 (13.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 345916

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.17 (162.2x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 3.86 (76.4x median), `CREDIT_TERM_MONTHS` = -1.63 (34.6x median), `BUREAU_ACTIVE_RATIO` = 0.99 (17.7x median), `OWN_CAR_AGE` = 6.79 (15.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 346266

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `INST_PAYMENT_RATIO_MEAN` = 1.68 (152.4x median), `BUREAU_BB_SEVERE_DPD_MEAN` = 2.95 (58.7x median), `YEARS_BIRTH` = 0.69 (21.6x median), `POS_MONTHS_COUNT` = 0.80 (20.5x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.47 (19.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 346395

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 3.23 (85.3x median), `EXT_SOURCE_1` = -0.37 (28.1x median), `BUREAU_COUNT` = 3.34 (19.6x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 1.85 (13.9x median), `YEARS_BIRTH` = -0.45 (12.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 346728

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `AMT_CREDIT` = -1.01 (30.8x median), `BUREAU_COUNT` = 4.22 (15.2x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.72 (15.1x median), `EXT_SOURCE_3` = -2.38 (13.2x median), `AMT_ANNUITY` = -0.68 (11.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 346737

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 2.86 (75.6x median), `EXT_SOURCE_1` = -0.88 (66.7x median), `YEARS_BIRTH` = -1.21 (35.2x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `CREDIT_TERM_MONTHS` = 0.87 (20.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 346988

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.73 (127.4x median), `EXT_SOURCE_3` = -2.10 (19.9x median), `YEARS_BIRTH` = -0.87 (12.2x median), `BUREAU_BB_DPD_RATIO_MEAN` = 1.93 (10.9x median), `AMT_INCOME_TOTAL` = -1.06 (10.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 347117

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.09 (154.0x median), `POS_MONTHS_COUNT` = -0.69 (19.4x median), `BUREAU_ACTIVE_RATIO` = 0.78 (14.2x median), `BUREAU_BB_DPD_RATIO_MEAN` = 1.63 (9.4x median), `EXT_SOURCE_3` = -0.85 (8.6x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 347271

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 3.79 (100.4x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `CREDIT_TERM_MONTHS` = 0.98 (22.5x median), `AMT_ANNUITY` = -2.57 (19.3x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.49 (17.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 347408

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟠 Tipe C — Risk Signal** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `YEARS_BIRTH` = -1.02 (14.2x median), `BUREAU_ACTIVE_RATIO` = 2.03 (13.4x median), `AMT_INCOME_TOTAL` = -1.06 (10.7x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.31 (10.5x median) |
| Justifikasi | Kombinasi finansial kontradiktif (mis. rasio cicilan/pendapatan ekstrem, income rendah + credit besar, atau skor eksternal tinggi di cluster bermasalah). |
| Business Impact | Underwriting: matikan auto-approve, wajibkan manual review oleh underwriter senior + verifikasi pendapatan fisik. |

---

## ROW_ID 347636

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.95 (71.5x median), `EXT_SOURCE_2` = 1.07 (11.5x median), `CNT_CHILDREN` = 4.99 (9.7x median), `EXT_SOURCE_3` = 0.91 (7.1x median), `AMT_INCOME_TOTAL` = 0.86 (5.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 347831

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.88 (140.7x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `EXT_SOURCE_3` = -2.07 (19.6x median), `YEARS_BIRTH` = -1.42 (19.3x median), `BUREAU_BB_DPD_RATIO_MEAN` = 2.96 (16.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 348174

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.94 (219.1x median), `AMT_ANNUITY` = 0.96 (13.6x median), `PREV_REFUSED_COUNT` = 9.57 (13.5x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.41 (9.1x median), `CC_MONTHS_COUNT` = 3.41 (8.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 349189

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.32 (99.0x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.89 (21.4x median), `CREDIT_TERM_MONTHS` = -0.93 (19.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 350284

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `PREV_APPROVAL_RATE` = 0.96 (46.5x median), `CREDIT_TERM_MONTHS` = 1.43 (19.9x median), `AMT_ANNUITY` = 1.77 (18.7x median), `AMT_CREDIT` = 2.05 (12.0x median), `AMT_INCOME_TOTAL` = 2.08 (10.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 350460

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.17 (88.0x median), `POS_SK_DPD_MEAN` = 7.69 (39.1x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `PREV_APPROVAL_RATE` = -0.69 (34.9x median), `CREDIT_TERM_MONTHS` = -1.30 (16.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 350628

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.35 (101.6x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `YEARS_BIRTH` = -1.82 (24.5x median), `AMT_INCOME_TOTAL` = -1.66 (16.2x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (11.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 350666

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.05 (76.9x median), `YEARS_EMPLOYED` = 5.19 (17.2x median), `AMT_ANNUITY` = 0.64 (8.7x median), `AMT_CREDIT` = 0.24 (8.4x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.37 (8.3x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 350908

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `BUREAU_ACTIVE_RATIO` = 1.25 (22.2x median), `CREDIT_TERM_MONTHS` = -1.08 (13.2x median), `AMT_ANNUITY` = 1.03 (10.5x median), `EXT_SOURCE_3` = -0.96 (9.7x median), `AMT_INCOME_TOTAL` = 1.24 (6.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 351177

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.51 (111.2x median), `AMT_CREDIT` = -2.99 (93.0x median), `AMT_ANNUITY` = -3.12 (48.3x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.58 (12.4x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 351245

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.03 (150.1x median), `POS_MONTHS_COUNT` = 4.07 (107.9x median), `YEARS_BIRTH` = 0.71 (22.0x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 351341

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 1.37 (35.6x median), `BUREAU_ACTIVE_RATIO` = 2.03 (35.5x median), `YEARS_BIRTH` = -1.03 (29.7x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.84 (20.9x median), `EXT_SOURCE_1` = 0.29 (20.4x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 351370

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 15.54 (304.4x median), `EXT_SOURCE_1` = 0.61 (44.5x median), `AMT_CREDIT` = 1.20 (38.5x median), `BUREAU_BB_DPD_RATIO_MEAN` = 7.24 (38.2x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 351494

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `BUREAU_BB_SEVERE_DPD_MEAN` = 10.53 (206.7x median), `BUREAU_BB_DPD_RATIO_MEAN` = 7.54 (39.8x median), `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `BUREAU_DAYS_CREDIT_MEAN` = -3.02 (20.9x median), `EXT_SOURCE_3` = 1.78 (15.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 351599

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `CC_SK_DPD_MEAN` = 7.85 (158.6x median), `CREDIT_TERM_MONTHS` = 0.69 (10.1x median), `CC_MONTHS_COUNT` = 3.45 (8.9x median), `YEARS_EMPLOYED` = 2.47 (8.3x median), `PREV_APPROVAL_RATE` = -0.14 (7.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 351754

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = -1.64 (34.9x median), `EXT_SOURCE_1` = 0.41 (29.6x median), `POS_MONTHS_COUNT` = -0.93 (25.9x median), `AMT_ANNUITY` = -2.51 (18.8x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 352083

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 1.51 (110.8x median), `AMT_ANNUITY` = -1.30 (20.8x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 0.73 (15.3x median), `AMT_CREDIT` = -0.45 (13.1x median), `BUREAU_ACTIVE_RATIO` = 0.46 (8.9x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 352158

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = -1.57 (33.4x median), `YEARS_BIRTH` = 0.69 (21.7x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `OWN_CAR_AGE` = 6.79 (15.9x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 352281

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `YEARS_BIRTH` = -1.36 (39.5x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `CREDIT_TERM_MONTHS` = -1.62 (34.5x median), `EXT_SOURCE_3` = -2.14 (20.2x median), `BUREAU_BB_DPD_RATIO_MEAN` = 3.06 (16.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 352401

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `POS_MONTHS_COUNT` = 1.85 (48.6x median), `INST_DPD_MAX` = 4.12 (40.6x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `CREDIT_TERM_MONTHS` = 1.27 (28.7x median), `CC_SK_DPD_MEAN` = 1.35 (28.1x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 352427

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_1` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.75 (55.1x median), `AMT_CREDIT` = -1.52 (46.8x median), `AMT_ANNUITY` = -0.66 (11.1x median), `CC_MONTHS_COUNT` = 3.01 (7.9x median), `BUREAU_ACTIVE_RATIO` = -0.48 (7.1x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 352431

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `YEARS_BIRTH` = -1.79 (52.2x median), `BUREAU_ACTIVE_RATIO` = 1.51 (26.6x median), `EXT_SOURCE_3` = -2.62 (24.6x median), `CREDIT_TERM_MONTHS` = -1.05 (22.1x median), `BUREAU_BB_DPD_RATIO_MEAN` = 3.27 (17.8x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 352475

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 0.80 (58.8x median), `CREDIT_TERM_MONTHS` = 1.43 (32.3x median), `BUREAU_ACTIVE_RATIO` = 1.41 (24.8x median), `AMT_INCOME_TOTAL` = 1.84 (15.8x median), `YEARS_EMPLOYED` = 2.62 (13.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 352605

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `YEARS_EMPLOYED` = 4.67 (21.5x median), `EXT_SOURCE_1` = 0.25 (17.5x median), `EXT_SOURCE_3` = 1.75 (14.7x median), `YEARS_BIRTH` = 1.13 (13.7x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 352804

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_0` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -2.93 (218.5x median), `EXT_SOURCE_2` = -2.17 (26.2x median), `INST_SEVERE_LATE_RATIO` = 4.23 (26.1x median), `EXT_SOURCE_3` = -1.85 (17.7x median), `BUREAU_ACTIVE_RATIO` = 0.78 (14.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 353124

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `CREDIT_TERM_MONTHS` = -1.22 (25.6x median), `EXT_SOURCE_3` = -2.28 (21.5x median), `BUREAU_COUNT` = 2.02 (12.2x median), `BUREAU_DEBT_TO_CREDIT_RATIO` = 1.01 (11.9x median), `BUREAU_DAYS_CREDIT_MEAN` = 0.66 (10.0x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 354139

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = 2.16 (159.3x median), `BUREAU_COUNT` = 6.64 (37.9x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `CREDIT_TERM_MONTHS` = 1.27 (28.8x median), `AMT_REQ_CREDIT_BUREAU_YEAR` = 2.43 (18.5x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 354498

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `INST_PAYMENT_RATIO_MEAN` = 8.62 (807.2x median), `EXT_SOURCE_1` = 2.63 (194.4x median), `YEARS_BIRTH` = 1.54 (19.0x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (11.5x median), `POS_MONTHS_COUNT` = 3.43 (8.7x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 355069

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `REGION_RATING_CLIENT_W_CITY` = 1.92 (34.6x median), `YEARS_EMPLOYED` = 4.52 (20.8x median), `YEARS_BIRTH` = 1.34 (16.3x median), `AMT_INCOME_TOTAL` = 1.84 (15.8x median), `EXT_SOURCE_3` = 1.70 (14.3x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 355232

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_4` |
| Tipe Anomali | **🟢 Tipe B — Rare but Valid** |
| Top Deviating Features | `YEARS_BIRTH` = -0.90 (25.8x median), `POS_MONTHS_COUNT` = -0.85 (23.7x median), `BUREAU_DAYS_CREDIT_MEAN` = 1.45 (20.7x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `INST_SEVERE_LATE_RATIO` = 2.49 (15.8x median) |
| Justifikasi | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). |
| Business Impact | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## ROW_ID 355324

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_3` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -1.09 (81.7x median), `PREV_APPROVAL_RATE` = -1.51 (75.5x median), `POS_SK_DPD_MEAN` = 5.16 (25.9x median), `BUREAU_ACTIVE_RATIO` = -1.11 (17.7x median), `CREDIT_TERM_MONTHS` = -1.08 (13.2x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---

## ROW_ID 356066

| Field | Nilai |
|-------|-------|
| Cluster | `cluster_2` |
| Tipe Anomali | **🔴 Tipe A — Data Error** |
| Top Deviating Features | `EXT_SOURCE_1` = -0.99 (74.6x median), `REGION_RATING_CLIENT_W_CITY` = -2.04 (34.6x median), `BUREAU_COUNT` = 2.24 (13.4x median), `BUREAU_DAYS_CREDIT_MEAN` = -1.25 (8.1x median), `ANNUITY_TO_INCOME` = 3.58 (8.0x median) |
| Justifikasi | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). |
| Business Impact | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |

---
