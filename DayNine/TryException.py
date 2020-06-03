'''Try Can't be written without except'''
try:
    print(x)
except NameError:
    print("Exception")
except:
    print("Other Exception")
else:
    print("All Ok!!!")
finally:
    print("Try Catch")