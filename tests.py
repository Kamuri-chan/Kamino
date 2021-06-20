import unittest
from process_message import ChatterMessage


class MessageTestCase(unittest.TestCase):
	def test_intro_message(self):
		result = ChatterMessage("Oi").response
		self.assertEqual(result, "Ola, tudo bem? Em que posso te ajudar?")

	def test_creator_message(self):
		result = ChatterMessage("quem é seu criador?").response
		self.assertEqual(result, "Uma pessoa apelidada Kamuri, da uma passada no GitHub: https://github.com/Kamuri-chan")


if __name__ == '__main__':
	unittest.main()
