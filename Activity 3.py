while True:
    import turtle
    polygon = turtle.Turtle()
    turtle.Screen().bgcolor("Yellow")
    turtle.Screen().setup(500,500)
    num = 5
    while True:
        polygon.forward(num)
        polygon.left(90)
        num = num + 3