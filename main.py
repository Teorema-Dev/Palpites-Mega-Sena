import customtkinter
from customtkinter import *
from palpaites import sorteando

janela = customtkinter.CTk()
janela.title("Mega sena")
janela.geometry("230x210")
janela.resizable(width=False, height=False)


# Função de configuração do preenchimento das Entrys
def sortear():
    entry.delete(0, END)
    entry.insert(END, str(sorteando()).strip('[]').replace(',', ' -'))

    entry2.delete(0, END)
    entry2.insert(END, str(sorteando()).strip('[]').replace(',', ' -'))

    entry3.delete(0, END)
    entry3.insert(END, str(sorteando()).strip('[]').replace(',', ' -'))


# configuração de Label
label = customtkinter.CTkLabel(janela, text="Suas Dezenas", text_color="#0000FF")
label.place(relx=0.05, rely=0.01)

# Configuração de Botão
button = customtkinter.CTkButton(janela, command=sortear, height=20, width=60, text="Sortear")
button.place(relx=0.55, rely=0.70)

# Confguração de Entrys
entry = customtkinter.CTkEntry(janela, height=20, width=150, placeholder_text="00 - 00 - 00 - 00 - 00 - 00")
entry.place(relx=0.17, rely=0.20)

entry2 = customtkinter.CTkEntry(janela, height=20, width=150, placeholder_text="00 - 00 - 00 - 00 - 00 - 00")
entry2.place(relx=0.17, rely=0.35)

entry3 = customtkinter.CTkEntry(janela, height=20, width=150, placeholder_text="00 - 00 - 00 - 00 - 00 - 00")
entry3.place(relx=0.17, rely=0.50)

janela.mainloop()
