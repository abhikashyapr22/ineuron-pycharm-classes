class bank:
    """Example multi level inheritance"""
    def transaction(self):
        print("Total transaction value")
    def account_opening(self):
        print("This will show your account open status")
    def deposite(self):
        print("This will show your deposited value")


class HDFC_bank(bank):
    def hdfc_to_icici(self):
        print("this will show you all the transactions happened to icici through hdfc")

class icici(HDFC_bank):
    pass

i = icici()
i.hdfc_to_icici()
i.transaction()