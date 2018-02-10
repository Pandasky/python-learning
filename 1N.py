import math
def main():
    print("This program finds the real solutions to aObj quadratic.\n")
    try:
        a, b, c = eval(input("please enter the coefficients (a, b, c): "))
        discRoot = math.sqrt(b*b - 4*a*c)
        root1 = (-b + discRoot) / (2*a)
        root2 = (-b - discRoot) /(2*a)
        print("\nThe solutions are", root1, root2)
    except ValueError as excObj:
        if str(excObj) == "math domain error":
            print("No real roots.")
        else:
            print("You did't give me the right number of coefficients")
    except NameError:
        print("\nYou didn't enter three numbers.")
    except TypeError:
        print("\nYou inputs were not all numbers.")
    except SyntaxError:
        print("\nYou inputs was not in the correct from. Missind comma")
    except:
        print("\nSomething went wrong, sorry!")
main()