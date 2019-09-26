def getInput():
    return input('What can I help you with?\n')


def respondToInput(msg):
    print(msg)


def exit():
    startingLine()
    print('Exiting...')
    endingLine()


def startingLine():
    print('\n------------------------------------------------------------')


def endingLine():
    print('------------------------------------------------------------\n')
