import tkinter as tk
import numpy as np
import matplotlib.pyplot as plot
import json

from tkinter import *

class na_dane_wykladnicza(Toplevel):
    def __init__(self, master = None):
        super().__init__(master = master)
        self.title("Na dane")
        self.geometry("250x200")

        tekst_A = Label(self, text = "Podaj a")
        tekst_A.pack()

        wspolczynnik_a = Entry(self)
        wspolczynnik_a.pack(pady=30)

        def drukujWartosc_dla_A():
            global zmienna_A
            A = wspolczynnik_a.get()
            zmienna_A = float(A)
            print(zmienna_A)

        Button(
            self,
            text="Zatwierdz",
            padx=10,
            pady=5,
            command=drukujWartosc_dla_A
        ).pack()

        button1 = tk.Button(self, text='Rysuj!', width=25, command=self.new_window)
        button1.place(x=35, y=150)

    def close_windows(self):
        self.master.destroy()

    def new_window(self):
        self.newWindow = tk.Toplevel.iconify(self.master)
        self.app = wykladnicza(self.newWindow)


class wykladnicza(na_dane_wykladnicza):
    def __init__(self, master):

        x = np.linspace(-2, 2, 50)

        y = zmienna_A**x

        fig = plot.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')

        plot.plot(x, y, 'y', label='y=e^x')

        plot.grid()
        plot.show()

    def close_windows(self):
        self.master.destroy()

'''
TUTAJ JEST PULSACYJNA
'''
class na_dane_pulsacyjna(Toplevel):

    def __init__(self, master = None):
        super().__init__(master = master)
        self.title("Na dane")

        sizex = 600
        sizey = 400
        posx = 0
        posy = 0
        self.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

        labels = []

        def myClick():

            del labels[:]  # usuwa poprzednie jakiekolwiek labele jesli byly w ogole wczesniej

            moja_lista = []
            def get_info():
                i: Entry
                lista = []
                for i in moja_lista:
                    x = i.get()
                    lista.append(x)

                n = 1
                nowa_lista = [lista[i:i + n] for i in range(0, len(lista), n)]

                translation = {39: None}
                NIEPoprawnaLista = str(nowa_lista).translate(translation)

                global res
                res = json.loads(NIEPoprawnaLista)
                print(res)

            myframe = Frame(self, width=400, height=380, bd=2, relief=GROOVE)
            myframe.place(x=10, y=10)
            x = myvalue.get()
            value = int(x)

            for i in range(value):
                labels.append(Label(myframe, text=" Współrzędna " + str(i+1)))
                labels[i].place(x=10, y=10 + (30 * i))
                wejscie = Entry(myframe, width=12)
                wejscie.place(x=110, y=10 + (30 * i))
                moja_lista.append(wejscie)

            ZapytajOIloscFunkcjiDoNarysowania = Label(self, text="Ile razy chcesz narysowac funkcje?")
            ZapytajOIloscFunkcjiDoNarysowania.place(x=410, y=70)

            global WartoscIloscFunkcjiDoWpisania
            WartoscIloscFunkcjiDoWpisania = Entry(self, width=12)
            WartoscIloscFunkcjiDoWpisania.place(x=420, y=100)

            def FunkcjaTestowa():
                print(WartoscIloscFunkcjiDoWpisania.get())

            mybutton2 = Button(self, text="Ok", command=FunkcjaTestowa)
            mybutton2.place(x=505, y=95)

            PrzyciskPotwierdzeniaDanych = Button(self, text="Zatwierdź wpisane dane", command=get_info)
            PrzyciskPotwierdzeniaDanych.place(x=430, y=130)

            rysuj = Button(self, text="Rysuj", bg='yellow', command=self.new_window)
            rysuj.place(x=505, y=170)

        zapytaj = Label(self, text = "Ile chcesz podac współrzędnych?")
        zapytaj.place(x=410, y=20)

        mybutton = Button(self, text="Ok", command=myClick)
        mybutton.place(x=505, y=40)

        myvalue = Entry(self, width=12)
        myvalue.place(x=420, y=42)

    def close_windows(self):
        self.master.destroy()

    def new_window(self):
        self.newWindow = tk.Toplevel.iconify(self.master)
        self.app = pulsacyjna(self.newWindow)

class pulsacyjna(na_dane_pulsacyjna):
    def __init__(self, master):

        data = (res)

        posortowana_lista = sorted(data, key=lambda x: [x[0], x[1]])
        print(posortowana_lista)

        posortowana_numpy = np.asarray(posortowana_lista)

        print(posortowana_numpy)
        print(type(posortowana_numpy))

        x, y = posortowana_numpy.T
        plot.scatter(x, y)
        plot.plot(x, y)
        #TODO: dziala, ale naprawic

        print(WartoscIloscFunkcjiDoWpisania.get())
        plot.plot(x+9, y)
        plot.plot(x + 18, y)
        plot.grid()
        plot.show()

    def close_windows(self):
        self.master.destroy()


class na_dane_jednostkowo_liniowa(Toplevel):

    def __init__(self, master = None):
        super().__init__(master = master)
        self.title("Na dane")

        sizex = 600
        sizey = 400
        posx = 0
        posy = 0
        self.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

        labels = []

        def myClick():

            del labels[:]  # usuwa poprzednie jakiekolwiek labele jesli byly w ogole wczesniej

            moja_lista = []
            def get_info():
                i: Entry
                lista = []
                for i in moja_lista:
                    x = i.get()
                    lista.append(x)

                n = 1
                nowa_lista = [lista[i:i + n] for i in range(0, len(lista), n)]

                translation = {39: None}
                NIEPoprawnaLista = str(nowa_lista).translate(translation)

                global res
                res = json.loads(NIEPoprawnaLista)
                print(res)


            myframe = Frame(self, width=400, height=380, bd=2, relief=GROOVE)
            myframe.place(x=10, y=10)
            x = myvalue.get()
            value = int(x)

            for i in range(value):
                labels.append(Label(myframe, text=" Współrzędna " + str(i+1)))
                labels[i].place(x=10, y=10 + (30 * i))
                wejscie = Entry(myframe, width=12)
                wejscie.place(x=110, y=10 + (30 * i))
                moja_lista.append(wejscie)

            mybutton2 = Button(self, text="Zatwierdź wpisane współrzędne", command=get_info)
            mybutton2.place(x=415, y=80)

            rysuj = Button(self, text="Rysuj", bg='yellow', command=self.new_window)
            rysuj.place(x=505, y=250)


        zapytaj = Label(self, text = "Ile chcesz podac współrzędnych?")
        zapytaj.place(x=410, y=10)

        mybutton = Button(self, text="Ok", command=myClick)
        mybutton.place(x=505, y=40)

        myvalue = Entry(self, width=12)
        myvalue.place(x=420, y=42)

    def close_windows(self):
        self.master.destroy()

    def new_window(self):
        self.newWindow = tk.Toplevel.iconify(self.master)
        self.app = jednostkowo_liniowa(self.newWindow)

class jednostkowo_liniowa(na_dane_jednostkowo_liniowa):
    def __init__(self, master):

        data = (res)

        posortowana_lista = sorted(data, key=lambda x: [x[0], x[1]])
        print(posortowana_lista)

        posortowana_numpy = np.asarray(posortowana_lista)

        print(posortowana_numpy)

        x, y = posortowana_numpy.T
        plot.scatter(x, y)
        plot.plot(x, y)
        plot.grid()
        plot.show()

    def close_windows(self):
        self.master.destroy()

class na_dane_sin(Toplevel):
    def __init__(self, master = None):
        super().__init__(master = master)
        self.title("Na dane Sinusa")
        self.geometry("250x500")

        tekst_X = Label(self, text = "Podaj y0")
        tekst_X.pack()

        wspolrzedna_x = Entry(self)
        wspolrzedna_x.pack(pady=30)

        def drukujWartosc_dla_X():
            global zmienna_X
            X = wspolrzedna_x.get()
            zmienna_X = float(X)
            print(zmienna_X)

        Button(
            self,
            text="Zatwierdz",
            padx=10,
            pady=5,
            command=drukujWartosc_dla_X
        ).pack()

        tekst_Y = Label(self, text = "Podaj yu")
        tekst_Y.pack()

        wspolrzedna_y = Entry(self)
        wspolrzedna_y.pack(pady=30)

        def drukujWartosc_dla_Y():
            global zmienna_Y
            Y = wspolrzedna_y.get()
            zmienna_Y = float(Y)
            print(zmienna_Y)

        Button(
            self,
            text="Zatwierdz",
            padx=10,
            pady=5,
            command=drukujWartosc_dla_Y
        ).pack()

        tekst_Z = Label(self, text = "Podaj f")
        tekst_Z.pack()

        wspolrzedna_z = Entry(self)
        wspolrzedna_z.pack(pady=30)

        def drukujWartosc_dla_Z():
            global zmienna_Z
            Z = wspolrzedna_z.get()
            zmienna_Z = float(Z)
            print(zmienna_Z)

        Button(
            self,
            text="Zatwierdz",
            padx=10,
            pady=5,
            command=drukujWartosc_dla_Z
        ).pack()

        button1 = tk.Button(self, text = 'Rysuj!', width = 25, command = self.new_window)
        button1.place(x=35, y=435)

    def close_windows(self):
        self.master.destroy()

    def new_window(self):
        self.newWindow = tk.Toplevel.iconify(self.master)
        self.app = sinus(self.newWindow)


class sinus(na_dane_sin):
    def __init__(self, master):

        time = np.arange(zmienna_X, zmienna_Y, zmienna_Z);

        amplitude = np.sin(time)
        plot.plot(time, amplitude)
        plot.title('Wykres sinusa')
        plot.xlabel('Time')
        plot.ylabel('Amplitude = sin(time)')
        plot.grid(True, which='both')
        plot.axhline(y=0, color='k')
        plot.show()
        plot.show()

    def close_windows(self):
        self.master.destroy()

class menu():
    def __init__(self, master):
        self.master = master

        przycisk_Jednostkowo_Liniowa = tk.Button(
            text="Funkcja jednostkowo-liniowa",
            width=250,
            height=2,
            bg="blue",
            fg="yellow"
        )

        przycisk_Jednostkowo_Liniowa.bind("<Button>", lambda e: na_dane_jednostkowo_liniowa(master))
        przycisk_Jednostkowo_Liniowa.pack()

        przycisk_Sinusoidalna = tk.Button(
            text="Funkcja sinusoidalna",
            width=250,
            height=2,
            bg="blue",
            fg="yellow"
        )

        przycisk_Sinusoidalna.bind("<Button>", lambda e: na_dane_sin(master))
        przycisk_Sinusoidalna.pack()

        przycisk_Pulsacyjna = tk.Button(
            text="Funkcja pulsacyjna",
            width=250,
            height=2,
            bg="blue",
            fg="yellow"
        )

        przycisk_Pulsacyjna.bind("<Button>", lambda e: na_dane_pulsacyjna(master))
        przycisk_Pulsacyjna.pack()

        przycisk_Wykladnicza = tk.Button(
            text="Funkcja wykladnicza",
            width=250,
            height =2,
            bg="blue",
            fg="yellow"
        )

        przycisk_Wykladnicza.bind("<Button>", lambda e: na_dane_wykladnicza(master))
        przycisk_Wykladnicza.pack()

        def komunikatAutorzy():
            tk.messagebox.showinfo("Autor", "Autor programu: Oliwier Piasecki")

        przycisk_Tworcy = tk.Button(
            text="Autor programu",
            width=250,
            height=2,
            bg="red",
            fg="yellow",
            command=komunikatAutorzy
        ).pack()


def main():
    root = tk.Tk()
    root.geometry("250x200")
    root.title("Program")
    root['bg'] = '#FFFFFF'
    app = menu(root)
    root.mainloop()

if __name__ == '__main__':
    main()