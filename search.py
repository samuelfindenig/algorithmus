#Liniear Search

def liniearSearch(arry, target):
    for i in arry:
        if arry[i] == target:
            return i


#Binary Search
def binarySearch(arry, target):
    l = 0
    r = len(arry) -1

    while l <=  r:
        m = (l+r)//2
        if arry[m] < target:
            l = m + 1
        elif arry[m] > target:
            r = m - 1
        else:
            return m
    return False
    

print(binarySearch([1,2,3,4,5,7,9,11], 9))
        

 