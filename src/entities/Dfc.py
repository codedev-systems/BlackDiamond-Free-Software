class Dfc():
	#Saldo Inicial
	initialBalance = 0.0

	#Saldo Operacional
	operationalBalance = 0.0
	totalOperationalInputs = 0.0
	totalOperationalOutputs = 0.0
	operationalInputs = {}
	operationalOutputs = {}

	#Saldo Financeiro
	financialBalance = 0.0
	totalFinancialInputs = 0.0
	totalFinancialOutputs = 0.0
	financialInputs = {}
	financialOutputs = {}

	#Balanço Final
	finalBalance = 0.0

	def __init__(self, initialBalance, operationalInputs, operationalOutputs, financialInputs, financialOutputs):
		self.initialBalance = float(initialBalance.replace("R$", "").replace(".", "").replace(",", "."))
		self.operationalInputs = operationalInputs
		self.operationalOutputs = operationalOutputs
		self.financialInputs = financialInputs
		self.financialOutputs = financialOutputs

		#Calcula as Entradas Operacionais
		for operationalInput in self.operationalInputs.values():
			self.totalOperationalInputs += float(operationalInput.replace("+R$", "").replace(".", "").replace(",", "."))

		#Calcula as Saídas Operacionais
		for operationalOutput in self.operationalOutputs.values():
			self.totalOperationalOutputs += float(operationalOutput.replace("-R$", "").replace(".", "").replace(",", "."))

		#Calcula o Saldo Operacional
		self.operationalBalance = self.totalOperationalInputs - self.totalOperationalOutputs



		#Calcula as Entradas Financeiras
		for financialInput in self.financialInputs.values():
			self.totalFinancialInputs += float(financialInput.replace("+R$", "").replace(".", "").replace(",", "."))

		#Calcula as Saídas Financeiras
		for financialOutput in self.financialOutputs.values():
			self.totalFinancialOutputs += float(financialOutput.replace("-R$", "").replace(".", "").replace(",", "."))

		#Calcula o Saldo Financeiro
		self.financialBalance = self.totalFinancialInputs - self.totalFinancialOutputs



		#Calcula o Saldo Final
		self.finalBalance = self.initialBalance + self.operationalBalance + self.financialBalance