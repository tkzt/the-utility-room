# bubble sort
import random

unsorted = [random.random() * 100 for i in range(100)]


def bubble_sort(a: list[float], n: int) -> list[float]:
    for i in range(n - 1):
        no_swap = True
        for j in range(1, n - i):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
                no_swap = False
        if no_swap:
            break
    return a


def quick_sort(a: list[float], n: int) -> list[float]:
    l, r, r_to_l = 0, n - 1, True
    while l < r:
        if a[l] > a[r]:
            a[l], a[r] = a[r], a[l]
            r_to_l = not r_to_l

        if r_to_l:
            r -= 1
        else:
            l += 1

    if l >= 2:
        quick_sort(a[:l], l)

    if n - 1 - l >= 2:
        quick_sort(a[l + 1:], n - 1 - l)

    return a


def insert_sort(a: list[float], n: int) -> list[float]:
    for i in range(1, n):
        for j in range(i):
            if a[n-1] < a[j]:
                a = [*a[:j], a[n-1], *a[j:n-1]]
                break
            elif j == i-1:
                a = [*a[:j+1], a[n-1], *a[j+1:n-1]]
    return a


# let's assume that bubble sort is super correct.
the_correct_answer = bubble_sort(unsorted, 100)
assert the_correct_answer == quick_sort(unsorted, 100), 'Wrong quick-sort function!'
assert the_correct_answer == insert_sort(unsorted, 100), 'Wrong insert-sort function!'
