import tkinter as tk
from datetime import datetime
import DataManager as dm
import json

class EditPlayerDataPage(tk.Frame):

    def __init__(self, parent, player):
        super().__init__(parent,bg='green')

        self.player = player
        self.parent = parent

        self.AccountBalanceSpinboxVariable = tk.DoubleVar(self, value=player.account_balance)
        self.IsAddicted = tk.BooleanVar(value=player.isAddicted)
        self.NameTextBoxVariable = tk.StringVar(self)
        self.StoryTextBosVariable = tk.StringVar(self)


        self.grid(row=0, column=3, sticky='nsew')

        #=====PlayerID=====#
        self.PlayerIdLabel = tk.Label(self, text='PlayerId: '+player.id)
        self.PlayerIdLabel.grid(row=0, column=3, padx =150,pady =15, sticky='nsew')

        # =====Imię=====#
        self.NameLabel = tk.Label(self, text='Imię')
        self.NameLabel.grid(row=2, column=2, padx =20,pady =15, sticky='nsew')

        self.NameTextBox = tk.Entry(self,textvariable=self.NameTextBoxVariable)
        self.NameTextBox.insert(0, player.name)
        self.NameTextBox.grid(row=2, column=3,padx =20,pady =15,  sticky='nsew')

        # =====Uzależnienie=====#
        self.IsAddictedLabel = tk.Label(self, text='Czy uzależniony: ')
        self.IsAddictedLabel.grid(row=3, column=2, padx=20, pady=15, sticky='nsew')


        self.IsAddictedCheckbutton = tk.Checkbutton(self, text='Uzależenienie', variable=self.IsAddicted, onvalue=True,offvalue=False)
        self.IsAddictedCheckbutton.grid(row=3, column=3,padx =20,pady =15,  sticky='nsew')


        # =====Stan konta=====#
        self.AccuntBalanceCurrentLabel = tk.Label(self, text='Pieniążki obecne: ')
        self.AccuntBalanceCurrentLabel.grid(row=4, column=2, padx=20, pady=15, sticky='nsew')

        self.AccountBalanceTextBox = tk.Label(self, text=player.account_balance)
        self.AccountBalanceTextBox.grid(row=4, column=3, padx=20, pady=15, sticky='nsew')

        self.AccuntBalanceEditLabel = tk.Label(self, text='Pieniążki edycja: ')
        self.AccuntBalanceEditLabel.grid(row=5, column=2, padx=20, pady=15, sticky='nsew')

        self.AccountBalanceSpinbox = tk.Spinbox(self, from_=0,to=1000000,increment=1, textvariable=self.AccountBalanceSpinboxVariable)
        self.AccountBalanceSpinbox.grid(row=5, column=3, padx =20,pady =15, sticky='nsew')



        # =====Historia=====#
        self.StoryCurrentLabel = tk.Label(self, text='Historia: ')
        self.StoryCurrentLabel.grid(row=6, column=2, padx=20, pady=15, sticky='nsew')

        self.StoryLabel = tk.Label(self, text=player.story, wraplength=300)
        self.StoryLabel.grid(row=6, column=3,padx =150,pady =15, sticky='nsew')

        self.StoryCurrentEditLabel = tk.Label(self, text='Historia edycja: ')
        self.StoryCurrentEditLabel.grid(row=7, column=2, padx=20, pady=15, sticky='nsew')

        self.StoryTextBox = tk.Entry(self, width=20, font='Arial 15', textvariable=self.StoryTextBosVariable)
        self.StoryTextBox.insert(0, player.story)
        self.StoryTextBox.grid(row=7, column=3,padx =150,pady =15,  sticky='nsew')

        self.SaveBtn = tk.Button(self, text="Zapisz", command= lambda: self.SaveBtnClicked())
        self.SaveBtn.grid(row = 8, column = 3, padx =20, pady =15, sticky='nsew')

        self.CancelBtn = tk.Button(self, text="Anuluj || Wroc", command= lambda: self.CancelBtnClicked())
        self.CancelBtn.grid(row=9, column=3, padx=20, pady=15, sticky='nsew')

        self.grid_propagate(False)

    def SaveBtnClicked(self):

        self.player.name = self.NameTextBoxVariable.get()
        self.player.story = self.StoryTextBosVariable.get()
        self.player.account_balance = self.AccountBalanceSpinboxVariable.get()
        self.player.isAddicted = self.IsAddicted.get()
        self.player.modification_date = str(datetime.now())
        dm.updatePlayerData(self.player.preparePlayerJSON())
        self.parent.refreshLeftPanel()

    def CancelBtnClicked(self):
        self.parent.switch_frame_GamePage([])
