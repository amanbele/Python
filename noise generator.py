# import modules
import random


while True:
	def run():
		num_limit = int(input('Input your limit \n'))

		lim_ = 0

		while lim_ <= num_limit:

			num = 0
			rand_inc = random.randint(0, 5)

			if (rand_inc >= 0) and (rand_inc <= 3):
				try:
					num = num-1
				except:
					pass

			elif (rand_inc >= 4):
				num += 1
			

			print(num)

			lim_ += 1

	cont = input("Want to generate again? Y for Yes and N for No\n")

	def exit():
                quit()

	run()

	if cont == 'Y':
		run()
	else:
                exit()

	

