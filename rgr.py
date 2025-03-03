import turtle
import math
import random

# Ініціалізуємо вікно та налаштування
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Рух космічних тіл")

# Додаємо зорі
num_stars = 25
stars = []
for _ in range(num_stars):
    star = turtle.Turtle()
    star.shape("circle")
    star.color("white")
    star.penup()
    x = random.randint(-600, 600)
    y = random.randint(-400, 400)
    star.goto(x, y)
    size = random.uniform(0.1, 1.0)  # Змінюємо розмір від 0.1 до 3.0
    star.shapesize(size)
    stars.append(star)

# Створюємо об'єкти Turtle для Сонця, Землі та Місяця
sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.shapesize(4)  # Збільшуємо розмір Сонця

earth = turtle.Turtle()
earth.shape("circle")
earth.color("blue")
earth.shapesize(1.5)  # Розмір Землі

moon = turtle.Turtle()
moon.shape("circle")
moon.color("white")
moon.shapesize(0.5)  # Розмір Місяця

# Встановлюємо радіуси орбіт та швидкості руху
earth_radius = 200
moon_radius = 50
earth_speed = 0.005
moon_speed = 0.025

# Функція для малювання орбіт
def draw_orbits():
    sun.penup()
    sun.goto(0, 0)
    sun.pendown()

# Функція для руху Землі
def move_earth():
    x = earth_radius * math.cos(earth.theta)
    y = earth_radius * math.sin(earth.theta)
    earth.goto(x, y)
    earth.theta += earth_speed

# Функція для руху Місяця
def move_moon():
    x = earth.xcor() + moon_radius * math.cos(moon.theta)
    y = earth.ycor() + moon_radius * math.sin(moon.theta)
    moon.goto(x, y)
    moon.theta += moon_speed

# Встановлюємо швидкість анімації
wn.tracer(0)

# Забезпечуємо виклик функції для малювання орбіт
draw_orbits()

# Встановлюємо початкові значення для кутів
earth.theta = 0
moon.theta = 0

# Основний цикл анімації
while True:
    move_earth()
    move_moon()
    wn.update()
