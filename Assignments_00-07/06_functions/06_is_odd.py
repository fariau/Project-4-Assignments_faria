def main():
    for i in range(10, 20):  # Loop from 10 to 19
        if is_odd(i):
            print(i, "odd")
        else:
            print(i, "even")
            
def is_odd(value: int):
    """
    Checks to see if a value is odd. If it is, returns true.
    """
    return value % 2 == 1

if __name__ == '__main__':
    main()
