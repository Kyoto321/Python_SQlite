###	Create an Create_data.db

class Cencus_data:
	"""A sample cencus_data"""

	def __init__(self, community_area_number, community_area_name, pecent_of_housing_crowded, pecent_households_below_poverty, pecent_age_16_unemployed, pecent_age_25_without_high_school_diploma, percent_age_under_18_or_over_64, per_capita_income, hardship_index):
		self.community_area_number = community_area_number
		self.community_area_name = community_area_name
		self.pecent_of_housing_crowded = pecent_of_housing_crowded
		self.pecent_households_below_poverty = pecent_households_below_poverty
		self.pecent_age_16_unemployed = pecent_age_16_unemployed
		self.pecent_age_25_without_high_school_diploma = pecent_age_25_without_high_school_diploma
		self.percent_age_under_18_or_over_64 = percent_age_under_18_or_over_64
		self.per_capita_income = per_capita_income
		self.hardship_index = hardship_index



	#@property
	#def email(self):
		#return  '{}.{}@gmail.com'.format(self.first, self.last)

	#@property
	#def fullname(self):
		#return '{}.{}',format(self.first, self.last)

	def __Repr__(self):
		return "Cencus_data('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}'".format(self.community_area_number, self.community_area_name, self.pecent_of_housing_crowded, self.pecent_households_below_poverty, self.pecent_age_16_unemployed, self.pecent_age_25_without_high_school_diploma, self.percent_age_under_18_or_over_64, self.per_capita_income, self.hardship_index)
