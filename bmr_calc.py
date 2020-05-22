#!/usr/bin/env python3.7


def get_user_gender():
	while True:
		try:
			get_user_gender = input(str("Gender (male or female): "))
		except ValueError:
			print("Sorry, I didn't get an input for your gender.")
			continue
		else:
			# weight_print = f"You weigh {get_user_weight}lbs"
			return get_user_gender
			break


def get_user_weight():
	while True:
		try:
			get_user_weight = int(input("please enter your current weight in lbs: "))
		except ValueError:
			print("Sorry, I didn't get an input for your weight.")
			continue
		else:
			# weight_print = f"You weigh {get_user_weight}lbs"
			return get_user_weight
			break
	 


def get_user_height_feet_inches():

	while True:
		try:
			feet = int(input("Height in feet: "))
			inches = int(input("inches: "))
		except ValueError:
			print("Sorry, I didn't get an input for height.")
			continue
		else:
			height_breakdown = f"Your height is {feet} feet {inches} inches"
			feet_plus_inches = (feet * 12 + inches)
			return feet_plus_inches
			break


def get_age():
	while True:
		try:
			age = int(input("age: "))
		except ValueError:
			print("Sorry, I didn't get an input.")
			continue
		else:
			# age_current = f"Your current age is {age}"
			return age
			break
		

def calculate_bmr():
	if gender == "male":
		male_calculated_bmr = 66.47 + (6.24 * weight) + (12.7 * height) - (6.755 * age)
		# print(male_calculated_bmr, "BMR")
		return male_calculated_bmr
		print(male_calculated_bmr)
	else:
		female_calculated_bmr = 655.1 + (4.35 * weight) + (4.7 * height) - (4.7 * age)
		# print(female_calculated_bmr, "BMR")
		return female_calculated_bmr
		print(male_calculated_bmr)


def calculate_tdee(calculate_bmr):
	while True:
		try:
			tdee_input = int(input(
				"""
				1. Sedentary = little or no exercise, desk job
				2. Lightly active = light exercise/ sports 1-3 days/week
				3. Moderately active = moderate exercise/ sports 6-7 days/week
				4. Very active = hard exercise every day, or exercising 2 xs/day
				5. Extra active = hard exercise 2 or more times per day, or training for
				marathon, or triathlon, etc. 

				Please choose one: """
				))
		except ValueError:
			print("Sorry, I didn't get an input for height.")
			continue
		else:
			if tdee_input == 1:
				final_cals = int(calculate_bmr * 1.2)
				print(final_cals, "calories")
				break
			elif tdee_input == 2:
				final_cals = int(calculate_bmr * 1.375)
				print(final_cals, "calories")
				break
			elif tdee_input == 3:
				final_cals = int(calculate_bmr * 1.55)
				print(final_cals, "calories")
				break
			elif tdee_input == 4:
				final_cals = int(calculate_bmr * 1.9)
				print(final_cals, "calories")
				break


if __name__ == "__main__":
	gender = get_user_gender()
	weight = get_user_weight()
	height = get_user_height_feet_inches()
	age = get_age()
	final_bmr = calculate_bmr()
	get_bmr_tdee = calculate_tdee(final_bmr)
