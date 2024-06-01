import tkinter as tk

from GUI.MainPage.BetPanel import BetPanel
from GUI.MainPage.GamePage import GamePage
from GUI.MainPage.PlayersPanel import PlayersPanel
from GUI.PlayerPages.EditPlayerDataPage import EditPlayerDataPage
import DataManager as dm

class LeftPanel(tk.Frame):

    def __init__(self,parent):
        super().__init__(parent, bg='grey')
        self.parent = parent
        self.grid(row=0, column=0, sticky='nsew')
        label = tk.Label(self, text="LeftPanel")
        label.grid()
        self.grid_propagate(False)

        # ===Panel z graczami===
        self.PlayersPanel = PlayersPanel(self)
        self.PlayersPanel.grid(row=0, column=0, sticky='nsew')

        # ===Panel do zakładów===
        self.BetPanel = BetPanel(self,dm.loadPlayerById(0))
        self.BetPanel.grid(row=1, column=0, sticky='nsew')



    def ShowGamePanel(self, logs):
        self.parent.switch_frame_GamePage(logs)

    def EditDetails(self, player):
        self.parent.switch_frame_EditPlayerDataPage(player)

    def ShowGameHistory(self, player):
        self.parent.switch_frame_PlayerGamesHistoryPage(player)

    def RefreshPlayersList(self):
        self.PlayersPanel = PlayersPanel(self)
        self.PlayersPanel.grid(row=0, column=0, sticky='nsew')

    def RefreshBetPanel(self):
        self.BetPanel = BetPanel(self,dm.loadPlayerById(0))
        self.BetPanel.grid(row=1, column=0, sticky='nsew')