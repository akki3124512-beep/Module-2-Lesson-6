while True:
    import turtle
    polygon = turtle.Turtle()
    turtle.Screen().bgcolor("Yellow")
    turtle.Screen().setup(500,500)
    polygon.fillcolor("red")
    polygon.begin_fill()
    for i in range(3):
        polygon.forward(75)
        polygon.right(120)

    polygon.penup()
    polygon.right(90)
    polygon.forward(45)
    polygon.left(90)
    polygon.pendown()

    for i in range(3):
        polygon.forward(75)
        polygon.left(120)
    polygon.end_fill()
    turtle.done()