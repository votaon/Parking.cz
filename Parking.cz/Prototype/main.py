#v souboru: ID místa, Název místa, souřadnice místa, celkem míst, obsazených míst
#operace: obsadit místo, uvolnit místo, celkem míst, celkem obsazených
#in text file: ID | Name of teh place | Coordinates | All spots | Free spots

def list_places():
    #projde seznam míst a vyplivne pole ID a název
    places=open("places.txt","r")
    nation=""
    for line in places:
        text=""
        i=0
        for char in line:
            if char == "|":
                i +=1
            if i == 0:
                text +=char           
            elif i == 1:
                text += char
        nation+=text
        nation+="\n"
    places.close()
    return nation
def get_place_free_spots(ID):
    #vrací počet aktuálně volných míst u místa ID
    places=open("places.txt","r")
    a=1
    i=0
    for line in places:
        if a==int(ID):
            for char in line:
                if char == "|":
                    i +=1
                if i == 4:
                    if char != "|" and char != "\n":
                        print("Free spots:", char)
        a+=1
    places.close()

def get_place_total_spots(ID):
    #vrací celkový počet míst na místě ID
    places=open("places.txt","r")
    a=1
    i=0
    for line in places:
        if a==int(ID):
            for char in line:
                if char == "|":
                    i +=1
                if i == 3:
                    if char != "|" and char != "\n":
                        print("Total spots:", char)
        a+=1
    places.close()

def get_place_name(ID):
    #vrací jméno místa ID
    places=open("places.txt","r")
    nation=""
    a=1
    for line in places:
        if a==int(ID):
            text=""
            i=0
            for char in line:
                if char == "|":
                    i +=1          
                elif i == 1:
                    text += char
            nation+=text
            nation+="\n"
        a+=1
    places.close()
    return nation

def get_place_coordinates(ID):
    #vrací souřadnice místa ID
    places=open("places.txt","r")
    a=1
    i=0
    text=""
    for line in places:
        if a ==ID:
            for char in line:
                if char == "|":
                    i +=1
                if i == 2:
                    if char !="\n" and char !="|":
                        text+=char
        a+=1
    places.close()
    return text

def enter_place(ID):
    #zapíše pro ID o jeden víc obsazených(a kontrola jestli je volné místo)
    places=open("places.txt","r")
    text2=""
    a=1
    i=0
    text=""
    text2=""
    for line in places:
        if a ==ID:
            for char in line:
                if char == "|":
                    i +=1
                if i == 4:
                    if char == "|" or char =="\n":
                        text+=char
                    else:
                        spots=int(char)
                        if spots > 0:
                            spots -=1
                            text+=str(spots)
                        else:
                            text2="Spots are already full."
                else:
                    text+=char
        else:
            text=line
        text2+=text
        a+=1
    places.close()
    places = open("places.txt","w")
    places.write(text2)
    return False

def leave_place(ID):
    places=open("places.txt","r")
    text2=""
    a=1
    i=0
    text=""
    text2=""
    for line in places:
        if a ==ID:
            for char in line:
                if char == "|":
                    i +=1
                if i == 4:
                    if char == "|" or char =="\n":
                        text+=char
                    else:
                        spots=int(char)
                        if spots < numa:
                            spots +=1
                            text+=str(spots)
                        else:
                            text2="Spots are already empty."
                elif i == 3:
                    if char == "|" or char =="\n":
                        text+=char
                    else:
                        numa=int(char)
                        text+=char
                else:
                    text+=char
        else:
            text=line
        text2+=text
        a+=1
    places.close()
    places = open("places.txt","w")
    places.write(text2)
    return 0
    #zapíše pro ID o jeden míň(s kontrolou)
    return False
print ("MENU\nTo list places type 1\nTo get free spots of place tzpe 2\n")