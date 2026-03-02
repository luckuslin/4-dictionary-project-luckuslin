""" C="c"
e="."
def parking(x,y,t):
    found = 0
    for i in range(x):
        if (y[i]== "C" and t[i]=="C"):
            found += 1
    print(found)        

parking(7,"CCCCCC","C.C.C.C") """

english=("t,T")
french=("s,S")
def lang(x):
    s_count = 0
    t_count = 0
    for i in range(x):
        if english[i] > french:
            print("English")
           
        elif french[i]> english:
            print("French")

        elif french[i] ==  english:
            print("french")
    

lang(3, "Lorsque j'avais six ans j'ai vu, une fois une magnifique image,dans un livre")