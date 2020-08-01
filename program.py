
import csv
import mechanize
with open('/home/sneha/Downloads/C2ImportGroupsSample.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		print(row[0])
		i = row[0]
		url = "http://duckduckgo.com/html"
		br = mechanize.Browser()
		br.set_handle_robots(False) # ignore robots
		br.open(url)
		br.select_form(name="x")
		br["q"] = i
		res = br.submit()
		content = res.read()
		with open("mechanize_results.html", "w") as f:
    			f.write(content)
		exit()
		




 


