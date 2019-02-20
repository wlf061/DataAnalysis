
"""
函数嵌套
"""
def fun1():
    def fun2():
        print("function2")
    print("fun1")
    return fun2

"""
函数闭包
"""
def f0(x):
    def f1(y):
        print(x+y)

if __name__ == '__main__':
    obj = fun1()
    print("-----")
    obj()