# everything in python is treated as an object including all data types, functions too. So, a function is known as a first-class object and can be passed around as arguments

# it is possible to define functions inside a function. That function is called an inner function


def func1(name):
    return f"Hello {name}"  # 	string interpolation


def func2(name):
    return f"{name}, how u doin'?"  # 	string interpolation


def func3(func4):
    return func4("yo")


print(func3(func1))
print(func3(func2))


# ------------------------------------------------------------------


def funct():
    print("function1")

    def funct2():
        print("child funct 1")

    def funct3():
        print("child funct 2")

    funct2()
    funct3()


funct()


# 	decorators -> they modify the behavior of a function without modifying it permanently. It basically wraps another function and since both functions are callable, it returns a callable


def function1(function):
    def wrapper():
        print("hello")
        function()
        print("world")

    return wrapper


# this can be made simple with decorators

# def function2():
#     print("yo")
# function2 = function1(function2)
# function2()


@function1
def function2():
    print("yo")


function2()

# decorators with arguments
def functionArg(function):
    def wrapper(*args, **kwargs):
        print("hello")
        function(*args, **kwargs)
        print("hehhehe")

    return wrapper


@functionArg
def functionArgW(name):
    return print(f"{name}")


functionArgW("pushpa")