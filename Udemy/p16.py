# import turtle

# timmy = turtle.Turtle()
# print(timmy)
# timmy.color("blue")
# timmy.shape("turtle")
# timmy.forward(100)
 
# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Name 1", "Name 2", "Name 3"])
table.add_column("Type",["Electric","Water","Fire"])
table.align = "L"
print(table)