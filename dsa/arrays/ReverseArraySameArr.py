#class ReverseArrayWithNewArray:

def rev(a):
    i=0
    j=len(a) - 1

    while (i<j):
        tp = a[i]
        a[i] = a[j]
        a[j] = tp
        i +=1
        j-=1


a = [1,2,3,4,5]
rev(a)
print(a)




