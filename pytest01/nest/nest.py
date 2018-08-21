"""这是我写的第一个python的函数，使用递归，进行判断，输出列表中的每一项 """


def f(key, flag=False, key1=0):
    for each in key:
        if(isinstance(each, list)):
            f(each, flag, key1+1)
        else:
            if flag:
                for number in range(key1):
                    print('\t', end='')
            print(each)
