import itertools
import random

def is_valid_SYT(candidate):
  """
  Check if the given candidate tableau is a valid standard Young tableau.

  Parameters:
  - candidate (Tuple[Tuple[int]]): The tableau to be checked.

  Returns:
  - bool: True if the matrix is valid, False otherwise.

  The function checks if the given matrix is a valid SYT matrix by verifying that:
  1. The elements in each column are in strictly increasing order.
  2. The elements in each row are in strictly increasing order.

  Example:
  >>> is_valid_SYT(((1, 2, 3), (4, 5, 6), (7, 8, 9)))
  True
  >>> is_valid_SYT(((1, 2, 3), (5, 4), (6))
  False
  """
  # return False
  for row in range(len(candidate)):
    if tuple(candidate[row]) != tuple(sorted(candidate[row])):
      return False

  max_columns = max(len(row) for row in candidate)
  for col in range(max_columns):
    columns = []
    for row in candidate:
      if col < len(row):
        columns.append(row[col])
    # columns = [candidate[row][col] for row in range(len(candidate))]
    if columns != sorted(columns):
      return False

  return True

def reshape_perm(perm, shape):
  """
  Reshapes a permutation into a tableau based on the given shape.

  Parameters:
  - perm (Tuple[int]): The permutation to be reshaped.
  - shape (Tuple[int]): The shape of the resulting tableau as a weakly decreasing tuple of integers.

  Returns:
  - Tuple[Tuple[int]]: A tuple of tuples representing the reshaped permutation as a tableau.

  Example:
  >>> reshape_perm((1, 2, 3, 4, 5, 6), (3, 2, 1))
  ((1, 2, 3), (4, 5), (6,))
  """
  # return tuple()
  output = []
  idx = 0
  for i in shape:
    output.append(tuple(perm[idx:idx + i]))
    idx = idx + i
  return tuple(output)

def SYTs(shape):
  """
  Generates SYTs (Standard Young Tableaux) of on the given shape.

  Parameters:
  - shape (Tuple[int]): The shape of the resulting SYTs as a tuple of integers.

  Returns:
  - List[Tuple[Tuple[int]]]: A list of valid SYTs generated based on the given shape.

  Example:
  >>> SYTs((2, 1))
  [((1, 2), (3,)), ((1, 3), (2,))]
  """

  n = sum(shape)
  tableau = [[] for _ in range(len(shape))]
  results = []
  generate_STY(shape, tableau, 1, results)
  return results

def generate_STY(shape, tableau, index, results):
  if index > sum(shape):
    if is_valid_SYT(tableau):
      results.append(tuple(tuple(row) for row in tableau))
    return

  for i in range(len(tableau)):
    if len(tableau[i]) < shape[i]:
      tableau[i].append(index)
      generate_STY(shape, tableau, index + 1, results)
      tableau[i].pop()

def random_SYT(shape):
  """
  Generates a random Standard Young Tableau (SYT) of the given shape.

  Parameters:
  - shape (Tuple[int]): The shape of the resulting SYT as a tuple of integers.

  Returns:
  - Tuple[Tuple[int]]: A random valid SYT generated based on the given shape.

  This function generates a random permutation of numbers from 1 to n+1, where n is the sum of the elements in the `shape` tuple. It then reshapes the permutation into a tableau using the `reshape_perm` function. If the resulting tableau is not valid, it shuffles the permutation and tries again. The function continues this process until a valid SYT is found, and then returns the reshaped permutation as a tableau.

  Example:
  >>> random_SYT((2, 1))
  ((1, 2), (3,))
  """
  # return tuple()
  n = sum(shape)
  while True:
    perm = random.sample(range(1, n + 1), n)
    tableau = reshape_perm(perm, shape)
    if is_valid_SYT(tableau):
      return tableau

def random_SYT_2(shape):
  """
  Generates a random Standard Young Tableau (SYT) of the given shape.

  Parameters:
  - shape (Tuple[int]): The shape of the resulting SYT as a tuple of integers.

  Returns:
  - Tuple[Tuple[int]]: A random valid SYT generated based on the given shape.

  The function generates a random SYT by starting off with the all zeroes tableau and greedily filling in the numbers from 1 to n. The greedy generation is repeated until a valid SYT is produced.

  Example:
  >>> random_SYT_2((2, 1))
  ((1, 2), (3,))
  """
  # return tuple()
  tableau = [[0] * i for i in shape]
  n = sum(shape)
  for index in list(range(1, n + 1)):
    potential_spots = []
    for i in range(len(shape)):
        for j in range(shape[i]):
            if tableau[i][j] == 0:
                if (j == 0 or (tableau[i][j-1] < index and tableau[i][j-1] != 0)) and (i == 0 or (tableau[i-1][j] < index and tableau[i-1][j] != 0)):
                    potential_spots.append((i, j))

    if potential_spots:
      i, j = random.choice(potential_spots)
      tableau[i][j] = index

  return tuple(tuple(row) for row in tableau)

  # This code was greedy, but it did not introduce much randomness, utilized course approved tools to modify in order to introduce randomness.
  # index = 1
  # for i in range(len(shape)):
  #   for j in range(shape[i]):
  #     tableau[i][j] = index
  #     index += 1
  # return tuple(tuple(row) for row in tableau)
