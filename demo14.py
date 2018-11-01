l1 = [11, -12, 1, -3, 4, 0, 5, -7, 2, -2]
pc = 0
nc = 0
for i in range(10):
    if (l1[i]>0):
        pc += 1
    elif(l1[i]<0):
        nc += 1
    else:
        print("both are not in the list")
print(pc)
print(nc)