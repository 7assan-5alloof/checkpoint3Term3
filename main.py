# Part A
periodicTable = []
for i in range(4):
    periodicTable.append(input("Enter an element: "))
print(periodicTable)

# Part B
del(periodicTable[1])
for i in range(2):
    periodicTable.append(input("Enter an element: "))
print(periodicTable)
print(periodicTable[0])
print(periodicTable[2])
print(len(periodicTable))
