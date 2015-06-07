import csv
import matplotlib.pyplot as plt
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
	
def main():
	visualize_days()
	
if __name__ == "__main__":
	main()
