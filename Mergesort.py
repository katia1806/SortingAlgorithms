import random
import timeit

def mergesort(arr):
    if len(arr) > 1:

        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergesort(L)

        mergesort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        return arr


if __name__ == '__main__':
    start = timeit.default_timer()
    arr = [random.randrange(1, 500, 1) for i in range(500)]

    mergesort(arr)
    print("Sorted array by merge sort is: ", end="\n")
    for i in range(len(arr)):
        print(arr[i], end=" ")


print("\n")
end = timeit.default_timer()
print((end - start)*1000, end=" ")
