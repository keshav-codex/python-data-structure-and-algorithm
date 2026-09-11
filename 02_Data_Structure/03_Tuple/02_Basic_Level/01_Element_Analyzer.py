# Given a tuple of numbers, find:

# maximum   minimum     sum     average

def element_analyzer(numbers: tuple)-> None:

    print(f"""
    Maximum: {max(numbers)}
    Minimum: {min(numbers)}
    Sum: {sum(numbers)}
    Average: {sum(numbers)/len(numbers)}""")

if __name__ == "__main__":
    numbers = (10, 20, 30, 40, 50)

    element_analyzer(numbers)