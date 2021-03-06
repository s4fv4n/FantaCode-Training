class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    QUES = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def round6(name):
    print(BColors.OKGREEN + "Round 6" + BColors.QUES + "\nThe Old lady died while crossing the river. How?\n\t(a) She had a bypass surgery the week before and her high blood pressure caused her death\n\t(b) The estimated depth of the river was incorrect as calculated by the old lady\n\t(c) There were sharks in the river who couldn't be possibly invited to any birthday party\n\t(d) Some strange, alien object fell from the sky and hit the Old lady, killing her instantly.")
    inn = input(BColors.OKBLUE + "\n>>")
    if inn == "d":
        print(BColors.OKGREEN + "That's wonderful feat. You have passed all the obstacles and Won the hearts of all the other defeated warriors. Congratulations.")
        exit()
    else:
        print("You have achieved so much but still failed. You will have to try again from the beginning. Good luck on your next try.")
        exit()

def round5(name):
    print(BColors.OKGREEN + "Round 5" + BColors.QUES + " \n\t An old lady is trying to cross the alligator pond. How will she cross it?\n\t(a) She makes a boat with the available resources around here\n\t(b) Death is inevitable to every Human. She decides her time is now and crosses it.\n\t(c) An elephant comes and she gets on it and both crosses the river together.\n")
    inn = input(BColors.OKBLUE + ">>")
    if inn == "b":
        print(BColors.OKGREEN + "That's true. She will be able to cross the river because all the animals are at the party of King Lion.\n You passed another test. Rejoice")
        round6(name)
    else:
        print(BColors.FAIL + "Alas, you failed. You were truly amazing but it is time we separate. Try again to see if you can pass this test.")
        exit()


def round4(name):
    print("\nRound 4\n" + BColors.QUES + "There's a birthday party of the King Lion going on in the forest. Everybody was invited but one. Who was the one that didn't get the invitation?")
    #cam = input()
    if input(BColors.OKBLUE + ">>") == "Camel":
        print(BColors.OKGREEN + "Great Answer. You are truly mischievous. You may enter the next round\n")
        round5(name)
    else:
        print(BColors.FAIL + "That's not the right answer. Why name someone when you put someone else in a refrigerator? Get a brain for rent," + name + ", and try again.")
        exit()


def round3(name):
    print(BColors.QUES + "How do you insert a camel into the refrigerator?\n\t(a) I don't know\n\t(b) Open the refrigerator, insert camel, close the refrigerator\n\t(c) Option (a)\n" + BColors.OKBLUE + ">>" + BColors.ENDC)
    read = input()
    if read == "a" or read == "b" or read == "c":
        print(BColors.FAIL + name + ", destined to be a failure. Your answer has been falsified, again. The correct answer is \n\tOpen the refrigerator, take the elephant out, insert the camel, close the refrigerator.\n" + BColors.OKGREEN + "As you are just a beginner, I shall pass you to the Round 4" + BColors.ENDC)
        round4(name)
    else:
        discontinue(name)


def discontinue(name):
    print(BColors.FAIL + "Your reply cannot be accepted, hence you cannot be tolerated here. So long, " + name)
    exit()


def round2(name):
    str = input(BColors.QUES + "\nHow do you insert an elephant into a refrigerator?\n\t(a) I don't know\n\t(b) Option (a)\n\t(c) Option (b)\n\t(d) All of the above\n" + BColors.OKBLUE + ">>" + BColors.ENDC)
    if str == "a" or str == "b" or str == "c" or str == "d":
        print(BColors.FAIL + "\nToo sad. Some knowledge lies beyond the mighty " + name + ". The real answer is : \n\t'Open the refrigerator, insert the elephant, close the refrigerator.'\n" + BColors.ENDC)
        goon = input(BColors.OKGREEN + "\nBut I shall excuse your for your measly brain. Shall we continue?\n" + BColors.OKBLUE + ">>" + BColors.ENDC)
        if goon == "Yes":
            round3(name)
        else:
            discontinue(name)
    else:
        discontinue(name)


def enter(name):
    brck = input(BColors.OKGREEN + "\nBold of you to Enter this holy path." + BColors.QUES + "\n\n There are 97 bricks in an aeroplane. If one was dropped, how many remains?\n" + BColors.OKBLUE + ">>" + BColors.ENDC)
    if brck == "96":
        print(BColors.OKGREEN + "Correct. Round 2" + BColors.ENDC)
        round2(name)
    else:
        print(BColors.FAIL + "You lack basic arithmetic abilities for even a caveman. Go back to your cave and learn to count. Good Bye." + BColors.ENDC)


def greeting():
    name = input(BColors.HEADER + "Greetings, warrior. What shall this internal voice of thou call you upon this journey?\n" + BColors.ENDC + BColors.OKBLUE + ">>" + BColors.ENDC)
    cont = input(BColors.OKGREEN + "\nWelcome to the Game, " + BColors.BOLD + name + BColors.ENDC + BColors.OKGREEN + " the PythonSlayer. Shall we enter?\n" + BColors.OKBLUE + ">>" + BColors.ENDC)
    if cont == 'Yes':
        enter(name)
    else:
        discontinue(name)


greeting()

