import random

def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_i = i
        for j in range(i+1, n):
            if array[j] < array[min_i]:
                min_i = j
        #swap elements
        array[i], array[min_i] = array[min_i], array[i]
    return array

if __name__ == '__main__':
    a = [random.randint(0, 10) for i in range(10)]
    print(a)
    a = selection_sort(a)
    print(a)

