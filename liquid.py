class drinks:

	count = 0

	def __init__(self, name, size):
		self._name = name
		self._size = size
		drinks.count +=1

	def price(self):
		if(self._size == "S" or self._size == "s"):
			return 2.50
		elif(self._size == "M" or self._size == "m" ):
			return 3.00
		elif(self._size == "L" or self._size == "l" ):
		else:
			return 0

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
		if(self._topping)>=0)
			return float(base_price + (self._topping*.75))
		else
			return base_price

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
 
