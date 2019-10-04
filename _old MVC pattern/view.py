def getInput():
    return input('Hvad kan jeg hjælpe dig med?\n')


def respondToInput(msg):
    print(msg)


def exit():
    startingLine()
    print('Håber jeg har hjulpet dig, med dine problemer!\n Farvel og forsat god dag!')
    endingLine()


def startingLine():
    print('\n------------------------------------------------------------')


def endingLine():
    print('------------------------------------------------------------\n')
