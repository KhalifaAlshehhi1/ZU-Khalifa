# -*- coding: utf-8 -*-
"""Assignment 1 Sorting Algorithms.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XVRFTEI6SXlFbVzHbJlVp2FibtWaTkXg
"""

def distribute_chocolates_iteratively(chocolates, students):
    # Assuming chocolates and students are lists of dictionaries and lists of student names respectively.
    # Distributing chocolates to students iteratively.
    distribution = {}
    for i, student in enumerate(students):
        if i < len(chocolates):
            distribution[student] = chocolates[i]
        else:
            break  # If there are more students than chocolates, stop assigning.

    return distribution

def distribute_chocolates_recursively(chocolates, students, distribution=None, index=0):
    # Base case: If no chocolates left or no students left, return the distribution.
    if distribution is None:
        distribution = {}

    if index >= len(students) or index >= len(chocolates):
        return distribution

    # Assign chocolate to student.
    distribution[students[index]] = chocolates[index]

    # Recursive call for the next student and the next chocolate.
    return distribute_chocolates_recursively(chocolates, students, distribution, index + 1)

# Test cases
chocolates = [{"weight": 5, "price": 2, "type": "Almond", "ID": "002"},
              {"weight": 7, "price": 4, "type": "Peanut butter", "ID": "005"}]
students = ["Khalifa", "Mohammed", "Abdulla", "Saeed"]

# Testing the iterative function
iterative_distribution = distribute_chocolates_iteratively(chocolates, students)
print("Iterative Distribution:", iterative_distribution)

# Testing the recursive function
recursive_distribution = distribute_chocolates_recursively(chocolates, students)
print("Recursive Distribution:", recursive_distribution)

class Chocolate:
    def __init__(self, weight, price, chocolate_type, chocolate_id):
        self.weight = weight
        self.price = price
        self.type = chocolate_type
        self.id = chocolate_id

    def __str__(self):
        return f"Chocolate(weight={self.weight} gm, price={self.price} AED, type={self.type}, id={self.id})"

def merge_sort_chocolates(chocolates, key_func):
    if len(chocolates) > 1:
        mid = len(chocolates) // 2
        left_half = chocolates[:mid]
        right_half = chocolates[mid:]

        merge_sort_chocolates(left_half, key_func)
        merge_sort_chocolates(right_half, key_func)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if key_func(left_half[i]) < key_func(right_half[j]):
                chocolates[k] = left_half[i]
                i += 1
            else:
                chocolates[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            chocolates[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            chocolates[k] = right_half[j]
            j += 1
            k += 1
    return chocolates

# Example usage:
chocolates = [
    Chocolate(weight=5, price=2, chocolate_type="Almond", chocolate_id="002"),
    Chocolate(weight=6, price=3, chocolate_type="Hazelnut", chocolate_id="004"),
    Chocolate(weight=7, price=4, chocolate_type="Peanut Butter", chocolate_id="005"),
]

# Using the generic merge_sort_chocolates function to sort by weight and price
sorted_chocolates_by_weight = merge_sort_chocolates(chocolates.copy(), key_func=lambda x: x.weight)
sorted_chocolates_by_price = merge_sort_chocolates(chocolates.copy(), key_func=lambda x: x.price)


# Displaying the sorted chocolates for verification
print("Chocolates sorted by Weight:")
print("[" + ",\n ".join([str(choco) for choco in sorted_chocolates_by_weight]) + "]")
print("Chocolates sorted by Price:")
print("[" + ",\n ".join([str(choco) for choco in sorted_chocolates_by_price]) + "]")

class Chocolate:
    def __init__(self, weight, price, type_chocolate, id_chocolate):
        self.weight = weight
        self.price = price
        self.type = type_chocolate
        self.id = id_chocolate

    def __repr__(self):
        return (f"Chocolate(weight={self.weight} gm, price={self.price} AED, "
                f"type={self.type}, id={self.id})")

class Student:
    def __init__(self, name):
        self.name = name
        self.chocolate = None

    def __repr__(self):
        return f"Student(name={self.name}, chocolate={self.chocolate})"

def find_student_with_chocolate(students, target, by_weight=True):
    left, right = 0, len(students) - 1
    while left <= right:
        mid = (left + right) // 2
        chocolate_attr = students[mid].chocolate.weight if by_weight else students[mid].chocolate.price
        if chocolate_attr == target:
            return mid
        elif chocolate_attr < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Target not found

# Creating students with real names and assigning chocolates
students_with_chocolates = [
    Student("Khalifa"),
    Student("Messi"),
    Student("Aziz")
]
students_with_chocolates[0].chocolate = Chocolate(5, 2, 'Almond', '002')
students_with_chocolates[1].chocolate = Chocolate(6, 3, 'Hazelnut', '004')
students_with_chocolates[2].chocolate = Chocolate(7, 4, 'Peanut Butter', '005')

# Test cases with real names
index_by_weight = find_student_with_chocolate(students_with_chocolates, 6, by_weight=True)
index_by_price = find_student_with_chocolate(students_with_chocolates, 4, by_weight=False)

# Displaying results
if index_by_weight != -1:
    print(f"Index by Weight: {index_by_weight}, Student: {students_with_chocolates[index_by_weight]}")
else:
    print("No student found with the specified chocolate weight.")

if index_by_price != -1:
    print(f"Index by Price: {index_by_price}, Student: {students_with_chocolates[index_by_price]}")
else:
    print("No student found with the specified chocolate price.")
