"""
Basis:
	Implementation of Genetic Algorithms. This specific implementation
	solves the problem of 'fitness' for a given string. The 'fitness' of
	a string is given by a set of rules supplied by the user. 'Fitness'
	always starts from 0 is increases based on succeeding pairs of chars.
	Given:
		1) 'abc'
		2) 'bac'
	Where:
		a->a = +0
		a->b = +1
		a->c = +2
		b->a = +2
		b->b = +0
		b->c = +1
		c->a = +1
		c->b = +0
		c->c = +1
	Result:
		1) 2
		2) 4
"""
import random

"""
Fitness test. Needs to run in polynomial time to be efficient

@param string -> string to test
@param rules -> dictionary of char pairings and fitnesses

returns @param fitness -> int calculated fitness
"""
def fitness(string, rules):
	fitness = 0
	for i in range(len(string)-1):
		pair = string[i]+string[i+1]
		if not pair in rules:
			raise ValueError("Incomplete rule or state set.")
		fitness += rules[pair]
	return fitness

"""
Takes two strings and returns a single string 'offspring'.
This example only allows a single 'crossover' between
parent strings.

@param string1 -> a string to be bred
@param string2 -> a string to be bred

returns @param child -> the resulting child string
"""
def breed(string1, string2):
	child = ''
	cross = random.randint(0,len(string1))
	for i in range(cross):
		child += string1[i]
	for i in range(cross, len(string1)):
		child += string2[i]
	return child

"""
TODO

matching fn:
	1) sort by fitness
	2) create matching data structure
		hashable key -> string + index
	3) use shrinking cutoff
	4) breed from best to worst to fill out 
		an equal sized new generation
	5) return generation

doGA:
	1) randomly gen first generation
	2) while timeout > 0, run matching fn
	3) gen = new_gen
	4) sort by fitness
	5) return highest value
"""


"""
The central algorithm
@param states -> a list of possible char states
@param rules -> a dictionary of char pairings and fitnesses
@param length -> length of each string
@param n -> int number of strings
@param timeout -> int amount of generations to run GA

returns @param solution -> string of the highest scoring solution
"""
def doGA(states, rules, length, n, timeout):
	gen = []
	for i in range(n):
		member = ''
		for i in range(length):
			index = random.randint(0,len(states))
			member += states[index]
		gen.append([member, fitness(member,rules)])

def main():
	states = ['a','b','c']

	rules = {
		'aa': 0,
		'ab': 1,
		'ac': 2,
		'ba': 2,
		'bb': 0,
		'bc': 1,
		'ca': 1,
		'cb': 0,
		'cc': 1
	}

	string1 = 'abc'
	string2 = 'bac'
	assert fitness(string1, rules) == 2
	assert fitness(string2, rules) == 4

if __name__ == "__main__":
	main()



