class Country:

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

    def isYear(self,year):
        if year in self.year:
            return True
        else:
            return False

    def yearIndex(self,year):
        assert(self.isYear(year))
        for i in range(len(self.year)):
            if year == self.year[i]:
                return i


    
    # def addYear(self,year):
    #     self.year.append(year)

    # def addMediaOfDays(self,media):
    #     self.numberOfDaysOfTourists.append(media)

    # def addNumberOfInmigrants(self,number):
    #     self.numberOfInmigrants.append(number)
