import tkinter as tk
from GUI.MainPage.PlayerPanel import PlayerPanel
import DataManager as dm

class PlayersPanel(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg='orange')
        self.parent = parent
        self.grid(row=0, column=0, sticky='nsew')

        playersList = dm.loadPlayers()

        # ===Tworzenie wierszy z info o graczach===
        for player in playersList:
            self.DynamicPlayer = PlayerPanel(self, player)
            self.DynamicPlayer.grid(row = player.id, column=1, padx=4, pady=10, sticky='nsew')



    def EditDetails(self, player):
        self.parent.EditDetails(player)
    def ShowGameHistory(self, player):
        self.parent.ShowGameHistory(player)