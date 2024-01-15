import os

y = []
x = []

def ReadTheData():
    # Check if the file exists
    if os.path.exists(os.sys.argv[1]):
        file = open(os.sys.argv[1], "r")
        index = 0
        for line in file:
            # Remove trailing newline characters
            line = line.rstrip()
            # Check for invalid input (non-numeric characters)
            for i in line:
                if (i < '0' or i > '9') and i != '-':
                    print("Error, invalid input")
                    os._exit(1)
            # Check for empty line
            if len(line) == 0 :             
                print("Error, invalid input")
                os._exit(1)
            # Append the parsed values to the lists
            y.append(int(line))
            x.append(index)
            index+=1
        file.close()
    else:
        print("Error, File not found")
        os._exit(1)

# Check if the correct number of arguments are provided
if len(os.sys.argv) != 2:
    print("Error, for help please read the read me file.")
    os._exit(1)

# Read the data from the file
ReadTheData()

# Calculate the numerator and denominator for the linear regression line equation
numeratorA = len(y)*sum(xi*yi for xi, yi in zip(x, y))-sum(x)*sum(y)
denominatorA = len(y)*sum(xi**2 for xi in x)- sum(x)**2

# Calculate the numerator and denominator for the intercept of the linear regression line equation
numeratorB = sum(y)*sum(xi**2 for xi in x) - sum(x)*sum(xi*yi for xi, yi in zip(x, y))
denominatorB = len(y)*sum(xi**2 for xi in x) - sum(x)**2

# Calculate the numerator and denominator for the Pearson correlation coefficient
numeratorR = len(y)*sum(xi*yi for xi, yi in zip(x, y))-sum(x)*sum(y)
denominatorR = ((len(y)*sum(xi**2 for xi in x)-sum(x)**2)*(len(y)*sum(yi**2 for yi in y)-sum(y)**2))**0.5

# Calculate the slope (a), intercept (b), and correlation coefficient (r) with the desired precision
a = "{:.6f}".format(numeratorA/denominatorA)
b = "{:.6f}".format(numeratorB/denominatorB)
r = "{:.10f}".format(numeratorR/denominatorR)

# Print the results
print(f"Linear Regression Line: y = {a}x + {b}")
print(f"Pearson Correlation Coefficient: {r}")

