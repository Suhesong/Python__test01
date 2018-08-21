import os
import nest
import pickle
os.chdir('./pytest01')

man=[]
other=[]
try:
    file =open('test.txt')
    for each in file:
        try:
            (role,line_spoken)=each.split(':',1)
            line_spoken=line_spoken.strip()
            if role == 'jonn':
                man.append(line_spoken)
            elif role=='Amy':
                other.append(line_spoken)
        except ValueError:
            pass
except IOError:
    print('the file is missing!')
if file in locals():
    file.close()
try:
    with open('man.txt','wb') as outMan, open('other.txt','wb') as outOther:
        pickle.dump(man,outMan)
        pickle.dump(other,outOther)

except IOError as err:
    print('the file'+ str(err))
except pickle.PickleError as peer:
    print('Pickinng err:'+str(peer))
finally:
    pass

print('all is ok!')