import csv
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

MY_FILE = "sample_sfpd_incident_all.csv"

def parse(raw_file, delimiter):
	"""Parses a raw CSV file to a JSON-like object."""
	#open csv file
	opened_file = open(raw_file)
	
	#read csv file
	csv_data = csv.reader(opened_file,delimiter=delimiter)
	
	#build parsed data
	parsed_data = []
	
	#define headers
	fields = csv_data.next()
	
	#Iterate over each row of the csv file, zip together field->value pairs
	for row in csv_data:
		parsed_data.append(dict(zip(fields, row)))
	
	#close csv file
	opened_file.close()
	
	return parsed_data

def visualize_days():
	"""Visualize data by day of week."""
	
	#grab our parsed data that we parsed earlier
	data_file = parse(MY_FILE, ",")
	
	#make a new variable, counter,  from iterating through each line of
	#data in the parsed data, and count how many incidents happen on each
	#day of the week
	counter = Counter(item["DayOfWeek"] for item in data_file)
	
	#separate the x-axis data (days of the week) from the counter variable
	#from the y-axis (number of incidents each day)
	data_list = [
				counter["Monday"],
				counter["Tuesday"],
				counter["Wednesday"],
				counter["Thursday"],
				counter["Friday"],
				counter["Saturday"],
				counter["Sunday"]
				]
	day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])
	
	#with y-axis data, assign it to a matplotlib plot instance
	plt.plot(data_list)
	
	#create amount of ticks need for x and y axes and assign labels
	plt.xticks(range(len(day_tuple)), day_tuple)
	
	#save the plot
	plt.savefig("Days.png")
	
	#close plot file
	plt.clf()
	
def visualize_type():
	"""Visualize data by category in a bar graph"""
	
	#grab our parsed data
	data_file = parse(MY_FILE, ",")
	
	#make a new variable, counter, from iterating through each line of
	#data in parsed data, and count how many incidents happen by category
	counter = Counter(item["Category"] for item in data_file)
	
	#set the labels which are based on the keys of our counter
	#since order doesn't matter, we can just use counter.keys()
	labels = tuple(counter.keys())
	
	#set exactly where the labels should hit the x-axis
	xlocations = np.arange(len(labels)) + 0.5
	
	#width of each bar that will be plotted
	width = 0.5
	
	#assign data to a bar plot
	plt.bar(xlocations, counter.values(), width=width)
	
	#assign labels and tick location to x-axis
	plt.xticks(xlocations + width /2, labels, rotation=90)
	
	#give more room to the x-axis so the labels aren't cut off
	plt.subplots_adjust(bottom=0.4)
	
	#make the overall graph/figure larger
	plt.rcParams['figure.figsize'] = 12, 8
	
	#save the graph
	plt.savefig("type.png")
	
	#close the plot figure
	plt.clf()

def main():
	visualize_days()
	visualize_type()
	
if __name__ == "__main__":
	main()
