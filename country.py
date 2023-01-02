class Country:

    def __init__(self,name,id):
        self.name = name
        self.id = [id]
        self.year = []
        self.numberOfDaysOfTourists = []
        self.numberOfInmigrants = []

    def isId(self,id):
        return id in self.id

    def isYear(self,year):
        return year in self.year

    def yearIndex(self,year):
        assert(self.isYear(year))
        for i in range(len(self.year)):
            if year == self.year[i]:
                return i

    def __repr__ (self) -> str:
        rep = f'{self.name} {self.id}\n'
        rep += f'\t{self.numberOfDaysOfTourists}\n'
        rep += f'\t{self.year}\n\n'

        return rep
    
    # def addYear(self,year):
    #     self.year.append(year)

    # def addMediaOfDays(self,media):
    #     self.numberOfDaysOfTourists.append(media)

    # def addNumberOfInmigrants(self,number):
    #     self.numberOfInmigrants.append(number)
