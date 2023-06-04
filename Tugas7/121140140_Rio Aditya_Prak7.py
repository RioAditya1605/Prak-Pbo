from tkinter import *
from tkinter import messagebox

def jual():
    try:
        check = entry.get()
        if not check:
            raise ValueError('Masukkan Nilai Mata Uang')
        j = (float(entry.get()) / 14000)
        hasil.config(text='Nilai Jual : ' + str(j) + ' Dolar')
    except ValueError as err:
        messagebox.showerror('Error', str(err))

def beli():
    try:
        check = entry.get()
        if not check:
            raise ValueError('Masukkan Nilai Mata Uang')
        b = (float(entry.get()) * 13000)
        hasil.config(text='Nilai Beli : ' + str(b) + ' Rupiah')
    except ValueError as err:
        messagebox.showerror('Error', str(err))

window=Tk()
window.title('Kurs Jual Beli')
window.geometry('300x300')

label01 = Label(window, text='Masukan Jumlah Uang : ', font=('Arial', 11))
label01.pack()
entry = Entry(window)
entry.pack()
frame = Frame(window)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

tombol01 = Button(frame, text='Nilai Jual', font=('Arial', 11), command=jual)
tombol01.grid(row=1, column=0)
tombol02 = Button(frame, text='Nilai Beli', font=('Arial', 11), command=beli)
tombol02.grid(row=2, column=0)
frame.pack()

label02 = Label(window, text='Hasil : ', font=('Arial', 11))
label02.pack()

hasil = Label(window, font=('Arial', 11))
hasil.pack()
window.mainloop()