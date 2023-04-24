from tkinter import *

# Importação da biblioteca para edeição de imagens
from PIL import Image, ImageTk
animal = Tk()
import subprocess

# Configurações da tela
animal.title("Dogin's")

animal.resizable(False, False)

width_screen = animal.winfo_screenwidth()
height_screen = animal.winfo_screenheight()

width = 900
height = 600


posx = (width_screen / 2) - (width / 2)
posy = (height_screen / 2) - (height / 2)

animal.maxsize(width, height)
animal.minsize(width, height)

animal.geometry("%dx%d+%d+%d" % (width, height, posx, posy))
animal.configure(bg='#fff')

#text "Cadastro do Cliente"
lbl_agradecimentos = Label(animal, text="Cadastro do Animal", bg="#FFF", font=("Helvetica 14 bold")).place(x=430, y=100)

# foto "logo"
fotoOriginal = Image.open("imgs/logo.png")
fotoResize = fotoOriginal.resize((150, 30))
fotoLogo = ImageTk.PhotoImage(fotoResize)
test = Label(animal, bg="#FFFFFF", image=fotoLogo).place(x=100, y=40)

#foto "perfil"
fotoOriginal = Image.open("imgs/perfil.png")
fotoResize = fotoOriginal.resize((130, 130))
fotoPerfil = ImageTk.PhotoImage(fotoResize)
Perfil = Label(animal, bg="#FFFFFF", image=fotoPerfil).place(x=100, y=150)

# botao voltar ao menu
def abrir_tela_menu():
    subprocess.run(["python", "menu.py"])
btn_menu = Button(animal, text="Voltar ao menu", bd=0, bg="#FFF", fg="#777777", font="Helvetica 10 underline", activebackground="#FFFFFF", activeforeground="#777", command=abrir_tela_menu)
btn_menu.place(x=700, y=40)

#text "Código de cadastro "
lbl_animal = Label(animal, bg="#FFF", text="Código de cadastro",font="Helvetica 10").place(x=310, y=150)
text_nome = Entry(animal, width=30).place(x=310, y=180)

#text "Peso"
lbl_Peso = Label(animal, bg="#FFF", text="Peso",font="Helvetica 10").place(x=530, y=150)
text_Peso = Entry(animal, width=30).place(x=530, y=180)

#text "Data de nascimento "
lbl_nasc = Label(animal, bg="#FFF", text="Data de nascimento",font="Helvetica 10").place(x=310, y=220)
text_nasc = Entry(animal, width=25).place(x=310, y=250)

#text "Idade "
lbl_idade = Label(animal, bg="#FFF", text="Idade",font="Helvetica 10").place(x=310, y=290) 
text_idade = Entry(animal, width=21).place(x=310, y=320)

# text " Esecie  "
lbl_dataNascimento = Label(animal, bg="#FFF", text="Especie",font="Helvetica 10").place(x=530, y=220)
text_dataNascimento = Entry(animal, width=25).place(x=530, y=240)

#text "Raça "
lbl_especie = Label(animal, bg="#FFF", text="Raça ",font="Helvetica 10").place(x=530, y=280)
text_especie = Entry(animal, width=25).place(x=530, y=310)

#text "Descrição"
txt_descricao = Label(animal,text="Descrição" ,bg = "#FFF", font=("Helvetica 10"))
txt_descricao.place(relx = .330, rely = .60)
lbl_descricao = Entry(animal)
lbl_descricao.place(relx = .540, rely = .65, anchor = "n" ,  width="400" , height="50")

# botao "Salvar", "Alterar", "Excluir"
btn_salvar = Button(animal, width=15, text="Salvar", activebackground="#76bce3", bd=0, bg="#85D3FF",compound=TOP).place(x=430, y=490)
btn_alterar = Button(animal, width=15, text="Alterar ", bg="#fff", bd=1,compound=TOP).place(x=550, y=490)
btn_excluir = Button(animal, width=15, text="Excluir ", bg="#fff", bd=1,compound=TOP).place(x=680, y=490)



animal.mainloop()