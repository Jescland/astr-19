def main():
	f = 10.0 + 7.0
	print("\nWhen adding two floating point numbers,")
	print("10.0 + 7.0 =")
	print(f)
	print("The data type of the sum is:")
	print(type(f))

	g = 4 - 6
	print("\nWhen subtracting two integers,")
	print("4 - 6 =")
	print(g)
	print("The data type of the difference is:")
	print(type(g))

	h = 2.0 * 7
	print("\nWhen multiplying a floating point number and an integer,")
	print("2.0 * 7 =")
	print(h)
	print("The data type of the product is:")
	print(type(h))

	i = 12 * 2.0
	print("\nEven if we flip the integer and floating point number,")
	print("12 * 2.0 =")
	print(i)
	print("Then the data type would still be:")
	print(type(i))

	j = 7 - 9.0
	k = 3.0 + 5
	print("\nThis also applies to addition and subtraction")
	print("7 - 9.0 =")
	print(j)
	print(type(j))
	print("3.0 + 5 =")
	print(k)
	print(type(k))
	print("\nIt seems that whenever there is an equation that utilizes both integers and float point numbers,\nthe latter takes precedence and the result will be classified as a float point number.")

if __name__ == "__main__":
	main()