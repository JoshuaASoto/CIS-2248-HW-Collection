# Joshua Soto
# 1553869


# Sorts inputs in descending order, outputs each iteration
def selection_sort_descend_trace(numbers):
    for i in range(len(numbers) - 1):
        ind = i
        for j in range(i + 1, len(numbers)):
            if numbers[ind] < numbers[j]:
                ind = j
        numbers[i], numbers[ind] = numbers[ind], numbers[i]
        for x in numbers:
            print(x, end=" ")
        print()
    return numbers

# Splits the inputs then runs selection_sort_descend_trace
if __name__ == "__main__":
    numbers = [int(x) for x in input("").split()]
    selection_sort_descend_trace(numbers)
