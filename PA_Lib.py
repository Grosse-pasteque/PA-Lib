from random import randint, choice

class Percent:
	def __init__(self, min_percent=0, max_percent=100):
		# default percentages values
		self.min_percent = min_percent
		self.max_percent = max_percent

		# all configs
		self.constants = {}
		self.allkeys = 0

		# valid args
		self.valid_keys = [
			"max_percent",
			"min_percent",
			"constants"
		]

	# add config function
	def add(self, percent, constant: any):  # percent: int or float
		if type(percent) == int or type(percent) == float:
			if self.min_percent <= percent <= self.max_percent:
				self.constants[percent] = constant

			else:
				raise ValueError(
					f"Percent: {percent} need to be between {self.min_percent} and {self.max_percent} !")
		else:
			raise TypeError(
				f"Percent: {percent} is not integer or float value !")

		for key in self.constants.keys():
			self.allkeys += key

			if self.allkeys > self.max_percent:
				raise ValueError(
					f"Percent: all percentages added can't be {self.allkeys} < {self.max_percent} !")
		
		self.allkeys = 0


	# delete config function
	def delete(self, percent: str):
		if type(percent) == int or type(percent) == float:
			if percent in self.constants.keys():
				self.constants.pop(percent)
				return

			raise ValueError(
				f"Percent: {percent} doesn't exist in {str(self.constants.keys()).replace('dict_keys(', '').replace(')', '')} !")
	
		raise TypeError(
			f"Percent: {percent} is not integer or float value !")


	# setting directly config function
	def setdirect(self, config: dict):
		for key in config.keys():
			if type(key) == int or type(key) == float:
				if self.min_percent <= key <= self.max_percent:
					self.constants[key] = config[key]
				else:
					raise ValueError(
						f"Percent: {key} need to be between {self.min_percent} and {self.max_percent} !")
			else:
				raise TypeError(
					f"Percent: {percent} is not integer or float value !")

	
	# this dunder method allows you to access almost any of the class variables by using self[item: -> self.valid_keys]
	def __getitem__(self, item: str):
		if item not in self.valid_keys:
			raise AttributeError(
				f"Attribute: -{item} is not valid !")

		if item == 'max_percent':
			return self.max_percent
		
		if item == 'min_percent':
			return self.min_percent
		
		return self.constants

	
	# random percent generator
	def randperct(self):
		value = randint(self.min_percent, self.max_percent)
		for key in self.constants:

			if list(self.constants.keys()).index(key) == 0:
				if self.min_percent <= value < key:
					if str(type(self.constants[key])).replace("<class '", '').replace("'>", '') != "function":
						return self.constants[key]
					else:
						return self.constants[key]()
			
			else:
				self.allkeys += list(self.constants.keys())[list(self.constants.keys()).index(key)-1]
				if self.allkeys <= value <= key + self.allkeys:
					if str(type(self.constants[key])) != "<class 'function'>":
						self.allkeys = 0
						return self.constants[key]

					else:
						self.allkeys = 0
						return self.constants[key]()


# allows you to make percentages groups easily
class Group:
	def __init__(self, name=None, version=None, description=None):
		self.name = name
		self.version = version
		self.description = description

		# config
		self.group = {
			'spec': {
				self.name,
				self.version,
				self.description
			},
			'percents': {}
		}


	# add Percentage to you group
	def add(self, percent: Percent, name=''):
		if type(percent) == Percent:
			if name not in self.group.keys():
				self.group['percents'][name] = percent
				return

			raise SyntaxError(
				f"Already used percent: {percent} is already used in group {self.name} !")
	
		raise TypeError(
			f"Type: of {percent} = {type(percent)} isn't valid !")


	# return config
	def getall(self):
		return self.group


	# return a random member(Percent) of you group
	def randgroup(self, return_choice=False):
		random_group = choice(list(self.group['percents'].keys()))
		
		if not return_choice:
			return self.group['percents'][random_group]

		return self.group['percents'][random_group], random_group
