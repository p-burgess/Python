# this is the standard text GUI for the assignment
from league import League
hockeyLeague = League()

#print the user menu
print("menu")
print("r remove the team")
print("f find the team")
print("d display the team")
print("s save theteam")
print("l load the team")
print("w wins")
print("d draws")
print("l losses")


#get input from the user

x=input("please input one choise above")
if x == 'r':
    hockeyLeague.display()
    team=input("please input one choise above")
    hockyLeague.Remove (team)
elif x == 'f':
    hockeyLeague.display()
    team=input("please input one choise above")
    num=hockyLeague.getPosition (team)
    if num <0:
        print("team not present")
        hockeyLeague.display()
    else:
        print("the position of team is",num)
elif x == 'd':
    print("the list of teams")
    for team in hockyLeague.list:
        print(team.getName(), team.getWins(), team.getLosses(), team.getDraws())
elif x == 's':
    #save the team data to a file
    hockeyLeague.saveList()
elif x == "l":
    hockeyLeague.loadList()
elif x == "w":
    y = input (" please enter the name of the team")
    hockeyLeague.y.getWins()
elif x == "d":
    y = input (" please enter the name of the team")
    hockeyLeague.y.getDraws()
elif x == "l":
    y = input (" please enter the name of the team")
    hockyLeague.y.getLosses()
    
    
    
    


#perform user task
