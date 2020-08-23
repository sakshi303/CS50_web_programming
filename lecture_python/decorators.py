def announce(f):
    def wrapper():
         print("about to run the funciton...")
         f()
         print("done with function")
    return wrapper

@announce
def hello():
    print("Hello world")

hello()