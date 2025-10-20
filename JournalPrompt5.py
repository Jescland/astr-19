#write a table of sin(x) vs x
#x is tabulated between 0 and 2 pi
#1000 entries

import math

def main():
	def datax(mini, maxi, entries):
		sinx_table = []
		if entries > 1:
			step = (maxi - mini)/(entries - 1) 
		else:
			step = 0
		for i in range(entries):
			x = mini + i*step
			sin_x = math.sin(x)
			sinx_table.append((x,sin_x))
		return sinx_table
	def table(data):
		print(f"{'x':<15} | {'sin(x)':<15}")
		print('-'*33)
		for x,sin_x in datax(mini,maxi,entries):
			print(f'{x:<15.6f} | {sin_x:<15.6f}')
	pi = math.pi 
	mini = 0.0
	maxi = 2.0*pi
	entries = 1000
	sine_table = datax(mini,maxi,entries)
	table(sine_table)

if __name__=="__main__":
	main()