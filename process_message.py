import json


class ChatterMessage:
	def __init__(self, raw):
		self.raw = str(raw).lower()
		self.processed_str = self.reduce()
		self.responses = self.get_responses()
		self.data = self.process_response()
		self.response = self.data['response']

	def remove_unwanted_chars(self, string):
		list_of_chars = ['?', ".", ",", "!", "@", "[", "]", "{", "}", "#", "$", "%", "*", "&", "(", ")", "-", "_", "+", "="]
		new_str = ""
		for char in string:
			if char not in list_of_chars:
				new_str += str(char)
		return new_str

	def get_responses(self, response_file="info.json"):
		with open(response_file, 'r') as file:
			return json.loads(file.read())


	def reduce(self):
		stopwords = ['de', 'a', 'o', 'que', 'e', 'é', 'do', 'da', 'em', 'um', 'para', 'com', 'não', 'uma', 'os', 'no', 'se', 'na', 'por', 'mais', 'as', 'dos', 'como', 'mas', 'ao', 'ele', 'das', 'à', 'seu', 'sua', 'ou', 'quando', 'muito', 'nos', 'já', 'eu', 'também', 'só', 'pelo', 'pela', 'até', 'isso', 'ela', 'entre', 'depois', 'sem', 'mesmo', 'aos', 'seus', 'quem', 'nas', 'me', 'esse', 'eles', 'você', 'essa', 'num', 'nem', 'suas', 'meu', 'às', 'minha', 'numa', 'pelos', 'elas', 'qual', 'nós', 'lhe', 'deles', 'essas', 'esses', 'pelas', 'este', 'dele', 'tu', 'te', 'vocês', 'vos', 'lhes', 'meus', 'minhas', 'teu', 'tua', 'teus', 'tuas', 'nosso', 'nossa', 'nossos', 'nossas', 'dela', 'delas', 'esta', 'estes', 'estas', 'aquele', 'aquela', 'aqueles', 'aquelas', 'isto', 'aquilo', 'estou', 'está', 'estamos', 'estão', 'estive', 'esteve', 'estivemos', 'estiveram', 'estava', 'estávamos', 'estavam', 'estivera', 'estivéramos', 'esteja', 'estejamos', 'estejam', 'estivesse', 'estivéssemos', 'estivessem', 'estiver', 'estivermos', 'estiverem', 'hei', 'há', 'havemos', 'hão', 'houve', 'houvemos', 'houveram', 'houvera', 'houvéramos', 'haja', 'hajamos', 'hajam', 'houvesse', 'houvéssemos', 'houvessem', 'houver', 'houvermos', 'houverem', 'houverei', 'houverá', 'houveremos', 'houverão', 'houveria', 'houveríamos', 'houveriam', 'sou', 'somos', 'são', 'era', 'éramos', 'eram', 'fui', 'foi', 'fomos', 'foram', 'fora', 'fôramos', 'seja', 'sejamos', 'sejam', 'fosse', 'fôssemos', 'fossem', 'for', 'formos', 'forem', 'serei', 'será', 'seremos', 'serão', 'seria', 'seríamos', 'seriam', 'tenho', 'tem', 'temos', 'tém', 'tinha', 'tínhamos', 'tinham', 'tive', 'teve', 'tivemos', 'tiveram', 'tivera', 'tivéramos', 'tenha', 'tenhamos', 'tenham', 'tivesse', 'tivéssemos', 'tivessem', 'tiver', 'tivermos', 'tiverem', 'terei', 'terá', 'teremos', 'terão', 'teria', 'teríamos', 'teriam']
		custom_filter = []
		keywords_list = []
		strlist = self.raw.split(" ")
		for x in strlist:
			if x not in stopwords and x not in custom_filter:
				keywords_list.append(self.remove_unwanted_chars(x))
		return keywords_list

	def process_response(self):
		percentage = lambda x, y: (100 * y) / x
		total = sum(len(x['keywords']) for x in self.responses)
		most_acc = 0
		response_data = None
		acc = 0
		for value in self.responses:
			c = 0
			for x in value['keywords']:
				if str(x).lower() in self.processed_str:
					c += 1
					if c > most_acc:
						most_acc = c
						acc = percentage(total, most_acc)
						print(acc)
						response_data = value
		if acc < 6:
			return {"response": "Desculpe, não entendi. Seja mais claro, por favor"}
		for x in self.processed_str:
			if x not in response_data['keywords']:
				response_data['keywords'].append(x)

		return response_data


if __name__ == '__main__':
	while True:
		k = input("Você: ")
		res = ChatterMessage(k).response
		print("Bot:", res)

