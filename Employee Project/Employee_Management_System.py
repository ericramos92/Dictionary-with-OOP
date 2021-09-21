class employee():
    def __init__(self,name,id_number,department,job):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job = job
        #setters
    def setname(self, name):
        self.__name = name
    def setid_number(self, id_number):
        self.__id_number = id_number
    def setdepartment(self, department):
        self.__department = department
    def setjob(self, job):
        self.__job = job
    #getters
    def getname(self):
        return self.__name
    def getid_number(self):
        return self.__id_number
    def getdepartment(self):
        return self.__department
    def getjob(self):
        return self.__job
    def __str__(self):
        return 'Name:' + self.__name + \
                '\nID:' + str(self.__id_number) +\
                "\nDepartment:" + self.__department + \
                "\nJob:" + self.__job
