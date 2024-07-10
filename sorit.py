
#Buble Sort
def bublesort(arry):
    for i in range(len(arry)):
        for j in range(0, len(arry)-i-1):
            if arry[j] > arry[j+1]:
                arry[j], arry[j+1] = arry[j+1], arry[j]
    return arry

