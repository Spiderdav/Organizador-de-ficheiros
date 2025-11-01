import customtkinter
import os
from organizador import Organizador



janela = Organizador()
janela.configurar_grelha()
janela.mostrar_grelha()
janela.criar_widgets()
janela.run()