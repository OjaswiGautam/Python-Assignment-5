L = []
for i in range(1,11):
    L.append(i)

print(L)
Ex = []
for i in L[0:5]:
    Ex.append(i)



print(f"Extracted first five elements: {Ex}")

Ex.reverse()
print(f"Reversed extracted elements: {Ex}")
