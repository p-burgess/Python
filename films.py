class Film:
    def __init__(self, name, year):
        self._name = name
        self._year=year
        self._actors=[]

    def addActor(self,name):
        self._actors.append(name)

    def getTitle(self):
        return self._name

    def getYear(self):
        return self._year

    def getActors(self):
        return self._actors

    def printTitle(self):
        print("Title: ", self.getTitle())

    def printYear(self):
        print("Year of release: ", self.getYear())

    def printActors(self):
        actors=self.getActors()
        print("The Actors were: ")
        for actor in actors:
            print(actor, end='\t')


film = Film("Titanic", 1997)

film.addActor("Kate Winslet")
film.addActor("Leonardo di Caprio")

film.printTitle()
film.printYear()
film.printActors()
