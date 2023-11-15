#union
set_a={1,2,3,4}
set_b={6,7,8,9}
union = set_a | set_b
print(union)
# diff
set_c={2,3,4}
set_d={1,3,5}
diff = set_c - set_d
print(diff)
#symmetric diff
set_a = {4, 2, 8}
set_b = {1, 2}
symmetric_diff = set_a ^ set_b
print(symmetric_diff)
#intersection
set_a = {4, 2, 8}
set_b = {1, 2}
intersection = set_a & set_b
print(intersection)
#disjoint set
set_a = {1, 2}
set_b = {3, 4}
is_disjoint = set_a.isdisjoint(set_b)
print(is_disjoint)
#super set
set_1 = {4, 6}
set_2 = {2, 6}
is_superset = set_1.issuperset(set_2)
print(is_superset)