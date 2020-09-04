from os import get_terminal_size as gts

def output_table(l, start_from=1, start_weekday_from="sun",select_on=0):
	sizes = [[len(y) for y in x] for x in l]
	terminal_size = [gts().columns, gts().lines]
	each_width = (terminal_size[0]-len(sizes)-1)//(max([len(x) for x in l])
	each_height = (terminal_size[1]-len(sizes)-1)//(len(l))
	if each_width<=0 or each_height<=0:
		return
	print("@"*terminal_size[0])
	for x in l:
		print("|",end="")
		for y in x:
			if len(y)<=each_width:
				print(y,end="|")
			elif each_width==1:
				print(" "+y[0]+" ",end="|")
			elif 2<=each_width<=5:
				print(" "+y[0:-1]+". ",end="|")
			elif 6<=each_width<=8:
				print(" "+y[0:-2]+".. ",end="|")
			else:
				print(" "+y[0:-3]+"... ",end="|")
		print("@"*terminal_size[0])
