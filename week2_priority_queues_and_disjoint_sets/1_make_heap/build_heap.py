# python3
from math import floor


def parent(i):
    return floor(i/2)


def left_child(i):
    return 2*i + 1


def right_child(i):
    return 2*i + 2


def swap(data, i, j, swaps):
    aux = data[i]
    data[i] = data[j]
    data[j] = aux
    swaps.append([i, j])
    # print(f"Swap realizado entre las posiciones {i}, {j}")
    return swaps


def shift_up(data, i, swaps):
    min_index = i
    # print(f"El índice mínimo al inicio es: {min_index}")
    left = left_child(i)
    if left < len(data) and data[left] < data[min_index]:
        # print(f"El número {data[left]} es menor a {data[min_index]}, se cambia el min index")
        min_index = left
    right = right_child(i)
    if right < len(data) and data[right] < data[min_index]:
        # print(f"El número {data[right]} es menor a {data[min_index]}, se cambia el min index")
        min_index = right
    if i != min_index:
        swaps = swap(data, i, min_index, swaps)
        swaps = shift_up(data, min_index, swaps)

    return swaps


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    swaps = []
    size = len(data)
    for i in reversed(range(0, floor(size/2))):
        swaps = shift_up(data, i, swaps)
    
    # print(data)
    return swaps

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
