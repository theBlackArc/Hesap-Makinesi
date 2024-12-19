import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Hesap Makinesi")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        carpma=tk.Button(root)
        carpma["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        carpma["font"] = ft
        carpma["fg"] = "#000000"
        carpma["justify"] = "center"
        carpma["text"] = "x"
        carpma.place(x=270,y=380,width=70,height=25)
        carpma["command"] = self.GButton_699_command

        cikarma=tk.Button(root)
        cikarma["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        cikarma["font"] = ft
        cikarma["fg"] = "#000000"
        cikarma["justify"] = "center"
        cikarma["text"] = "-"
        cikarma.place(x=190,y=380,width=70,height=25)
        cikarma["command"] = self.GButton_416_command

        toplama=tk.Button(root)
        toplama["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        toplama["font"] = ft
        toplama["fg"] = "#000000"
        toplama["justify"] = "center"
        toplama["text"] = "+"
        toplama.place(x=110,y=380,width=70,height=25)
        toplama["command"] = self.GButton_579_command

        bolme=tk.Button(root)
        bolme["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        bolme["font"] = ft
        bolme["fg"] = "#000000"
        bolme["justify"] = "center"
        bolme["text"] = "/"
        bolme.place(x=350,y=380,width=70,height=25)
        bolme["command"] = self.GButton_271_command

        GLineEdit_201=tk.Entry(root)
        GLineEdit_201["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_201["font"] = ft
        GLineEdit_201["fg"] = "#333333"
        GLineEdit_201["justify"] = "center"
        GLineEdit_201["text"] = "Entry"
        GLineEdit_201.place(x=350,y=190,width=70,height=25)

        GLineEdit_698=tk.Entry(root)
        GLineEdit_698["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_698["font"] = ft
        GLineEdit_698["fg"] = "#333333"
        GLineEdit_698["justify"] = "center"
        GLineEdit_698["text"] = "Entry"
        GLineEdit_698.place(x=120,y=190,width=70,height=25)

        GLineEdit_189=tk.Entry(root)
        GLineEdit_189["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_189["font"] = ft
        GLineEdit_189["fg"] = "#333333"
        GLineEdit_189["justify"] = "center"
        GLineEdit_189["text"] = "Entry"
        GLineEdit_189.place(x=220,y=190,width=70,height=25)

    def GButton_699_command(self):
        print("buton3'e basıldı")


    def GButton_416_command(self):
        print("buton2'ye basıldı")


    def GButton_579_command(self):
        print("buton1'e basıldı")


    def GButton_271_command(self):
        print("buton4'e basıldı")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)

    textBoxYazilanlar1=tk.StringVar #değişken tanımlama
    textBoxYazilanlar2=tk.StringVar #değişken tanımlama
    textBoxYazilanlar3=tk.StringVar #değişken tanımlama
    root.mainloop()
