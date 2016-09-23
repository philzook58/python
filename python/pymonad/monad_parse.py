



# parser is of form string  -> [(symbol, therestofstring), (other possiblity), (other possiblity), ...]

#parserbind needsto return 
def parsebind(parser , parserproducer):
	def combinerparser(string):
		possibleparses = parser(string)
		for (symb, restofstring) in possibleparses:
			
	return combinedparser