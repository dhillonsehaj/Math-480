import itertools

def parenthesizations(n):
  """
  Returns a set of all possible parenthesizations of length n.

  Parameters:
    n (int): The length of the parenthesizations.

  Returns:
    A set of strings, where each inner string represents a valid parenthesization of length n.

  Example:
  >>> parenthesizations(3)
  {'((()))', '(()())', '(())()', '()(())', '()()()'}
  """
  if n == 0:
    return {""}
  else:
    output = set()
    for i in range(n):
      for left in parenthesizations(i):  # q_1
        for right in parenthesizations(n - 1 - i):  # q_2
          output.add('(' + left + ')' + right)  # ( left ) right --> ( q_1 ) q_2
    return output

def product_orders(n):
  """
  Returns a set of all possible ways to multiply of n elements.

  Parameters:
    n (int): The number of elements multiplied.

  Returns:
    A set of strings where each string represents a way to multiply n elements.

  Example:
  >>> product_orders(4)
  {'((?*?)*?)*?', '(?*(?*?))*?', '(?*?)*(?*?)', '?*((?*?)*?)', '?*(?*(?*?))'}
  """
  if n == 0:
    return {""}
  elif n == 1:
    return {"?"}
  elif n == 2:
    return {"?*?"}
  else:
    output = set()
    for i in range(1, n):
      for left in product_orders(i):  # q_1
        for right in product_orders(n - i):  # q_2
          # output.add('(' + left + ')*(' + right + ')')  # sanity check # (q_1) * (q_2)
          output.add((left if i == 1 else '(' + left + ')') + '*' + (right if n - i == 1 else '(' + right + ')'))
    return output

def permutations_avoiding_231(n):
  """
  Returns a set of permutations of length n avoiding the pattern 2-3-1.

  Parameters:
    n (int): The length of the permutation.

  Returns:
    A set of permutations of length n that do not contain the pattern 2-3-1.

  Example:
  >>> permutations_avoiding_231(4)
  {(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (3, 1, 2, 4), (3, 2, 1, 4), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 3, 1, 2), (4, 3, 2, 1)}
  """
  if n < 3:
    return set(itertools.permutations(range(1, n+1)))
  else:
    output = set(itertools.permutations(range(1, n+1)))  # brute force check
    remove_perms = set()  # set of permutations with 2-3-1 pattern
    for perm in output:
      for i in range(0, n - 2):  # first index of the 3-subsequence
        for j in range(i + 1, n - 1):  # second index
          for k in range(j + 1, n):  # third index
            if perm[i] < perm[j] and perm[i] > perm[k] and perm[j] > perm[k]:  # check pattern
              remove_perms.add(perm)  # if pattern match, keep track
    for perm in remove_perms:  # remove matching patterns
      output.remove(perm)
    return output  # return appropriate permutations

def triangulations_old(n, vertices=None):  # This is the code I originally came up with, it was inefficient so the optimized output/efficiency code is below in accordance with course policy using course tools. It was inefficient because the output file was ~2GB. For the most part, the code is still my original code with some small tweaks to check for redundant or duplicated triangulations using additional structures and if/else/for blocks.
  """
  Returns a set of all possible triangulations of an n-sided polygon. A triangulation
  is represented as a tuple of internal edges. Vertices are labeled 0 through n-1 clockwise.

  Parameters:
    n (int): The number of sides of the polygon.

  Returns:
    A set of tuple of pairs, where each pair represents an internal edge in the triangulation.

  Example:
  >>> triangulations(3)
  {((0, 3), (1, 3)), ((1, 4), (2, 4)), ((1, 3), (1, 4)), ((0, 2), (2, 4)), ((0, 2), (0, 3))}
  """
  if n < 3:
    return set()
  elif n == 3:
    return {tuple()}
  else:
    if vertices is None:  # keep track of which vertices to use
      vertices = list(range(n))
    output = set()  # keep track of output
    for idx, i in enumerate(vertices[:-1]):  # start at beginning and go up until the end, maintain a triangle
      end = n if idx > 0 else n - 1  # edge case
      for jdx, j in zip(range(idx + 2, end), vertices[idx + 2:end]):  # edge must skip a vertex to be a triangle creator
        if i == vertices[1] and j == vertices[-1]:  # case where no internal edge
          edges = [tuple([i, j])]  # save tuple
          edges.extend(sorted(triangulations(n - 1, vertices[idx:jdx + 1])))  # recurse on n - 1
          output.add(tuple(edges))  # save
        else:  # case with internal edge
          edges = [tuple([i, j])]  # save tuple
          edges.extend(sorted(triangulations(jdx - idx + 1, vertices[idx:jdx + 1])))  # recurse on half one
          edges.extend(sorted(triangulations(n - jdx + idx + 1, vertices[jdx:] + vertices[:idx + 1])))  # recurse on half two
          output.add(tuple(edges))  # save tuple
    return output  # formatting is kinda off and there are some duplicates but it finds all the possible
                   # triangulations of an n-sided polygon.

def triangulations(n, vertices=None):
    if n < 3:
        return set()
    elif n == 3:
        return {tuple()}
    else:
        if vertices is None:
            vertices = list(range(n))
        output = set()
        seen = set()  # supposedly to reduce redundant/duplicates found during the process
        for idx, i in enumerate(vertices[:-1]):
            end = n if idx > 0 else n - 1
            for jdx, j in zip(range(idx + 2, end), vertices[idx + 2:end]):
                edges = [tuple(sorted([i, j]))]  # help reduce redundancy
                sub_triangulations1 = triangulations(jdx - idx + 1, vertices[idx:jdx + 1])
                sub_triangulations2 = triangulations(n - jdx + idx + 1, vertices[jdx:] + vertices[:idx + 1])
                if sub_triangulations1 and sub_triangulations2:  # both return something
                    for sub1 in sub_triangulations1:
                        for sub2 in sub_triangulations2:
                            triangulation = tuple(sorted(edges + list(sub1) + list(sub2)))  # add these edges and recursed
                            if triangulation not in seen:
                                seen.add(triangulation)  # track redundancy
                                output.add(triangulation)  # track output
                elif sub_triangulations1:  # only first returned
                    for sub1 in sub_triangulations1:
                        triangulation = tuple(sorted(edges + list(sub1)))  # add these edges and recursed
                        if triangulation not in seen:
                            seen.add(triangulation)  # track redundancy
                            output.add(triangulation)  # track output
                elif sub_triangulations2:  # only second returned
                    for sub2 in sub_triangulations2:
                        triangulation = tuple(sorted(edges + list(sub2)))  # add these edges and recursed
                        if triangulation not in seen:
                            seen.add(triangulation)  # track redundancy
                            output.add(triangulation)  # track output
                else:  # nothing returned
                    triangulation = tuple(edges)  # only these edges
                    if triangulation not in seen:  # make sure not redundant
                        seen.add(triangulation)  # track redundancy
                        output.add(triangulation)  # track output
        return output
