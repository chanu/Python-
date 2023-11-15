a = 2
list_a = [5, "Six", a, 8.2]
list_b = [1, list_a]
print(list_b)
#length
a = 2
list_a = [5, "Six", a, 8.2]
print(len(list_a))

#index
a = 2
list_a = [5, "Six", a, 8.2]
print(list_a[1])
# join
list_a = ['Python is ', ' progr', 'mming l', 'ngu', 'ge']
string_a = "a".join(list_a)
print(string_a)

#rev of string
list_a = [5, 4, 3, 2, 1]
list_b = list_a[::-1]
print(list_b)
# slicing
list_a = [5, 4, 3, 2, 1]
list_b = list_a[-3:-1]
print(list_b)

#append
list_k=["cars","bikes","aerplane"]
list_k.append("ships")
print(list_k)

#clear
list_k=["cars","bikes","aerplane"]
list_kk=list_k.clear()
print(list_kk)

#insert
list_k=["cars","bikes","aerplane"]
list_k.insert(1,"developer")
print(list_k)

#pop
list_k=["cars","bikes","aerplane"]
list_k.pop(1)
print(list_k)

#sort
list_k=["cars","bikes","aerplane"]
list_k.sort()
print(list_k)