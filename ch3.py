# stacks and recursion

# greet
# each new function call gets added to call stack
# when greet() is called
# bye() finished first, then greet2(), then greet()  
def greet(name):
    print('hello ', name, '!')
    greet2(name)
    print("lets go")
    bye()

def greet2(name):
    print ("how are you, ", name, "?")

def bye():
    print("Good Bye")


# factorial using recursion, errors with neg numbers
def fact(x):
    # base case
    if x == 1:
        return 1
    # recursive case
    else:
        return x * fact(x-1)       


# test 
greet("peter")
print( fact(3) ) #  3 * 2 * 1 