class Person:

    def __init__(abhi,name,surename,emailid,year_of_birth):
        abhi.name = name
        abhi.surename = surename
        abhi.emailid = emailid
        abhi.year_of_birth = year_of_birth

    def age(self,current_year = 2022,birth_year=0):
        return current_year-birth_year

anuj_var = Person("Anuj","Bhandari","anuj@gmail.com",1992)

diff = anuj_var.age(1997)
print(diff)

print(anuj_var.name + anuj_var.surename)
print(anuj_var.surename)