import math
import turtle

""" Config """
Brush = turtle.Turtle()
Brush.color("red")
Brush.shape("arrow")
Brush.pensize(15)
Brush.speed(0)
Brush.penup()
Brush.left(90)
Brush.forward(50)

LetterInclinationDistance = math.sqrt(25**2 + 100**2) + 10

""" Letter: J """
Brush.left(90)
Brush.forward(200)

Brush.pendown()
Brush.forward(100)
Brush.back(50)
Brush.left(90)
Brush.forward(75)
Brush.circle(-25, 180, 180)

""" Letter: O """
Brush.penup()
Brush.back(25)
Brush.right(90)
Brush.forward(175)

Brush.pendown()
Brush.circle(50, 360, 360)

""" Letter: A """
Brush.penup()
Brush.forward(75)
Brush.left(60)

Brush.pendown()
Brush.forward(LetterInclinationDistance)
Brush.right(120)
Brush.forward(LetterInclinationDistance)
Brush.back(LetterInclinationDistance / 3)
Brush.right(120)
Brush.forward(70)

""" Letter: N """
Brush.penup()
Brush.back(70)
Brush.left(120)
Brush.forward(LetterInclinationDistance / 3)
Brush.left(60)
Brush.forward(25)
Brush.left(90)

LetterInclinationDistance = math.sqrt(65**2 + 100**2) + 10

Brush.pendown()
Brush.forward(100)
Brush.right(70 * 2)
Brush.forward(LetterInclinationDistance)
Brush.left(70 * 2)
Brush.forward(100)


# Crear el pincel
Brush.penup()
Brush.back(100)
Brush.right(90)
Brush.forward(50)
Brush.pendown()

# Dibujar el fondo amarillo del logo
Brush.color("#f7df1e")  # Color oficial de fondo del logo JS
Brush.begin_fill()
for _ in range(4):
    Brush.forward(100)
    Brush.left(90)
Brush.end_fill()

# Dibujar las letras "JS" (simplificadas)
Brush.penup()
Brush.right(90)
Brush.forward(10)
Brush.left(90)
Brush.forward(25)
Brush.color("black")
Brush.hideturtle()
Brush.write("JS", font=("Arial", 50, "bold"))


turtle.done()