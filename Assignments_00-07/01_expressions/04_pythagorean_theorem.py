import math

def main():
    ab = float(input("Enter the lenght of the size AB:"))
    ac = float(input("Enter the lenght of the size BC:"))
    
    bc = math.sqrt(ab**2 + ac**2)
    
    print(f"The lenght of the hypotenuse is {bc}")
    
if __name__ == "__main__":
    main()