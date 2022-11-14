class Generator:
    def __init__(self,filename):
        self.filename = filename
        try:
            self.fp = open(filename)
        except IOError:
            print(f'{filename} not a valid path')


    def setFilename(self,filename):
        self.filename = filename
        self.fp = open(filename)

    def parseFile(self):
        baseStringOne = ""
        baseStringTwo = ""
        mode = 0
        for line in self.fp.readlines():
            if line[0]>='0' and line[0]<='9':
                index = int(line)
                #print(f'{index} {mode}')
                if mode == 1:
                    if index >= len(baseStringOne):
                        print("invalid input file")
                        return "error","error"
                    baseStringOne = baseStringOne[:index+1]+baseStringOne+baseStringOne[index+1:]
                    #print(f'string one from str {baseStringOne}')
                else:
                    if index >= len(baseStringOne):
                        print("invalid input file")
                        return "error","error"
                    baseStringTwo = baseStringTwo[:index+1]+baseStringTwo+baseStringTwo[index+1:]
                    #print(f'string two from str {baseStringTwo}')
            else:
                if mode == 0:
                    baseStringOne = line[:-1]
                    mode = 1
                else:
                    baseStringTwo = line[:-1]
                    mode = 2
        return baseStringOne, baseStringTwo
