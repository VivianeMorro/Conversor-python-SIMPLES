from tkinter import *
#import tkinter.ttk as ttk

janela = Tk()
janela.title("Conversor")

def celsiusParaF():
    if(entrada.get()).isnumeric():
        x = float(entrada.get())
        result = (x * 9 / 5) + 32
        lb2["text"] = result

    else:
        lb2["text"] = "Valores informados inválidos"
        lb2.place(x=75, y=205)

def fahrenheitParaC():
    if(entrada.get()).isnumeric():
        y = float(entrada.get())
        result = ((y - 32) * 5) / 9
        lb2["text"] = result

    else:
        lb2["text"] = "Valores informados inválidos"
        lb2.place(x=75, y=205)

def limpaTela():
    entrada.delete(0, END)
    entrada.delete(0, "a")


entrada = Entry(janela, width=20, bg="#DCDCE4")
entrada.place(x=90, y=50)

bt1 = Button(janela, width=20, text="Converter para Celsius", command=fahrenheitParaC, bg="#985F6F")
bt1.place(x=75, y=100)

bt2 = Button(janela, width=20, text="Converter para Fahrenheit", command=celsiusParaF, bg="#985F6F")
bt2.place(x=75, y=130)

bt3 = Button(janela, width=10,command=limpaTela,  text="Limpar tela", bg="#985F6F")
bt3.place(x=110, y=160)

lb1 = Label(janela, text="Conversor de temperatura Fahrenheit/Celsius", bg="#B4869F")
lb1.place(x=30, y=10)

lb2 = Label(janela, text="Resultado", bg="#B4869F")
lb2.place(x=120, y=205)

janela["bg"] = "#B4869F"




janela.geometry("300x250+800+200")
janela.mainloop()