

# def writeToFile(data):
#     f = open('Log.txt', 'w+')
#     for element in data:
#         f.write(element.toFile())
#     f.close()


def addToFile(data, startTime):
    f = open('logs/Log-{}.txt'.format(startTime), 'a+')
    f.write(data + '\n')
    f.close()


# def readFromFile():
#     f = open('Log.txt', 'r')
#     lines = f.readlines()
#     for element in lines:
#         if not len(element.strip()) == 0:
#             print('something')
