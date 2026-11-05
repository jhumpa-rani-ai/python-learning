
try:
    num = int(input("Enter a number: "))
    result = 100 / num

except ValueError:
    print("Please enter a valid number")

except ZeroDivisionError:
    print("Number cannot be zero")

else:
    print("Result =", result)
    
finally:
    print("Program completed")