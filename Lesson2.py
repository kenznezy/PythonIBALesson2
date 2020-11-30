import random
import datetime
import prettytable                  # пакет для таблицы
import matplotlib.pyplot as plt     # библиотека для графика

def BubbleSort(A):                  # сортировка пузырьком
    for i in range(len(A)):
        for j in range(len(A)-1-i):
            if A[j] > A[j+1]:
                a = A[j]
                A[j] = A[j+1]
                A[j+1] = a

'''
def QuickSort(A, fst, lst):         # быстрая сортировка
    if fst >= lst:
        return

    #i, j = fst, lst
    pivot = A[fst]
    # pivot = A[random.randint(fst, lst)]
    first_bigger = fst+1
    while first_bigger <= lst:
        if A[first_bigger] >= pivot:
            break
        first_bigger += 1
    i = first_bigger+1
    while i <= lst:
        if A[i] < pivot:
            A[i], A[first_bigger] = A[first_bigger], A[i]
            first_bigger += 1
        i += 1

    last_smaller = first_bigger-1
    A[fst], A[last_smaller] = A[last_smaller], A[fst]
    QuickSort(A, fst, last_smaller-1)
    QuickSort(A, first_bigger, lst)
'''

def ShakerSort(A):
    for i in range(0, int(len(A)/2)):
        for j in range(i-1, len(A)-1-i):
            if A[j] > A[j+1]:
                a = A[j]
                A[j] = A[j + 1]
                A[j + 1] = a
        for j in range(len(A)-2-i, i+1, -1):
            if A[j] < A[j-1]:
                a = A[j]
                A[j] = A[j-1]
                A[j-1] = a

'''def ShakerSort(A):
    for i1 in range(int(len(A) / 2)):
        for j1 in range(i1-1, len(A) - 1 - i1):
            if A[j1] > A[j1 + 1]:
                a1 = A[j1]
                A[j1] = A[j1 + 1]
                A[j1 + 1] = a1
                for j1 in range(len(A) - 2 - i1, i1 + 1, -1):
                    if A[j1] < A[j1 - 1]:
                        a2 = A[j1]
                        A[j1] = A[j1 - 1]
                        A[j1 - 1] = a2'''


'''def MergeSort(A, sm, em):
    if em-sm<2:
        return
    i = int((em - sm)/2)
    MergeSort(A, sm, i)
    MergeSort(A, i, em)
    B=[]
    for j in range (sm, em):
        B[j-sm]= A[j]
    l=sm
    r=i
    for j in range (sm, em):
        if (B[l-sm]<B[r-sm]) and l<i:
            A[j]=B[l-sm]
            l=l+1
        elif r<em:
                A[j]=B[r-sm]
                r=r+1
        else:
            if l<i:
                A[j]=B[l-sm]
                r=r+1
    B=clear()'''





table = prettytable.PrettyTable(["Размер списка", "Время merge", "Время шейкера"])
x=[]
y1=[]
y2=[]



for N in range(1000,5001,1000):
    x.append(N)
    min=1
    max=N
    A=[]
    for i in range (N):
        A.append(int(round(random.random()*(max-min)+min)))

    #print(A)

    B = A.copy()
    # print(B)

    #BubbleSort(A)
    print("---")
    # print(A)


    #QuickSort(B, 0, len(B)-1)
    print("---")
    # print(B)

    print(A)

    t1 = datetime.datetime.now()
    #MergeSort(A, 0, len(A)-1)
    t2 = datetime.datetime.now()
    print(A)
    y1.append((t2-t1).total_seconds())
    print("Merge   " +str(N)+"   заняла   "+str((t2-t1).total_seconds()) + "c")

    print(B)
    t3 = datetime.datetime.now()
#   QuickSort(B, 0, len(B)-1)
    ShakerSort(B)
    t4 = datetime.datetime.now()
    print(B)
    y2.append((t4 - t3).total_seconds())
    print("Шейкер   " +str(N)+"   заняла   "+str((t4-t3).total_seconds()) + "c")

    table.add_row([str(N), str((t2-t1).total_seconds()), str((t4-t3).total_seconds())])
print(table)

plt.plot(x, y1, "C0")
plt.plot(x, y2, "C1")
plt.show()