ep1={1:122,2:34,3:54,4:64,5:87}
ep2={43,45,53,65}
ep1.update(ep2)
print(ep1)
ep1.clear()
print(ep1)
ep1.popitem()
print(ep1)
del ep1[5]
print(ep1)