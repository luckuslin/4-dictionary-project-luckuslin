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
    Count=0
    
    for char in x:
        if Count == 0 and char.upper() == 'H':
            Count = 1
        elif Count == 1 and char.upper() == 'O':
            Count = 2
        elif Count == 2 and char.upper() == 'N':
            Count = 3        
        elif Count == 3 and char.upper() == 'I':
            Carlsen += 1
            Count = 0 

            print(Carlsen)       
magnus("PROHODNIHODNIK")

