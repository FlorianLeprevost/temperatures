#program that convert Fahrencheit to cellcius and vice versa
# put F ou C as first arg, and put number as second arg


import sys

if len(sys.argv) != 3:
	print("""Usage:
		python Fahrenheit_celcius {F,C} temperature

		converts C to F or F to C
		""")
	sys.exit(1)

if sys.argv[1]=="F":
    temp = (int(sys.argv[2]) - 32)*5/9
    print(round(temp,2), " °C")
if sys.argv[1] == "C":
    temp = int(sys.argv[2]) *9/5 + 32
    print(f"{temp:.3f} °F")
