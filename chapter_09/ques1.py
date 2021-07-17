with open ("poems.txt") as f:
    text = f.read()
    print(text)
    
if text.index('twinkle'):
    print('present')
else:
    print('not present')
