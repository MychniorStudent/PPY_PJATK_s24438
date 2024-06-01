import tkinter as tk
import DataManager as dm
class PlayerHistoryPage(tk.Frame):

    def __init__(self, parent, player):
        super().__init__(parent,bg='pink')
        self.grid(row=0, column=1, sticky='nsew')
        self.grid_propagate(False)
        rowCounter = 1;
        WonGames = dm.getWonGamesForPlayerByIdJSON(player.id)
        LostGames = dm.getLostGamesForPlayerByIdJSON(player.id)

        # ===Wyświetlenie wygranych gier===
        self.WonGamesLabel = tk.Label(self, text='Wygrane gry: ')
        self.WonGamesLabel.grid(row=0,column=0 ,padx=20, pady=15, sticky='nsew')

        for date,game in WonGames.items():
            self.DateInfoLabel = tk.Label(self, text="Data gry: ")
            self.DateInfoLabel.grid(row=rowCounter,column=0 ,padx=5, pady=5, sticky='nsew')
            self.DateLabel = tk.Label(self, text=date)
            self.DateLabel.grid(row=rowCounter,column=1 ,padx=5, pady=5, sticky='nsew')
            self.BetInfoLabel = tk.Label(self, text="Zakład: ")
            self.BetInfoLabel.grid(row=rowCounter,column=2 ,padx=5, pady=5, sticky='nsew')
            self.BetLabel = tk.Label(self, text=game["Bet"])
            self.BetLabel.grid(row=rowCounter,column=3 ,padx=5, pady=5, sticky='nsew')
            self.PrizeInfoLabel = tk.Label(self, text="Wygrana: ")
            self.PrizeInfoLabel.grid(row=rowCounter,column=4 ,padx=5, pady=5, sticky='nsew')
            self.PrizeLabel = tk.Label(self, text=game["Prize"])
            self.PrizeLabel.grid(row=rowCounter,column=5 ,padx=5, pady=5, sticky='nsew')
            rowCounter+=1

        # ===Wyświetlenie przegranych gier===
        self.WonGamesLabel = tk.Label(self, text='Przegrane gry: ')
        self.WonGamesLabel.grid(row=rowCounter, column=0, padx=20, pady=15, sticky='nsew')
        rowCounter+=1


        for date,game in LostGames.items():
            self.DateInfoLabel = tk.Label(self, text="Data gry: ")
            self.DateInfoLabel.grid(row=rowCounter, column=0, padx=5, pady=5, sticky='nsew')
            self.DateLabel = tk.Label(self, text=date)
            self.DateLabel.grid(row=rowCounter, column=1, padx=5, pady=5, sticky='nsew')
            self.BetInfoLabel = tk.Label(self, text="Zakład: ")
            self.BetInfoLabel.grid(row=rowCounter, column=2, padx=5, pady=5, sticky='nsew')
            self.BetLabel = tk.Label(self, text=game["Bet"])
            self.BetLabel.grid(row=rowCounter, column=3, padx=5, pady=5, sticky='nsew')
            rowCounter += 1

