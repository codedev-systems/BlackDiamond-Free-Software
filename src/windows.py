import exceptions.input_errors
from config.events import *
from config.config import *
from config.masks import *
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from entities.Dre import *
from entities.Bp import *
from entities.Dfc import *
from entities.Document import *

''' Tela Principal '''
class MainWindow():
	app = Tk()
	
	def show(self):
		self.app.title(MAIN_WINDOW_TITLE)
		self.app.minsize(WINDOWS_MINIME_WIDTH, WINDOWS_MINIME_HEIGHT)
		self.app.configure(bg=WINDOW_BACKGROUND)

		#Estilização das Tabelas
		tableStyle = ttk.Style(self.app)
		tableStyle.theme_use("clam")
		tableStyle.configure("Treeview", font=(TABLE_FONT))
		tableStyle.configure("Treeview.Heading", background=WHITE, foreground=BLACK, borderwidth=0, relief="solid", font=(TABLE_FONT))

		Menu().show()
		DreWindow().show()

		self.app.mainloop()
		
#Menu
class Menu(MainWindow):
	menu_Frame = Frame(MainWindow().app, bg=DARK, width=MENU_WIDTH)

	#Botão DRE
	dre_Button = Button(menu_Frame, text="DRE", fg=BLACK, bg=WINDOW_BACKGROUND, relief="sunken", font=MENU_BUTTON_FONT, cursor="hand2")

	#Botão BP
	bp_Button = Button(menu_Frame, text="BP", fg=WHITE, bg=DARK, relief="raised", font=MENU_BUTTON_FONT, cursor="hand2")

	#Botão DFC
	dfc_Button = Button(menu_Frame, text="DFC", fg=WHITE, bg=DARK, relief="raised", font=MENU_BUTTON_FONT, cursor="hand2")

	#Botão Indicadores
	indicator_Button = Button(menu_Frame, text="%", fg=WHITE, bg=DARK, relief="raised", font=MENU_BUTTON_FONT, cursor="hand2")

	#Botão Ajuda
	help_Button = Button(menu_Frame, text="?", fg=WHITE, bg=BLUE, relief="raised", font=MENU_BUTTON_FONT, cursor="hand2")
	
	icon_Frame = Frame(MainWindow().app, bg=BLACK, height=HEADER_HEIGHT, width=HEADER_WIDTH)

	#Logo do programa
	logo_Image = Image.open(ICON_IMAGE)
	logo_Photo = ImageTk.PhotoImage(logo_Image)
	icon_ImageLabel = Label(icon_Frame, bg=BLACK, image=logo_Photo)

	def showDreWindow(self):
		DreWindow().show()
		BpWindow().remove()
		DfcWindow().remove()

		self.dre_Button.configure(bg=WHITE, fg=BLACK, relief="sunken")
		self.dre_Button.unbind("<Enter>")
		self.dre_Button.unbind("<Leave>")

		self.bp_Button.configure(bg=DARK, fg=WHITE, relief="raised")
		self.bp_Button.bind("<Enter>", onMouseIntoDarkButton)
		self.bp_Button.bind("<Leave>", onMouseOutDarkButton)

		self.dfc_Button.configure(bg=DARK, fg=WHITE, relief="raised")
		self.dfc_Button.bind("<Enter>", onMouseIntoDarkButton)
		self.dfc_Button.bind("<Leave>", onMouseOutDarkButton)

	def showBpWindow(self):
		DreWindow().remove()
		BpWindow().show()
		DfcWindow().remove()

		self.dre_Button.configure(bg=DARK, fg=WHITE, relief="raised")
		self.dre_Button.bind("<Enter>", onMouseIntoDarkButton)
		self.dre_Button.bind("<Leave>", onMouseOutDarkButton)

		self.bp_Button.configure(bg=WHITE, fg=BLACK, relief="sunken")
		self.bp_Button.unbind("<Enter>")
		self.bp_Button.unbind("<Leave>")

		self.dfc_Button.configure(bg=DARK, fg=WHITE, relief="raised")
		self.dfc_Button.bind("<Enter>", onMouseIntoDarkButton)
		self.dfc_Button.bind("<Leave>", onMouseOutDarkButton)

	def showDfcWindow(self):
		DreWindow().remove()
		BpWindow().remove()
		DfcWindow().show()

		self.dre_Button.configure(bg=DARK, fg=WHITE, relief="raised")
		self.dre_Button.bind("<Enter>", onMouseIntoDarkButton)
		self.dre_Button.bind("<Leave>", onMouseOutDarkButton)

		self.bp_Button.configure(bg=DARK, fg=WHITE, relief="raised")
		self.bp_Button.bind("<Enter>", onMouseIntoDarkButton)
		self.bp_Button.bind("<Leave>", onMouseOutDarkButton)

		self.dfc_Button.configure(bg=WHITE, fg=BLACK, relief="sunken")
		self.dfc_Button.unbind("<Enter>")
		self.dfc_Button.unbind("<Leave>")

	def showIndicatorsWindow(self):
		DreWindow().remove()
		BpWindow().remove()
		DfcWindow().remove()

		self.dre_Button.configure(bg=DARK, fg=WHITE, relief="raised")
		self.dre_Button.bind("<Enter>", onMouseIntoDarkButton)
		self.dre_Button.bind("<Leave>", onMouseOutDarkButton)

		self.bp_Button.configure(bg=DARK, fg=WHITE, relief="raised")
		self.bp_Button.bind("<Enter>", onMouseIntoDarkButton)
		self.bp_Button.bind("<Leave>", onMouseOutDarkButton)

		self.dfc_Button.configure(bg=DARK, fg=WHITE, relief="raised")
		self.dfc_Button.bind("<Enter>", onMouseIntoDarkButton)
		self.dfc_Button.bind("<Leave>", onMouseOutDarkButton)

	def openHelpWindow(self):
		HelpWindow().show()

	def show(self):
		self.menu_Frame.pack(fill="y", side="left")

		self.icon_Frame.place(x=0, y=0, width=MENU_WIDTH, height=HEADER_HEIGHT)
		self.icon_ImageLabel.place(x=27, y=1)
		
		self.dre_Button.place(x=0, y=90, width=MENU_WIDTH, height=MENU_BUTTON_HEIGHT)
		self.dre_Button.configure(command=self.showDreWindow)

		self.bp_Button.place(x=0, y=135, width=MENU_WIDTH, height=MENU_BUTTON_HEIGHT)
		self.bp_Button.bind("<Enter>", onMouseIntoDarkButton)
		self.bp_Button.bind("<Leave>", onMouseOutDarkButton)
		self.bp_Button.configure(command=self.showBpWindow)

		self.dfc_Button.place(x=0, y=180, width=MENU_WIDTH, height=MENU_BUTTON_HEIGHT)
		self.dfc_Button.bind("<Enter>", onMouseIntoDarkButton)
		self.dfc_Button.bind("<Leave>", onMouseOutDarkButton)
		self.dfc_Button.configure(command=self.showDfcWindow)

		self.help_Button.place(x=0, y=225, width=MENU_WIDTH, height=MENU_BUTTON_HEIGHT)
		self.help_Button.bind("<Enter>", onMouseIntoBlueButton)
		self.help_Button.bind("<Leave>", onMouseOutBlueButton)
		self.help_Button.configure(command=self.openHelpWindow)

''' Telas de Operação '''
#Tela de Geração de DRE
class DreWindow(MainWindow):
	dreWindow_Frame = Frame(MainWindow().app, bg=WINDOW_BACKGROUND)
	documentGenerator_Frame = Frame(dreWindow_Frame, bg=WINDOW_BACKGROUND, height=50)
	documentGenerator_Button = Button(documentGenerator_Frame, text=GENERATE_DOCUMENT_BUTTON_TEXT, fg=WHITE, bg=BLUE, relief="raised", font=BUTTON_FONT, cursor="hand2")

	def generateDocument(self, startDate, finishDate, revenue, dedutionsTable, cmvsTable, operationalMovementsTable, financialMovementsTable, irCsllProvision):
		if(len(revenue) == 0):
			revenue = "R$0,00"

		dedutions = {}
		for i in dedutionsTable.get_children():
			dedution = dedutionsTable.item(i)["values"]
			dedutions.update({dedution[0]:dedution[1]})

		cmvs = {}
		for i in cmvsTable.get_children():
			cmv = cmvsTable.item(i)["values"]
			cmvs.update({cmv[0]:cmv[1]})

		operationalMovements = {}
		for i in operationalMovementsTable.get_children():
			operationalMovement = operationalMovementsTable.item(i)["values"]
			operationalMovements.update({operationalMovement[0]:operationalMovement[1]})

		financialMovements = {}
		for i in financialMovementsTable.get_children():
			financialMovement = financialMovementsTable.item(i)["values"]
			financialMovements.update({financialMovement[0]:financialMovement[1]})

		if(len(irCsllProvision) == 0):
			irCsllProvision = "R$0,00"

		dre = Dre(revenue, dedutions, cmvs, operationalMovements, financialMovements, irCsllProvision)
		document = Document(startDate, finishDate)
		document.generateDre(dre)

	def removeItemFromTable(self, table):
		for selected in table.selection():
			table.delete(selected)

	def valueWasExistsInTable(self, table, desc):
		descWasExists = False
		for i in table.get_children():
				name = table.item(i)["values"][0]
				if(name == desc):
					descWasExists = True
					break

		return descWasExists

	def remove(self):
		self.dreWindow_Frame.pack_forget()
		self.documentGenerator_Frame.pack_forget()
		self.documentGenerator_Button.pack_forget()

	def show(self):
		self.dreWindow_Frame.pack(expand=True, fill="both")

		''' Área de Definição de Período '''
		period_Label = Label(self.dreWindow_Frame, text="Período", bg=WINDOW_BACKGROUND, font=TEXT_FONT)
		period_Label.place(x=15, y=10)

		#Início
		startPeriod_DateEntry = DateEntry(self.dreWindow_Frame, locale='pt_BR', date_pattern='dd/MM/yyyy', bg=WHITE, font=TEXT_FONT)
		startPeriod_DateEntry.place(x=85, y=10)

		#Simples Junção -
		periodJunction_Label = Label(self.dreWindow_Frame, text="-", bg=WINDOW_BACKGROUND, font=TEXT_FONT)
		periodJunction_Label.place(x=219, y=10)

		#Final
		finishPeriod_DateEntry = DateEntry(self.dreWindow_Frame, locale='pt_BR', date_pattern='dd/MM/yyyy', bg=WHITE, font=TEXT_FONT)
		finishPeriod_DateEntry.place(x=235, y=10)

		

		''' Área de Definição de Receita Bruta '''
		revenue_Label = Label(self.dreWindow_Frame, text="Receita Bruta", bg=WINDOW_BACKGROUND, font=TEXT_FONT)
		revenue_Label.place(x=15, y=47)
		revenue_Entry = Entry(self.dreWindow_Frame, bg=WHITE, fg=GRAY, font=TEXT_FONT, relief="solid")
		revenue_Entry.place(x=125, y=47)
		revenue_Entry.bind("<KeyRelease>", onTypingMonetaryEntry)



		''' Área de Deduções '''
		dedutions_Frame = Frame(self.dreWindow_Frame, background=WINDOW_BACKGROUND, height=TABLE_FRAME_HEIGHT)
		dedutions_Frame.place(x=15, y=84, relwidth=TABLE_FRAME_RELATIVE_WIDTH)

		dedutions_Label = Label(dedutions_Frame, text="Deduções", bg=WINDOW_BACKGROUND, fg=DARK, font=TITLE_FONT)
		dedutions_Label.place(x=0, y=0)

		#Tabela de Deduções
		dedutions_TreeView = ttk.Treeview(dedutions_Frame, columns=('DESCRICAO', 'VALOR'), show='headings')
		dedutions_TreeView.column("DESCRICAO", anchor="w")
		dedutions_TreeView.column("VALOR", width=90, anchor="center")
		dedutions_TreeView.heading("DESCRICAO", text=TABLE_DESC_COLUMN_TEXT, anchor="w")
		dedutions_TreeView.heading("VALOR", text=TABLE_VALUE_COLUMN_TEXT, anchor="center")
		dedutions_TreeView.place(x=3, y=28, relwidth=TABLE_RELATIVE_WIDTH, height=TABLE_HEIGHT)
		dedutions_TreeView.tag_configure("negative", foreground=RED)

		#Botões de Remoção e Adição de Itens
		addRemove_Frame = Frame(dedutions_Frame, height=40, bg=WINDOW_BACKGROUND)
		addRemove_Frame.place(x=0, y=BUTTONS_TABLE_Y, relwidth=ADD_REMOVE_BUTTONS_AREA_RELATIVE_WIDTH, height=26)
		
		add_Button = Button(addRemove_Frame, text=ADD_BUTTONS_TEXT, bg=BLUE, fg=WHITE, cursor="hand2", width=3, font=(SMALL_BUTTON_FONT), command=lambda:AddDebtWindow().show(dedutions_TreeView))
		add_Button.bind("<Enter>", onMouseIntoBlueButton)
		add_Button.bind("<Leave>", onMouseOutBlueButton)
		add_Button.pack(side="right", padx=SMALL_BUTTON_PADX)
		
		remove_Button = Button(addRemove_Frame, text=REMOVE_BUTTONS_TEXT, bg=RED, fg=WHITE, cursor="hand2", width=3, font=(SMALL_BUTTON_FONT), command=lambda:self.removeItemFromTable(dedutions_TreeView))
		remove_Button.bind("<Enter>", onMouseIntoRedButton)
		remove_Button.bind("<Leave>", onMouseOutRedButton)
		remove_Button.pack(side="right", padx=SMALL_BUTTON_PADX)



		''' Área de cmv/CSP '''
		cmv_Frame = Frame(self.dreWindow_Frame, bg=WINDOW_BACKGROUND, height=TABLE_FRAME_HEIGHT)
		cmv_Frame.place(relx=0.52, y=84, relwidth=TABLE_FRAME_RELATIVE_WIDTH)

		dedutions_Label = Label(cmv_Frame, text="CMV/CSP", bg=WINDOW_BACKGROUND, fg=DARK, font=TITLE_FONT)
		dedutions_Label.place(x=0, y=0)

		#Tabela de cmv/CSP
		cmv_TreeView = ttk.Treeview(cmv_Frame, columns=('DESCRICAO', 'VALOR'), show='headings')
		cmv_TreeView.column("DESCRICAO", anchor="w")
		cmv_TreeView.column("VALOR", width=90, anchor="center")
		cmv_TreeView.heading("DESCRICAO", text=TABLE_DESC_COLUMN_TEXT, anchor="w")
		cmv_TreeView.heading("VALOR", text=TABLE_VALUE_COLUMN_TEXT, anchor="center")
		cmv_TreeView.place(x=3, y=28, relwidth=TABLE_RELATIVE_WIDTH, height=TABLE_HEIGHT)
		cmv_TreeView.tag_configure("negative", foreground=RED)
		
		#Botões de Remoção e Adição de Itens
		addRemove_Frame = Frame(cmv_Frame, height=40, bg=WINDOW_BACKGROUND)
		addRemove_Frame.place(x=0, y=BUTTONS_TABLE_Y, relwidth=ADD_REMOVE_BUTTONS_AREA_RELATIVE_WIDTH, height=26)
		
		add_Button = Button(addRemove_Frame, text=ADD_BUTTONS_TEXT, bg=BLUE, fg=WHITE, cursor="hand2", width=3, font=(SMALL_BUTTON_FONT), command=lambda:AddDebtWindow().show(cmv_TreeView))
		add_Button.bind("<Enter>", onMouseIntoBlueButton)
		add_Button.bind("<Leave>", onMouseOutBlueButton)
		add_Button.pack(side="right", padx=SMALL_BUTTON_PADX)
		
		remove_Button = Button(addRemove_Frame, text=REMOVE_BUTTONS_TEXT, bg=RED, fg=WHITE, cursor="hand2", width=3, font=(SMALL_BUTTON_FONT), command=lambda:self.removeItemFromTable(cmv_TreeView))
		remove_Button.bind("<Enter>", onMouseIntoRedButton)
		remove_Button.bind("<Leave>", onMouseOutRedButton)
		remove_Button.pack(side="right", padx=SMALL_BUTTON_PADX)



		''' Área de Resultados Operacionais '''
		operationalResult_Frame = Frame(self.dreWindow_Frame, bg=WINDOW_BACKGROUND, height=TABLE_FRAME_HEIGHT)
		operationalResult_Frame.place(x=15, y=330, relwidth=TABLE_FRAME_RELATIVE_WIDTH)

		operationalResult_Label = Label(operationalResult_Frame, text="Receitas e Despesas Operacionais", bg=WINDOW_BACKGROUND, fg=DARK, font=TITLE_FONT)
		operationalResult_Label.place(x=0, y=0)

		#Tabela de Resultado Operacional
		operationalResult_TreeView = ttk.Treeview(operationalResult_Frame, columns=('DESCRICAO', 'VALOR'), show='headings')
		operationalResult_TreeView.column("DESCRICAO", anchor="w")
		operationalResult_TreeView.column("VALOR", width=90, anchor="center")
		operationalResult_TreeView.heading("DESCRICAO", text=TABLE_DESC_COLUMN_TEXT, anchor="w")
		operationalResult_TreeView.heading("VALOR", text=TABLE_VALUE_COLUMN_TEXT, anchor="center")
		operationalResult_TreeView.place(x=3, y=28, relwidth=TABLE_RELATIVE_WIDTH, height=TABLE_HEIGHT)
		operationalResult_TreeView.tag_configure("negative", foreground=RED)
		operationalResult_TreeView.tag_configure("positive", foreground=BLUE)
		
		#Botões de Remoção e Adição de Itens
		addRemove_Frame = Frame(operationalResult_Frame, height=40, bg=WINDOW_BACKGROUND)
		addRemove_Frame.place(x=0, y=BUTTONS_TABLE_Y, relwidth=ADD_REMOVE_BUTTONS_AREA_RELATIVE_WIDTH, height=26)
		
		add_Button = Button(addRemove_Frame, text=ADD_BUTTONS_TEXT, bg=BLUE, fg=WHITE, cursor="hand2", width=3, font=(SMALL_BUTTON_FONT), command=lambda:AddMovementWindow().show(operationalResult_TreeView))
		add_Button.bind("<Enter>", onMouseIntoBlueButton)
		add_Button.bind("<Leave>", onMouseOutBlueButton)
		add_Button.pack(side="right", padx=SMALL_BUTTON_PADX)
		
		remove_Button = Button(addRemove_Frame, text=REMOVE_BUTTONS_TEXT, bg=RED, fg=WHITE, cursor="hand2", width=3, font=(SMALL_BUTTON_FONT), command=lambda:self.removeItemFromTable(operationalResult_TreeView))
		remove_Button.bind("<Enter>", onMouseIntoRedButton)
		remove_Button.bind("<Leave>", onMouseOutRedButton)
		remove_Button.pack(side="right", padx=SMALL_BUTTON_PADX)



		''' Área de Receitas Financeiras '''
		financialResult_Frame = Frame(self.dreWindow_Frame, bg=WINDOW_BACKGROUND, height=TABLE_FRAME_HEIGHT)
		financialResult_Frame.place(relx=0.52, y=330, relwidth=TABLE_FRAME_RELATIVE_WIDTH)

		financialResult_Label = Label(financialResult_Frame, text="Receitas e Despesas Financeiras", bg=WINDOW_BACKGROUND, fg=DARK, font=TITLE_FONT)
		financialResult_Label.place(x=0, y=0)

		#Tabela de Resultado Financeiro
		financialResult_TreeView = ttk.Treeview(financialResult_Frame, columns=('DESCRICAO', 'VALOR'), show='headings')
		financialResult_TreeView.column("DESCRICAO", anchor="w")
		financialResult_TreeView.column("VALOR", width=90, anchor="center")
		financialResult_TreeView.heading("DESCRICAO", text=TABLE_DESC_COLUMN_TEXT, anchor="w")
		financialResult_TreeView.heading("VALOR", text=TABLE_VALUE_COLUMN_TEXT, anchor="center")
		financialResult_TreeView.place(x=3, y=28, relwidth=TABLE_RELATIVE_WIDTH, height=TABLE_HEIGHT)
		financialResult_TreeView.tag_configure("negative", foreground=RED)
		financialResult_TreeView.tag_configure("positive", foreground=BLUE)		
		
		#Botões de Remoção e Adição de Itens
		addRemove_Frame = Frame(financialResult_Frame, height=40, bg=WINDOW_BACKGROUND)
		addRemove_Frame.place(x=0, y=BUTTONS_TABLE_Y, relwidth=ADD_REMOVE_BUTTONS_AREA_RELATIVE_WIDTH, height=26)

		add_Button = Button(addRemove_Frame, text=ADD_BUTTONS_TEXT, bg=BLUE, fg=WHITE, cursor="hand2", width=3, font=(SMALL_BUTTON_FONT), command=lambda:AddMovementWindow().show(financialResult_TreeView))
		add_Button.bind("<Enter>", onMouseIntoBlueButton)
		add_Button.bind("<Leave>", onMouseOutBlueButton)
		add_Button.pack(side="right", padx=SMALL_BUTTON_PADX)
		
		remove_Button = Button(addRemove_Frame, text=REMOVE_BUTTONS_TEXT, bg=RED, fg=WHITE, cursor="hand2", width=3, font=(SMALL_BUTTON_FONT), command=lambda:self.removeItemFromTable(financialResult_TreeView))
		remove_Button.bind("<Enter>", onMouseIntoRedButton)
		remove_Button.bind("<Leave>", onMouseOutRedButton)
		remove_Button.pack(side="right", padx=SMALL_BUTTON_PADX)



		''' Área de IR e CSLL '''
		irCsllProvision_Label = Label()
		irCsllProvision_Label = Label(self.dreWindow_Frame, text="Provisão para IR e CSLL", bg=WINDOW_BACKGROUND, font=TEXT_FONT)
		irCsllProvision_Label.place(x=15, y=573)
		
		irCsllProvision_Entry = Entry(self.dreWindow_Frame, bg=WHITE, fg=GRAY, font=TEXT_FONT, relief="solid")
		irCsllProvision_Entry.place(x=210, y=573)
		irCsllProvision_Entry.bind("<KeyRelease>", onTypingMonetaryEntry)



		''' Botão de Geração de Documento '''
		self.documentGenerator_Frame.pack(fill="x", side="bottom")
		self.documentGenerator_Button.pack(side="right", padx=BUTTON_PADX, pady=BUTTON_PADY)
		self.documentGenerator_Button.bind("<Enter>", onMouseIntoBlueButton)
		self.documentGenerator_Button.bind("<Leave>", onMouseOutBlueButton)
		self.documentGenerator_Button.config(command=lambda:self.generateDocument(startPeriod_DateEntry.get_date(), finishPeriod_DateEntry.get_date(), revenue_Entry.get(), dedutions_TreeView, cmv_TreeView, operationalResult_TreeView, financialResult_TreeView, irCsllProvision_Entry.get()))

#Tela de Geração de BP
class BpWindow(MainWindow):
	bpWindow_Frame = Frame(MainWindow().app, bg=WINDOW_BACKGROUND)
	documentGenerator_Frame = Frame(bpWindow_Frame, bg=WINDOW_BACKGROUND, height=50)
	documentGenerator_Button = Button(documentGenerator_Frame, text=GENERATE_DOCUMENT_BUTTON_TEXT, fg=WHITE, bg=BLUE, relief="raised", font=BUTTON_FONT, cursor="hand2")

	def generateDocument(self, startDate, finishDate, currentActivesTable, noCurrentActivesTable, currentPassivesTable, noCurrentPassivesTable):
		currentActives = {}
		for i in currentActivesTable.get_children():
			currentActive = currentActivesTable.item(i)["values"]
			currentActives.update({currentActive[0]:currentActive[1]})

		noCurrentActives = {}
		for i in noCurrentActivesTable.get_children():
			noCurrentActive = noCurrentActivesTable.item(i)["values"]
			noCurrentActives.update({noCurrentActive[0]:noCurrentActive[1]})

		currentPassives = {}
		for i in currentPassivesTable.get_children():
			currentPassive = currentPassivesTable.item(i)["values"]
			currentPassives.update({currentPassive[0]:currentPassive[1]})

		noCurrentPassives = {}
		for i in noCurrentPassivesTable.get_children():
			noCurrentPassive = noCurrentPassivesTable.item(i)["values"]
			noCurrentPassives.update({noCurrentPassive[0]:noCurrentPassive[1]})


		bp = Bp(currentActives, noCurrentActives, currentPassives, noCurrentPassives)
		document = Document(startDate, finishDate)
		document.generateBp(bp)

	def removeItemFromTable(self, table):
		for selected in table.selection():
			table.delete(selected)

	def valueWasExistsInTable(self, table, desc):
		descWasExists = False
		for i in table.get_children():
				name = table.item(i)["values"][0]
				if(name == desc):
					descWasExists = True
					break

		return descWasExists

	def remove(self):
		self.bpWindow_Frame.pack_forget()
		self.documentGenerator_Frame.pack_forget()
		self.documentGenerator_Button.pack_forget()

	def show(self):
		self.bpWindow_Frame.pack(expand=True, fill="both")	

		''' Área de Definição de Período '''
		period_Label = Label(self.bpWindow_Frame, text="Período", bg=WINDOW_BACKGROUND, font=TEXT_FONT)
		period_Label.place(x=15, y=47)

		#Início
		startPeriod_DateEntry = DateEntry(self.bpWindow_Frame, locale='pt_BR', date_pattern='dd/MM/yyyy', bg=WHITE, font=TEXT_FONT)
		startPeriod_DateEntry.place(x=85, y=47)

		#Simples Junção -
		periodJunction_Label = Label(self.bpWindow_Frame, text="-", bg=WINDOW_BACKGROUND, font=TEXT_FONT)
		periodJunction_Label.place(x=219, y=47)

		#Final
		finishPeriod_DateEntry = DateEntry(self.bpWindow_Frame, locale='pt_BR', date_pattern='dd/MM/yyyy', bg=WHITE, font=TEXT_FONT)
		finishPeriod_DateEntry.place(x=235, y=47)



		''' Área de Ativos Circulantes '''
		currentActive_Frame = Frame(self.bpWindow_Frame, bg=WINDOW_BACKGROUND, height=TABLE_FRAME_HEIGHT)
		currentActive_Frame.place(x=15, y=84, relwidth=TABLE_FRAME_RELATIVE_WIDTH)

		currentActive_Label = Label(currentActive_Frame, text="Ativos Circulantes", bg=WINDOW_BACKGROUND, fg=DARK, font=TITLE_FONT)
		currentActive_Label.place(x=0, y=0)

		#Tabela de Ativos Circulantes
		currentActive_TreeView = ttk.Treeview(currentActive_Frame, columns=('DESCRICAO', 'VALOR'), show='headings')
		currentActive_TreeView.column("DESCRICAO", anchor="w")
		currentActive_TreeView.column("VALOR", width=90, anchor="center")
		currentActive_TreeView.heading("DESCRICAO", text=TABLE_DESC_COLUMN_TEXT, anchor="w")
		currentActive_TreeView.heading("VALOR", text=TABLE_VALUE_COLUMN_TEXT, anchor="center")
		currentActive_TreeView.place(x=3, y=28, relwidth=TABLE_RELATIVE_WIDTH, height=TABLE_HEIGHT)
		currentActive_TreeView.tag_configure("positive", foreground=BLUE)		
		
		#Botões de Remoção e Adição de Itens
		addRemove_Frame = Frame(currentActive_Frame, height=40, bg=WINDOW_BACKGROUND)
		addRemove_Frame.place(x=0, y=BUTTONS_TABLE_Y, relwidth=ADD_REMOVE_BUTTONS_AREA_RELATIVE_WIDTH, height=26)
		
		add_Button = Button(addRemove_Frame, text=ADD_BUTTONS_TEXT, bg=BLUE, fg=WHITE, cursor="hand2", width=3, font=(SMALL_BUTTON_FONT), command=lambda:AddValueWindow().show(currentActive_TreeView))
		add_Button.bind("<Enter>", onMouseIntoBlueButton)
		add_Button.bind("<Leave>", onMouseOutBlueButton)
		add_Button.pack(side="right", padx=SMALL_BUTTON_PADX)
		
		remove_Button = Button(addRemove_Frame, text=REMOVE_BUTTONS_TEXT, bg=RED, fg=WHITE, cursor="hand2", width=3, font=(SMALL_BUTTON_FONT), command=lambda:self.removeItemFromTable(currentActive_TreeView))
		remove_Button.bind("<Enter>", onMouseIntoRedButton)
		remove_Button.bind("<Leave>", onMouseOutRedButton)
		remove_Button.pack(side="right", padx=SMALL_BUTTON_PADX)



		''' Área de Ativos Não Circulantes '''
		noCurrentActives_Frame = Frame(self.bpWindow_Frame, bg=WINDOW_BACKGROUND, height=TABLE_FRAME_HEIGHT)
		noCurrentActives_Frame.place(relx=0.52, y=84, relwidth=TABLE_FRAME_RELATIVE_WIDTH)

		noCurrentActives_Label = Label(noCurrentActives_Frame, text="Ativos Não Circulantes", bg=WINDOW_BACKGROUND, fg=DARK, font=TITLE_FONT)
		noCurrentActives_Label.place(x=0, y=0)

		#Tabela de Ativos Não Circulantes
		noCurrentActives_TreeView = ttk.Treeview(noCurrentActives_Frame, columns=('DESCRICAO', 'VALOR'), show='headings')
		noCurrentActives_TreeView.column("DESCRICAO", anchor="w")
		noCurrentActives_TreeView.column("VALOR", width=90, anchor="center")
		noCurrentActives_TreeView.heading("DESCRICAO", text=TABLE_DESC_COLUMN_TEXT, anchor="w")
		noCurrentActives_TreeView.heading("VALOR", text=TABLE_VALUE_COLUMN_TEXT, anchor="center")
		noCurrentActives_TreeView.place(x=3, y=28, relwidth=TABLE_RELATIVE_WIDTH, height=TABLE_HEIGHT)
		noCurrentActives_TreeView.tag_configure("positive", foreground=BLUE)
		
		#Botões de Remoção e Adição de Itens
		addRemove_Frame = Frame(noCurrentActives_Frame, height=40, bg=WINDOW_BACKGROUND)
		addRemove_Frame.place(x=0, y=BUTTONS_TABLE_Y, relwidth=ADD_REMOVE_BUTTONS_AREA_RELATIVE_WIDTH, height=26)
		
		add_Button = Button(addRemove_Frame, text=ADD_BUTTONS_TEXT, bg=BLUE, fg=WHITE, cursor="hand2", width=3, font=(SMALL_BUTTON_FONT), command=lambda:AddValueWindow().show(noCurrentActives_TreeView))
		add_Button.bind("<Enter>", onMouseIntoBlueButton)
		add_Button.bind("<Leave>", onMouseOutBlueButton)
		add_Button.pack(side="right", padx=SMALL_BUTTON_PADX)
		
		remove_Button = Button(addRemove_Frame, text=REMOVE_BUTTONS_TEXT, bg=RED, fg=WHITE, cursor="hand2", width=3, font=(SMALL_BUTTON_FONT), command=lambda:self.removeItemFromTable(noCurrentActives_TreeView))
		remove_Button.bind("<Enter>", onMouseIntoRedButton)
		remove_Button.bind("<Leave>", onMouseOutRedButton)
		remove_Button.pack(side="right", padx=SMALL_BUTTON_PADX)



		''' Área de Passivos Circulantes '''
		currentPassive_Frame = Frame(self.bpWindow_Frame, bg=WINDOW_BACKGROUND, height=TABLE_FRAME_HEIGHT)
		currentPassive_Frame.place(x=15, y=330, relwidth=TABLE_FRAME_RELATIVE_WIDTH)

		currentPassive_Label = Label(currentPassive_Frame, text="Passivos Circulantes", bg=WINDOW_BACKGROUND, fg=DARK, font=TITLE_FONT)
		currentPassive_Label.place(x=0, y=0)

		#Tabela de Passivos Circulantes
		currentPassive_TreeView = ttk.Treeview(currentPassive_Frame, columns=('DESCRICAO', 'VALOR'), show='headings')
		currentPassive_TreeView.column("DESCRICAO", anchor="w")
		currentPassive_TreeView.column("VALOR", width=90, anchor="center")
		currentPassive_TreeView.heading("DESCRICAO", text=TABLE_DESC_COLUMN_TEXT, anchor="w")
		currentPassive_TreeView.heading("VALOR", text=TABLE_VALUE_COLUMN_TEXT, anchor="center")
		currentPassive_TreeView.place(x=3, y=28, relwidth=TABLE_RELATIVE_WIDTH, height=TABLE_HEIGHT)
		currentPassive_TreeView.tag_configure("negative", foreground=RED)		
		
		#Botões de Remoção e Adição de Itens
		addRemove_Frame = Frame(currentPassive_Frame, height=40, bg=WINDOW_BACKGROUND)
		addRemove_Frame.place(x=0, y=BUTTONS_TABLE_Y, relwidth=ADD_REMOVE_BUTTONS_AREA_RELATIVE_WIDTH, height=26)
		
		add_Button = Button(addRemove_Frame, text=ADD_BUTTONS_TEXT, bg=BLUE, fg=WHITE, cursor="hand2", width=3, font=(SMALL_BUTTON_FONT), command=lambda:AddDebtWindow().show(currentPassive_TreeView))
		add_Button.bind("<Enter>", onMouseIntoBlueButton)
		add_Button.bind("<Leave>", onMouseOutBlueButton)
		add_Button.pack(side="right", padx=SMALL_BUTTON_PADX)
		
		remove_Button = Button(addRemove_Frame, text=REMOVE_BUTTONS_TEXT, bg=RED, fg=WHITE, cursor="hand2", width=3, font=(SMALL_BUTTON_FONT), command=lambda:self.removeItemFromTable(currentPassive_TreeView))
		remove_Button.bind("<Enter>", onMouseIntoRedButton)
		remove_Button.bind("<Leave>", onMouseOutRedButton)
		remove_Button.pack(side="right", padx=SMALL_BUTTON_PADX)



		''' Área de Passivos Não Circulantes '''
		noCurrentPassive_Frame = Frame(self.bpWindow_Frame, bg=WINDOW_BACKGROUND, height=TABLE_FRAME_HEIGHT)
		noCurrentPassive_Frame.place(relx=0.52, y=330, relwidth=TABLE_FRAME_RELATIVE_WIDTH)

		noCurrentPassive_Label = Label(noCurrentPassive_Frame, text="Passivos Não Circulantes", bg=WINDOW_BACKGROUND, fg=DARK, font=TITLE_FONT)
		noCurrentPassive_Label.place(x=0, y=0)

		#Tabela de Passivos Não Circulantes
		noCurrentPassive_TreeView = ttk.Treeview(noCurrentPassive_Frame, columns=('DESCRICAO', 'VALOR'), show='headings')
		noCurrentPassive_TreeView.column("DESCRICAO", anchor="w")
		noCurrentPassive_TreeView.column("VALOR", width=90, anchor="center")
		noCurrentPassive_TreeView.heading("DESCRICAO", text=TABLE_DESC_COLUMN_TEXT, anchor="w")
		noCurrentPassive_TreeView.heading("VALOR", text=TABLE_VALUE_COLUMN_TEXT, anchor="center")
		noCurrentPassive_TreeView.place(x=3, y=28, relwidth=TABLE_RELATIVE_WIDTH, height=TABLE_HEIGHT)
		noCurrentPassive_TreeView.tag_configure("negative", foreground=RED)
		
		#Botões de Remoção e Adição de Itens
		addRemove_Frame = Frame(noCurrentPassive_Frame, height=40, bg=WINDOW_BACKGROUND)
		addRemove_Frame.place(x=0, y=BUTTONS_TABLE_Y, relwidth=ADD_REMOVE_BUTTONS_AREA_RELATIVE_WIDTH, height=26)

		add_Button = Button(addRemove_Frame, text=ADD_BUTTONS_TEXT, bg=BLUE, fg=WHITE, cursor="hand2", width=3, font=(SMALL_BUTTON_FONT), command=lambda:AddDebtWindow().show(noCurrentPassive_TreeView))
		add_Button.bind("<Enter>", onMouseIntoBlueButton)
		add_Button.bind("<Leave>", onMouseOutBlueButton)
		add_Button.pack(side="right", padx=SMALL_BUTTON_PADX)
		
		remove_Button = Button(addRemove_Frame, text=REMOVE_BUTTONS_TEXT, bg=RED, fg=WHITE, cursor="hand2", width=3, font=(SMALL_BUTTON_FONT), command=lambda:self.removeItemFromTable(noCurrentPassive_TreeView))
		remove_Button.bind("<Enter>", onMouseIntoRedButton)
		remove_Button.bind("<Leave>", onMouseOutRedButton)
		remove_Button.pack(side="right", padx=SMALL_BUTTON_PADX)



		''' Botão de Geração de Documento '''
		self.documentGenerator_Frame.pack(fill="x", side="bottom")
		self.documentGenerator_Button.pack(side="right", padx=BUTTON_PADX, pady=BUTTON_PADY)
		self.documentGenerator_Button.bind("<Enter>", onMouseIntoBlueButton)
		self.documentGenerator_Button.bind("<Leave>", onMouseOutBlueButton)
		self.documentGenerator_Button.config(command=lambda:self.generateDocument(startPeriod_DateEntry.get_date(), finishPeriod_DateEntry.get_date(), currentActive_TreeView, noCurrentActives_TreeView, currentPassive_TreeView, noCurrentPassive_TreeView))

#Tela de Geração de DFC
class DfcWindow(MainWindow):
	dfcWindow_Frame = Frame(MainWindow().app, bg=WINDOW_BACKGROUND)
	documentGenerator_Frame = Frame(dfcWindow_Frame, bg=WINDOW_BACKGROUND, height=50)
	documentGenerator_Button = Button(documentGenerator_Frame, text=GENERATE_DOCUMENT_BUTTON_TEXT, fg=WHITE, bg=BLUE, relief="raised", font=BUTTON_FONT, cursor="hand2")

	def generateDocument(self, startDate, finishDate, initialBalance, operationalInputsTable, operationalOutputsTable, financialInputsTable, financialOutputsTable):
		if(len(initialBalance) == 0):
			initialBalance = "R$0,00"

		operationalInputs = {}
		for i in operationalInputsTable.get_children():
			operationalInput = operationalInputsTable.item(i)["values"]
			operationalInputs.update({operationalInput[0]:operationalInput[1]})

		operationalOutputs = {}
		for i in operationalOutputsTable.get_children():
			operationalOutput = operationalOutputsTable.item(i)["values"]
			operationalOutputs.update({operationalOutput[0]:operationalOutput[1]})

		financialInputs = {}
		for i in financialInputsTable.get_children():
			financialInput = financialInputsTable.item(i)["values"]
			financialInputs.update({financialInput[0]:financialInput[1]})

		financialOutputs = {}
		for i in financialOutputsTable.get_children():
			financialOutput = financialOutputsTable.item(i)["values"]
			financialOutputs.update({financialOutput[0]:financialOutput[1]})

		dfc = Dfc(initialBalance, operationalInputs, operationalOutputs, financialInputs, financialOutputs)
		document = Document(startDate, finishDate)
		document.generateDfc(dfc)	

	def removeItemFromTable(self, table):
		for selected in table.selection():
			table.delete(selected)

	def valueWasExistsInTable(self, table, desc):
		descWasExists = False
		for i in table.get_children():
				name = table.item(i)["values"][0]
				if(name == desc):
					descWasExists = True
					break

		return descWasExists

	def remove(self):
		self.dfcWindow_Frame.pack_forget()
		self.documentGenerator_Frame.pack_forget()
		self.documentGenerator_Button.pack_forget()

	def show(self):
		self.dfcWindow_Frame.pack(expand=True, fill="both")	

		''' Área de Definição de Período '''
		period_Label = Label(self.dfcWindow_Frame, text="Período", bg=WINDOW_BACKGROUND, font=TEXT_FONT)
		period_Label.place(x=15, y=10)

		#Início
		startPeriod_DateEntry = DateEntry(self.dfcWindow_Frame, locale='pt_BR', date_pattern='dd/MM/yyyy', bg=WHITE, font=TEXT_FONT)
		startPeriod_DateEntry.place(x=85, y=10)

		#Simples Junção -
		periodJunction_Label = Label(self.dfcWindow_Frame, text="-", bg=WINDOW_BACKGROUND, font=TEXT_FONT)
		periodJunction_Label.place(x=219, y=10)

		#Final
		finishPeriod_DateEntry = DateEntry(self.dfcWindow_Frame, locale='pt_BR', date_pattern='dd/MM/yyyy', bg=WHITE, font=TEXT_FONT)
		finishPeriod_DateEntry.place(x=235, y=10)



		''' Área de Definição de Saldo Inicial '''
		initialBalance_Label = Label(self.dfcWindow_Frame, text="Saldo Inicial", bg=WINDOW_BACKGROUND, font=TEXT_FONT)
		initialBalance_Label.place(x=15, y=47)
		initialBalance_Entry = Entry(self.dfcWindow_Frame, bg=WHITE, fg=GRAY, font=TEXT_FONT, relief="solid")
		initialBalance_Entry.place(x=125, y=47)
		initialBalance_Entry.bind("<KeyRelease>", onTypingMonetaryEntryNegativePermissive)



		''' Área de Entradas Operacionais '''
		operationalInputs_Frame = Frame(self.dfcWindow_Frame, bg=WINDOW_BACKGROUND, height=TABLE_FRAME_HEIGHT)
		operationalInputs_Frame.place(x=15, y=84, relwidth=TABLE_FRAME_RELATIVE_WIDTH)

		operationalInputs_Label = Label(operationalInputs_Frame, text="Entradas Operacionais", bg=WINDOW_BACKGROUND, fg=DARK, font=TITLE_FONT)
		operationalInputs_Label.place(x=0, y=0)

		#Tabela de Entradas Operacionais
		operationalInputs_TreeView = ttk.Treeview(operationalInputs_Frame, columns=('DESCRICAO', 'VALOR'), show='headings')
		operationalInputs_TreeView.column("DESCRICAO", anchor="w")
		operationalInputs_TreeView.column("VALOR", width=90, anchor="center")
		operationalInputs_TreeView.heading("DESCRICAO", text=TABLE_DESC_COLUMN_TEXT, anchor="w")
		operationalInputs_TreeView.heading("VALOR", text=TABLE_VALUE_COLUMN_TEXT, anchor="center")
		operationalInputs_TreeView.place(x=3, y=28, relwidth=TABLE_RELATIVE_WIDTH, height=TABLE_HEIGHT)
		operationalInputs_TreeView.tag_configure("positive", foreground=BLUE)
		
		#Botões de Remoção e Adição de Itens
		addRemove_Frame = Frame(operationalInputs_Frame, height=40, bg=WINDOW_BACKGROUND)
		addRemove_Frame.place(x=0, y=BUTTONS_TABLE_Y, relwidth=ADD_REMOVE_BUTTONS_AREA_RELATIVE_WIDTH, height=26)
		
		add_Button = Button(addRemove_Frame, text=ADD_BUTTONS_TEXT, bg=BLUE, fg=WHITE, cursor="hand2", width=3, font=(SMALL_BUTTON_FONT), command=lambda:AddValueWindow().show(operationalInputs_TreeView))
		add_Button.bind("<Enter>", onMouseIntoBlueButton)
		add_Button.bind("<Leave>", onMouseOutBlueButton)
		add_Button.pack(side="right", padx=SMALL_BUTTON_PADX)
		
		remove_Button = Button(addRemove_Frame, text=REMOVE_BUTTONS_TEXT, bg=RED, fg=WHITE, cursor="hand2", width=3, font=(SMALL_BUTTON_FONT), command=lambda:self.removeItemFromTable(operationalInputs_TreeView))
		remove_Button.bind("<Enter>", onMouseIntoRedButton)
		remove_Button.bind("<Leave>", onMouseOutRedButton)
		remove_Button.pack(side="right", padx=SMALL_BUTTON_PADX)



		''' Área de Saídas Operacionais '''
		operationalOutputs_Frame = Frame(self.dfcWindow_Frame, bg=WINDOW_BACKGROUND, height=TABLE_FRAME_HEIGHT)
		operationalOutputs_Frame.place(relx=0.52, y=84, relwidth=TABLE_FRAME_RELATIVE_WIDTH)

		operationalOutputs_Label = Label(operationalOutputs_Frame, text="Saídas Operacionais", bg=WINDOW_BACKGROUND, fg=DARK, font=TITLE_FONT)
		operationalOutputs_Label.place(x=0, y=0)

		#Tabela de Saídas Operacionais
		operationalOutputs_TreeView = ttk.Treeview(operationalOutputs_Frame, columns=('DESCRICAO', 'VALOR'), show='headings')
		operationalOutputs_TreeView.column("DESCRICAO", anchor="w")
		operationalOutputs_TreeView.column("VALOR", width=90, anchor="center")
		operationalOutputs_TreeView.heading("DESCRICAO", text=TABLE_DESC_COLUMN_TEXT, anchor="w")
		operationalOutputs_TreeView.heading("VALOR", text=TABLE_VALUE_COLUMN_TEXT, anchor="center")
		operationalOutputs_TreeView.place(x=3, y=28, relwidth=TABLE_RELATIVE_WIDTH, height=TABLE_HEIGHT)
		operationalOutputs_TreeView.tag_configure("negative", foreground=RED)
		
		#Botões de Remoção e Adição de Itens
		addRemove_Frame = Frame(operationalOutputs_Frame, height=40, bg=WINDOW_BACKGROUND)
		addRemove_Frame.place(x=0, y=BUTTONS_TABLE_Y, relwidth=ADD_REMOVE_BUTTONS_AREA_RELATIVE_WIDTH, height=26)
		
		add_Button = Button(addRemove_Frame, text=ADD_BUTTONS_TEXT, bg=BLUE, fg=WHITE, cursor="hand2", width=3, font=(SMALL_BUTTON_FONT), command=lambda:AddDebtWindow().show(operationalOutputs_TreeView))
		add_Button.bind("<Enter>", onMouseIntoBlueButton)
		add_Button.bind("<Leave>", onMouseOutBlueButton)
		add_Button.pack(side="right", padx=SMALL_BUTTON_PADX)
		
		remove_Button = Button(addRemove_Frame, text=REMOVE_BUTTONS_TEXT, bg=RED, fg=WHITE, cursor="hand2", width=3, font=(SMALL_BUTTON_FONT), command=lambda:self.removeItemFromTable(operationalOutputs_TreeView))
		remove_Button.bind("<Enter>", onMouseIntoRedButton)
		remove_Button.bind("<Leave>", onMouseOutRedButton)
		remove_Button.pack(side="right", padx=SMALL_BUTTON_PADX)



		''' Área de Entradas Financeiras '''
		financialInput_Frame = Frame(self.dfcWindow_Frame, bg=WINDOW_BACKGROUND, height=TABLE_FRAME_HEIGHT)
		financialInput_Frame.place(x=15, y=330, relwidth=TABLE_FRAME_RELATIVE_WIDTH)

		financialInput_Label = Label(financialInput_Frame, text="Entradas Financeiras", bg=WINDOW_BACKGROUND, fg=DARK, font=TITLE_FONT)
		financialInput_Label.place(x=0, y=0)

		#Tabela de Entradas Financeiras
		financialInput_TreeView = ttk.Treeview(financialInput_Frame, columns=('DESCRICAO', 'VALOR'), show='headings')
		financialInput_TreeView.column("DESCRICAO", anchor="w")
		financialInput_TreeView.column("VALOR", width=90, anchor="center")
		financialInput_TreeView.heading("DESCRICAO", text=TABLE_DESC_COLUMN_TEXT, anchor="w")
		financialInput_TreeView.heading("VALOR", text=TABLE_VALUE_COLUMN_TEXT, anchor="center")
		financialInput_TreeView.place(x=3, y=28, relwidth=TABLE_RELATIVE_WIDTH, height=TABLE_HEIGHT)
		financialInput_TreeView.tag_configure("positive", foreground=BLUE)		
		
		#Botões de Remoção e Adição de Itens
		addRemove_Frame = Frame(financialInput_Frame, height=40, bg=WINDOW_BACKGROUND)
		addRemove_Frame.place(x=0, y=BUTTONS_TABLE_Y, relwidth=ADD_REMOVE_BUTTONS_AREA_RELATIVE_WIDTH, height=26)
		
		add_Button = Button(addRemove_Frame, text=ADD_BUTTONS_TEXT, bg=BLUE, fg=WHITE, cursor="hand2", width=3, font=(SMALL_BUTTON_FONT), command=lambda:AddValueWindow().show(financialInput_TreeView))
		add_Button.bind("<Enter>", onMouseIntoBlueButton)
		add_Button.bind("<Leave>", onMouseOutBlueButton)
		add_Button.pack(side="right", padx=SMALL_BUTTON_PADX)
		
		remove_Button = Button(addRemove_Frame, text=REMOVE_BUTTONS_TEXT, bg=RED, fg=WHITE, cursor="hand2", width=3, font=(SMALL_BUTTON_FONT), command=lambda:self.removeItemFromTable(financialInput_TreeView))
		remove_Button.bind("<Enter>", onMouseIntoRedButton)
		remove_Button.bind("<Leave>", onMouseOutRedButton)
		remove_Button.pack(side="right", padx=SMALL_BUTTON_PADX)



		''' Área de Saídas Financeiras '''
		financialOutputs_Frame = Frame(self.dfcWindow_Frame, bg=WINDOW_BACKGROUND, height=TABLE_FRAME_HEIGHT)
		financialOutputs_Frame.place(relx=0.52, y=330, relwidth=TABLE_FRAME_RELATIVE_WIDTH)

		noCurrentPassive_Label = Label(financialOutputs_Frame, text="Saídas Financeiras", bg=WINDOW_BACKGROUND, fg=DARK, font=TITLE_FONT)
		noCurrentPassive_Label.place(x=0, y=0)

		#Tabela de Saídas Financeiras
		financialOutputs_TreeView = ttk.Treeview(financialOutputs_Frame, columns=('DESCRICAO', 'VALOR'), show='headings')
		financialOutputs_TreeView.column("DESCRICAO", anchor="w")
		financialOutputs_TreeView.column("VALOR", width=90, anchor="center")
		financialOutputs_TreeView.heading("DESCRICAO", text=TABLE_DESC_COLUMN_TEXT, anchor="w")
		financialOutputs_TreeView.heading("VALOR", text=TABLE_VALUE_COLUMN_TEXT, anchor="center")
		financialOutputs_TreeView.place(x=3, y=28, relwidth=TABLE_RELATIVE_WIDTH, height=TABLE_HEIGHT)
		financialOutputs_TreeView.tag_configure("negative", foreground=RED)
		
		#Botões de Remoção e Adição de Itens
		addRemove_Frame = Frame(financialOutputs_Frame, height=40, bg=WINDOW_BACKGROUND)
		addRemove_Frame.place(x=0, y=BUTTONS_TABLE_Y, relwidth=ADD_REMOVE_BUTTONS_AREA_RELATIVE_WIDTH, height=26)

		add_Button = Button(addRemove_Frame, text=ADD_BUTTONS_TEXT, bg=BLUE, fg=WHITE, cursor="hand2", width=3, font=(SMALL_BUTTON_FONT), command=lambda:AddDebtWindow().show(financialOutputs_TreeView))
		add_Button.bind("<Enter>", onMouseIntoBlueButton)
		add_Button.bind("<Leave>", onMouseOutBlueButton)
		add_Button.pack(side="right", padx=SMALL_BUTTON_PADX)
		
		remove_Button = Button(addRemove_Frame, text=REMOVE_BUTTONS_TEXT, bg=RED, fg=WHITE, cursor="hand2", width=3, font=(SMALL_BUTTON_FONT), command=lambda:self.removeItemFromTable(financialOutputs_TreeView))
		remove_Button.bind("<Enter>", onMouseIntoRedButton)
		remove_Button.bind("<Leave>", onMouseOutRedButton)
		remove_Button.pack(side="right", padx=SMALL_BUTTON_PADX)



		''' Botão de Geração de Documento '''
		self.documentGenerator_Frame.pack(fill="x", side="bottom")
		self.documentGenerator_Button.pack(side="right", padx=BUTTON_PADX, pady=BUTTON_PADY)
		self.documentGenerator_Button.bind("<Enter>", onMouseIntoBlueButton)
		self.documentGenerator_Button.bind("<Leave>", onMouseOutBlueButton)
		self.documentGenerator_Button.config(command=lambda:self.generateDocument(startPeriod_DateEntry.get_date(), finishPeriod_DateEntry.get_date(), initialBalance_Entry.get(), operationalInputs_TreeView, operationalOutputs_TreeView, financialInput_TreeView, financialOutputs_TreeView))

''' POP-UPS '''
#Janela de Adição de Débitos
class AddDebtWindow(MainWindow):
	def addDebtToTable(self, table, desc, value):
		#Verifica se o campo DESCRIÇÃO foi preenchido
		if not(len(desc.replace(" ", "")) == 0):
			#Verifica se há outro valor na tabela com a mesma descrição
			if DreWindow().valueWasExistsInTable(table, desc):
				cont=1
				while(True):
					if DreWindow().valueWasExistsInTable(table, desc+"_"+str(cont)):
						cont+=1
					else:
						break

				desc+="_"+str(cont)

			if(len(value) == 0):
				value = "R$0,00"

			table.insert("", 'end', values=(desc, "-"+str(value)), tag="negative")
		else:
			exceptions.input_errors.showMessageError(1)

	def show(self, table):
		modal = Toplevel(MainWindow().app)
		modal.title(ADD_DEBT_WINDOW_TITLE)
		modal.configure(bg=WINDOW_BACKGROUND)
		modal.geometry(ADD_DEBT_WINDOW_RESOLUTION)
		modal.resizable(False, False)
		modal.grab_set()

		#Área de Descrição
		description_Label = Label(modal, text=TABLE_DESC_COLUMN_TEXT, bg=WINDOW_BACKGROUND, font=TEXT_FONT)
		description_Label.place(x=10, y=10)

		description_Entry = Entry(modal, bg=WHITE, fg=GRAY, font=TEXT_FONT, relief="solid")
		description_Entry.place(x=96, y=10, width=230)

		#Área de Valor
		value_Label = Label(modal, text="Valor", bg=WINDOW_BACKGROUND, font=TEXT_FONT)
		value_Label.place(x=10, y=43)

		value_Entry = Entry(modal, bg=WHITE, fg=GRAY, font=TEXT_FONT, relief="solid")
		value_Entry.place(x=96, y=43)
		value_Entry.bind("<KeyRelease>", onTypingMonetaryEntry)

		addItem_Button = Button(modal, text="ADICIONAR", fg=WHITE, bg=BLUE, relief="raised", font=BUTTON_FONT, cursor="hand2", command=lambda:self.addDebtToTable(table, description_Entry.get(), value_Entry.get()))
		addItem_Button.pack(side="bottom", anchor="e", padx=BUTTON_PADX, pady=BUTTON_PADY)
		addItem_Button.bind("<Enter>", onMouseIntoBlueButton)
		addItem_Button.bind("<Leave>", onMouseOutBlueButton)

#Janela de Adição de Valores (Positivos)
class AddValueWindow(MainWindow):
	def addValueToTable(self, table, desc, value):
		#Verifica se o campo DESCRIÇÃO foi preenchido
		if not(len(desc.replace(" ", "")) == 0):
			#Verifica se há outro valor na tabela com a mesma descrição
			if DreWindow().valueWasExistsInTable(table, desc):
				cont=1
				while(True):
					if DreWindow().valueWasExistsInTable(table, desc+"_"+str(cont)):
						cont+=1
					else:
						break

				desc+="_"+str(cont)

			if(len(value) == 0):
				value = "R$0,00"

			table.insert("", 'end', values=(desc, "+"+str(value)), tag="positive")
		else:
			exceptions.input_errors.showMessageError(1)

	def show(self, table):
		modal = Toplevel(MainWindow().app)
		modal.title(ADD_VALUE_WINDOW_TITLE)
		modal.configure(bg=WINDOW_BACKGROUND)
		modal.geometry(ADD_DEBT_WINDOW_RESOLUTION)
		modal.resizable(False, False)
		modal.grab_set()

		#Área de Descrição
		description_Label = Label(modal, text=TABLE_DESC_COLUMN_TEXT, bg=WINDOW_BACKGROUND, font=TEXT_FONT)
		description_Label.place(x=10, y=10)

		description_Entry = Entry(modal, bg=WHITE, fg=GRAY, font=TEXT_FONT, relief="solid")
		description_Entry.place(x=96, y=10, width=230)

		#Área de Valor
		value_Label = Label(modal, text="Valor", bg=WINDOW_BACKGROUND, font=TEXT_FONT)
		value_Label.place(x=10, y=43)

		value_Entry = Entry(modal, bg=WHITE, fg=GRAY, font=TEXT_FONT, relief="solid")
		value_Entry.place(x=96, y=43)
		value_Entry.bind("<KeyRelease>", onTypingMonetaryEntry)

		addItem_Button = Button(modal, text="ADICIONAR", fg=WHITE, bg=BLUE, relief="raised", font=BUTTON_FONT, cursor="hand2", command=lambda:self.addValueToTable(table, description_Entry.get(), value_Entry.get()))
		addItem_Button.pack(side="bottom", anchor="e", padx=BUTTON_PADX, pady=BUTTON_PADY)
		addItem_Button.bind("<Enter>", onMouseIntoBlueButton)
		addItem_Button.bind("<Leave>", onMouseOutBlueButton)

#Janela de Adição de Valores (Positivos e Negativos)
class AddMovementWindow(MainWindow):
	def addMovementToTable(self, table, desc, value, type):
		#Verifica se o campo DESCRIÇÃO foi preenchido
		if not(len(desc.replace(" ", "")) == 0):
			#Verifica se há outro valor na tabela com a mesma descrição
			if DreWindow().valueWasExistsInTable(table, desc):
				cont=1
				while(True):
					if DreWindow().valueWasExistsInTable(table, desc+"_"+str(cont)):
						cont+=1
					else:
						break

				desc+="_"+str(cont)

			if(len(value) == 0):
				value = "R$0,00"
			if(type == "Receita"):
				table.insert("", 'end', values=(desc, "+"+str(value)), tag="positive")
			else:
				table.insert("", 'end', values=(desc, "-"+str(value)), tag="negative")
		else:
			exceptions.input_errors.showMessageError(1)

	def show(self, table):
		modal = Toplevel(MainWindow().app)
		modal.title(ADD_MOVEMENT_WINDOW_TITLE)
		modal.configure(bg=WINDOW_BACKGROUND)
		modal.geometry(ADD_MOVEMENT_WINDOW_RESOLUTION)
		modal.resizable(False, False)
		modal.grab_set()

		#Área de Descrição
		description_Label = Label(modal, text=TABLE_DESC_COLUMN_TEXT, bg=WINDOW_BACKGROUND, font=TEXT_FONT)
		description_Label.place(x=10, y=10)

		description_Entry = Entry(modal, bg=WHITE, fg=GRAY, font=TEXT_FONT, relief="solid")
		description_Entry.place(x=96, y=10, width=230)

		#Área de Valor
		value_Label = Label(modal, text="Valor", bg=WINDOW_BACKGROUND, font=TEXT_FONT)
		value_Label.place(x=10, y=43)

		value_Entry = Entry(modal, bg=WHITE, fg=GRAY, font=TEXT_FONT, relief="solid")
		value_Entry.place(x=96, y=43)
		value_Entry.bind("<KeyRelease>", onTypingMonetaryEntry)

		#Área de Natureza
		type_Label = Label(modal, text="Natureza", bg=WINDOW_BACKGROUND, font=TEXT_FONT)
		type_Label.place(x=10, y=76)

		type_Combo = ttk.Combobox(modal, values=['Receita', 'Dívida'], state="readonly", font=TEXT_FONT)
		type_Combo.set('Receita')
		type_Combo.place(x=96, y=76, width=COMBO_WIDTH)

		addItem_Button = Button(modal, text="ADICIONAR", fg=WHITE, bg=BLUE, relief="raised", font=BUTTON_FONT, cursor="hand2", command=lambda:self.addMovementToTable(table, description_Entry.get(), value_Entry.get(), type_Combo.get()))
		addItem_Button.pack(side="bottom", anchor="e", padx=BUTTON_PADX, pady=BUTTON_PADY)
		addItem_Button.bind("<Enter>", onMouseIntoBlueButton)
		addItem_Button.bind("<Leave>", onMouseOutBlueButton)

#Tela de Ajuda
class HelpWindow(MainWindow):
	def show(self):
		modal = Toplevel(MainWindow().app)
		modal.title(HELP_WINDOW_TITLE)
		modal.configure(bg=WINDOW_BACKGROUND)
		modal.geometry(HELP_WINDOW_RESOLUTION)
		modal.resizable(False, False)
		modal.grab_set()

		#Título
		title_Frame = Frame(modal, bg=WINDOW_BACKGROUND)
		title_Frame.pack(side="top", fill="x")
		title_Label = Label(title_Frame, text=TITLE_TEXT, bg=WINDOW_BACKGROUND, fg=DARK, font=(HELP_TITLE_FONT), anchor="center")
		title_Label.pack(padx=5, pady=HELP_TITTLE_PADY)

		''' Textos '''
		text_Frame = Frame(modal, bg=WINDOW_BACKGROUND)
		text_Frame.pack(side="top", pady=HELP_TEXT_PADY)

		text_Label = Message(text_Frame, text=HELP_TEXT, bg=WINDOW_BACKGROUND, width=520, justify="center", font=(HELP_TEXT_FONT))
		text_Label.pack(fill="x", pady=HELP_TEXT_PADY)

		ok_Button = Button(modal, text="OK", fg=WHITE, bg=BLUE, relief="raised", font=BUTTON_FONT, cursor="hand2", width=5, command=lambda: modal.destroy())
		ok_Button.pack(side="bottom", anchor="e", padx=BUTTON_PADX, pady=BUTTON_PADY)
		ok_Button.bind("<Enter>", onMouseIntoBlueButton)
		ok_Button.bind("<Leave>", onMouseOutBlueButton)