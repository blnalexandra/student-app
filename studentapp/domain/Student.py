class Student:
    def __init__(self, id, nume):
        self.__id = id
        self.__nume = nume

    def get_id(self):
        return self.__id

    def get_nume(self):
        return self.__nume

    def set_id(self, id_nou):
        self.__id = id_nou

    def set_nume(self, nume_nou):
        self.__nume = nume_nou

    def __str__(self):
        return "Student " + str(self.get_id()) + " : " + self.get_nume()