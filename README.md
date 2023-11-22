# beadando
Himpelmann Előd MOZK2T
ez egy számoló gép amely képes egyszerűbb műveletek elvégzésére
__init__(self, master): Az osztály konstruktora, ami inicializálja az osztályt. A master paraméter egy Tkinter főablakot jelöl.
self.bevitel_valtozo = tk.StringVar():   Beviteli mező értékének tárolása
self.bevitel = ttk.Entry(master, textvariable=self.bevitel_valtozo, justify="right", font=('Arial', 14)): Beviteli mező megjelenítése
self.bevitel.grid(row=0, column=0, columnspan=4): Beviteli mező elhelyezkedése
gombok: Itt adtam meg hogy milyenek legyenek a gombok
for gomb in gombok: Kiválasztja a lenyomott gombot
a. Az if blokkok az egyes gombokhoz kapcsolódó különböző funkciókat állítják be.
b. A ttk.Button hozzáadja a gombot a főablakhoz a megfelelő funkcióval.
c. Az elrendezési paraméterek, gombok helye
app = tk.Tk(): Létrehozza a fő Tkinter ablakot.
calculator = Szamologep(app):   beállítja a számológép ablakát és gombjait
app.mainloop(): Elindítja a Tkinter eseményciklust, amely megjeleníti az ablakot és lehetővé teszi az események kezelését.
