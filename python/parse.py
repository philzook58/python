rules = {
	
S: [['(','E',')']],
E: [['(', 'E',')'], ['term']]

}

nonterminals = rules.getkeys()


def parse(tokenlist, rules, currentNonTerminal='S'):

	for nonterminal, replaceoptions in rules:
		for rule in replaceoptions:
			for token in rule:
				if tokenlist[0] != rule[0]
				if token in nonterminals:
					val = parse(tokenlist[1:],rules)
					if val == False:
						break
			if tokenlist[0] == rule[0]
				val = parse(tokenlist[1:],rules)

	#failed to parse 
	return False
