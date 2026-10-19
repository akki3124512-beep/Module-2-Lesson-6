while True:
    import turtle
    polygon = turtle.Turtle()
    turtle.Screen().bgcolor("beige")
    turtle.Screen().setup(1000, 1000)

    polygon.fillcolor("pink")
    polygon.begin_fill()
    polygon.penup()
    polygon.goto(-250, 0)
    polygon.pendown()

    polygon.forward(500)
    polygon.right(125)
    polygon.forward(100)    
    polygon.right(55)
    polygon.forward(300)
    polygon.goto(-250,0)
    polygon.goto(0, 0)
    polygon.right(90)
    polygon.forward(210)
    polygon.backward(10)
    polygon.left(90)
    for i in range(2):
        polygon.forward(100)
        polygon.left(90)
        polygon.forward(65)
        polygon.left(90)
    polygon.right(90)
    polygon.forward(10)
    polygon.shape("arrow")
    polygon.end_fill()

    turtle.done()