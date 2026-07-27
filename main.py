from greetings import greet
from calculator import add
from weather import show_weather
from student import show_student

print("=== Demo Project ===")

greet("Ishaan")

result = add(10, 20)
print(f"Addition Result: {result}")

show_weather()

show_student()

print("Program Finished Successfully!")