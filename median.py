"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

numbers = sorted(numbers)
count = int(len(numbers)) 

if count % 2 == 0:
    half = int(count/2)
    median = (numbers[half] + numbers[half-1])/2
else:
    median = numbers[(count//2)]

print(median)
