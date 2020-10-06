import tkinter as tk
import random

def porownanie(event):
    i = 0
    ile_v = int(ile.get())
    maks_v = int(maks.get())
    if (ile_v>maks_v):
        err.configure(text="Błędne dane")
        err.grid(row=2)
    else:
        while i < ile_v:
            liczba = random.randint(1, maks_v)
            if liczby.count(liczba) == 0:
                liczby.append(liczba)
                i += 1
                continue
        err.destroy()
        tk.Label(w, text="Wytypuj " + str(ile_v) + " z " + str(maks_v) + " liczb: ").grid(row=2)
        podaj.configure(text="Podaj liczbę 1: ")
        print(liczby)
        podaj.grid(row=3, column=0)
        typ.grid(row=3, column=1)

def przypisanie(event, licznik_wrapper):
    typ_v = int(typ.get())
    ile_v = int(ile.get())
    maks_v = int(maks.get())
    if 0 < typ_v <= maks_v and licznik_wrapper[0] <= ile_v and typ_v not in typy:
        typy.add(typ_v)
        podaj1.destroy()
        podaj.configure(text="Podaj liczbę %s:" % (licznik_wrapper[0]+2))
        podaj.grid(row=3, column=0)
        licznik_wrapper[0] += 1
        if licznik_wrapper[0] == ile_v:
            podaj.destroy()
            typ.destroy()
            trafione = set(liczby) & typy
            if trafione:
                tk.Label(w, text="\nIlość trafień: %s" % len(trafione)).grid(row=4)
                tk.Label(w, text="Trafione liczby: %s" % (trafione)).grid(row=5)
            else:
                tk.Label(w, text="Brak trafień. Spróbuj jeszcze raz!").grid(row=4)


w = tk.Tk()

licznik = 0
licznik_wrapper = [licznik]

typy = set()
liczby = []

tk.Label(w, text="Podaj ilość typowanych liczb: ").grid(row=0, column=0)
tk.Label(w, text="Podaj maksymalną losowaną liczbę: ").grid(row=1, column=0)
err = tk.Label(w)
podaj1 = tk.Label(w)
podaj = tk.Label()

ile = tk.Entry(w)
ile.bind("<Return>")
ile.grid(row=0, column=1)

maks = tk.Entry(w)
maks.bind("<Return>", porownanie)
maks.grid(row=1, column=1)

typ = tk.Entry(w)
typ.bind("<Return>", lambda event: przypisanie(event, licznik_wrapper))



w.mainloop()
