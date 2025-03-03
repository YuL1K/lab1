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
    star.color("lightblue")  # Зміна кольору зірок
    star.penup()
    x = random.randint(-600, 600)
    y = random.randint(-400, 400)
    star.goto(x, y)
    size = random.uniform(0.1, 1.0)  # Змінюємо розмір від 0.1 до 3.0
    star.shapesize(size)
    star.brightness = random.uniform(0.5, 1.5)  # Додаємо параметр яскравості
    stars.append(star)

# Створюємо об'єкти Turtle для Сонця, Землі та Місяця
sun = turtle.Turtle()
sun.shape("circle")
sun.color("orange")  # Зміна кольору Сонця
sun.shapesize(5)  # Збільшуємо розмір Сонця

earth = turtle.Turtle()
earth.shape("circle")
earth.color("green")  # Зміна кольору Землі
earth.shapesize(2)  # Зміна розміру Землі

earth.trail = turtle.Turtle()
earth.trail.speed(0)
earth.trail.color("lime")  # Зміна кольору сліду Землі
earth.trail.penup()
earth.trail.hideturtle()

moon = turtle.Turtle()
moon.shape("circle")
moon.color("gray")  # Зміна кольору Місяця
moon.shapesize(0.7)  # Збільшення розміру Місяця

moon.trail = turtle.Turtle()
moon.trail.speed(0)
moon.trail.color("white")
moon.trail.penup()
moon.trail.hideturtle()

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
    earth.trail.goto(x, y)
    earth.trail.pendown()
    earth.theta += earth_speed

# Функція для руху Місяця
def move_moon():
    x = earth.xcor() + moon_radius * math.cos(moon.theta)
    y = earth.ycor() + moon_radius * math.sin(moon.theta)
    moon.goto(x, y)
    moon.trail.goto(x, y)
    moon.trail.pendown()
    moon.theta += moon_speed

# Функція для зміни яскравості зірок
def twinkle_stars():
    for star in stars:
        new_size = random.uniform(0.1, 1.0) * star.brightness
        star.shapesize(new_size)

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
    twinkle_stars()
    wn.update()