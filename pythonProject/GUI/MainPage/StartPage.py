import tkinter as tk
from GUI.MainPage.LeftPanel import LeftPanel
from GUI.MainPage.GamePage  import GamePage
from GUI.PlayerPages.EditPlayerDataPage import EditPlayerDataPage
from GUI.PlayerPages.PlayerHistoryPage import PlayerHistoryPage


class StartPage(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        # ===Wymiary zapewniające najwięcej FPSów w trakcie gry!===
        self.geometry('1000x700')
        self.title('Ruletka')
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.rightPanel = GamePage(self,[])
        self.leftPanel = LeftPanel(self)

        self.leftPanel.grid(row=0, column=0, sticky='nsew')
        self.rightPanel.grid(row=0, column=1, sticky='nsew')

        self.grid_rowconfigure(0,weight=1)

    def switch_frame_EditPlayerDataPage(self,player):
        self.rightPanel.grid_forget()
        self.rightPanel = EditPlayerDataPage(self,player)
        self.rightPanel.grid(row=0, column=1, sticky='nsew')

    def switch_frame_GamePage(self, lastGameLogs):
        self.rightPanel.grid_forget()
        self.rightPanel = GamePage(self,lastGameLogs)
        self.rightPanel.grid(row=0, column=1, sticky='nsew')

    def switch_frame_PlayerGamesHistoryPage(self,player):
        self.rightPanel.grid_forget()
        self.rightPanel = PlayerHistoryPage(self,player)
        self.rightPanel.grid(row=0, column=1, sticky='nsew')

    def refreshLeftPanel(self):
        self.leftPanel = LeftPanel(self)
        self.leftPanel.grid(row=0, column=0, sticky='nsew')