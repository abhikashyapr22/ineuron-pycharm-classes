class ineuron:
    """data encapsulation -- user are not allowed to modify anything"""

    def __init__(self):
        self.name = "data science"

    def students(self):
        print(self.name)
        print("hi")


# i = ineuron()
# i.students()
# i.name = "data analytics"
# print(i.name)


class ineuron1:
    def __init__(self):
        self.__name = "data science"

    def students(self):
        print(self.__name)
        print("hi")
        print(self._ineuron1__student1)

    def student_change(self, new_value):
        self.__student1 = new_value


i1 = ineuron1()
i1.name = "data analytics"
print(i1.name)
i1.student_change("Abhishek")
i1.students()
