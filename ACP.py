while True:
    import turtle
    polygon = turtle.Turtle()
    turtle.Screen().bgcolor("beige")
    turtle.Screen().setup(1000, 1000)

    polygon.fillcolor("pink")
    polygon.begin_fill()
    polygon.penup()
    polygon.goto(-250, 250)
    polygon.pendown()
    for i in range(4):
        polygon.forward(500)
        polygon.right(90)
    polygon.end_fill()
    turtle.done()