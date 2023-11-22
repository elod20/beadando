import tkinter as tk
from tkinter import ttk, messagebox
import math

class Szamologep:
    def __init__(self, master):
        self.master = master
        master.title("Gombvezérelt Számológép")

        self.bevitel_valtozo = tk.StringVar()
        self.bevitel = ttk.Entry(master, textvariable=self.bevitel_valtozo, justify="right", font=('Arial', 14))
        self.bevitel.grid(row=0, column=0, columnspan=4)

        gombok = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+',
            '^', '√', 'log', 'sin', 'cos'
        ]

        sor_ertek = 1
        oszlop_ertek = 0

        for gomb in gombok:
            if gomb == '^':
                ttk.Button(master, text=gomb, command=self.hatvanyozas).grid(row=sor_ertek, column=oszlop_ertek, ipadx=20, ipady=20)
            elif gomb == '√':
                ttk.Button(master, text=gomb, command=self.negyzetgyokvonas).grid(row=sor_ertek, column=oszlop_ertek, ipadx=20, ipady=20)
            elif gomb == 'log':
                ttk.Button(master, text=gomb, command=self.logaritmus).grid(row=sor_ertek, column=oszlop_ertek, ipadx=20, ipady=20)
            elif gomb == 'sin':
                ttk.Button(master, text=gomb, command=self.szinus).grid(row=sor_ertek, column=oszlop_ertek, ipadx=20, ipady=20)
            elif gomb == 'cos':
                ttk.Button(master, text=gomb, command=self.koszinusz).grid(row=sor_ertek, column=oszlop_ertek, ipadx=20, ipady=20)
            elif gomb == 'C':
                ttk.Button(master, text=gomb, command=self.bevitel_torlese).grid(row=sor_ertek, column=oszlop_ertek, ipadx=20, ipady=20)
            else:
                ttk.Button(master, text=gomb, command=lambda gomb=gomb: self.gomb_kattintas(gomb) if gomb != '=' else self.kiszamol() if gomb != 'C' else self.bevitel_torlese()).grid(row=sor_ertek, column=oszlop_ertek, ipadx=20, ipady=20)
            oszlop_ertek += 1
            if oszlop_ertek > 3:
                oszlop_ertek = 0
                sor_ertek += 1

    def gomb_kattintas(self, ertek):
        aktualis = self.bevitel_valtozo.get()
        self.bevitel_valtozo.set(aktualis + str(ertek))

    def bevitel_torlese(self):
        aktualis = self.bevitel_valtozo.get()
        self.bevitel_valtozo.set(aktualis[:-1])

    def kiszamol(self):
        try:
            eredmeny = eval(self.bevitel_valtozo.get())
            eredmeny_uzenet = f"Eredmény: {eredmeny}"
            messagebox.showinfo("Eredmény", eredmeny_uzenet)
            self.bevitel_valtozo.set(eredmeny)
        except Exception as e:
            messagebox.showerror("Hiba", "Hibás kifejezés")

    def hatvanyozas(self):
        aktualis = self.bevitel_valtozo.get()
        self.bevitel_valtozo.set(aktualis + '**')

    def negyzetgyokvonas(self):
        aktualis = self.bevitel_valtozo.get()
        self.bevitel_valtozo.set('math.sqrt(' + aktualis + ')')

    def logaritmus(self):
        aktualis = self.bevitel_valtozo.get()
        self.bevitel_valtozo.set('math.log(' + aktualis + ')')

    def szinus(self):
        aktualis = self.bevitel_valtozo.get()
        self.bevitel_valtozo.set('math.sin(math.radians(' + aktualis + '))')

    def koszinusz(self):
        aktualis = self.bevitel_valtozo.get()
        self.bevitel_valtozo.set('math.cos(math.radians(' + aktualis + '))')

app = tk.Tk()
calculator = Szamologep(app)
app.mainloop()
