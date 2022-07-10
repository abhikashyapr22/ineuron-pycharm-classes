# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def test1():

    print("This is my first time i am using pycharm and created a new project")

def fibbonacci(n):
    a = 1
    b = 1

    for i in range(n):
        print(b)
        a,b = b, a+1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    test1()
    fibbonacci(7)

    import test2


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
