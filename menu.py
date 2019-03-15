from films import Film

def options(x, films):
    if x== 'a':
        name=input('Title of the film')
        year = int(input("Realesed year"))
        m = Film(name, year)
        number=int (input("Number of actors"))
        for i in range(number):
            actor=input("Enter actor")
            m.addActor(actor)
        films.append(m)
    elif x=='d':
        for mov in films:
            print(mov.getTitle())
    elif x=='s':
        movFile = open("films.txt",'a')
        for movie in films:
            print(movie.getTitle(), file=movFile)
            print(movie.getYear(), file=movFile)
            print(len(movie.getActors()), file=movFile)
            for act in movie.getActors():
                print(act, file=movFile)
                
    elif x=='q':
        print('goodbye')
    else:
        print('wrong option')


def display():
    print('Welcome to the Films DB')
    print('Options are: ')
    print('Add a film:s a')
    print('Save film: s')
    print('Display films: d')
    print('Quit: q')

listFilms=[]
display()
choice=input('Enter an option')

while choice !='q':
    options(choice, listFilms)
    choice=input('Enter an option')
