fruits = {"apple", "banana", "cherry"}

fruits.add("orange")

print(fruits)
fruits = {"apple", "banana", "cherry"}

fruits.clear()

print(fruits)
fruits = {"apple", "banana", "cherry"}

x = fruits.copy()

print(x)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)

print(z)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)

print(x)
fruits = {"apple", "banana", "cherry"}

fruits.discard("banana")

print(fruits)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)

print(z)
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)

print(z)
fruits = {"apple", "banana", "cherry"}

fruits.pop()

print(fruits)
"""
Created on Mon Jul 12 19:23:37 2021

@author: arpis
"""

