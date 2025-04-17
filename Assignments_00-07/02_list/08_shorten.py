MAX_LENGTH = 3

def shorten(lst):
    # While the list is longer than MAX_LENGTH, remove elements from the end
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()  # Removes and returns the last element from the list
        print(last_elem)  # Print the element that is removed

# The code below is provided for getting the list from user input and calling shorten function

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()  # Get the list from the user
    shorten(lst)  # Shorten the list if necessary

if __name__ == '__main__':
    main()
