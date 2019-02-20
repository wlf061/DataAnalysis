
def hello(name, msg):
    print(name,',',msg)

"""
不定长参数, * 表示为不定长参数
"""
def mylist(*list):
    r=[]
    for item in list:
        r.append(item * 2)
    return r

"""
不定长的关键字参数, 参数名称和值会以字典的形式传入
"""
def userinfo(name,age,**otherInfo):
    info = {}
    info['name'] = name
    info['age'] = age
    for key,val in otherInfo.items():
        info[key] = val
    print(info)



if __name__=="__main__":
    hello("chybin","hello")
    hello(msg="hello!",name="chybin") //指定 入参,无所谓顺序
    r=mylist(4,6,2,9,10)
    print(r)