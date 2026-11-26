name = input("Enter name: ")
age = int(input("Enter age: "))
filename = input("Enter filename: ")

with open("records/" + filename, "r") as f:
    data = f.read()

print("Name:", name)
print("Age:", age)
print("File content:", data)
