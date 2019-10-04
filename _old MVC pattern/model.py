def addToFile(data, startTime):
    filePath = 'logs/Log_{}.txt'.format(startTime)
    f = open(filePath, 'a+')
    f.write(data + '\n')
    f.close()
