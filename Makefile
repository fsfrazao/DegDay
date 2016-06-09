all:GDD_4 #GDD_2

GDD_2:url_2
	mkdir -p Task2_input
	mkdir -p csv-data_2
	python plot_cummulative_GDD.py --folder ./Task2_input ./csv-data_2  

GDD_4:url_4
	mkdir -p Task4_input
	python GDD.py --folder ./Task4_input ./csv-data

url_4:input_GDD.txt
	python urlcode.py 

input_4.txt:

input_GDD.txt:

pandas:
	sudo apt-get install python-pandas

cleancsv:url
	python cleancsv.py

plotCGDD:
	python plot_cummulative_GDD.py

GDD_Report_Group_4.pdf:GDD_Report_Group_4.tex
	pdflatex GDD_Report_Group_4.tex
	pdflatex GDD_Report_Group_4.tex
	pdflatex GDD_Report_Group_4.tex

clean:
	rm -rf ./csv-data/*
	rm -rf ./Task4_input
	rm -rf ./Task2_input
	rm -rf ./csv-data_2
	rm -rf ./*.csv    