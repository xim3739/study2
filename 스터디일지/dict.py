my_dict = {'name' : '홍길동' , 'birth' : '1128' , 'age' : 30}

for e in my_dict.items():
    print('{} : {}'.format(e[0],e[1]))
    
    
a = dict()

###a[[1]] = 'python'


b = {'A':90, 'B':80}
###print(b['C'])
b.get('C', 70)
for w in b.items():
    print('{} : {}'.format(w[0],w[1]))
