with open('donkey.txt') as f:
    s = f.read()

new = s.replace('donkey', '######')

with open('donkey.txt', 'w') as f:
    f.write(new)