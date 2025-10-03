
import random

def main():
	intro()
	prompt()
def intro():
	print("Hi, I'm Jane! What would you like to know about me?")
def prompt():
	print("[1] Full Name\n[2] Pronouns\n[3] Favorite Movie\n[4] Favorite Food\n[5] Fun Fact\n[6] Goodbye")
	number_input = input("Type a number: ")
	while True:
		try:
			i = int(number_input)
			break
		except ValueError:
			print("\nType a number to get to know me!")
			prompt()
	i = int(number_input)
	if i == 6:
		print("\n[6] Goodbye")
		print("Alright, see ya around!") 
	else:
		if i == 1:
			print("\n[1] Full Name")
			print("My full name is Janerryll Esclanda. Janerryll pronounced kind of like \"General\"")
			redirect()
		if i == 2:
			print("\n[2] Pronouns")
			print("My pronouns are she/her, but I'm fine with any!")
			redirect()
		elif i == 3:
			print("\n[3] Favorite Movie")
			print("Hmm... I think my favorite movie at the moment would have to be \"Uma Musume: Beginning of a New Era\"")
			redirect()
		elif i == 4:
			print("\n[4] Favorite Food")
			print("Favorite food? Probably Filipino milkfish, or bangus!")
			redirect()
		elif i == 5: 
			print("\n[5] Fun Fact")
			fact_list = ["My first name is a combination of my parents' names.", "I've been 4'9\" ever since middle school.", "I used to play soccer in high school.", "A lot of my hobbies revolve around video games, but more specifically gacha games... It's not good ahaha...", "I'm not a fan of heights or insects.", "I did a bit of CS in high school, but it was through code.org.", "I've lived in LA for my entire life, so being here in Santa Cruz is really new for me."]
			print(random.choice(fact_list))
			redirect()
		else:
			print("\nType a number that corresponds to a topic!")
			prompt()
def redirect():
	print("\nAnything else you'd like to know?")
	prompt()


if __name__=="__main__":
	main()

