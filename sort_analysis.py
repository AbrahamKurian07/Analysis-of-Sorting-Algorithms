import numpy as np
import matplotlib.pyplot as plt
import time


def insertion_sort(arr):

    n = len(arr)

    for i in range(1,n):
        temp = arr[i]
        j = i-1
        while j>=0 and arr[j]>temp:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp


def selection_sort(arr):

    n = len(arr)

    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if arr[min_index] > arr[j]:
                min_index = j
        temp = arr[min_index]
        arr[min_index] = arr[i]
        arr[i] = temp


def bubble_sort(arr):

    n = len(arr)
    swap_flag = 0

    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                swap_flag = 1
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
        if not swap_flag:
            break


def mergesort(arr):

    n = len(arr)
    if n <= 1:
        return arr

    m = n//2

    arr_l = arr[:m]
    arr_r = arr[m:]

    mergesort(arr_l)
    mergesort(arr_r)

    i = j = k = 0

    while i<m and j<n-m:
        if arr_l[i] < arr_r[j]:
            arr[k] = arr_l[i]
            i += 1
        else:
            arr[k] = arr_r[j]
            j += 1
        k += 1

    while i < m:
        arr[k] = arr_l[i]
        i += 1
        k += 1

    while j < n-m:
            arr[k] = arr_r[j]
            j += 1
            k += 1


def quicksort(arr, low, high):

    if low < high:

        pivot = arr[high]

        i = low-1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        i += 1
        arr[high], arr[i] = arr[i], arr[high]
        
        quicksort(arr, low, i-1)
        quicksort(arr, i+1, high)


def check_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True


# analyzing the time complexities
rng = np.random.default_rng(28)

t_ins = []
t_sel = []
t_bub = []
t_mer = []
t_qui = []
t_inbuilt = []

ns = [i for i in range(1,1000)]

for i in range(1,1000):

    a1 = [rng.uniform()*1000 for k in range(i)]
    a2 = a1.copy()
    a3 = a2.copy()
    a4 = a3.copy()
    a5 = a4.copy()
    a6 = a5.copy()

    start = time.perf_counter()
    insertion_sort(a1)
    end = time.perf_counter()
    if check_sorted(a1):
        t_ins.append(end-start)

    start = time.perf_counter()
    selection_sort(a2)
    end = time.perf_counter()
    if check_sorted(a2):
        t_sel.append(end-start)

    start = time.perf_counter()
    bubble_sort(a3)
    end = time.perf_counter()
    if check_sorted(a3):
        t_bub.append(end-start)

    start = time.perf_counter()
    mergesort(a4)
    end = time.perf_counter()
    if check_sorted(a4):
        t_mer.append(end-start)

    start = time.perf_counter()
    quicksort(a5, 0, i-1)
    end = time.perf_counter()
    if check_sorted(a5):
        t_qui.append(end-start)

    start = time.perf_counter()
    a6.sort()
    end = time.perf_counter()
    if check_sorted(a6):
        t_inbuilt.append(end-start)

slope_ins, inter_ins = np.polyfit(np.log(ns[50:]), np.log(t_ins[50:]), 1)
slope_sel, inter_sel = np.polyfit(np.log(ns[50:]), np.log(t_sel[50:]), 1)
slope_bub, inter_bub = np.polyfit(np.log(ns[50:]), np.log(t_bub[50:]), 1)
slope_mer, inter_mer = np.polyfit(np.log(ns[50:]), np.log(t_mer[50:]), 1)
slope_qui, inter_qui = np.polyfit(np.log(ns[50:]), np.log(t_qui[50:]), 1)
slope_inbuilt, inter_inbuilt = np.polyfit(np.log(ns[50:]), np.log(t_inbuilt[50:]), 1)

print("Time complexities: O(N^_)")
print(f"Insertion sort: {slope_ins:.3f}")
print(f"Selecion sort: {slope_sel:.3f}")
print(f"Bubble sort: {slope_bub:.3f}")
print(f"Mergesort: {slope_mer:.3f}")
print(f"Quicksort: {slope_qui:.3f}")
print(f"Inbuilt sort: {slope_inbuilt:.3f}")

plt.figure(figsize = (15, 15))
plt.loglog(ns, t_ins, color = 'red', label = 'insertion sort')
plt.loglog(ns, np.exp(inter_ins)*ns**slope_ins, color = 'orange', linestyle = '--')
plt.loglog(ns, t_sel, color = 'blue', label = 'selection sort')
plt.loglog(ns, np.exp(inter_sel)*ns**slope_sel, color = 'cyan', linestyle = '--')
plt.loglog(ns, t_bub, color = 'green', label = 'bubble sort')
plt.loglog(ns, np.exp(inter_bub)*ns**slope_bub, color = 'lightgreen', linestyle = '--')
plt.loglog(ns, t_mer, color = 'purple', label = 'mergesort')
plt.loglog(ns, np.exp(inter_mer)*ns**slope_mer, color = 'pink', linestyle = '--')
plt.loglog(ns, t_qui, color = 'brown', label = 'quicksort')
plt.loglog(ns, np.exp(inter_qui)*ns**slope_qui, color = 'tan', linestyle = '--')
plt.loglog(ns, t_inbuilt, color = 'black', label = 'inbuilt sort')
plt.loglog(ns, np.exp(inter_inbuilt)*ns**slope_inbuilt, color = 'gray', linestyle = '--')
plt.legend()
plt.grid(True)
plt.xlabel("size of array")
plt.ylabel("time taken")
plt.tight_layout()
plt.savefig("sort_analysis.png")

