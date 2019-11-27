from tkinter import *

root = Tk()
root.title('Colors')
root.iconbitmap('img/i.ico')
root.geometry('220x220+1500+200')

colors = {
    '#ff0000': 'Красный',
    '#ff7d00': 'Оранжевый',
    '#ffff00': 'Желтый',
    '#00ff00': 'Зеленый',
    '#007dff': 'Голубой',
    '#0000ff': 'Синий',
    '#7d00ff': 'Фиолетовый',
}


class Buttons:
    def __init__(self, master, text_color, hex_color):
        self.text_color = text_color
        self.hex_color = hex_color
        self.btn = Button(root, bg=hex_color, command=self.get_color)
        self.btn.pack(fill=X)

    def  get_color(self):
        lbl['text'] = self.text_color
        ent.delete(0, END)
        ent.insert(0, self.hex_color)


lbl = Label(root)
ent = Entry(root, width=30, justify=CENTER)
lbl.pack()
ent.pack()

for code, color in colors.items():
    Buttons(root, color, code)


root.mainloop()