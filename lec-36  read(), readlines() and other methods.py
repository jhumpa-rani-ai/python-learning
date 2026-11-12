while True:
    i=i+1
    line=f.readline()
    if not line:
     break

m1 = int(line.split(",")[0])
m2 = int(line.split(",")[1])
m3 = int(line.split(",")[2])

print(f"marks of the student {i} in maths  is :{m1}")
print(f"marks of the student {i} in GK is :{m2}")
print(f"marks of the student {i} in sst  is :{m3}")

print(line)
