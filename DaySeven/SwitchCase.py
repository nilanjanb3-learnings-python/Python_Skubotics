def one():
    return "Done"
def two():
    return "Not Done"
def decission(arguments):
    switcher={
        1:one,
        2:two
    }
    func=switcher.get(arguments)
    print(func())
num=int(input("Give A Number"))
decission(num)