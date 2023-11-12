def sort_list_imperative(numbers):
    for i in range(len(numbers)):
        for j in range(0, len(numbers) - i - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


print(sort_list_imperative([5, 7, 6, 2, 8]))


def sort_list_declarative(numbers):
    return sorted(numbers, reverse=True)


print(sort_list_declarative([5, 7, 6, 2, 8]))
