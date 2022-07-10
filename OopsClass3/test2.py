class bank:
    """Example multiple inheritance"""

    def transaction(selfself):
        print("Total transaction value")

    def account_opening(self):
        print("This will show your account open status")

    def deposite(self):
        print("This will show your deposited value")

    def test(self):
        print("this is a test method from bank class")

class HDFC_bank:
    def hdfc_to_icici(self):
        print("this will show you all the transactions happened to icici through hdfc")

    def test(self):
        print("this is a method from hdfc bank")

class ineuron_bank:
    def account_status_icici(self):
        print("ineuron bank status")

class icici(bank, HDFC_bank, ineuron_bank):
    pass

i = icici()
i.test()
i.account_status_icici()