#Create a class
class Animal:
	#What is included in the class
	def __init__(ani, name, a_length, l_length, eyes, tail, furry):
		#Animal name (string)
		ani.name = name
		#Arm length (float)
		ani.arm_length = a_length
		#Leg length (float)
		ani.leg_length = l_length
		#Eyes (int)
		ani.eyes = eyes
		#Tail (bool)
		ani.tail = tail
		#Furry (bool)
		ani.furry = furry
		
	def desc(ani):
		print(f"[Animal: {ani.name}]")
		print(f"[Arm length: {ani.arm_length}cm]")
		print(f"[Leg length: {ani.leg_length}cm]")
		print(f"[Eye count: {ani.eyes}]")
		print(f"[Tail: {ani.tail}]")
		print(f"[Furry: {ani.furry}]")

def main():
	penguin = Animal("Penguin", 76.0, 0.0, 2, True, False)
	penguin.desc()
	print("\nSide note: Penguin leg length isn't actually known.\nIt is only described as short.")
	print("And baby penguins are considered furry, but not adults.")



if __name__=='__main__':
	main()