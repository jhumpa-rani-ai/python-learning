s1={2,3,4,5}
s2={3,5,8,}
print(s1.union(s2))
s1.update(s2)
print(s1,s2)

cities = {"tokiyo","delhi", "merdlin", "berlin"}
cities2 ={"seol", "kabu" ,"delhi"}
# cities3=(cities.difference(cities2))
# print(cities3)
print(cities.issuperset(cities2))
cities3 ={"tokiyo","mardlin"," delhi"}
print(cities.issuperset(cities3))
print(cities3.issuperset(cities))
