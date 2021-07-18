with open('log.txt') as f:
    content = f.read()

if 'python' in content.lower():
    print('Yes')
else: 
    print('No')