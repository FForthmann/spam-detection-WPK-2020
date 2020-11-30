import csv

def main():
	base_path = "/Sandboxes/spam-detection-WPK-2020"
	data_file_path = "spam_task_train.csv"
	data_file_delimiter = "\t"
	csv_reader = csv.reader(open(data_file_path, encoding='utf-8'), delimiter=data_file_delimiter)
	data_lines = [line for line in csv_reader]
	counter = 0
	datei = open("test.txt", "w")
	for line in data_lines:
		data_text = line[0].split(" ")
		datei.write(str(data_text[0].encode('utf-8')))
		datei.write("\n")
		if ("#ERROR!" in data_text[0]):
			counter += 1
	print(counter)
	datei.close()

if __name__ == "__main__":
	main()