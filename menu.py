from tkinter import *

# Importação da biblioteca para edeição de imagens
from PIL import Image, ImageTk
menu = Tk()
import subprocess

#Configurações da tela
menu.title("Dogin's")

menu.resizable(False, False)

width_screen = menu.winfo_screenwidth()
height_screen = menu.winfo_screenheight()

width = 870
height = 500

posx = (width_screen / 2) - (width / 2)
posy = (height_screen / 2) - (height / 2)

menu.maxsize(width, height)
menu.minsize(width, height)

menu.geometry("%dx%d+%d+%d" % (width, height, posx, posy))
menu.configure(bg='#fff')

# foto "logo" e Label para guardar a imagem Logo
fotoOriginal = Image.open("imgs/logo.png")
fotoResize = fotoOriginal.resize((150, 30))
fotoLogo = ImageTk.PhotoImage(fotoResize)
test = Label(menu, bg="#FFFFFF", image=fotoLogo).place(x=80, y=30)

# escrita "Menu"
lbl_menu = Label(menu, text="Bem Vindo", bg="#FFF", font=(
    "Helvetica 14 bold")).place(relx=.45, rely=.200, anchor="center")
fotoOriginal = Image.open("imgs/coracao.png")
fotoResize = fotoOriginal.resize((15, 13))
fotoCoracao = ImageTk.PhotoImage(fotoResize)
coracao = Label(menu, bg="#FFF", image=fotoCoracao).place(relx=.53, rely=.200, anchor="e")

#barra de menu
largura = 1000
altura = 700

barra_menu = Menu(menu)

opcoes_menu_arquivo = Menu(barra_menu)
opcoes_menu_gestao = Menu(barra_menu)

barra_menu.add_cascade(label="Arquivo" , menu=opcoes_menu_arquivo)
barra_menu.add_cascade(label="Gestão" , menu=opcoes_menu_gestao)

opcoes_menu_arquivo.add_command(label="Abrir")
opcoes_menu_arquivo.add_command(label="Salvar")
opcoes_menu_arquivo.add_command(label="Salvar como ...")
opcoes_menu_arquivo.add_separator()
opcoes_menu_arquivo.add_command(label="Sair" , command=menu.quit)

opcoes_novo = Menu(opcoes_menu_arquivo)

opcoes_menu_arquivo.add_cascade(label="Novo" , menu=opcoes_novo)
opcoes_menu_arquivo.add_command(label="Abrir")


opcoes_novo.add_command(label="Salvar Imagem")
opcoes_novo.add_command(label="Upload Arquivos")

menu.config(menu=barra_menu)

foto_animais = PhotoImage(file =r"imgs/cadastro-ani.png")
foto_usuario = PhotoImage(file =r"imgs/cadastro-cli.png")
foto_serviços = PhotoImage(file =r"imgs/servicos.png")


btn_animais = Button(menu, text="Animais",image=foto_animais,compound = TOP).place(relx=.25 , rely=.30 , width="150" , height="150" )
btn_Clientes = Button(menu, text="Clientes",image=foto_usuario,compound = TOP).place(relx=.45 , rely=.30 ,width="150" , height="150" )
btn_Serviços = Button(menu, text="Serviços",image=foto_serviços,compound = TOP).place(relx=.65 , rely=.30, width="150" , height="150" )

def abrir_tela_animal():
    subprocess.run(["python", "animal.py"])
def abrir_tela_clientes():
    subprocess.run(["python", "clientes.py"])
def abrir_tela_servicos():
    subprocess.run(["python", "servicos.py"])
def abrir_tela_op():
    subprocess.run(["python", "operação-concluida.py"])
                    
opcoes_menu_gestao.add_command(label="Animais", command=abrir_tela_animal)
opcoes_menu_gestao.add_command(label="Clientes", command=abrir_tela_clientes)
opcoes_menu_gestao.add_command(label="Serviços", command=abrir_tela_servicos)
opcoes_menu_gestao.add_command(label="Operação concluida" , command=abrir_tela_op)


menu.title("Pet shop Dogin's")

menu.mainloop()