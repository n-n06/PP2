class String:
    def __init__(self):
        self.val = ""
    
    def getString(self):
        self.val = input()

    def printString(self):
        print(self.val.upper())

a = String()
a.getString()
a.printString()