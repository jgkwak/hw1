import unittest 
import liquid



class TestDrinks(unittest.TestCase):

	def setUp(self):
		self.person1 = liquid.drinks ("Person 1","S")
		self.person2 = liquid.boba ("Person 2", "M", 2)
		self.person3 = liquid.soda ("Person 3", "L", "sprite", "glass")
		self.person4 = liquid.soda ("Person 4", "S", "coke", "can")
		self.person5 = liquid.soda ("Person 5", "M", "sprite", "cup")

	def test_drink_total(self):
		self.assertEqual(self.person5.total_drinks(), 5)

	def test_price(self):
		self.assertEqual(self.person1.price(), 2.5)
		self.assertEqual(self.person2.price(), 4.5)
		self.assertEqual(self.person3.price(), 4.0)
		self.assertEqual(self.person4.price(), 3.25)
		self.assertEqual(self.person5.price(), 3.0)

	def test_report(self):
		self.assertEqual(self.person1.report(), "Person 1 ordered a S sized ")
		self.assertEqual(self.person2.report(), "Person 2 ordered a M sized boba with 2 toppings")
		self.assertEqual(self.person3.report(), "Person 3 ordered a L sized sprite in a glass")
		self.assertEqual(self.person4.report(), "Person 4 ordered a S sized coke in a can")
		self.assertEqual(self.person5.report(), "Person 5 ordered a M sized sprite in a cup")


if __name__ == "__main__":
	unittest.main()
