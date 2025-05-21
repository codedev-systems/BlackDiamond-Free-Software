from config.config import *
from config.masks import *
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import *
from entities.Dre import *
from tkinter import filedialog
from tkinter import messagebox

class Document():
	startDate = ""
	finishDate = ""

	def __init__(self, startDate, finishDate):
		self.startDate = f"{startDate.strftime('%d/%m/%Y')}" #Data Inicial da Competência
		self.finishDate = f"{finishDate.strftime('%d/%m/%Y')}" #Data Final da Competência
	
	#Seleciona o nome do documento e onde o usuário quer salvá-lo
	def setDocumentName(self, defaultName):
		nameFile = filedialog.asksaveasfilename(defaultextension=".pdf",
                                             filetypes=[("Documento PDF (*.pdf)", "*.pdf")],
                                             initialfile=defaultName)
		return nameFile

	#Gera documento de DRE
	def generateDre(self, dre):
		try:
			file = self.setDocumentName("DRE")
			pdf = canvas.Canvas(file, pagesize=A4)
			width, height = A4

			''' Cabeçalho '''
			pdf.setFillColor(HexColor(BLACK))
			pdf.rect(0, height - 80, width, 80, fill=1, stroke=0)

			#Título do Documento
			pdf.setFont("Helvetica-Bold", 20)
			pdf.setFillColor(white)
			pdf.drawString(99, height - 35, "Demonstrativo de Resultado do Exercício")
			pdf.drawString(270, height - 58, "(DRE)")

			

			''' Área de Período '''
			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(black)
			pdf.drawString(20, height - 110, "Período: ")

			pdf.setFont("Helvetica", 14)
			pdf.setFillColor(black)
			pdf.drawString(82, height - 110, self.startDate+" - ")

			pdf.setFont("Helvetica", 14)
			pdf.setFillColor(black)
			pdf.drawString(164, height - 110, self.finishDate)



			''' Área da Tabela '''
			#Receita Bruta
			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(black)
			pdf.drawString(20, height - 150, "Receita Bruta")

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(black)
			pdf.drawString(430, height - 150, monetaryMask(dre.grossRevenue))

			pdf.setLineWidth(1)
			pdf.line(20, height-155, width-20, height-155)

			#Receita Líquida
			y = 184
			pdf.setFillColor(HexColor(CLEAN_GRAY))
			pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(black)
			pdf.drawString(30, height - (y-8), "Receita Líquida")

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(black)
			if(dre.liquidRevenue < 0):
				pdf.drawString(430, height - (y-8), "-"+monetaryMask(dre.liquidRevenue))
			else:
				pdf.drawString(430, height - (y-8), monetaryMask(dre.liquidRevenue))
			y+=28

			#Deduções
			if(len(dre.dedutions) == 0):
				if height - y < 60:
					pdf.showPage()
					y = 60
				pdf.setFillColor(white)
				pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

				pdf.setFont("Helvetica", 14)
				pdf.setFillColor(HexColor(RED))
				pdf.drawString(80, height - (y-8), "-")

				pdf.setFont("Helvetica", 14)
				pdf.setFillColor(HexColor(RED))
				pdf.drawString(430, height - (y-8), "-")
				y+=28
			else:
				for dedution in dre.dedutions.keys():
					if height - y < 60:
					    pdf.showPage()
					    y = 60	
					pdf.setFillColor(white)
					pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

					pdf.setFont("Helvetica", 14)
					pdf.setFillColor(HexColor(RED))
					pdf.drawString(80, height - (y-8), dedution)

					pdf.setFont("Helvetica", 14)
					pdf.setFillColor(HexColor(RED))
					pdf.drawString(430, height - (y-8), dre.dedutions.get(dedution))
					y+=28

			#Lucro Bruto
			if height - y < 60:
			    pdf.showPage()
			    y = 60
			pdf.setFillColor(HexColor(CLEAN_GRAY))
			pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(black)
			pdf.drawString(30, height - (y-8), "Lucro Bruto")

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(black)
			if(dre.grossProfit < 0):
				pdf.drawString(430, height - (y-8), "-"+monetaryMask(dre.grossProfit))
			else:
				pdf.drawString(430, height - (y-8), monetaryMask(dre.grossProfit))
			y+=28

			#CMVs e CSPs
			if(len(dre.cmvs) == 0):
				if height - y < 60:
				    pdf.showPage()
				    y = 60
				pdf.setFillColor(white)
				pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

				pdf.setFont("Helvetica", 14)
				pdf.setFillColor(HexColor(RED))
				pdf.drawString(80, height - (y-8), "-")

				pdf.setFont("Helvetica", 14)
				pdf.setFillColor(HexColor(RED))
				pdf.drawString(430, height - (y-8), "-")
				y+=28
			else:
				for cmv in dre.cmvs.keys():
					if height - y < 60:
					    pdf.showPage()
					    y = 60
					pdf.setFillColor(white)
					pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

					pdf.setFont("Helvetica", 14)
					pdf.setFillColor(HexColor(RED))
					pdf.drawString(80, height - (y-8), cmv)

					pdf.setFont("Helvetica", 14)
					pdf.setFillColor(HexColor(RED))
					pdf.drawString(430, height - (y-8), dre.cmvs.get(cmv))
					y+=28

			#Lucro Operacional
			if height - y < 60:
			    pdf.showPage()
			    y = 60
			pdf.setFillColor(HexColor(CLEAN_GRAY))
			pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(black)
			pdf.drawString(30, height - (y-8), "Lucro Operacional")

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(black)
			if(dre.operationalProfit < 0):
				pdf.drawString(430, height - (y-8), "-"+monetaryMask(dre.operationalProfit))
			else:
				pdf.drawString(430, height - (y-8), monetaryMask(dre.operationalProfit))
			y+=28

			#Total Receitas Operacionais
			if height - y < 60:
			    pdf.showPage()
			    y = 60
			pdf.setFillColor(white)
			pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(HexColor(BLUE))
			pdf.drawString(50, height - (y-8), "Receitas Operacionais")

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(HexColor(BLUE))
			pdf.drawString(430, height - (y-8), "+"+monetaryMask(dre.totalOperationalRevenue))
			y+=28

			#Receitas Operacionais
			if(len(dre.operationalRevenues) == 0):
				if height - y < 60:
				    pdf.showPage()
				    y = 60
				pdf.setFillColor(white)
				pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

				pdf.setFont("Helvetica", 14)
				pdf.setFillColor(HexColor(BLUE))
				pdf.drawString(80, height - (y-8), "-")

				pdf.setFont("Helvetica", 14)
				pdf.setFillColor(HexColor(BLUE))
				pdf.drawString(430, height - (y-8), "-")
				y+=28
			else:
				for revenue in dre.operationalRevenues.keys():
					if height - y < 60:
					    pdf.showPage()
					    y = 60
					pdf.setFillColor(white)
					pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

					pdf.setFont("Helvetica", 14)
					pdf.setFillColor(HexColor(BLUE))
					pdf.drawString(80, height - (y-8), revenue)

					pdf.setFont("Helvetica", 14)
					pdf.setFillColor(HexColor(BLUE))
					pdf.drawString(430, height - (y-8), dre.operationalRevenues.get(revenue))
					y+=28

			#Total Despesas Operacionais
			if height - y < 60:
			    pdf.showPage()
			    y = 60
			pdf.setFillColor(white)
			pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(HexColor(RED))
			pdf.drawString(50, height - (y-8), "Despesas Operacionais")

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(HexColor(RED))
			pdf.drawString(430, height - (y-8), "-"+monetaryMask(dre.totalOperationalDebt))
			y+=28

			#Despesas Operacionais
			if(len(dre.operationalDebts) == 0):
				if height - y < 60:
				    pdf.showPage()
				    y = 60
				pdf.setFillColor(white)
				pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

				pdf.setFont("Helvetica", 14)
				pdf.setFillColor(HexColor(RED))
				pdf.drawString(80, height - (y-8), "-")

				pdf.setFont("Helvetica", 14)
				pdf.setFillColor(HexColor(RED))
				pdf.drawString(430, height - (y-8), "-")
				y+=28

			else:
				for debt in dre.operationalDebts.keys():
					if height - y < 60:
					    pdf.showPage()
					    y = 60
					pdf.setFillColor(white)
					pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

					pdf.setFont("Helvetica", 14)
					pdf.setFillColor(HexColor(RED))
					pdf.drawString(80, height - (y-8), debt)

					pdf.setFont("Helvetica", 14)
					pdf.setFillColor(HexColor(RED))
					pdf.drawString(430, height - (y-8), dre.operationalDebts.get(debt))
					y+=28

			#LAIR
			if height - y < 60:
			    pdf.showPage()
			    y = 60
			pdf.setFillColor(HexColor(CLEAN_GRAY))
			pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(black)
			pdf.drawString(30, height - (y-8), "Lucro antes do Imposto de Renda (LAIR)")

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(black)
			if(dre.lair < 0):
				pdf.drawString(430, height - (y-8), "-"+monetaryMask(dre.lair))
			else:
				pdf.drawString(430, height - (y-8), monetaryMask(dre.lair))
			y+=28

			#Total Receitas Financeiras
			if height - y < 60:
			    pdf.showPage()
			    y = 60
			pdf.setFillColor(white)
			pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(HexColor(BLUE))
			pdf.drawString(50, height - (y-8), "Receitas Financeiras")

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(HexColor(BLUE))
			pdf.drawString(430, height - (y-8), "+"+monetaryMask(dre.totalFinancialRevenue))
			y+=28

			#Receitas Financeiras
			if(len(dre.financialRevenues) == 0):
				if height - y < 60:
				    pdf.showPage()
				    y = 60
				pdf.setFillColor(white)
				pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

				pdf.setFont("Helvetica", 14)
				pdf.setFillColor(HexColor(BLUE))
				pdf.drawString(80, height - (y-8), "-")

				pdf.setFont("Helvetica", 14)
				pdf.setFillColor(HexColor(BLUE))
				pdf.drawString(430, height - (y-8), "-")
				y+=28

			else:
				for revenue in dre.financialRevenues.keys():
					if height - y < 60:
					    pdf.showPage()
					    y = 60
					pdf.setFillColor(white)
					pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

					pdf.setFont("Helvetica", 14)
					pdf.setFillColor(HexColor(BLUE))
					pdf.drawString(80, height - (y-8), revenue)

					pdf.setFont("Helvetica", 14)
					pdf.setFillColor(HexColor(BLUE))
					pdf.drawString(430, height - (y-8), dre.financialRevenues.get(revenue))
					y+=28

			#Total Despesas Financeiras
			if height - y < 60:
			    pdf.showPage()
			    y = 60
			pdf.setFillColor(white)
			pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(HexColor(RED))
			pdf.drawString(50, height - (y-8), "Despesas Financeiras")

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(HexColor(RED))
			pdf.drawString(430, height - (y-8), "-"+monetaryMask(dre.totalFinancialDebt))
			y+=28

			#Despesas Financeiras
			if(len(dre.financialDebts) == 0):
				if height - y < 60:
				    pdf.showPage()
				    y = 60
				pdf.setFillColor(white)
				pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

				pdf.setFont("Helvetica", 14)
				pdf.setFillColor(HexColor(RED))
				pdf.drawString(80, height - (y-8), "-")

				pdf.setFont("Helvetica", 14)
				pdf.setFillColor(HexColor(RED))
				pdf.drawString(430, height - (y-8), "-")
				y+=28
			else:
				for debt in dre.financialDebts.keys():
					if height - y < 60:
					    pdf.showPage()
					    y = 60
					pdf.setFillColor(white)
					pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

					pdf.setFont("Helvetica", 14)
					pdf.setFillColor(HexColor(RED))
					pdf.drawString(80, height - (y-8), debt)

					pdf.setFont("Helvetica", 14)
					pdf.setFillColor(HexColor(RED))
					pdf.drawString(430, height - (y-8), dre.financialDebts.get(debt))
					y+=28

			#Lucro Líquido
			if height - y < 60:
			    pdf.showPage()
			    y = 60
			pdf.setFillColor(HexColor(CLEAN_GRAY))
			pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(black)
			pdf.drawString(30, height - (y-8), "Lucro Líquido")

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(black)
			if(dre.liquidProfit < 0):
				pdf.drawString(430, height - (y-8), "-"+monetaryMask(dre.liquidProfit))
			else:
				pdf.drawString(430, height - (y-8), monetaryMask(dre.liquidProfit))
			y+=28

			#Provisão para IR e CSLL
			if height - y < 60:
			    pdf.showPage()
			    y = 60
			pdf.setFillColor(white)
			pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

			pdf.setFont("Helvetica", 14)
			pdf.setFillColor(HexColor(RED))
			pdf.drawString(80, height - (y-8), "Provisão para IR e CSLL")

			pdf.setFont("Helvetica", 14)
			pdf.setFillColor(HexColor(RED))
			pdf.drawString(430, height - (y-8), "-"+monetaryMask(dre.irCsllProvision))

			pdf.save()
			messagebox.showinfo(title="Arquivo Salvo com Sucesso", message="O documento foi gerado com sucesso!")
		except:	
			print("ERROR")

	#Gera documento de BP
	def generateBp(self, bp):
		try:
			file = self.setDocumentName("BP")
			pdf = canvas.Canvas(file, pagesize=A4)
			width, height = A4

			''' Cabeçalho '''
			pdf.setFillColor(HexColor(BLACK))
			pdf.rect(0, height - 80, width, 80, fill=1, stroke=0)

			#Título do Documento
			pdf.setFont("Helvetica-Bold", 20)
			pdf.setFillColor(white)
			pdf.drawString(205, height - 35, "Balanço Patrimonial")
			pdf.drawString(280, height - 58, "(BP)")

			

			''' Área de Período '''
			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(black)
			pdf.drawString(20, height - 110, "Período: ")

			pdf.setFont("Helvetica", 14)
			pdf.setFillColor(black)
			pdf.drawString(82, height - 110, self.startDate+" - ")

			pdf.setFont("Helvetica", 14)
			pdf.setFillColor(black)
			pdf.drawString(164, height - 110, self.finishDate)



			''' Área da Tabela '''
			#Patrimônio Líquido
			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(black)
			pdf.drawString(20, height - 150, "Patrimônio Líquido")

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(black)
			if bp.netWorth < 0:
				pdf.drawString(430, height - 150, "-"+monetaryMask(bp.netWorth))
			else:
				pdf.drawString(430, height - 150, monetaryMask(bp.netWorth))

			pdf.setLineWidth(1)
			pdf.line(20, height-155, width-20, height-155)

			#Ativo Total
			y = 184
			pdf.setFillColor(HexColor(CLEAN_GRAY))
			pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(black)
			pdf.drawString(30, height - (y-8), "Ativo Total")

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(black)
			pdf.drawString(430, height - (y-8), monetaryMask(bp.totalActive))
			y+=28

			#Ativo Circulante Total
			pdf.setFillColor(white)
			pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(HexColor(BLUE))
			pdf.drawString(50, height - (y-8), "Ativo Circulante")

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(HexColor(BLUE))
			pdf.drawString(430, height - (y-8), "+"+monetaryMask(bp.totalCurrentActive))
			y+=28

			#Ativos Circulantes
			if(len(bp.currentActives) == 0):
				if height - y < 60:
				    pdf.showPage()
				    y = 60
				pdf.setFillColor(white)
				pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

				pdf.setFont("Helvetica", 14)
				pdf.setFillColor(HexColor(BLUE))
				pdf.drawString(80, height - (y-8), "-")

				pdf.setFont("Helvetica", 14)
				pdf.setFillColor(HexColor(BLUE))
				pdf.drawString(430, height - (y-8), "-")
				y+=28

			else:
				for currentActive in bp.currentActives.keys():
					if height - y < 60:
					    pdf.showPage()
					    y = 60
					pdf.setFillColor(white)
					pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

					pdf.setFont("Helvetica", 14)
					pdf.setFillColor(HexColor(BLUE))
					pdf.drawString(80, height - (y-8), currentActive)

					pdf.setFont("Helvetica", 14)
					pdf.setFillColor(HexColor(BLUE))
					pdf.drawString(430, height - (y-8), bp.currentActives.get(currentActive))
					y+=28

			#Ativo Não Circulante Total
			pdf.setFillColor(white)
			pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(HexColor(BLUE))
			pdf.drawString(50, height - (y-8), "Ativo Não Circulante")

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(HexColor(BLUE))
			pdf.drawString(430, height - (y-8), "+"+monetaryMask(bp.totalNoCurrentActive))
			y+=28

			#Ativos Não Circulantes
			if(len(bp.noCurrentActives) == 0):
				if height - y < 60:
				    pdf.showPage()
				    y = 60
				pdf.setFillColor(white)
				pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

				pdf.setFont("Helvetica", 14)
				pdf.setFillColor(HexColor(BLUE))
				pdf.drawString(80, height - (y-8), "-")

				pdf.setFont("Helvetica", 14)
				pdf.setFillColor(HexColor(BLUE))
				pdf.drawString(430, height - (y-8), "-")
				y+=28

			else:
				for noCurrentActive in bp.noCurrentActives.keys():
					if height - y < 60:
					    pdf.showPage()
					    y = 60
					pdf.setFillColor(white)
					pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

					pdf.setFont("Helvetica", 14)
					pdf.setFillColor(HexColor(BLUE))
					pdf.drawString(80, height - (y-8), noCurrentActive)

					pdf.setFont("Helvetica", 14)
					pdf.setFillColor(HexColor(BLUE))
					pdf.drawString(430, height - (y-8), bp.noCurrentActives.get(noCurrentActive))
					y+=28

			#Passivo Total
			pdf.setFillColor(HexColor(CLEAN_GRAY))
			pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(black)
			pdf.drawString(30, height - (y-8), "Passivo Total")

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(black)
			pdf.drawString(430, height - (y-8), "-"+monetaryMask(bp.totalPassive))
			y+=28

			#Passivo Circulante Total
			pdf.setFillColor(white)
			pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(HexColor(RED))
			pdf.drawString(50, height - (y-8), "Passivo Circulante")

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(HexColor(RED))
			pdf.drawString(430, height - (y-8), "-"+monetaryMask(bp.totalCurrentPassive))
			y+=28

			#Passivos Circulantes
			if(len(bp.currentPassives) == 0):
				if height - y < 60:
				    pdf.showPage()
				    y = 60
				pdf.setFillColor(white)
				pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

				pdf.setFont("Helvetica", 14)
				pdf.setFillColor(HexColor(RED))
				pdf.drawString(80, height - (y-8), "-")

				pdf.setFont("Helvetica", 14)
				pdf.setFillColor(HexColor(RED))
				pdf.drawString(430, height - (y-8), "-")
				y+=28

			else:
				for currentPassive in bp.currentPassives.keys():
					if height - y < 60:
					    pdf.showPage()
					    y = 60
					pdf.setFillColor(white)
					pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

					pdf.setFont("Helvetica", 14)
					pdf.setFillColor(HexColor(RED))
					pdf.drawString(80, height - (y-8), currentPassive)

					pdf.setFont("Helvetica", 14)
					pdf.setFillColor(HexColor(RED))
					pdf.drawString(430, height - (y-8), bp.currentPassives.get(currentPassive))
					y+=28

			#Passivo Não Circulante Total
			pdf.setFillColor(white)
			pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(HexColor(RED))
			pdf.drawString(50, height - (y-8), "Passivo Não Circulante")

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(HexColor(RED))
			pdf.drawString(430, height - (y-8), "-"+monetaryMask(bp.totalNoCurrentPassive))
			y+=28

			#Passivos Não Circulantes
			if(len(bp.noCurrentPassives) == 0):
				if height - y < 60:
				    pdf.showPage()
				    y = 60
				pdf.setFillColor(white)
				pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

				pdf.setFont("Helvetica", 14)
				pdf.setFillColor(HexColor(RED))
				pdf.drawString(80, height - (y-8), "-")

				pdf.setFont("Helvetica", 14)
				pdf.setFillColor(HexColor(RED))
				pdf.drawString(430, height - (y-8), "-")
				y+=28

			else:
				for noCurrentPassive in bp.noCurrentPassives.keys():
					if height - y < 60:
					    pdf.showPage()
					    y = 60
					pdf.setFillColor(white)
					pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

					pdf.setFont("Helvetica", 14)
					pdf.setFillColor(HexColor(RED))
					pdf.drawString(80, height - (y-8), noCurrentPassive)

					pdf.setFont("Helvetica", 14)
					pdf.setFillColor(HexColor(RED))
					pdf.drawString(430, height - (y-8), bp.noCurrentPassives.get(noCurrentPassive))
					y+=28

			#CGL (Capital de Giro Líquido)
			pdf.setFillColor(HexColor(CLEAN_GRAY))
			pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(black)
			pdf.drawString(30, height - (y-8), "Capital de Giro Líquido (CGL)")

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(black)
			if bp.cgl < 0:
				pdf.drawString(430, height - (y-8), "-"+monetaryMask(bp.cgl))
			else:
				pdf.drawString(430, height - (y-8), monetaryMask(bp.cgl))
			y+=28

			pdf.save()
			messagebox.showinfo(title="Arquivo Salvo com Sucesso", message="O documento foi gerado com sucesso!")
		except:
			print("ERROR")

	#Gera documento  de DFC
	def generateDfc(self, dfc):
		try:
			file = self.setDocumentName("DFC")
			pdf = canvas.Canvas(file, pagesize=A4)
			width, height = A4

			''' Cabeçalho '''
			pdf.setFillColor(HexColor(BLACK))
			pdf.rect(0, height - 80, width, 80, fill=1, stroke=0)

			#Título do Documento
			pdf.setFont("Helvetica-Bold", 20)
			pdf.setFillColor(white)
			pdf.drawString(130, height - 35, "Demonstrativo de Fluxo de Caixa")
			pdf.drawString(270, height - 58, "(DFC)")

			

			''' Área de Período '''
			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(black)
			pdf.drawString(20, height - 110, "Período: ")

			pdf.setFont("Helvetica", 14)
			pdf.setFillColor(black)
			pdf.drawString(82, height - 110, self.startDate+" - ")

			pdf.setFont("Helvetica", 14)
			pdf.setFillColor(black)
			pdf.drawString(164, height - 110, self.finishDate)



			''' Área da Tabela '''
			#Saldo Inicial
			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(black)
			pdf.drawString(20, height - 150, "Saldo Inicial")

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(black)
			if dfc.initialBalance < 0:
				pdf.drawString(430, height - 150, "-"+monetaryMask(dfc.initialBalance))
			else:
				pdf.drawString(430, height - 150, monetaryMask(dfc.initialBalance))

			pdf.setLineWidth(1)
			pdf.line(20, height-155, width-20, height-155)

			#Saldo Operacional
			y = 184
			pdf.setFillColor(HexColor(CLEAN_GRAY))
			pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(black)
			pdf.drawString(30, height - (y-8), "Saldo Operacional")

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(black)
			if(dfc.operationalBalance < 0):
				pdf.drawString(430, height - (y-8), "-"+monetaryMask(dfc.operationalBalance))
			else:
				pdf.drawString(430, height - (y-8), monetaryMask(dfc.operationalBalance))
			y+=28

			#Total Entradas Operacionais
			if height - y < 60:
			    pdf.showPage()
			    y = 60
			pdf.setFillColor(white)
			pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(HexColor(BLUE))
			pdf.drawString(50, height - (y-8), "Entradas Operacionais")

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(HexColor(BLUE))
			pdf.drawString(430, height - (y-8), "+"+monetaryMask(dfc.totalOperationalInputs))
			y+=28

			#Entradas Operacionais
			if(len(dfc.operationalInputs) == 0):
				if height - y < 60:
				    pdf.showPage()
				    y = 60
				pdf.setFillColor(white)
				pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

				pdf.setFont("Helvetica", 14)
				pdf.setFillColor(HexColor(BLUE))
				pdf.drawString(80, height - (y-8), "-")

				pdf.setFont("Helvetica", 14)
				pdf.setFillColor(HexColor(BLUE))
				pdf.drawString(430, height - (y-8), "-")
				y+=28
			else:
				for operationalInput in dfc.operationalInputs.keys():
					if height - y < 60:
					    pdf.showPage()
					    y = 60
					pdf.setFillColor(white)
					pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

					pdf.setFont("Helvetica", 14)
					pdf.setFillColor(HexColor(BLUE))
					pdf.drawString(80, height - (y-8), operationalInput)

					pdf.setFont("Helvetica", 14)
					pdf.setFillColor(HexColor(BLUE))
					pdf.drawString(430, height - (y-8), dfc.operationalInputs.get(operationalInput))
					y+=28

			#Total Saídas Operacionais
			if height - y < 60:
			    pdf.showPage()
			    y = 60
			pdf.setFillColor(white)
			pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(HexColor(RED))
			pdf.drawString(50, height - (y-8), "Saídas Operacionais")

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(HexColor(RED))
			pdf.drawString(430, height - (y-8), "-"+monetaryMask(dfc.totalOperationalOutputs))
			y+=28

			#Saídas Operacionais
			if(len(dfc.operationalOutputs) == 0):
				if height - y < 60:
				    pdf.showPage()
				    y = 60
				pdf.setFillColor(white)
				pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

				pdf.setFont("Helvetica", 14)
				pdf.setFillColor(HexColor(RED))
				pdf.drawString(80, height - (y-8), "-")

				pdf.setFont("Helvetica", 14)
				pdf.setFillColor(HexColor(RED))
				pdf.drawString(430, height - (y-8), "-")
				y+=28
			else:
				for operationalOutput in dfc.operationalOutputs.keys():
					if height - y < 60:
					    pdf.showPage()
					    y = 60
					pdf.setFillColor(white)
					pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

					pdf.setFont("Helvetica", 14)
					pdf.setFillColor(HexColor(RED))
					pdf.drawString(80, height - (y-8), operationalOutput)

					pdf.setFont("Helvetica", 14)
					pdf.setFillColor(HexColor(RED))
					pdf.drawString(430, height - (y-8), dfc.operationalOutputs.get(operationalOutput))
					y+=28

			#Saldo Financeiro
			if height - y < 60:
			    pdf.showPage()
			    y = 60
			pdf.setFillColor(HexColor(CLEAN_GRAY))
			pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(black)
			pdf.drawString(30, height - (y-8), "Saldo Financeiro")

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(black)
			if(dfc.financialBalance < 0):
				pdf.drawString(430, height - (y-8), "-"+monetaryMask(dfc.financialBalance))
			else:
				pdf.drawString(430, height - (y-8), monetaryMask(dfc.financialBalance))
			y+=28

			#Total Entradas Financeiras
			if height - y < 60:
			    pdf.showPage()
			    y = 60
			pdf.setFillColor(white)
			pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(HexColor(BLUE))
			pdf.drawString(50, height - (y-8), "Entradas Financeiras")

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(HexColor(BLUE))
			pdf.drawString(430, height - (y-8), "+"+monetaryMask(dfc.totalFinancialInputs))
			y+=28

			#Entradas Financeiras
			if(len(dfc.financialInputs) == 0):
				if height - y < 60:
				    pdf.showPage()
				    y = 60
				pdf.setFillColor(white)
				pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

				pdf.setFont("Helvetica", 14)
				pdf.setFillColor(HexColor(BLUE))
				pdf.drawString(80, height - (y-8), "-")

				pdf.setFont("Helvetica", 14)
				pdf.setFillColor(HexColor(BLUE))
				pdf.drawString(430, height - (y-8), "-")
				y+=28
			else:
				for financialInput in dfc.financialInputs.keys():
					if height - y < 60:
					    pdf.showPage()
					    y = 60
					pdf.setFillColor(white)
					pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

					pdf.setFont("Helvetica", 14)
					pdf.setFillColor(HexColor(BLUE))
					pdf.drawString(80, height - (y-8), financialInput)

					pdf.setFont("Helvetica", 14)
					pdf.setFillColor(HexColor(BLUE))
					pdf.drawString(430, height - (y-8), dfc.financialInputs.get(financialInput))
					y+=28

			#Total Saídas Financeiras
			if height - y < 60:
			    pdf.showPage()
			    y = 60
			pdf.setFillColor(white)
			pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(HexColor(RED))
			pdf.drawString(50, height - (y-8), "Saídas Financeiras")

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(HexColor(RED))
			pdf.drawString(430, height - (y-8), "-"+monetaryMask(dfc.totalFinancialOutputs))
			y+=28

			#Saídas Financeiras
			if(len(dfc.financialOutputs) == 0):
				if height - y < 60:
				    pdf.showPage()
				    y = 60
				pdf.setFillColor(white)
				pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

				pdf.setFont("Helvetica", 14)
				pdf.setFillColor(HexColor(RED))
				pdf.drawString(80, height - (y-8), "-")

				pdf.setFont("Helvetica", 14)
				pdf.setFillColor(HexColor(RED))
				pdf.drawString(430, height - (y-8), "-")
				y+=28
			else:
				for financialOutput in dfc.financialOutputs.keys():
					if height - y < 60:
					    pdf.showPage()
					    y = 60
					pdf.setFillColor(white)
					pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

					pdf.setFont("Helvetica", 14)
					pdf.setFillColor(HexColor(RED))
					pdf.drawString(80, height - (y-8), financialOutput)

					pdf.setFont("Helvetica", 14)
					pdf.setFillColor(HexColor(RED))
					pdf.drawString(430, height - (y-8), dfc.financialOutputs.get(financialOutput))
					y+=28

			#Saldo Final
			pdf.setFillColor(HexColor(CLEAN_GRAY))
			pdf.rect(20, height - y, width-40, 25, fill=1, stroke=0)

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(black)
			pdf.drawString(30, height - (y-8), "Saldo Final")

			pdf.setFont("Helvetica-Bold", 14)
			pdf.setFillColor(black)
			if dfc.finalBalance < 0:
				pdf.drawString(430, height - (y-8), "-"+monetaryMask(dfc.finalBalance))
			else:
				pdf.drawString(430, height - (y-8), monetaryMask(dfc.finalBalance))
			y+=28

			pdf.save()
			messagebox.showinfo(title="Arquivo Salvo com Sucesso", message="O documento foi gerado com sucesso!")
		except:
			print("ERROR")