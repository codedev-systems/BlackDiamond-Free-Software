class Bp():
	#Ativo Total
	totalActive = 0.0

	#Ativos Circulantes
	totalCurrentActive = 0.0
	currentActives = {}

	#Ativos Não Circulantes
	totalNoCurrentActive = 0.0
	noCurrentActives = {}

	#Passivo Total
	totalPassive = 0.0

	#Passivos Circulantes
	totalCurrentPassive = 0.0
	currentPassives = {}

	#Passivos Não Circulantes
	totalNoCurrentPassive = 0.0
	noCurrentPassives = {}

	#Patrimônio Líquido e CGL (Capital de Giro Líquido)
	netWorth = 0.0
	cgl = 0.0

	def __init__(self, currentActives, noCurrentActives, currentPassives, noCurrentPassives):
		self.currentActives = currentActives
		self.noCurrentActives = noCurrentActives
		self.currentPassives = currentPassives
		self.noCurrentPassives = noCurrentPassives

		#Calcula o Ativo Circulante Total
		for currentActive in self.currentActives.values():
			self.totalCurrentActive += float(currentActive.replace("+R$", "").replace(".", "").replace(",", "."))

		#Calcula o Ativo Não Circulante Total
		for noCurrentActive in self.noCurrentActives.values():
			self.totalNoCurrentActive += float(noCurrentActive.replace("+R$", "").replace(".", "").replace(",", "."))

		#Calcula o Ativo Total
		self.totalActive = self.totalCurrentActive + self.totalNoCurrentActive



		#Calcula o Passivo Circulante Total
		for currentPassive in self.currentPassives.values():
			self.totalCurrentPassive += float(currentPassive.replace("-R$", "").replace(".", "").replace(",", "."))

		#Calcula o Passivo Não Circulante Total
		for noCurrentPassive in self.noCurrentPassives.values():
			self.totalNoCurrentPassive += float(noCurrentPassive.replace("-R$", "").replace(".", "").replace(",", "."))

		#Calcula o Passivo Total
		self.totalPassive = self.totalCurrentPassive + self.totalNoCurrentPassive



		#Calcula o Patrimônio Líquido e o CGL (Capital de Giro Líquido)
		self.netWorth = self.totalActive - self.totalPassive
		self.cgl = self.totalCurrentActive - self.totalCurrentPassive