#set is an unordered collection of unique elements
#set is abbreviated by {}
#set is unorderd
#set is muttaable
#we cannot find indexing in set
#we cannnot reversed set()
#we cannot find key value in set as we can find in dictionary

#methods in sets are:
'''
<1>union
<2>intersection
<3>difference
<4>add
<5>clear
<6>pop
<7>remove'''

#IN BUILT FUNCTIONS IN SET ARE
'''
<1>len()
<2>max()
<3>min()
<4>sum()
<5>all()
<6>any()'''
#note : reversed function doesnot work in set


#CODE
'''s1={1,2,3,4,5}
s2={2,3,5,6,7,8}
union=s1.union(s2)
print(union)
intersection=s1.intersection(s2)
print(intersection)
difference=s1.difference(s2)
print(difference)'''

s1={2,3,34,5,6}
s1.add(8)
print(s1)
s1.remove(3)
print(s1)
s1.pop()
print(s1)
s1.clear()
print(s1)