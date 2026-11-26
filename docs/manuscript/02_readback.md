# Archived readback {#sec:readback}

The source is the public docxology-panelqr archive for October 31, 2026
[@archive20261031]. The local reader checks the first forecast group, which
uses location code `01` and horizon zero. The target week ends on the
reference date for this group. The reader verifies all 23 declared quantile
rows before selecting the three shown here.

| Quantile | Forecast admission count |
| --- | --- |
| 0.1 | 55 |
| 0.5 | 104 |
| 0.9 | 242 |

The rows are reproduced as submitted. The check compares the group with the
tracked task configuration and verifies that counts are nonnegative integers
and do not decrease across the quantile grid.
