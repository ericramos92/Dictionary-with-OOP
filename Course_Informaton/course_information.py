class courseinformation:
    def __init__(self,key,value):
        self.__key = key
        self.__value = value
        self.__coursedic = {}
    def additemstodic(self):
        self.__coursedic[self.__key] = self.__value
    def getdictionary(self):
        return self.__coursedic
