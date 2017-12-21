'''def warpper():
    print("begin wapper")
    def inner():
        print("in inner")
    return inner

if __name__ == '__main__':
    warpper()
    a = warpper()
    a()



def line_conf(a, b):
    # a,b 称为自由变量,环境变量
    # 内置函数和其引用的环境变量总称为 闭包
    def line(x):
        # (python3)nonlocal 用于修改环境变量的方式
        # (python2)将环境变量包装到列表里 用于修改环境变量的方式
        nonlocal a
        a += 1
        return a*x+b
    return line

line1 = line_conf(1, 2)
line2 = line_conf(5, 5)

print(line1(5))
print(line2(5))
# __closure__保存闭包用到的属性
print(line1.__closure__)'''

def make_avg():
    data = list()
    def addnumber(value):
        data.append(value)
        total = sum(data)
        return total/len(data)
    return addnumber

myavg = make_avg()
print(myavg(100))
print(myavg(300))

