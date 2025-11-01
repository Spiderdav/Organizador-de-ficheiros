import customtkinter
import os

class Organizador:
    def __init__(self):
        self.janela = customtkinter.CTk()
        self.janela.title("Organizador de Ficheiros")
        self.janela.geometry("1920x1080")
        customtkinter.set_appearance_mode("system")

    def configurar_grelha(self):
        for linha in range(0, 9):
            self.janela.rowconfigure(linha, weight=1)

        for coluna in range(0, 9):
            self.janela.columnconfigure(coluna, weight=1)

    def mostrar_grelha(self):
        for linha in range(0, 9):
            for coluna in range(0, 9):
                if (linha + coluna) % 2 == 0:
                    label = customtkinter.CTkLabel(self.janela, text=f"L{linha}", fg_color="#555555")
                    label.grid(row=linha, column=coluna, sticky="nsew")
                else:
                    label = customtkinter.CTkLabel(self.janela, text=f"C{coluna}", fg_color="#333333")
                    label.grid(row=linha, column=coluna, sticky="nsew")

    def criar_widgets(self):
        titulo = customtkinter.CTkLabel(self.janela, text="Organizador de Ficheiros", font=("Arial", 40))
        titulo.grid(row=0, column=3, sticky="nsew", columnspan=3)

        entry_origem = customtkinter.CTkEntry(self.janela)
        # entry_origem.grid(customtkinter)



    def run(self):
        self.janela.mainloop()
