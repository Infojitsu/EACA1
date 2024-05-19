import customtkinter, cmath, math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
import numpy as np

"""
PROIECT REALIZAT DE :
- Asoltanei Șerban
- Rotaru Denis
- Voinea Alexandru
"""


customtkinter.set_appearance_mode("System")  # Dark / Light cum e si Windows-ul
customtkinter.set_default_color_theme("blue")  # Tema de culoare

app = customtkinter.CTk()  # Creez fereastra CTk
app.geometry("1000x600")

tabview = customtkinter.CTkTabview(app, width=900, height= 500)
tabview.place(relx = 0.5, rely = 0.5, anchor = customtkinter.CENTER)

tab1 = tabview.add("Calculare")  # Adaug un tab
tabview.set("Calculare")  # Setez tab-ul vizibil


"""
Rezolvare directa pe tab1
"""

a = customtkinter.CTkEntry(master=tab1,
                               placeholder_text="Valoarea lui a",
                               width=120,
                               height=25,
                               border_width=2,
                               corner_radius=10)
a.place(relx=0.24, rely=0.2, anchor=customtkinter.E)

b = customtkinter.CTkEntry(master=tab1,
                               placeholder_text="Valoarea lui b",
                               width=120,
                               height=25,
                               border_width=2,
                               corner_radius=10)
b.place(relx=0.24, rely=0.4, anchor=customtkinter.E)

c = customtkinter.CTkEntry(master=tab1,
                               placeholder_text="Valoarea lui c",
                               width=120,
                               height=25,
                               border_width=2,
                               corner_radius=10)
c.place(relx=0.24, rely=0.6, anchor=customtkinter.E)

d = customtkinter.CTkEntry(master=tab1,
                               placeholder_text="Valoarea lui d",
                               width=120,
                               height=25,
                               border_width=2,
                               corner_radius=10)
d.place(relx=0.24, rely=0.8, anchor=customtkinter.E)

label_a = customtkinter.CTkLabel(master = tab1, text = "Coeficientul a :")
label_a.place(relx = 0.1, rely = 0.2, anchor = customtkinter.E)

label_b = customtkinter.CTkLabel(master = tab1, text = "Coeficientul b :")
label_b.place(relx = 0.1, rely = 0.4, anchor = customtkinter.E)

label_c = customtkinter.CTkLabel(master = tab1, text = "Coeficientul c :")
label_c.place(relx = 0.1, rely = 0.6, anchor = customtkinter.E)

label_d = customtkinter.CTkLabel(master = tab1, text = "Coeficientul d :")
label_d.place(relx = 0.1, rely = 0.8, anchor = customtkinter.E)

label_rezultat = customtkinter.CTkLabel(master = tab1, text = '')
label_rezultat.place(relx = 0.7, rely = 0.5, anchor = customtkinter.CENTER)

def ComplexToString(z):
    x = round(z.real, 3)
    y = round(z.imag, 3)
    if y == 0:
        return f"{x:g}"
    if x == 0:
        return f"{y:g}j"
    return f"{x:g}{y:+g}j"

def RezolvareEcuatie(a, b, c, d):
    def Radix3(w):
        rho, theta = cmath.polar(w)
        return [cmath.rect(math.pow(rho, 1 / 3), (theta + 2 * k * math.pi) / 3) for k in range(3)]

    if a == 0:
        label_rezultat.configure(text="Eroare ! Coeficientul a este 0")
    assert a != 0
    p = c / a - b * b / (3.0 * a * a)
    q = 2.0 * b ** 3 / (27.0 * a ** 3) - b * c / (3.0 * a * a) + d / a
    Delta = q * q + 4.0 * p ** 3 / 27.0
    w = (-q + cmath.sqrt(Delta)) / 2
    # w = (-q - cmath.sqrt(Delta)) / 2
    lista = []
    for k, u in enumerate(Radix3(w)):
        z = u - p / (3 * u)
        z -= b / (3.0 * a)
        print(f"z{k} = {ComplexToString(z)}")
        lista.append(ComplexToString(z))

    return lista

def calculeaza():
    #print(f"Am apasat pe buton !  {a.get()} {b.get()} {c.get()} {d.get()}")

    if a.get() == "0":
        label_rezultat.configure(text = "Eroare ! Coeficientul a este 0 !")
    if "" in [a.get(), b.get(), c.get(), d.get()]:
        label_rezultat.configure(text="Eroare ! Completeaza toti coeficientii !")
    else:
        solutii = RezolvareEcuatie(complex(a.get()), complex(b.get()), complex(c.get()), complex(d.get()))
        label_rezultat.configure(text = f"Rezultatul ecuatiei ({a.get()})x^3 + ({b.get()})x^2 + ({c.get()})x + {d.get()} = 0 : \nz1 = {solutii[0]}, \nz2 = {solutii[1]}, \nz3 = {solutii[2]}")




button = customtkinter.CTkButton(master=tab1, text="Calculeaza", command=calculeaza)
button.place(relx=0.5, rely=0.9, anchor=customtkinter.S)



app.mainloop()
