import tkinter as tk

class GamePage(tk.Frame):

    def __init__(self, parent, LastGameLogs):
        super().__init__(parent,bg='blue')
        self.grid(row=0, column=1, sticky='nsew')
        self.grid_propagate(False)
        logRowCounter = 0

        # ===Wyswietlanie logow z gry===
        for log in LastGameLogs:
            self.LogLabel = tk.Label(self, text=log)
            self.LogLabel.grid(row=logRowCounter, column=0, padx=20, pady=15, sticky='nsew')
            logRowCounter += 1

        # ===Domyslna wiadomosc===
        if logRowCounter == 0:
            self.LogLabel = tk.Label(self, text='Zagraj w grę, śmiało!!!')
            self.LogLabel.grid(row=logRowCounter, column=0, padx=20, pady=15, sticky='nsew')

