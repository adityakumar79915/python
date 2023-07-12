#tuple is immutable we cannot change or modify tupple
#tuple is similar to list but cannot be modify
#Tuple method are:
'''
<1>count:count how many time a number or word come
<2>index:this function helps us to find index of element
'''
#we can find index on tuple
#tupples are ordered
#we cannot find key values in tuples as we find it on dictionary
#tupple is abbreviated by()

#IN BUILT FUNCTIONS IN PYTHON ARE
'''
len():it is used to find length 
min():it is used to find min value of element
max():it is used to find max value of element
sum():it is used to find sum
sort():it is used to arrange element in ascending order
all():it return true if all elemnt in tpl
any():it return true if element in tpl else return false
reversed():used for reversing tpl'''   


#CODE
'''x=(1,2,3,4,5,6,7,6)
print(x.count(6))
print(x.index(4))'''

x=(2,4,6,8,1)
print(len(x))
print(max(x))
print(min(x))
print(sum(x))
print(sorted(x))
print(reversed(x))