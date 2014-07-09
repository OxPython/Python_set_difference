'''
Created on Jul 8, 2014

@author: viejoemer

HowTo get the difference items of two or more sets in Python?

¿Cómo obtener los elementos diferentes de dos o más sets en Python?

difference(other, ...)
set - other - ...
Return a new set with elements in the set that are not in the others.
'''

#Create a set with values.
s = set([0,1,2,3])
print("set one", s)

s2 = set([1,6])
print("set two", s2)

#Get the difference
d = s.difference(s2)
print("Items in 'set one' that aren't in 'set two'",d)

#Get the difference
d = s2.difference(s)
print("Items in 'set two' that aren't in 'set one'",d)

s3 = set([3])
#Get the difference
d = s.difference(s2,s3)
print("Items in 'set one' that aren't in 'others'",d)