# Quiz: Implement my_enumerate
# Write your own generator function that works like the built-in function enumerate.
#
# Calling the function like this:

# lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]
#
# for i, lesson in my_enumerate(lessons, 1):
#     print("Lesson {}: {}".format(i, lesson))

# should output:

# Lesson 1: Why Python Programming
# Lesson 2: Data Types and Operators
# Lesson 3: Control Flow
# Lesson 4: Functions
# Lesson 5: Scripting

lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    i = 0
    while i <= len(iterable) - 1:
        yield start, list(iterable)[i]
        start += 1
        i += 1


for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))

for i, lesson in enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))
