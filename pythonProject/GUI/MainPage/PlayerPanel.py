import tkinter as tk


class PlayerPanel(tk.Frame):
    def __init__(self,parent, player):
        super().__init__(parent, highlightbackground="blue", highlightthickness=1, bg='orange')


        self.parent = parent
        self.grid(row=0, column=0, sticky='nsew')
        self.player = player

        # ===Podstawowe informacje o graczu===
        self.NameLabel = tk.Label(self, text=self.player.name)
        self.ActualMoneyLabel = tk.Label(self, text=str(self.player.account_balance)+'$')

        # ===Przyciski nawigacji dla poszczególnych graczy===
        self.editDataButton = tk.Button(self, text="EditData", command= lambda: self.parent.EditDetails(self.player))
        self.gameHistoryButton = tk.Button(self, text="GameHistory", command= lambda: self.parent.ShowGameHistory(self.player))

        #===Układanka widżetów===
        self.NameLabel.grid(row = 0, column = 0, padx =2,pady =2)
        self.ActualMoneyLabel.grid(row = 0, column = 1, padx =2,pady =2)
        self.editDataButton.grid(row = 0, column=2, padx=2, pady=2)
        self.gameHistoryButton.grid(row = 0, column=3, padx=2, pady=2)