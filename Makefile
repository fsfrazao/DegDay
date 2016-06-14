all:GDD_Basic_2.png GDD_Optional_3.png ./output/*.png

./csv-data/*.csv:input_GDD.txt
	mkdir -p Task4_input
	python urlcode.py input_GDD.txt ./Task4_input
	mkdir -p csv-data
	python GDD.py ./Task4_input ./csv-data
	mkdir -p output
	mkdir -p Min_Max_input
	python urlcode.py Input_MinMax.txt ./Min_Max_input

GDD_Basic_2.png:./csv-data/*.csv
	python plot_cummulative_GDD.py ./csv-data ./output/GDD_Basic_2.png

GDD_Optional_3.png:./csv-data/*.csv
	python tbase_GDD_analysis.py ./Task4_input ./output/GDD_Optional_3.png

./output/*.png:./csv-data/*.csv
	mkdir -p output
	python min_max_plot.py

###################################################################################################
url_MinMax:Input_MinMax.txt
	mkdir -p Task
	python urlcode.py Input_MinMax.txt ./Task

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
##################################################################################################

clean:
	rm -rf ./csv-data
	rm -rf ./Task4_input
	rm -rf ./output
	rm -rf ./Min_Max_input
	rm -rf ./*.csv
	rm -rf ./*.png
