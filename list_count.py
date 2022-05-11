list_fruit = ['apple' , 'banana' , 'tomato']
list_animal = ['bear' , 'elepant' , 'monkey']
list_instrument = ['guitar' , 'piano' , 'harmonica']

x = (len(list_animal[0]) + len(list_animal[1]) + len(list_animal[2]))
y = (len(list_fruit[0]) + len(list_fruit[1]) + len(list_fruit[2]))
z = (len(list_instrument[0]) + len(list_instrument[1]) + len(list_instrument[2]))

r = input(print('list_fruit','list_animal','list_instrument','중 문자의 개수를 구할 리스트를 입력해주세요'))
if r == 'list_animal' :
    print(x)
if r == 'list_fruit':
    print(y)
if r == 'list_instrument':
    print(z)