def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
        print(array)
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

def bubbleSort(data,size):
    print("Bubble Sort")
    for i in range(size):
        for j in range(size - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
        print(*data)
    print()

def selection(l,size):
    print("Seclection Sort")
    for i in range(0,size-1):
        index = i
        for j in range(i+1,size):
            if l[j]<l[index]:
                index = j
        l[index],l[i]=l[i],l[index]
        print(*l)
    print()

def Insertion(l,size):
    print("Insertion Sort")
    for i in range(1,size):
        k = l[i]
        j = i-1
        while j>=0 and l[j]>k:
            l[j+1]=l[j]
            j=j-1
        l[j+1]=k
        print(*l)
    print()


def Merge(l):
    print("Merge Sort")
    if len(l)>1:
        r = len(l)//2
        f = l[:r]
        s = l[r:]
        Merge(f);Merge(s)
        i=j=k=0
        while len(f)>i and len(s)>j:
            if f[i]<s[j]:
                l[k]=f[i]
                i+=1
            else:
                l[k]=s[j]
                j+=1
            k+=1

        while len(f)>i:
            l[k]=f[i]
            i+=1;k+=1
        while len(s)>j:
            l[k]=s[j]
            j+=1;k+=1
    print(l)
    print()

data = [50 ,40 ,30 ,20 ,10]
size = len(data)
quickSort(data, 0, size - 1)
bubbleSort(data,size)
selection(data,size)
Insertion(data,size)
Merge(data)

