all:GDD_Basic_2.png GDD_Optional_3.png ./output/*.png ./output/linear/*.png

./csv-data/*.csv:input_GDD.txt Input_MinMax.txt
	mkdir -p Task4_input
	python urlcode.py input_GDD.txt ./Task4_input
	mkdir -p csv-data
	python GDD.py ./Task4_input ./csv-data
	mkdir -p output
	mkdir -p Min_Max_input
	python urlcode.py Input_MinMax.txt ./Min_Max_input

./linear-csv-input/*.csv:Input_Lin_Reg.txt
	mkdir -p linear-csv-input
	python urlcode.py Input_Lin_Reg.txt ./linear-csv-input
	mkdir -p linear-csv-cum-input
	python GDD.py ./linear-csv-input ./linear-csv-cum-input

GDD_Basic_2.png:./csv-data/*.csv
	python plot_cummulative_GDD.py ./csv-data ./output/GDD_Basic_2.png

GDD_Optional_3.png:./csv-data/*.csv
	python tbase_GDD_analysis.py ./Task4_input ./output/GDD_Optional_3.png

./output/*.png:./csv-data/*.csv
	mkdir -p output
	python min_max_plot.py

./output/linear/*.png:./linear-csv-input/*.csv
	python linear_regression.py ./linear-csv-cum-input ./output/linear_model_plot.png

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
	rm -rf ./linear-csv-cum-input
	rm -rf ./linear-csv-input
	rm -rf ./csv-data
	rm -rf ./Task4_input
	rm -rf ./output
	rm -rf ./Min_Max_input
	rm -rf ./*.csv
	rm -rf ./*.png
