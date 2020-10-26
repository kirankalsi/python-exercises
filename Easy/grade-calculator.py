mmark = int(input("Please enter your maths mark: "))
cmark = int(input("Please enter your chemistry mark: "))
pmark = int(input("Please enter your physics mark: "))
perc = (((mmark/100) + (cmark/100) + (pmark/100))/3)
print("{:.1%}".format(perc))
if perc >= 0.7:
	print ("A")
elif perc >= 0.6:
	print ("B")
elif perc >= 0.5:
	print ("C")
elif perc >= 0.4:
	print ("D")
else:
	print ("You failed")