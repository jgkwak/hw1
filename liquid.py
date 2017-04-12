class drinks:

	count = 0

	def __init__(self, name, size):
		self._name = name
		self._size = size
		drinks.count +=1

	def price(self):
		if(self._size == "S"):
			return 2.50
		elif(self._size == "M"):
			return 3.00
		else:
			return 3.50

	def report(self):
		return '{} ordered a {} sized '.format(self._name, self._size)

	@classmethod
	def total_drinks(cls):
		return drinks.count


class boba(drinks):
	def __init__(self, name, size, topping):
		super().__init__(name,size)
		self._topping = topping

	def price(self):
		base_price = super().price()
		return float(base_price + (self._topping*.75))

	def report(self):
		beginning = super().report()
		return beginning + 'boba with {} toppings'.format(self._topping)


class soda(drinks):
	def __init__(self, name, size, typ, cup):
		super().__init__(name,size)
		self._cup = cup
		self._type = typ

	def price(self):
		base_price = super().price()

		if(self._cup == "glass"):
			return (base_price + .5)


		elif(self._cup == "can"):
			return (base_price + .75)

		else:
			return base_price

	def report(self):
		beginning = super().report()
		return beginning + '{} in a {}'.format(self._type, self._cup)
 
 # application screen

# print("")

# jennifer = boba("Jen", "L", 1)
# print("{} which cost ${}".format(jennifer.report(),jennifer.price()))

# joanne = boba ("Joanne", "M", 2)
# print("{} which cost ${}".format(joanne.report(),joanne.price()))

# faith = soda("Faith", "L", "sprite", "can")
# print("{} which cost ${}".format(faith.report(),faith.price()))

# lily = drinks("Lily", "S")
# print("{} which cost ${}".format(lily.report(),lily.price()))

# total_price = lily.price()+faith.price()+joanne.price()+jennifer.price()
# print("There were a total of {} drinks ordered. \nThe total price was: ${}".format(drinks.total_drinks(),total_price) )

# print("")

# random_drinks = []

# tot_cost = 0
# for x in range(10):
# 	random_drinks.append(boba(str(x), "S", x))
# 	tot_cost += random_drinks[x].price()
# 	print(random_drinks[x].report())
# print("The total cost of the random drinks were: {}".format(tot_cost))

# print("")











