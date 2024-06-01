import tkinter as tk
from tkinter import messagebox
import Roulette as rl

class BetPanel(tk.Frame):
    def __init__(self, parent, player):
        super().__init__(parent, bg='grey')
        self.grid(row=0, column=1, sticky='nsew')
        self.player = player
        self.parent = parent

        # ===Zmienne do zakładu===
        self.BetBalanceSpinboxVariable = tk.DoubleVar(self, value=0)
        self.BetSelectedColor = tk.StringVar(value="G")

        # ===Widżety do obstawiania===
        self.InfoLabel = tk.Label(self, text="Wybierz kolor, ustal kwotę i graj!")
        self.InfoLabel.grid(row=0, column=1, padx=40, pady=30, sticky='nsew')
        self.RadioGreen = tk.Radiobutton(self, text="Green", variable=self.BetSelectedColor, value="G")
        self.RadioGreen.grid(row=1, column=1, padx=20, pady=15, sticky='nsew')
        self.RadioRed = tk.Radiobutton(self, text="Red", variable=self.BetSelectedColor, value="R")
        self.RadioRed.grid(row=2, column=1, padx=20, pady=15, sticky='nsew')
        self.RadioBlack = tk.Radiobutton(self, text="Black", variable=self.BetSelectedColor, value="B")
        self.RadioBlack.grid(row=3, column=1, padx=20, pady=15, sticky='nsew')


        self.BetBalanceSpinbox = tk.Spinbox(self, from_=0, to=player.account_balance, increment=1,
                                            textvariable=self.BetBalanceSpinboxVariable)
        self.BetBalanceSpinbox.grid(row=4, column=1, padx=20, pady=15, sticky='nsew')

        # ===Przycisk do rozpoczęcia gry===
        self.PlayBtn = tk.Button(self, text = 'Bet&Play',command= lambda: self.spin())
        self.PlayBtn.grid(row = 5, column=1, padx=20, pady=15, sticky='nsew')


    def spin(self):

        #===Walidacja stanu konta===
        if self.player.account_balance < float(self.BetBalanceSpinbox.get()):
            messagebox.showinfo("Brak srodkow", "Nie mozesz postawic więcej niż masz :<")
            return

        #===Start gierki===
        logsResult = rl.startGame(self.BetSelectedColor.get(),self.BetBalanceSpinbox.get())
        self.parent.ShowGamePanel(logsResult)
        self.parent.RefreshPlayersList()
        self.parent.RefreshBetPanel()
