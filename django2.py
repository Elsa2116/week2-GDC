def find_largest(numbers):
    if not numbers:  # Check if the list is empty
        return None
    return max(numbers)

numbers = [10, 20, 5, 40, 25]
print("Largest number:", find_largest(numbers))