# file = open("p24.txt")
# content = file.read()
# print(content)
# file.close()

with open("p24.txt") as file:
  content = file.read()
  print(content)

test