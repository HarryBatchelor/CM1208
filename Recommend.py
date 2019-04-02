import numpy as np
from collections import Counter
import matplotlib
import math
global table

raw_history = open('history.txt','r')
raw_queries = open('queries.txt','r')

history = raw_history.read().split('\n')
queries = raw_queries.read().split('\n')

infomation = history[0].split(' ')
del(history[0])

Number_of_Customers = int(infomation[0])
Number_of_items = int(infomation[1])
Number_of_Transactions = int(infomation[2])

def build_table():
	global table
	table = []
	for i in range(Number_of_Customers+1):
		table.append([0]*(Number_of_items+1))
	for case in history:
		user = int(case.split(' ')[0])
		item_bought = int(case.split(' ')[1])
		table[item_bought][user] = 1
	print("Positive entries: %s" %Counter(str(table))['1'])
	print('Average angle: %s'%angle_averages())

def angle_averages():
	all_pairs = []
	for ix in range(1, Number_of_items+1):
		for iy in range(1,Number_of_items+1):
			if ix!=iy:
				all_pairs.append(calculate_angle(table[ix],table[iy]))
	return round(np.mean(all_pairs),2)

def calculate_angle(x, y):
	norm_y = np.linalg.norm(y)
	norm_x = np.linalg.norm(x)
	return round(math.degrees(math.acos(np.dot(x,y) / (norm_x * norm_y))),2)

def angle_check(item,cart):
	all_angles = []
	if item !=' ':
		for i in range(1,6):
			if str(i) not in cart:
				all_angles.append([i,(calculate_angle(table[int(item)], table[i]))])
	return sorted(all_angles,key=lambda x: x[1])[0]

def order(matches):
	ordered_matches = sorted(matches, key=lambda x: x[0])
	output_string= ''
	for entries in ordered_matches:
		output_string += str(entries[1])+''
	return(output_string)

def main():
	build_table()
	for cart in queries:
		matches_found=[]
		re_ordered_matches=[]
		print("Shopping Cart: %s" %cart)
		items_in_cart = cart.split(' ')
		for item in items_in_cart:
			match, angle = angle_check(item,list(cart))
			if angle > 90:
				continue
			elif match not in re_ordered_matches:
				matches_found.append([angle,match])
				re_ordered_matches.append(match)
			if angle != 90:
				print('Item: %s: match: %s, angle: %s'%(item,match,angle))
			else:
				print('Item: %s no match found '%item)
		print('Recommend: '+order(matches_found))
main()
