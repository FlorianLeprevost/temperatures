#program that convert Fahrencheit to cellcius and vice versa
# put F ou C as first arg, and put number as second arg


import sys
if sys.argv[1]=="F":
    temp = (int(sys.argv[2]) - 32)*5/9
    print(round(temp,2), " °C")
if sys.argv[1] == "C":
    temp = int(sys.argv[2]) *9/5 + 32
    print(f"{temp:.3f} °F")
