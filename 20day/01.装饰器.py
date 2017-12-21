
def wi(func):
    def inner():

        print("正在验证------>")
        func()
    return inner

@wi
def func1():
    print("-------1--------")

@wi
def func2():
    print("-------2--------")
    

func1()
func2()

