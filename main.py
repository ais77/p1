# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def menu():
    x = int(input("enter x"))
    y = int(input("enter y"))
    print("1.add")
    print("2,subtract")
    n = int(input("enter choice"))
    if n == 1:
        print(x+y)
    elif n == 2:
        print(x*y)
    else:
        print("invalid choice")

menu()
