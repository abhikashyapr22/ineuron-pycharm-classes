class ineuron:
    def student(self):
        print("print the details of all the students")

    def achievers(self):
        print("print the list the of all the achievers ")

    def hall_of_fame(self):
        print("print details from hall of fame")


class ineuron_vision(ineuron):

    def student(self):
        """Method overriding -  For example if our ancestor have some bad habbit we try to override that/ redefine
        that """
        print("these are the filter student list")

iv = ineuron_vision()
iv.student()

