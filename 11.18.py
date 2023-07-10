# Joshua Soto
# 1553869

# Converts string input into integer input
# .split separates strings by the space provided
# Stores integer into list only if input is larger or equal to 0
inputs = [int(i) for i in input().split() if int(i) >= 0]

# sorts integers in list in ascending order
inputs.sort()

# Prints list with spaces between integers
for number in inputs:
    print(number, end=" ")
