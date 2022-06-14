# coding=utf-8

from tkinter import *
import unicodedata

root = Tk()


def remove_accents(b):
    normalized = unicodedata.normalize('NFKD', b)
    print(type(normalized))
    return ''.join([c for c in normalized if not unicodedata.combining(c)])


def click(event=None):
    send = 'Você: ' + a.get()
    text.insert(END, '\n' + send)
    b = a.get().lower()
    b = remove_accents(b)

    if b == 'oi':
        text.insert(END, '\n' + 'kcha,resposta : (Quem pode doar? digite 1) (Responsabilidade dos documentários? digite 2)  (Sobre doações? digite 3) (duvidas por email, telefone ou whatsapp? digite 4)')
    elif b == '1':
        text.insert(END, '\n' + 'kcha,resposta : Todos podem fazer doações de pix a alimentação, faça sua parte, doe ')
    elif b == '2':
        text.insert(END, '\n' + 'kcha,resposta : A responsabilidade dos documentários são das próprias ONGs que faz a divugação')
    elif b == '3':
        text.insert(END, '\n' + 'kcha,resposta : No final dos videos tem os canais de atedimentos para fazer sua doação')
    elif b == '4':
        text.insert(END, '\n' + 'kcha,resposta : E-mail = projetoKCharity@gmail.com                                              Telefone = (81)5555-5555                                                        Whatsapp = (81)99999-9999')
    else:
        text.insert(END, '\n' + 'kcha,resposta : Desculpe, ainda não conheço essa palavra, poderia digitar um OI?')
    a.delete(0, 'end')


text = Text(root, bg='white')
text.grid(row=0, column=0, columnspan=2)

a = Entry(root, width=40)

send = Button(root, text='Enviar', bg='white', width=20,
              command=click).grid(row=1, column=1)
a.grid(row=1, column=0)

root.title('projeto-KCharity chat')
root.bind('<Return>', click)
root.mainloop()
