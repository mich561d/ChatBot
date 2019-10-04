import view
import model
from datetime import datetime

def start():
    startTime = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    userInput = ''
    while userInput.lower() != 'exit':
        userInput = view.getInput()
        validateInput(userInput, startTime)


def validateInput(userInput, startTime):
    userInputTime = datetime.now()
    userInputLower = userInput.lower()
    if userInputLower == 'farvel':
        view.exit()
    else:
        msg = 'Jeg kan høre dig! Du sagde {}'.format(userInput)
        view.respondToInput(msg)
        model.addToFile('{} Input: {}'.format(userInputTime, userInput), startTime)
        model.addToFile('{} Response: {}'.format(datetime.now(), msg), startTime)


if __name__ == "__main__":
    start()
