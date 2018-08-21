import os
os.chdir('./pytest01')

man=[];
other=[];
try:
    file =open('test.txt');
    for each in file:
        try:
            (role,line_spoken)=each.split(':',1)
            line_spoken=line_spoken.strip()
            if role == 'jonn':
                man.append(line_spoken)
            elif role=='Amy':
                other.append(line_spoken)
            print(role,end='')
            print(' said: ', end='')
            print(line_spoken,end='')
        except ValueError:
            pass
except IOError:
    print('the file is missing!')
file.close();
print(man)
print(other)