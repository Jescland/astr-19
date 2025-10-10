def main():
	def f(x):
		return x**3 + 8
	print("f(x) = x**3 + 8")
	print("If x = 9, f(9) =")
	print(f(9))
	if f(9) > 27:
		print("Yay! Prompt completed!")


if __name__ == "__main__":
	main()