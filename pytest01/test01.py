import pickle
import os
os.chdir('./pytest01')
with open('man.txt','rb') as data:
    a_list=pickle.load(data)

print(a_list)