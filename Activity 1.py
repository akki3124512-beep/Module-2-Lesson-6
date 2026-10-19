while True:
    import turtle
    polygon = turtle.Turtle()
    turtle.Screen().bgcolor("Yellow")
    turtle.Screen().setup(500,500)

    polygon.fillcolor("blue")
    polygon.begin_fill()

    for i in range(8):
        polygon.forward(100)
        polygon.right(45)
    polygon.end_fill()
    turtle.done()
