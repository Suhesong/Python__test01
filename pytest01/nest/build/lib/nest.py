""" 这是我写的第一个python的函数，使用递归，进行判断，输出列表中的每一项
    它有四个参数，第一个参数是需要处理的列表，第二参数是是否需要缩进，默认不需要，第三个参数是缩进的个数，
    当第二值为True时有效，第四个参数是文件路径，可以指定输出位置，默认为显示台输出。
"""
import sys

def f(key, flag=False, key1=0,fn=sys.stdout):
    print(fn)
    for each in key:
        if(isinstance(each, list)):
            f(each, flag, key1+1,fn)
        else:
            if flag:
                for number in range(key1):
                    print('\t', end='',file=fn)
            print(each,file=fn)
