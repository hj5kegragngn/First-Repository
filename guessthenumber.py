def new_game():
    global secret_number
    secret_number= random.randrange(0,100) or 12
    print "Welcome to guess the number!"
    print "Your range is 0-100"
    print "You have 5 guesses. Good luck."


def range100():
    global secret_number
    secret_number= random.randrange(0,100)
    new_game()

def range1000():
    global secret_number
    secret_number= random.randrange(0,1000)
    new_game()

n=5

def input_guess(inp):
    global n
    global guess
    guess = float(inp)
    print " guess was"+" "+ inp
    if guess < secret_number:
        print " higher"
        n= n-1
        print " number of guesses left is" +" " + str(n)
    elif guess > secret_number:
        print"lower"
        n=n-1
        print " number of guesses left is" +" " + str(n)
    else :
        print "correct"
        New_game
    if(n==0):
        print" you loose"
        New_game()

frame= simplegui.create_frame("GAME",200,300)
inp= frame.add_input('My label', input_guess, 50)
button1 = frame.add_button('0-100', range100)
button2 = frame.add_button('0-1000', range1000)

frame.start()
new_game()
