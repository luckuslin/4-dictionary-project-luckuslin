""" C="c"
e="."
def parking(x,y,t):
    found = 0
    for i in range(x):
        if (y[i]== "C" and t[i]=="C"):
            found += 1
    print(found)        

parking(7,"CCCCCC","C.C.C.C") """

""" 
def lang(x,y):
    english=0
    french=0
    for letter in y:
        if letter == "s" or letter == "S":
            french += 1
        elif letter == "t" or letter == "T":
            english += 1
    if english > french:
        print("English")
    else :
        print("French")

lang(3,"Lorsque j'avais six ans j'ai vu, une fois, une magnifique image, dans un livre")
 """

def magnus(x):
    Carlsen=0
    Crotia="HODI"
    for letter in x:
        if letter == Crotia:
            Carlsen +=1
        print (f"{Carlsen}")
    

magnus("PROHODNIHODNIK")