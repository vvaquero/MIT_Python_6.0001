
num_guesses_left = 6
num_warnings = 3

while True:
    print('while loop 1')
    in1 = input('Continue while 1?: ')
    if in1 != 'y':
        print('breaking while 1')
        break
    print('Cont breaking while 1')

    while True:
        print('while loop 2')
        in1 = input('Continue while 2?: ')
        if in1 != 'yy':
            print('breaking while 2')
            break
        print('Cont breaking while 2')

    print('Cont breaking while 11')