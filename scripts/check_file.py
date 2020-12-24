import os, os.path

folder = r'/tmp'
file = 'test.txt'

if os.path.exists(os.path.join(folder, file)):
    print('File exists')
else:
    print('File does not exist')
