from tkinter import *
from config.config import *

#Máscara Monetária
def onTypingMonetaryEntry(event):
	value = event.widget.get().replace("R$", "").replace(".", "").replace(",", "")

	try:
		value = float(value)
		event.widget.delete(0, END)
		event.widget.insert(0, f"R${value/100:,.2f}".replace(",", "x").replace(".", ",").replace("x", "."))
	except:
		event.widget.delete(len(event.widget.get())-1, END)

#Máscara Monetária (Permite valores negativos)
def onTypingMonetaryEntryNegativePermissive(event):
	value = event.widget.get().replace("R$", "").replace(".", "").replace(",", "")
	
	if len(value) > 0:
		value = value[0] + value[1:].replace("-", "")

	try:
		if value[0] == "-" and not(value == "-00"): 
			if len(event.widget.get()) > 1:
				value = float(value)
				event.widget.delete(0, END)
				event.widget.insert(0, f"-R${abs(value)/100:,.2f}".replace(",", "x").replace(".", ",").replace("x", "."))
		else:
			value = float(value)
			event.widget.delete(0, END)
			event.widget.insert(0, f"R${abs(value)/100:,.2f}".replace(",", "x").replace(".", ",").replace("x", "."))	
	except:
		event.widget.delete(len(event.widget.get())-1, END)

#Máscara Numérica (VALOR INTEIRO)
def onTypingIntegerEntry(event):
	value = event.widget.get().replace(".", "")
	try:
		value = int(value)
		event.widget.delete(0, END)
		event.widget.insert(0, f"{value:,}".replace(",", "."))
	except:
		event.widget.delete(len(event.widget.get())-1, END)

#Evento ao passar o mouse dentro de um botão azul
def onMouseIntoBlueButton(event):
	event.widget.configure(bg=CLEAN_BLUE)

#Evento ao tirar o mouse de dentro de um botão azul
def onMouseOutBlueButton(event):
	event.widget.configure(bg=BLUE)

#Evento ao passar o mouse dentro de um botão azul
def onMouseIntoRedButton(event):
	event.widget.configure(bg=CLEAN_RED)

#Evento ao tirar o mouse de dentro de um botão azul
def onMouseOutRedButton(event):
	event.widget.configure(bg=RED)

#Evento ao passar o mouse dentro de um botão cinza
def onMouseIntoDarkButton(event):
	event.widget.configure(bg=WHITE, fg=BLACK, relief="sunken")

#Evento ao tirar o mouse de dentro de um botão cinza
def onMouseOutDarkButton(event):
	event.widget.configure(bg=DARK, fg=WHITE, relief="raised")