set1={"Apple","Banana","Mango","Cherry","Orange"}
set2={"Melon","Kiwi","Strawberry","Orange"}
set3={"Apple","Banana","Cherry"}
print(set1)
for i in set1:
    print(i)
print("Banana" in set1)
print("Banana" not in set1)
set1.add("Strawberry")
print(set1)
set1.remove("Cherry")
print(set1)
set1.add("Cherry")
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))
print(set1.issubset(set2))
print(set1.issuperset(set2))
print(set1.issubset(set3))
print(set1.issuperset(set3))