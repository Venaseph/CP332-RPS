import sys
import re
import argparse
import random
import time

# !/usr/bin/env python

pwins = 0
cwins = 0
play = True
pchoice = None
draw = 0


def main():
    print("Welcome to Rock Paper Scissors")
    parser = argparse.ArgumentParser(description='asdfasdfasdfas')

    parser.add_argument('--selection', '-s', help='Choose "(R)ock", "(P)aper", or "(S)cissor" for single game')
    parser.add_argument('--bestof', '-b', help='Play a best of series, odd numbers only')

    args = parser.parse_args()
    if args.selection is not None and args.bestof is not None:
        print('You can only define one argument')
    elif args.bestof is not None and int(args.bestof) % 2 == 0:
        print('--bestof can only receive an odd number')
    elif args.selection is not None and re.fullmatch('[r|p|s]', str(args.selection), re.IGNORECASE) is None:
        print('--selection must match "(R)ock, (P)aper, or (S)cissor')
    else:
        gamemode(args)

    print('Thanks for Playing!')
    return 0


def gamemode(args):
    global play
    while play:
        if args.selection is None and args.bestof is None:
            select(args)
        if args.bestof is not None:
            bestofcontrol(args)
        if args.selection is not None:
            selectioncontrol(args)


def select(args):
    global pwins, cwins, play, pchoice, draw
    pchoice = None
    if args.selection is None or draw == 1:
        if args.bestof is not None:
            pick = input("Enter selection: (R)ock, (P)aper, (S)cissors:")
        else:
            pick = input("Enter selection: (R)ock, (P)aper, (S)cissors, or (E)xit:")

    if args.selection is not None:
        pick = args.selection

    if re.fullmatch('[r|R]', pick):
        pchoice = 0
    elif re.fullmatch('[p|P]', pick):
        pchoice = 1
    elif re.fullmatch('[s|S]', pick):
        pchoice = 2
    elif args.bestof is None and re.fullmatch('[e|E]', pick):
        print('Thanks for Playing!')
        sys.exit()
    else:
        print("Incorrect Option, try again")
        select(args)

    gameplay(args)


def bestofcontrol(args):
    global play, cwins, pwins
    count = int(args.bestof)
    for x in range(0, count):
        if (count + 1) - x > pwins or (count + 1) - x > cwins:
            select(args)
        else:
            break
    if pwins > cwins:
        print("You won the Best of " + str(args.bestof))
    else:
        print("The Computer won the best of " + str(args.bestof))
    play = False


def selectioncontrol(args):
    global play
    play = False
    select(args)


def gameplay(args):
    global pchoice, pwins, cwins, draw
    cchoice = random.randint(0, 2)

    dictonary = {0: 'Rock', 1: 'Paper', 2: "Scissor"}

    timerprint()
    print('You chose ' + dictonary[pchoice] + '. The computer chose ' + dictonary[cchoice] + '.')

    if cchoice == pchoice:
        print("It's a draw. Please try again")
        draw = 1
        select(args)
    elif pchoice == 0 and cchoice == 2:
        print("You win this round")
        pwins += 1
        printscore(args)
    elif pchoice == 1 and cchoice == 0:
        print("You win this round")
        pwins += 1
        printscore(args)
    elif pchoice == 2 and cchoice == 1:
        print("You win this round")
        pwins += 1
        printscore(args)
    else:
        print('The computer wins this round.')
        cwins += 1
        printscore(args)


def timerprint():
    print('Rock... ', end="", flush=True)
    time.sleep(1)
    print('Paper... ', end="", flush=True)
    time.sleep(1)
    print('Scissor... ', end="", flush=True)
    time.sleep(1)
    print('Shoot!')

def printscore(args):
    if args.selection is None:
        print('Score [You: ' + str(pwins) + '; Computer: ' + str(cwins) + ']')


if __name__ == "__main__":
    sys.exit(main())
