#in text file: ID | Name of teh place | Coordinates | All spots | Free spots

#shows ID and name of place
def list_places():
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

#shows free spots of ID
def get_place_free_spots(ID):
    places=open("places.txt","r")
    a=1
    i=0
    for line in places:
        if str(a)==str(ID):
            for char in line:
                if char == "|":
                    i +=1
                if i == 4:
                    if char != "|" and char != "\n":
                        print("Free spots:",char)
        a+=1
    places.close()

#shows total spots of ID
def get_place_total_spots(ID):
    places=open("places.txt","r")
    a=1
    i=0
    for line in places:
        if str(a)==str(ID):
            for char in line:
                if char == "|":
                    i +=1
                if i == 3:
                    if char != "|" and char != "\n":
                        print("Total spots",char)
        a+=1
    places.close()

#basically first function but doesn't show ID
def get_place_name(ID):
    places=open("places.txt","r")
    nation=""
    a=1
    for line in places:
        if str(a)==str(ID):
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
#shows coordinates of ID
def get_place_coordinates(ID):
    places=open("places.txt","r")
    a=1
    i=0
    text=""
    for line in places:
        if str(a) ==str(ID):
            for char in line:
                if char == "|":
                    i +=1
                if i == 2:
                    if char !="\n" and char !="|":
                        text+=char
        a+=1
    places.close()
    return text
#subtracts 1 from free spots
def enter_place(ID):
    places=open("places.txt","r")
    a=1
    i=0
    text2=""
    for line in places:
        text=""
        if str(a) ==str(ID):
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
                        else:
                            print("Spots are already full.")
                        text+=str(spots)
                else:
                    text+=char
        else:
            text=line
        text2+=text
        a+=1
    places.close()
    places = open("places.txt","w")
    places.write(text2)

#adds 1 to free spots
def leave_place(ID):
    places=open("places.txt","r")
    a=1
    i=0
    text2=""
    for line in places:
        text=""
        if str(a) ==str(ID):
            for char in line:
                if char == "|":
                    i +=1
                if i == 4:
                    if char == "|" or char =="\n":
                        text+=char
                    else:
                        spots=int(char)
                        if spots >= numa:
                            print("Spots are already empty.")
                        else:
                            spots +=1
                        text+=str(spots)
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
def definer(kuk2):
    if kuk2 == "spodni brno bohunice" or kuk2 == "1":
        kuk2 = "1"
    elif kuk2 == "parkoviste penzion pro duchodce stary liskovec" or kuk2 =="2":
        kuk2 =="2"
    elif kuk2 == "parkoviste mikulaskovo namesti" or kuk2 == "3":
        kuk2 ="3"
    return kuk2
import os

while True:
    kuk = str(input("MENU\nTo get free spots of place type 1\nTo get all spots of place type 2\nTo get coordinations of places type 3\nTo enter place type 4\nTo leave place type 5\nTo exit type L:"))
    if kuk=="l":
        exit()
    else:
        print("ID|Name of place\n" + list_places())
        if kuk == "1":
            kuk2 = str(input("Type ID or name of place(without punctuation):").lower())
            kuk2=definer(kuk2)
            if kuk2 == "1" or kuk2 == "2" or kuk2 == "3":
                get_place_free_spots(kuk2)
                continue
            else :
                print("Nonexistent ID or name")
                continue
        elif kuk == "2":
            kuk2 = str(input("Type ID or name of place(without punctuation):").lower())
            kuk2=definer(kuk2)
            if kuk2 == "1" or kuk2 == "2" or kuk2 == "3":
                get_place_total_spots(kuk2)
                continue
            else:
                print("Nonexistent ID or name")
                continue
        elif kuk == "3":
            kuk2 = str(input("Type ID or name of place(without punctuation):").lower())
            kuk2=definer(kuk2)
            if kuk2 == "1" or kuk2 == "2" or kuk2 == "3":
                print("Coordinates:",get_place_coordinates(kuk2))
                continue
            else :
                print("Nonexistent ID or name")
                continue
        elif kuk == "4":
            kuk2 = str(input("Type ID or name of place(without punctuation):").lower())
            kuk2=definer(kuk2)
            if kuk2 == "1" or kuk2 == "2" or kuk2 == "3":            
                enter_place(kuk2)
                continue
            else:
                print("Nonexistent ID or name")
                continue
        elif kuk == "5":
            kuk2 = str(input("Type ID or name of place(without punctuation):").lower())
            kuk2=definer(kuk2)
            if kuk2 == "1" or kuk2 == "2" or kuk2 == "3":
                leave_place(kuk2)
                continue
            else :
                print("Nonexistent ID or name")
                continue
        else:
            print("Wrong input")
            continue