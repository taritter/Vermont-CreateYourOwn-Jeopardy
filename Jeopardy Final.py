#Jeopardy Game by Noel Thomas and Tess Ritter
#structure pace of game
import time

#main function - Noel
def main():
    #choose game mode
    start = int(input("""Welcome to Jeopardy.
If you wish to continue playing the default version press 1.
If you haven't played before press 2.
If you wish to create your own jeopardy press 3.
If you want to play jeopardy with your own file press 4.
If you wish to quit press 5.
"""))
    #different parts based on number inputted
    if start == 1:
        #default mode with given question file
        jeopardy('vtjeopardy.txt')
    elif start == 2:
        #explanation of instructions
        rules()
    elif start == 3:
        #create a new file with questions and answers to use for jeopardy
        byo()
    elif start == 4:
        #instructions to use your own file
        correct = input("""Please make sure your file is in the following format:

            Common Knowledge, $100, the tallest mountain in the world, What is the Himalayas?

            So the category is at the top and the questions follow it. Make sure the
            information is separated by commas. If this is all correct enter 'Yes', if not
            enter 'No' and you will have to rerun the program. \n \t""")
        if correct == 'yes' or 'Yes':
            #set filename to use for the game 
            filename = input('Please enter you filename: ')
            #call jeopardy function to play game
            jeopardy(filename)
    elif start == 5:
        #exit the game
        print('Ending the game...')
        time.sleep(2)
        print('Thanks for playing.')
    else:
        #invalid check in case the user doesn't enter one of the given values
        print('Please enter 1, 2, 3, 4, or 5')

        
#jeopardy function - Tess
def jeopardy(file):
    #variables to keep track of the money
    bank_one=0
    bank_two=0
    teamone = 0
    teamtwo = 0
    value = set()
    #copy file and make new one
    name = copy(file)
    #exception to open file
    try:
        pardy = open(name, 'r')
        #split the lines in the file by a comma so you can index(search) the values
    except:
        print('Input Error')
    else:
        #counts number of lines in txt
        linenum = 0
        #creates a set for category and money
        cat = set()
        mon = set()
        #creates dictionary from category and money
        check = {}
        #for loop to split line by ,
        for l in pardy:
            linenum += 1
            splitt = l.split(',')
            #index 0 is category
            cat.add(splitt[0])
            #index 1 is money
            mon.add(splitt[1])
        #for each line
        for num in range(1,linenum):
            display(cat)
            #differentiate who is answering the question and recieving the points
            category=input('Enter category wanted: ')
            #make sure category is valid
            while category not in cat:
                category=input('Invalid category entered. Enter category wanted: ')
            money=input('Enter money value wanted: ')
            #make sure money is valid amount
            while money not in mon:
                money=input('Invalid amount entered. Enter money value wanted: ')

            #to see if key (the category) is in check
            for key in check:
                #to see if value (money) is in check
                for v in value:
                    while key==category and v == money:
                        #set bounds so the user can't answer the same question more than once
                        category=input('This category and money value was already done. Enter another category: ')
                        money=input('This category and money value was already done. Enter another money value: ')
            value.add(money)
            check[category] = value

            bank_one, bank_two = qanda(category, money, name, num)
            #add money from the round to the total bank
            teamone += bank_one
            teamtwo += bank_two
            #display the amount of money for each team so the users know who is winning
            print(f'Team one, you have ${teamone}')
            print(f'Team two, you have ${teamtwo}')
        if teamone > teamtwo:
            print('Team one won!')
        elif teamtwo > teamone:
            print('Team two won!')
        else:
            print('It was a tie!')
        #close file
        pardy.close()
        check.clear()
        value.clear()

#function to see if answer is correct - Tess
def qanda(category, money, filename, num):
    #open file to read category's and money values
    file = open(filename, 'r')
    bank_one = 0
    bank_two = 0
    for line in file:
        #split up file to use parts for game and allow user to select existent values from file
        part = line.rstrip('\n').split(',')
        #search for selected question
        if part[0] == category and part[1] == money:
            #find user inputs in file to output the selected question
            dollar = money.strip('$')
            print(part[2])
            #get user answer
            answer = input('Enter answer [What is (a) ...]: ')
            #give money for correct answer
            if answer == part[3]:
                #give money to player 2
                if num % 2 == 0:
                    print(part[3])
                    bank_two+=int(dollar)
                #give money to player 1
                elif answer == part[3] and num % 2 != 0:
                    print(part[3])
                    bank_one+=int(dollar)
            #no money awarded for incorrect answers
            else:
                print('Incorrect answer.')
    #give money from the round to total bank for the appropriate player
    return bank_one, bank_two

#copies the file wanted - Noel
def copy(file):
    #opens file
    copy = open(file, 'r')
    #splits the filename by .
    filename = file.split('.')
    #adds filename to game_copy.txt
    new_name = filename[0] + 'game_copy.txt'
    newfile = open(new_name, 'w')
    #for the line in the original txt it writes it in game_copy.txt
    for line in copy:
        newfile.write(line)
    #returns new file
    return new_name


#function that displays the board - Tess
def display(cat):
    #list of categories
    category = list(cat)
    #list of money values
    money = [100,200,300,400,500]

    #to count length so the dashes are correct
    letcount = 0
    #iterates through category list and adds the length of i to count
    for i in category:
        letcount += len(i)
    print('\n')
    #prints the category and 16 spaces between each category
    for i in category:
        print(i, end = spaces(16))

    print('\n')
    #prints a dash for every space
    dash = letcount + len(category)*15 - 15
    for i in range(0,dash):
        print("-", end ='')
    print('\n')

    #prints money and aligns it with the categories
    for m in money:
        for num in range(0,5):
            print(f'${m:1d}', end = spaces(12+len(category[num])))
        print('\n')


#count spaces function function - Tess (helps with display)
def spaces(num):
    space = ''
    #adds num amount of spaces
    for i in range(0,num-1):
        space += ' '
    #return space
    return space



#print the rules of jeopardy for new players - Noel
def rules():
    print("""Hi and welcome to the rules of Jeopardy.
    Jeopardy is a fairly simple trivia game which requires teams of two with
    atleast one player per team. You will be shown five different categories
    and in each category will be given a question worth an amount of money.
    The more the question is worth the harder the question is. Each team will
    have the opportunity to select the category and money amount of their
    choosing for the chance to win that money.If the question is answered
    correctly the money value will be added to the team total. If the question
    is answered incorrectly the other team can answer and steal the money if
    the correct answer is given. If neither team gets the correct answer this
    question is discarded and the money isn't awarded to either.""")
    

#build your own file function - Tess
def byo():
    #names file
    name = input("What would you like to name your file? ")
    #how many categories
    catnum = int(input('How many categories? '))
    #opens file to write in
    newgame = open(name, 'w')
    #must have 5 categories
    for cat in range(0,catnum):
        #enter category
        category = input(f"Enter category {cat}. ")
        #money starts at 100
        money = 100
        #ask for question and answer for each caegory
        for i in range(0,catnum):
            #ask for question
            question = input(f'Enter the question for ${money} for category {category} ')
            #ask for answer
            answer = input(f'Enter the answer (What is) for ${money} for category {category} ')
            #writes the line into the file
            newgame.write(category + ', $' + str(money) + ', ' + question + ', ' + answer + '\n')
            #adds 100 to money
            money += 100
    #closes file
    newgame.close()


#calls the main
main()
