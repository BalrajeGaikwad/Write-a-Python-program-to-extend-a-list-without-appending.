"""
5. Write a Python program to extend a list without appending.
Sample data: [10, 20, 30]
[40, 50, 60]
Expected output : [40, 50, 60, 10, 20, 30]
"""

list1 = [10, 20, 30]
list2 = [40, 50, 60]

result = list2 + list1

print("Resulting list:", result)
