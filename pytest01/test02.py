import os
import nest
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
    outMan = open('man.txt1','w')
    outOther=open('other.txt1','w')

    nest.f(man,fn=outMan)
    nest.f(other,True,0,outOther)
except IOError as err:
    print('the file'+ str(err))
finally:
    if outMan in locals():
        outMan.close()
    if outOther in locals():
        outOther.close()

print('all is ok!')