#Savion Peebles
#Professor Alesso
#CS-499
#11/15/2024

class Pet :
    # These variables define our pet name & type
    petName = None
    petType = None

    # These variables are initialized to zero to place hold until a new value is inserted
    petAge = 0
    dogSpaces = 0
    catSpaces = 0
    daysStay = 0
    # Shows the amount due to the shelter which is initialized to a float value
    amountDue = 0.0
    # object method definitions  and associated parameters
    def __init__(self, petType,  petName,  petAge,  daysStay) :
        self.petType = petType
        self.petName = petName
        self.petAge = petAge
        self.daysStay = daysStay

    # Associated function definitions and calls
    def  getPetName(self) :
        return self.petName
    def setPetName(self, petName) :
        self.petName = petName
    def  getPetType(self) :
        return self.petType
    def setPetType(self, petType) :
        self.petType = petType
    def  getPetAge(self) :
        return self.petAge
    def setPetAge(self, petAge) :
        self.petAge = petAge
    def  getDogSpaces(self) :
        return self.dogSpaces
    def setDogSpaces(self, dogSpaces) :
        self.dogSpaces = dogSpaces
    def  getCatSpaces(self) :
        return self.catSpaces
    def setCatSpaces(self, catSpaces) :
        self.catSpaces = catSpaces
    def  getDaysStay(self) :
        return self.daysStay
    def setDaysStay(self, daysStay) :
        self.daysStay = daysStay
    def  getAmountDue(self) :
        return self.amountDue
    def setAmountDue(self, amountDue) :
        self.amountDue = amountDue