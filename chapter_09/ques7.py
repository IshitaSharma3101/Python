content = True
i = 1

with open('log.txt') as f:

    while content:
        content = f.readline()

        if 'python' in content.lower():
            print('Yes')
            print(f'Line number {i}.')
        i+=1