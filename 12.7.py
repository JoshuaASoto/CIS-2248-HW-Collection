# Joshua Soto
# 1553869

# checks if age is valid
def get_age():
    age = int(input())
    if age < 18 or age > 75:
        raise ValueError("Invalid age.")
    return age


# calculates heart rate
def fat_burning_heart_rate(age):
    heart_rate = 220 - age
    heart_rate *= 0.7
    return heart_rate

# calls heart rate or prints error message
if __name__ == "__main__":
    try:
        age = get_age()
        rate = fat_burning_heart_rate(age)
        print("Fat burning heart rate for a", age, "year-old: ", end="")
        print(rate, "bpm")
    except ValueError as error:
        print(error)
        print("Could not calculate heart rate info.\n")