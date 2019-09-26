import view
import model
from datetime import datetime

def start():
    startTime = datetime.now()
    userInput = ''
    while userInput.lower() != 'exit':
        userInput = view.getInput()
        validateInput(userInput, startTime)


def validateInput(userInput, startTime):
    userInputTime = datetime.now()
    userInputLower = userInput.lower()
    if userInputLower == 'exit':
        view.exit()
    else:
        msg = 'I can hear you! You said {}'.format(userInput)
        view.respondToInput(msg)
        model.addToFile('{} Input: {}'.format(userInputTime, userInput), startTime)
        model.addToFile('{} Response: {}'.format(datetime.now(), msg), startTime)


if __name__ == "__main__":
    start()
