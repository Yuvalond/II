import random
import timeit

def merge_sort(arr, srav_count=0, peremesh_count=0):
    if len(arr) <= 1:
        return arr, srav_count, peremesh_count
    
    mid = len(arr) // 2
    left, srav_count, peremesh_count = merge_sort(arr[:mid], srav_count, peremesh_count)
    right, srav_count, peremesh_count = merge_sort(arr[mid:], srav_count, peremesh_count)
    
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        srav_count += 1
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        peremesh_count += 1
        
    result += left[i:]
    result += right[j:]
    
    return result, srav_count, peremesh_count

n = int(input("Введите количество элементов в массиве: "))
A = random.sample(range(1, 1000), k=n)

print("Исходный массив: ", A)

A, srav_count, peremesh_count = merge_sort(A)

print("Отсортированный массив: ", A)
print("Количество операций сравнения: ", srav_count)
print("Количество операций перемещения: ", peremesh_count)

print("Время выполнения сортировки: ", timeit.timeit(lambda: merge_sort(A), number=1), "секунд")