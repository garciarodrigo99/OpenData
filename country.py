class Country:

    name = None
    #id = []
    year = []
    numberOfDaysOfTourists = []
    numberOfInmigrants = []

    def __init__(self,name):
        self.name = name
        self.id = []
        self.year = []
        self.numberOfDaysOfTourists = []
        self.numberOfInmigrants = []

    def isId(self,id):
        if id in self.id:
            return True
        else:
            return False
    
    def sizeId(self):
        return len(self.id)

    def addId(self,id):
        self.id.append(id)
    
    # def addYear(self,year):
    #     self.year.append(year)

    # def addMediaOfDays(self,media):
    #     self.numberOfDaysOfTourists.append(media)

    # def addNumberOfInmigrants(self,number):
    #     self.numberOfInmigrants.append(number)
