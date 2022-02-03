

def main():
    category = ['Art', 'History', 'Food', 'Recreation', 'Animals']
    money = [100,200,300,400,500]

    letcount = 0
    for i in category:
        letcount += len(i)

    for i in category:
        print(i, end = spaces(16))

    print('\n')
    dash = letcount + len(category)*15 - 15
    for i in range(0,dash):
        print("-", end ='')
    print('\n')


    for m in money:
        for num in range(0,5):
            print(f'${m:1d}', end = spaces(12+len(category[num])))
        print('\n')

def spaces(num):
    space = ''
    for i in range(0,num-1):
        space += ' '
    return space

main()
