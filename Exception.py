try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error!")
else:
    print("Success:", result)
finally:
    print("This always runs")
