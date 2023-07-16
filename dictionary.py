#dictionary is collection of key values where key is unique and corresponds to value
#dictionary is muttable
#dictionary is not ordered
#dictionary is abbreviated by {}
#indexing is not possible in dictionary
#we can find key values in dictioanry
#multiple pairs of dictionaary is separated by comma(,)


#methods in dictiopnary
'''
<1>keys():return list of all  key values in the dictionary
<2>values():return list of all values in the dictionary
<3>clear():remove all the key values
<4>update():merge two dictionary together
<5>items():return all the key values pairs as tuple'''

#dictionary comprehension
'''n=int(input("enter no:-"))
sq={x:x*x for x in range(1,n+1)}
print(sq)'''

#CODE
d1={'x':1,'y':2}
x=d1.keys()
print(x)
x=d1.values()
print(x)
x=d1.items()
print(x)
x=d1.clear()
print(x)
d2={'z':3}
d1.update(d2)
print(d1)