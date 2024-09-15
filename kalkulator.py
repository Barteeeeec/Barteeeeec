
import math
PI =math.pi
print("a-ppK b-Obkw c-ppPR  d-ObPr e- ppRown f-ObRown g-ppTrap h-ObTrap i-ppTrk j-ObTrk k-ppTrkr l-obTrkr m-ppkol n-Obkol o-ppRom1 p-ObRom r-ppRom2 s-tw.pit t-przkkwad u-wysktrkrow x-ppSz  y-objSz z-ppProp aa-objProp ab-ppGran ac-objGran ad-ppOstr ae-objOstr af-ppWalec ag-objWalec ah-ppStozek ai-objStozek aj-ppkula ak-objKula")
print("trojkat","trojkatrow","kwadrat", "prostokat", "rownoleglobok" ,"trapez" ,"rombwysokosc", "rombprzekatna")
inp= input()
inp2=input()
if "a" == inp:
    a =float(input("podaj bok kwadratu = "))
    print(a*a)
elif "b"== inp:
    a =float(input("podaj bok kwadratu = "))
    print(4*a)
elif "c"== inp:
    a=float(input("podaj dluzszy bok prostokata "))
    b=float(input("podaj krotszy bok prostokata "))
    print(a*b)
elif "d" == inp:
    a=float(input("podaj dluzszy bok prostokata "))
    b=float(input("podaj krotszy bok prostokata "))
    print(2*a+ 2*b)
elif "e" == inp:
    a=float(input("podaj dluzszy bok rownolegloboku "))
    h=float(input("podaj wysokosc rownolegloboku "))
    print(a*h)
elif "f" == inp:
    a=float(input("podaj dluzszy bok rownolegloboku "))
    b=float(input("podaj krotszy bok rownolegloboku "))
    print(2*a + 2*b)
elif "g" == inp:
    a=float(input("podaj dluzszy bok trapezu "))
    b=float(input("podaj krotszy bok trapezu "))
    h=float(input("podaj wysokosc trapezu "))
    print((a+b)*h/2)
elif "h" == inp:
    a=float(input("podaj dluzszy bok trapezu "))
    b=float(input("podaj krotszy bok trapezu "))
    c=float(input("dlugosc 2 ramienia trapezu "))
    d=float(input("dlugosc 1 ramienia trapezu "))
    print(a+b+c+d)
elif "i" ==inp:
    a=float(input("podaj  bok trojkata "))
    h=float(input("podaj wysokosc trojkata "))
    print(1/2*a*h)
elif "j" ==inp:
    a=float(input("podaj podstawe trojkata "))
    b=float(input("podaj 1 ramie trojakta "))
    c=float(input("podaj 2 ramie trojkata "))
    print(a+b+c+d)
elif "k" ==inp:
    a=float(input("podaj bok trojkata "))
    print(a*a*math.sqrt(3)*1/4)
elif "l" ==inp:
    a=float(input("podaj bok trojkata "))
    print(3*a)
elif "m" ==inp:
    r=float(input("podaj promien "))
    print(PI*r*r)
elif "n" ==inp:
    r=float(input("podaj promien "))
    print(PI*2*r)
elif "o" ==inp:
    a=float(input("podaj bok rombu "))
    h=float(input("podaj wysokosc rombu "))
    print(a*h)
elif "p" ==inp:
    a=float(input("podaj bok rombu "))
    print(4*a)
elif "r" ==inp:
    e=float(input("podaj przekatna 1 rombu "))
    f=float(input("podaj przekatna 2 rombu "))
    print(e*f/2)
elif "s" ==inp:
    a=float(input("podaj przyprostokatna trojkata "))
    b=float(input("podaj przyprostokatna trojakta "))
    c=float(input("podaj przeciwprostokatna trojakta "))
    print(a*a+b*b)
    print(c*c)
elif "t" ==inp:
    a=float(input("podaj bok kwadratu "))
    print(a*math.sqrt(2))
elif "u" ==inp:
    a=float(input("podaj bok trojkata rownobocznego "))
    print((a*math.sqrt(3))/2)
elif "x" ==inp:
    a=float(input("podaj krawedz szescianu "))
    print(6*a*a)
elif "y" ==inp:
    a=float(input("podaj krawedz szescianu "))
    print(a*a*a)
elif "z" ==inp:
    a=float(input("podaj 1 krawedz prostopadloscianu "))
    b=float(input("podaj 2 krawedz prostopadloscianu "))
    c=float(input("podaj 3 krawedz prostopadloscianu "))
    print(2*a*b+2*a*c+2*b*c)
elif "aa" ==inp:
    a=float(input("podaj 1 krawedz prostopadloscianu "))
    b=float(input("podaj 2 krawedz prostopadloscianu "))
    c=float(input("podaj 3 krawedz prostopadloscianu "))
    print(a*b*c)
elif "af" == inp:
    r=float(input("podaj promien "))
    h=float(input("podaj wysokosc walca"))
    print(2*PI*r*r+2*PI*r*h)
elif "ag" ==inp:
    r=float(input("podaj promien "))
    h=float(input("podaj wysokosc walca "))
    print(PI*r*r*h)
elif "ah" ==inp:
    r=float(input("podaj promien "))
    l=float(input("podaj pole powierzchni bocznej stozka "))
    print(PI*r*r+PI*r*l)
elif "ai" ==inp:
    r=float(input("podaj promien "))
    h=float(input("podaj wysokosc stozka "))
    print(1/3*PI*r*r*h)
elif "aj" ==inp:
    r=float(input("podaj promien "))
    print(4*PI*r*r)
elif "aj" ==inp:
    r=float(input("podaj promien "))
    print(4/3*PI*r*r*r)
elif "ab" ==inp:
    if "trojkat"==inp2:
        a=float(input("podaj dlugosc podstawy trojkata z podstawy "))
        b=float(input("podaj dlugosc 1 boku trojkata z podstawy "))
        c=float(input("podaj dlugosc 2 boku trojkata z podstawy "))
        ht=float(input("podaj wysokosc trojkata z podstawy "))
        h=float(input("podaj wysokosc graniastoslupa "))
        print(2*(a*ht/2)+h*(a+b+c))
    elif "trojkatrow"==inp2:
        a=float(input("podaj dlugosc podstawy trojkata z podstawy "))
        h=float(input("podaj wysokosc graniastoslupa "))
        print(2*((a*math.sqrt(3))/2)+3*h*a)
    elif "kwadrat"==inp2:
        a=float(input("podaj dlugosc krawedzi kwadratu z podstawy "))
        h=float(input("podaj wysokosc graniastoslupa "))
        print(2*(a*a)+h*(a+a+a+a))
    elif "prostokat"==inp2:
        a=float(input("podaj dlugosc 1 boku z podstawy "))
        b=float(input("podaj dlugosc 2 boku z podstawy "))
        h=float(input("podaj wysokosc graniastoslupa "))
        print(2*(a*b)+h*(a+a+b+b))
    elif "rownoleglobok"==inp2:
        a=float(input("podaj dlugosc dluzszego boku  podstawy "))
        b=float(input("podaj dlugosc 2 boku podstawy "))
        h=float(input("podaj wysokosc graniastoslupa "))
        ht=float(input("podaj wysokosc rownolegloboku"))
        print(2*(a*ht)+h*(a+a+b+b))
    elif "trapez"==inp2:
        a=float(input("podaj dlugosc 1 boku z podstawy "))
        b=float(input("podaj dlugosc 2 boku z podstawy "))
        c=float(input("podaj dlugosc 1 ramienia "))
        d=float(input("podaj dlugosc 2 ramienia"))
        ht=float(input("podaj wysokosc trapezu z podstawy "))
        h=float(input("podaj wysokosc graniastoslupa "))
        print(2*((a+b)*h/2)+h*(a+b+c+d))
    elif "rombprzekatna"==inp2:
        d1=float(input("podaj dlugosc podstawy trojkata z podstawy "))
        d2=float(input("podaj dlugosc 1 boku trojkata z podstawy "))
        h=float(input("podaj wysokosc graniastoslupa "))
        print(d1*d2/2*2+4*(math.squrt((d1/2)**2+(d2/2)**2))*h)
    elif "rombwysokasc"==inp2:
        a=float(input("podaj dlugosc bok rombu z podstawy "))
        hr=float(input("podaj wysokosc rombu z podstawy "))
        h=float(input("podaj wysokosc graniastoslupa "))
        print(2*(a*hr)+4*a*h)
elif "ac" ==inp:
    if "trojkat"==inp2:
        a=float(input("podaj dlugosc podstawy trojkata z podstawy "))
        ht=float(input("podaj wysokosc trojkata z podstawy "))
        h=float(input("podaj wysokosc graniastoslupa "))
        print((a*ht/2)*h)
    elif "trojkatrow"==inp2:
        a=float(input("podaj dlugosc podstawy trojkata z podstawy "))
        h=float(input("podaj wysokosc graniastoslupa "))
        print(((a*math.sqrt(3))/2)*h)
    elif "kwadrat"==inp2:
        a=float(input("podaj dlugosc krawedzi kwadratu z podstawy "))
        h=float(input("podaj wysokosc graniastoslupa "))
        print((a*a)*h)
    elif "prostokat"==inp2:
        a=float(input("podaj dlugosc 1 boku z podstawy "))
        b=float(input("podaj dlugosc 2 boku z podstawy "))
        h=float(input("podaj wysokosc graniastoslupa "))
        print((a*b)*h)
    elif "rownoleglobok"==inp2:
        a=float(input("podaj dlugosc dluzszego boku  podstawy "))
        h=float(input("podaj wysokosc graniastoslupa "))
        ht=float(input("podaj wysokosc rownolegloboku"))
        print((a*ht)*h)
    elif "trapez"==inp2:
        a=float(input("podaj dlugosc 1 boku z podstawy "))
        b=float(input("podaj dlugosc 2 boku z podstawy "))
        ht=float(input("podaj wysokosc trapezu z podstawy "))
        h=float(input("podaj wysokosc graniastoslupa "))
        print(((a+b)*h/2)*h)
    elif "rombprzekatna"==inp2:
        d1=float(input("podaj dlugosc podstawy trojkata z podstawy "))
        d2=float(input("podaj dlugosc 1 boku trojkata z podstawy "))
        h=float(input("podaj wysokosc graniastoslupa "))
        print(d1*d2/2*h)
    elif "rombwysokasc"==inp2:
        a=float(input("podaj dlugosc bok rombu z podstawy "))
        hr=float(input("podaj wysokosc rombu z podstawy "))
        h=float(input("podaj wysokosc graniastoslupa "))
        print((a*hr)*h)
elif "ad" ==inp:
    if "trojkat"==inp2:
        a=float(input("podaj dlugosc podstawy trojkata z podstawy "))
        b=float(input("podaj dlugosc 1 boku trojkata z podstawy "))
        c=float(input("podaj dlugosc 2 boku trojkata z podstawy "))
        ht=float(input("podaj wysokosc trojkata z podstawy "))
        hs=float(input("podaj wysokosc sciany ostroslupa "))
        print((a*ht/2)+(a*hs/2+b*hs/2+c*hs/2))
    elif "trojkatrow"==inp2:
        a=float(input("podaj dlugosc podstawy trojkata z podstawy "))
        h=float(input("podaj wysokosc ostroslupa "))
        hs=float(input("podaj wysokosc sciany ostroslupa "))
        print(((a*math.sqrt(3))/4)+3*(a*hs/2))
    elif "kwadrat"==inp2:
        a=float(input("podaj dlugosc krawedzi kwadratu z podstawy "))
        h=float(input("podaj wysokosc ostroslupa "))
        hs=float(input("podaj wysokosc sciany ostroslupa "))
        print((a*a)+4*(hs*a/2))
    elif "prostokat"==inp2:
        a=float(input("podaj dlugosc 1 boku z podstawy "))
        b=float(input("podaj dlugosc 2 boku z podstawy "))
        h=float(input("podaj wysokosc ostroslupa "))
        hs=float(input("podaj wysokosc sciany ostroslupa "))
        print((a*b)+2*(hs*a/2)+2*(hs*b/2))
    elif "rownoleglobok"==inp2:
        a=float(input("podaj dlugosc dluzszego boku  podstawy "))
        b=float(input("podaj dlugosc 2 boku podstawy "))
        h=float(input("podaj wysokosc ostroslupa "))
        ht=float(input("podaj wysokosc rownolegloboku"))
        hs=float(input("podaj wysokosc sciany ostroslupa "))
        print((a*ht)+2*(hs*a/2)+2*(hs*b/2))
    elif "trapez"==inp2:
        a=float(input("podaj dlugosc 1 boku z podstawy "))
        b=float(input("podaj dlugosc 2 boku z podstawy "))
        c=float(input("podaj dlugosc 1 ramienia "))
        d=float(input("podaj dlugosc 2 ramienia"))
        ht=float(input("podaj wysokosc trapezu z podstawy "))
        h=float(input("podaj wysokosc ostroslupa "))
        hs=float(input("podaj wysokosc sciany ostroslupa "))
        print(((a+b)*h/2)(hs*a/2)+(hs*b/2)+(hs*c/2)+(hs*d/2)) 
    elif "rombprzekatna"==inp2:
        d1=float(input("podaj dlugosc podstawy trojkata z podstawy "))
        d2=float(input("podaj dlugosc 1 boku trojkata z podstawy "))
        h=float(input("podaj wysokosc ostroslupa "))
        hs=float(input("podaj wysokosc sciany ostroslupa "))
        print(d1*d2/2*2+4*(math.squrt((d1/2)**2+(d2/2)**2)*hs/2))
    elif "rombwysokasc"==inp2:
        a=float(input("podaj dlugosc bok rombu z podstawy "))
        hr=float(input("podaj wysokosc rombu z podstawy "))
        h=float(input("podaj wysokosc ostroslupa "))
        hs=float(input("podaj wysokosc sciany ostroslupa "))
        print((a*hr)+4*(a*hs/2))
elif "ae" ==inp:
    if "trojkat"==inp2:
        a=float(input("podaj dlugosc podstawy trojkata z podstawy "))
        ht=float(input("podaj wysokosc trojkata z podstawy "))
        h=float(input("podaj wysokosc ostroslupa "))
        print((a*ht/2)*h/3)
    elif "trojkatrow"==inp2:
        a=float(input("podaj dlugosc podstawy trojkata z podstawy "))
        h=float(input("podaj wysokosc ostroslupa "))
        print(((a*math.sqrt(3))/4)*h/3)
    elif "kwadrat"==inp2:
        a=float(input("podaj dlugosc krawedzi kwadratu z podstawy "))
        h=float(input("podaj wysokosc ostroslupa "))
        print((a*a)*h/3)
    elif "prostokat"==inp2:
        a=float(input("podaj dlugosc 1 boku z podstawy "))
        b=float(input("podaj dlugosc 2 boku z podstawy "))
        h=float(input("podaj wysokosc ostroslupa "))
        print((a*b)*h/3)
    elif "rownoleglobok"==inp2:
        a=float(input("podaj dlugosc dluzszego boku  podstawy "))
        h=float(input("podaj wysokosc ostroslupa "))
        ht=float(input("podaj wysokosc rownolegloboku"))
        print((a*ht)*h/3)
    elif "trapez"==inp2:
        a=float(input("podaj dlugosc 1 boku z podstawy "))
        b=float(input("podaj dlugosc 2 boku z podstawy "))
        ht=float(input("podaj wysokosc trapezu z podstawy "))
        h=float(input("podaj wysokosc ostroslupa "))
        print(((a+b)*h/2)*h/3)
    elif "rombprzekatna"==inp2:
        d1=float(input("podaj dlugosc podstawy trojkata z podstawy "))
        d2=float(input("podaj dlugosc 1 boku trojkata z podstawy "))
        h=float(input("podaj wysokosc ostroslupa "))
        print(d1*d2/2*h/3)
    elif "rombwysokasc"==inp2:
        a=float(input("podaj dlugosc bok rombu z podstawy "))
        hr=float(input("podaj wysokosc rombu z podstawy "))
        h=float(input("podaj wysokosc ostroslupa "))
        print((a*hr)*h/3)
else:
    print("nie ma")

          