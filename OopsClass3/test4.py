class ineuron:
    """data abstraction/data hiding - says that if we hide something from user means not
    giving direct access to the inside info"""

    """why??? example how list is implemented, we can only using methods
     associated with list object"""

    __student = "data science"

    def __init__(self):
        self._ineuron = "Abhi"

    def student1(self):
        print(self._ineuron)
        """
            static method
        """
        print(f"print the class of students: {ineuron.__student}")


i = ineuron()
i.student1()
print(i._ineuron)
print(i._ineuron__student)
