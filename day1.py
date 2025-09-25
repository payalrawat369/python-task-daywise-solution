# Google Form Simulation with Different Print Methods

# Taking user input (different data types)
name = input("Enter your name: ")            # string
age = int(input("Enter your age: "))         # integer
height = float(input("Enter your height (in cm): "))   # float
student = input("Are you a student? (yes/no): ")       # string
marks = float(input("Enter your marks (out of 100): "))  # float

print("\n--- Form Submitted Successfully! ---")

# 1. Using Comma
print("Name:", name, ", Age:", age, ", Height:", height, ", Student:", student, ", Marks:", marks)

# 2. Using Plus (+)
print("Name: " + name + " | Age: " + str(age) + " | Height: " + str(height) + " | Student: " + student + " | Marks: " + str(marks))

# 3. Using Percent (%)
print("Name: %s | Age: %d | Height: %.2f | Student: %s | Marks: %.1f" % (name, age, height, student, marks))

# 4. Using format()
print("Name: {} | Age: {} | Height: {:.2f} | Student: {} | Marks: {:.1f}".format(name, age, height, student, marks))

# 5. Using f-string
print(f"Name: {name} | Age: {age} | Height: {height:.2f} | Student: {student} | Marks: {marks:.1f}")
