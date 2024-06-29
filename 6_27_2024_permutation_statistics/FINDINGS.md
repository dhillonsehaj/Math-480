# Summary of findings.

## Statistic 1
**Accuracy achieved:** 100.0%

**Description of model weights:** A 1 in the last index would contribute negatively towards predicting 0 and contribute positively towards predicting 1.

**How to compute statistic:** Determine whether the last index is a 1 or not. Assign a 1 if the last index is a 1. Otherwise assign a 0.


## Statistic 2
**Accuracy achieved:** 100.0%

**Description of model weights:** A value in the second last index that is greater than the last index would contribute negatively towards predicting 0 and contribute positively towards predicting 1.

**How to compute statistic:** Determine whether the second last index is a value greater than the value in the last index and if so, assign 1. Otherwise assign a 0.


## Statistic 3
**Accuracy achieved:** 77.08333333333333%

**Description of model weights:** A value in its respective index seems to have positive and negative contributions to predicting 0 and 1.

**How to compute statistic:** Assign 1 when value is index, otherwise 0. (not too sure)

## Statistic 4
**Accuracy achieved:** 100.0%

**Description of model weights:** A value matching its index would contribute positively towards predicting 0 and contribute negatively towards predicting 1.

**How to compute statistic:** Determine whether a value is in its matching index. If no value is in its matching index, assign a 1, otherwise assign a 0.

## Statistic 5
**Accuracy achieved:** 39.583333333333336%

**Description of model weights:** When going in increasing order of rows, the weights contribute more positively to values in decreasing order for each index. That is, for row 0 (predicting 0) the in order values of the indices contribute more positively and for the last row (predicting greatest) the reverse order values of the indices contribute more positively.

**How to compute statistic:** Reverse the permutation.

## Statistic 6
**Accuracy achieved:** 52.083333333333336%

**Description of model weights:** The weights contribute positively and negatively randomly. (not really sure).

**How to compute statistic:** Randomly assign 1 and 0.

## Statistic 7
**Accuracy achieved:** 54.166666666666664%

**Description of model weights:** Similar to statistic 5 sooo.... when going in increasing order of rows, the weights contribute more positively to values in decreasing order for each index. That is, for row 0 (predicting 0) the in order values of the indices contribute more positively and for the last row (predicting greatest) the reverse order values of the indices contribute more positively. (not really sure).

**How to compute statistic:** Reverse the permutation.

## Statistic 8
**Accuracy achieved:** 81.25%

**Description of model weights:** The weights contribute positively and negatively randomly. (not really sure).

**How to compute statistic:** Randomly assign 1 and 0.

## Statistic 9
**Accuracy achieved:** 81.25%

**Description of model weights:** The weights contribute positively and negatively randomly. (not really sure).

**How to compute statistic:** Randomly assign 1 and 0.