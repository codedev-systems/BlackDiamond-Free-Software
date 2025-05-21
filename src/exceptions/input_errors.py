from tkinter import messagebox

def showMessageError(code):
	if code == 1:
		messagebox.showerror(title="Erro de Entrada", message="Preencha o campo DESCRIÇÃO!")