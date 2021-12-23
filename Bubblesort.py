import random
import timeit


def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


start = timeit.default_timer()
array = [random.randrange(1, 500, 1) for i in range(500)]
bubblesort(array)
print("The sorted list by bubble sort is:")
for i in range(len(array)):
    print("%d" % array[i], end=" ")


print("\n")
end = timeit.default_timer()
print((end - start)*1000, end=" ")