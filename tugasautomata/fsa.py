import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo




class VendingMachine:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg='tomato')
        self.root.title("Vending Machine")
        self.root.geometry("800x1200")
        self.root.resizable(False,False)
        
        
        
        
        self.balance = 0
        self.cocacola = 10000
        self.fanta = 10000
        self.pepsi = 7000
        self.aqua = 5000
        self.tebs = 8000
        self.sprite = 9000
        
        self.label_items = tk.Label(self.root, text="Vending Machine FSA Output",font=("Times New Roman", 22, "normal"),bg='tomato')
        self.label_items.pack()
        
        self.label_items = tk.Label(self.root, text="Menggunakan Bahasa Python Dengan Library Tkinter",font=("Times New Roman", 22, "normal"),bg='tomato')
        self.label_items.pack()

        self.frame_items = tk.Frame(self.root, bg='tomato')
        self.frame_items.pack()
        
        self.cocacolagambar = PhotoImage(file="cocacola.png")
        self.cocacolalabel = Label(image=self.cocacolagambar, borderwidth=0)
        self.cocacolalabel.pack()
        self.cocacolalabel.place(x=100, y=175)
        self.cocacolainfo = Label(text="Cocacola\nRp 10000", font=("Times New Roman", 12, "normal"), bg='tomato')
        self.cocacolainfo.pack()
        self.cocacolainfo.place(x=152, y=353)
        self.buttoncocacola = tk.Button(text="Beli", width=10 , command=self.select_itemcocacola)
        self.buttoncocacola.pack(padx=40, pady=20)
        self.buttoncocacola.place(x=145, y=403)
        
        self.fantagambar = PhotoImage(file="fanta.png")
        self.fantalabel = Label(image=self.fantagambar, borderwidth=0)
        self.fantalabel.pack()
        self.fantalabel.place(x=315, y=175)
        self.fantainfo = Label(text="Fanta\nRp 10000", font=("Times New Roman", 12, "normal"),bg='tomato')
        self.fantainfo.pack()
        self.fantainfo.place(x=367, y=353)
        self.buttonfanta = tk.Button(text="Beli", width=10 , command=self.select_itemfanta)
        self.buttonfanta.pack(padx=40, pady=20)
        self.buttonfanta.place(x=358, y=403)
        
        self.pepsigambar = PhotoImage(file="pepsi.png")
        self.pepsilabel = Label(image=self.pepsigambar, borderwidth=0)
        self.pepsilabel.pack()
        self.pepsilabel.place(x=530, y=175)
        self.pepsiinfo = Label(text="Pepsi\nRp 7000", font=("Times New Roman", 12, "normal"),bg='tomato')
        self.pepsiinfo.pack()
        self.pepsiinfo.place(x=585, y=353)
        self.buttonpepsi = tk.Button(text="Beli", width=10 , command=self.select_itempepsi)
        self.buttonpepsi.pack(padx=40, pady=20)
        self.buttonpepsi.place(x=575, y=403)
        
        self.aquagambar = PhotoImage(file="aqua.png")
        self.aqualabel = Label(image=self.aquagambar, borderwidth=0)
        self.aqualabel.pack()
        self.aqualabel.place(x=100, y=475)
        self.aquainfo = Label(text="Aqua\nRp 5000", font=("Times New Roman", 12, "normal"),bg='tomato')
        self.aquainfo.pack()
        self.aquainfo.place(x=157, y=653)
        self.buttonaqua = tk.Button(text="Beli", width=10 , command=self.select_itemaqua)
        self.buttonaqua.pack(padx=40, pady=20)
        self.buttonaqua.place(x=145, y=703)
        
        self.tebsgambar = PhotoImage(file="tebs.png")
        self.tebslabel = Label(image=self.tebsgambar, borderwidth=0)
        self.tebslabel.pack()
        self.tebslabel.place(x=315, y=475)
        self.tebsinfo = Label(text="Tebs\nRp 8000", font=("Times New Roman", 12, "normal"),bg='tomato')
        self.tebsinfo.pack()
        self.tebsinfo.place(x=370, y=653)
        self.buttontebs = tk.Button(text="Beli", width=10 , command=self.select_itemtebs)
        self.buttontebs.pack(padx=40, pady=20)
        self.buttontebs.place(x=358, y=703)
        
        self.spritegambar = PhotoImage(file="sprite.png")
        self.spritelabel = Label(image=self.spritegambar, borderwidth=0)
        self.spritelabel.pack()
        self.spritelabel.place(x=530, y=475)
        self.spriteinfo = Label(text="Sprite\nRp 9000", font=("Times New Roman", 12, "normal"),bg='tomato')
        self.spriteinfo.pack()
        self.spriteinfo.place(x=587, y=653)
        self.buttonsprite = tk.Button(text="Beli", width=10 , command=self.select_itemsprite)
        self.buttonsprite.pack(padx=40, pady=20)
        self.buttonsprite.place(x=575, y=703)
        
        self.label_balance = tk.Label(self.root, text=f"Saldo saat ini: Rp {self.balance}",font=("Times New Roman", 16, "normal"), bg='tomato')
        self.label_balance.pack()
        
        
        
        
        
        self.frame_coins = tk.Frame(self.root,bg='tomato')
        self.frame_coins.pack()
        
        self.coins = {
            "5000": 5000,
            "10000": 10000,
            "20000": 20000,
            "50000": 50000,
            "100000": 100000,
        }

        for coin_value in self.coins.values():
            button = tk.Button(self.frame_coins, width=10, text=f"Rp{coin_value}", command=lambda value=coin_value: self.insert_coin(value))
            button.pack(side=tk.LEFT, padx=10, pady=20)
            
        
        
        
        
    def insert_coin(self, amount):
        self.balance += amount
        self.update_balance_label()
    
    def select_itemcocacola(self):
        if self.balance >= self.cocacola:
            self.balance -= self.cocacola
            self.update_balance_label()
            self.show_message(f"Pembelian Cocacola Berhasil!!\nMohon tunggu sebentar hingga minuman keluar dari Mesin")
            if self.balance > 0:
                self.show_message(f"Uang kembalian anda: Rp{self.balance}")
                self.balance = 0
        else:
            self.show_message("Saldo tidak mencukupi, Uang dikembalikan.")
            self.balance = 0
    
    def select_itemfanta(self):
        if self.balance >= self.fanta:
            self.balance -= self.fanta
            self.update_balance_label()
            self.show_message(f"Pembelian Fanta Berhasil!!\nMohon tunggu sebentar hingga minuman keluar dari Mesin")
            if self.balance > 0:
                self.show_message(f"Uang kembalian anda: Rp{self.balance}")
                self.balance = 0
        else:
            self.show_message("Saldo tidak mencukupi, Uang dikembalikan.")
            self.balance = 0
    
    def select_itempepsi(self):
        if self.balance >= self.pepsi:
            self.balance -= self.pepsi
            self.update_balance_label()
            self.show_message(f"Pembelian Pepsi Berhasil!!\nMohon tunggu sebentar hingga minuman keluar dari Mesin")
            if self.balance > 0:
                self.show_message(f"Uang kembalian anda: Rp{self.balance}")
                self.balance = 0
        else:
            self.show_message("Saldo tidak mencukupi, Uang dikembalikan.")
            self.balance = 0
    
    def select_itemaqua(self):
        if self.balance >= self.aqua:
            self.balance -= self.aqua
            self.update_balance_label()
            self.show_message(f"Pembelian Aqua Berhasil!!\nMohon tunggu sebentar hingga minuman keluar dari Mesin")
            if self.balance > 0:
                self.show_message(f"Uang kembalian anda: Rp{self.balance}")
                self.balance = 0
        else:
            self.show_message("Saldo tidak mencukupi, Uang dikembalikan.")
            self.balance = 0
    
    def select_itemtebs(self):
        if self.balance >= self.tebs:
            self.balance -= self.tebs
            self.update_balance_label()
            self.show_message(f"Pembelian Tebs Berhasil!!\nMohon tunggu sebentar hingga minuman keluar dari Mesin")
            if self.balance > 0:
                self.show_message(f"Uang kembalian anda: Rp{self.balance}")
                self.balance = 0
        else:
            self.show_message("Saldo tidak mencukupi, Uang dikembalikan.")
            self.balance = 0
    
    def select_itemsprite(self):
        if self.balance >= self.sprite:
            self.balance -= self.sprite
            self.update_balance_label()
            self.show_message(f"Pembelian Sprite Berhasil!!\nMohon tunggu sebentar hingga minuman keluar dari Mesin")
            if self.balance > 0:
                self.show_message(f"Uang kembalian anda: Rp{self.balance}")
                self.balance = 0
        else:
            self.show_message("Saldo tidak mencukupi, Uang dikembalikan.")
            self.balance = 0


    def update_balance_label(self):
        self.label_balance.config(text=f"Saldo saat ini: Rp{self.balance}",font=("Times New Roman", 16, "normal"))
    

    def show_message(self, message):
        tk.messagebox.showinfo("Vending Machine", message)

        
root = tk.Tk()
vending_machine = VendingMachine(root)
root.mainloop()