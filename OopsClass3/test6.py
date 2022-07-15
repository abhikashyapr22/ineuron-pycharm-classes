class dog_info:
    """Polymorphism - when a function or operator behaves differently under different circumstances
    use case - creating a common interface"""

    def name(self):
        print("jakei")

class cat_info:
    def name(self):
        print("kitten")


def pet_name(ob):
    ob.name()


c =cat_info()
d = dog_info()

pet_name(c)
pet_name(d)