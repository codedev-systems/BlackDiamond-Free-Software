class Dre():
	#Receita Bruta
	grossRevenue = 0.0

	#Receita Líquida e Deduções
	liquidRevenue = 0.0
	dedutions = {}

	#Lucro Bruto e CVMs/CSPs
	grossProfit = 0.0
	cmvs = {}

	#Lucro Operacional, Resultado Operacional, Receitas Operacionais e Despesas Operacionais
	operationalProfit = 0.0
	totalOperationalRevenue = 0.0
	totalOperationalDebt = 0.0
	operationalRevenues = {}
	operationalDebts = {}

	#LAIR, Resultado Financeiro, Receitas Financeiras e Despesas Financeiras
	lair = 0.0
	totalFinancialRevenue = 0.0
	totalFinancialDebt = 0.0
	financialRevenues = {}
	financialDebts = {}

	#Lucro Líquido e Provisão para IR e CSLL
	liquidProfit = 0.0
	irCsllProvision = 0.0

	def __init__(self, grossRevenue, dedutions, cmvs, operationalMovements, financialMovements, irCsllProvision):
		self.grossRevenue = float(grossRevenue.replace("R$", "").replace(".", "").replace(",", "."))
		self.dedutions = dedutions
		self.cmvs = cmvs
		self.irCsllProvision = float(irCsllProvision.replace("R$", "").replace(".", "").replace(",", "."))

		#Separa as Receitas Operacionais das Dívidas Operacionais
		self.operationalRevenues.clear()
		self.operationalDebts.clear()
		for key in operationalMovements.keys():
			if operationalMovements.get(key)[0] == "+":
				self.operationalRevenues[key] = operationalMovements.get(key)
			else:
				self.operationalDebts[key] = operationalMovements.get(key)

		#Separa as Receitas Financeiras das Dívidas Financeiras
		self.financialRevenues.clear()
		self.financialDebts.clear()
		for key in financialMovements.keys():
			if financialMovements.get(key)[0] == "+":
				self.financialRevenues[key] = financialMovements.get(key)
			else:
				self.financialDebts[key] = financialMovements.get(key)


		#Calcula a Receita Líquida
		totalDeduction = 0.0
		for deduction in self.dedutions.values():
			totalDeduction += float(deduction.replace("-R$", "").replace(".", "").replace(",", "."))
		self.liquidRevenue = self.grossRevenue - totalDeduction

		
		#Calcula o Lucro Bruto
		totalCvm = 0.0
		for cvm in self.cmvs.values():
			totalCvm += float(cvm.replace("-R$", "").replace(".", "").replace(",", "."))
		self.grossProfit = self.liquidRevenue - totalCvm

		
		#Calcula o Lucro Operacional
		for debt in self.operationalDebts.values():
		    self.totalOperationalDebt += float(debt.replace("-R$", "").replace(".", "").replace(",", "."))

		for revenue in self.operationalRevenues.values():
		    self.totalOperationalRevenue += float(revenue.replace("+R$", "").replace(".", "").replace(",", "."))

		self.operationalProfit = self.grossProfit + (self.totalOperationalRevenue-self.totalOperationalDebt)


		#Calcula o LAIR
		for debt in self.financialDebts.values():
		    self.totalFinancialDebt += float(debt.replace("-R$", "").replace(".", "").replace(",", "."))

		for revenue in self.financialRevenues.values():
		    self.totalFinancialRevenue += float(revenue.replace("+R$", "").replace(".", "").replace(",", "."))

		self.lair = self.operationalProfit + (self.totalFinancialRevenue-self.totalFinancialDebt)


		#Calcula o Lucro Líquido
		self.liquidProfit = self.lair-self.irCsllProvision