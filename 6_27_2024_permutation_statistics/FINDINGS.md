# Summary of findings.

## Statistic 1
**Accuracy achieved:** 100.0%

**Description of model weights:** A 1 in the last index would contribute negatively towards predicting 0 and contribute positively towards predicting 1.

**How to compute statistic:** Determine whether the last index is a 1 or not. Assign a 1 if the last index is a 1. Otherwise assign a 0.


## Statistic 2
**Accuracy achieved:** 100.0%

**Description of model weights:** A value greater than to `ceil(n / 2)` in the second last index and a value less than or equal to `floor(n / 2)` in the last index would contribute negatively towards predicting 0 and contribute positively towards predicting 1.

**How to compute statistic:** Determine whether the second last index is a value in the greater half of values from 1 to n and if the last index is a value in the lesser half of values from 1 to n and assign a 1 if this holds. Otherwise assign a 0.


## Statistic 3
**Accuracy achieved:** 77.08333333333333%

**Description of model weights:**

**How to compute statistic:**

## Statistic 4
**Accuracy achieved:** 100.0%

**Description of model weights:** A value matching its index would contribute positively towards predicting 0 and contribute negatively towards predicting 1.

**How to compute statistic:** Determine whether a value is in its matching index. If no value is in its matching index, assign a 1, otherwise assign a 0.

## Statistic 5
**Accuracy achieved:** 39.583333333333336%

**Description of model weights:**

**How to compute statistic:**

## Statistic 6
**Accuracy achieved:** 52.083333333333336%

**Description of model weights:**

**How to compute statistic:**

## Statistic 7
**Accuracy achieved:** 54.166666666666664%

**Description of model weights:**

**How to compute statistic:**

## Statistic 8
**Accuracy achieved:** 81.25%

**Description of model weights:**

**How to compute statistic:**

## Statistic 9
**Accuracy achieved:** 81.25%

**Description of model weights:**

**How to compute statistic:**