# from itertools import combinations
# from itertools import chain
import numpy as np
from itertools import product


# """ Set vs. Dif """
# A = [['A', 'B', 'C']]
# B = [['A', 'B', 'C']]
#
# A_set = set(map(tuple, A))
# B_set = set(map(tuple, B))
#
# print(A_set)
# print(B_set)
#
# Dif_2 = B_set.issubset(A_set)
# Dif = A_set.issubset(B_set)
#
# print(Dif)
# print(Dif_2)

#
# """ Combinations """
# A = [['A', 'B', 'D'], ['A', 'B', 'D']]
# B = [['A', 'B', 'C']]
#
# Pack = [*A, *B]
#
# Comb = list(combinations(Pack, 2))
#
# print('Pack:', Pack)
# print('Comb:', Comb)
#
#
# """ Nothing is returned """
#
#
# def check(something):
#     if something > 0:
#         return [True]
#     else:
#         return []
#
#
# solution = check(-1)
# print(solution)
# solution = check(2)
# print(solution)
# numpy_array = np.array([[1, 5, 6, 7],
#                         [5, 2, -2, -1],
#                         [-2, 4, -2, -1],
#                         [-2, 4, 5, 1]])
# neg_array = np.negative(numpy_array).tolist()
# A = [-1]
# B = [1]
#
# clause_1 = set(A)
# clause_2 = set(np.negative(np.array(B)).tolist())
#
# intersect = clause_1.intersection(clause_2)
#
# clause_1 -= intersect
# clause_2 -= intersect
#
# clause_2 = set(np.negative(np.array(list(clause_2))).tolist())
#
# union = clause_1.union(clause_2)
#
# resolvent = list(union)
#
# print(resolvent)
print(all([]))
