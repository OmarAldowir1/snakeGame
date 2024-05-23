import turtle

t = turtle.Turtle()
t.speed(2)  # Adjust speed to 2 (or any other value between 1 and 10)
t.color('red')
t.fillcolor('red')

t.begin_fill()
t.left(140)
t.forward(200)
t.circle(-100, 200)
t.left(120)
t.circle(-100, 200)
t.forward(200)
t.end_fill()

t.penup()
t.goto(-115, 130)  # Adjust position for writing
t.color('white')  # Change color to white for better visibility
t.write("MAHACIM", font=("Arial", 40, "normal"))

t.hideturtle()

turtle.done()
