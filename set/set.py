#1 example
# cities={"Almaty","Symkent","Astana","Aqtau"}
# q=input("In this set: ")
# if q in cities:
#    print(f"Your {q},please")
# else:
#    print(f"We don't have {q},but you can get another one")

#2 example
# cities={"Almaty","Symkent","Astana","Aqtau"}
# q=input("Write the city you want to add: ")
# if q in cities:
#     print(f"This {q} is already in this set")
# else:
#     cities.add(q)
#     print(f"{q}has been added to the set")

#3 example
# cities={"Almaty","Symkent","Astana","Aqtau"}
# q=input("What elemant do you want to add ?  ")
# q_list=q.split(" ")
# cities.update(q_list)
# print(cities)

#4 exemple
# cities={"Almaty","Symkent","Astana","Aqtau"}
# q=input("What elemant do you want to remove ?  ")
# if q in cities:
#     cities.remove(q)
#     print(f"{q} item has been removed")
# else:
#     print("There was no such element,it was removed",cities.pop())
# print(cities)

#HW
#level1
#1
# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# print(len(it_companies))
# #2
# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# it_companies.add("Twitter")
# print(it_companies)
# #3
# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# q=input("What elemant do you want to add ?  ")
# q_list=q.split(" ")
# it_companies.update(q_list)
# print(it_companies)
# #4
# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# it_companies.pop()
# print(it_companies)
#5
# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# it_companies.discard("DXC")
# print(it_companies)

# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# it_companies.remove("DXC")
# print(it_companies)

#level2
#1
# A = {19, 22, 24, 20, 25, 26}
# B = {19, 22, 20, 25, 26, 24, 28, 27}
# print(A.union(B))
# #2
# A = {19, 22, 24, 20, 25, 26}
# B = {19, 22, 20, 25, 26, 24, 28, 27}
# print(A.intersection(B))
# #3
# A = {19, 22, 24, 20, 25, 26}
# B = {19, 22, 20, 25, 26, 24, 28, 27}
# print(B.issubset(A))
# #4
# A = {19, 22, 24, 20, 25, 26}
# B = {19, 22, 20, 25, 26, 24, 28, 27}
# print(A.isdisjoint(B))
# #5
# A = {19, 22, 24, 20, 25, 26}
# B = {19, 22, 20, 25, 26, 24, 28, 27}
# print(A.union(B))
# print(B.union(A))
# #6
# A = {19, 22, 24, 20, 25, 26}
# B = {19, 22, 20, 25, 26, 24, 28, 27}
# print(A.symmetric_difference(B))
# #7
# a = {19, 22, 24, 20, 25, 26}
# b = {19, 22, 20, 25, 26, 24, 28, 27}
# del a
# del b

# # Level 3
# # 1
# age = [22 , 19 , 24 , 25 , 26 , 24 , 25 , 24]
# print(len(age))
# print(len(set(age)))
# print(len(set(age)) < len(age))
# #2
# String = '''
# Strings are an integrable data structure. 
# There are two ways to iterate over the elements of strings by characters and by indexes. 
# Each element of the string is represented by one character. 
# Strings are an immutable data structure.
# '''

# List = '''
# Lists are ordered. 
# The list item can be accessed by index. Lists are mutable types. 
# The list can store the number of different elements.
# '''

# Tuble = '''
# Tuples in Python are the same lists with one exception. 
# Tuples are immutable data structures. 
# Just like lists, they can consist of elements of different types, separated by commas.
# Tuples are enclosed in round brackets, not square brackets.
# '''

# Set = '''
# Set is an unordered collection of unique elements. 
# Unique, that is, there are no duplicate values in it.
# '''
# #3
# sentence = 'I am a teacher and I love to inspire and teach people'
# sentence_set = sentence.split()
# sentence = set(sentence_set)
# print(sentence)
