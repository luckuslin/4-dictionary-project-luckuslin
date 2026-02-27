C="c"
e="."
def parking(x,y,t):
    found = 0
    for i in range(x):
        if (y[i]== "C" and t[i]=="C"):
            found += 1
    print(found)        

parking(7,"CCCCCC","C.C.C.C")