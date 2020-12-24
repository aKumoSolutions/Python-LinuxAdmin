with open(r'/tmp/testfile', 'r') as f:
    data = f.read()
    word = 'sample-string'
    if word in data:
       print(word,'is in this file')
    else:
       print(word,'is not in this file')
