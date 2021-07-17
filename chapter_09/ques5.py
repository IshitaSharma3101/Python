words = ['donkey', 'pagal', 'hatt']

with open('donkey.txt') as f:
    s = f.read()



for word in words:
    s = s.replace(word, '######')
    with open('donkey.txt', 'w') as f:
        f.write(s)