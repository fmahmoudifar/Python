# file = open("p24.txt")
# content = file.read()
# print(content)
# file.close()

# with open("p24.txt") as file:
#     content = file.read()
#     print(content)

# with open("p24.txt" , "w") as file:
#     file.write("New text.")

with open("p24.txt" , "a") as file:
    file.write("\nNew text.")
    #ss