# DegDay
Growing Degrees per day project for CMSC6950 


#Requirements:
Python 3.5

**Python libraries:**
-Numpy

-Pandas

-Matplotliib

-mpl_toolkits.basemap

-Statsmodels


**Input files**
Degdays uses a series of .txt files to know which stations and years to use for each of the tasks in the workflow.

All of these files have two columns with no column labels. The first contains the station ID and the second the year.
Columns are separated by commas.

**Important:** Make sure there are no blank line in the input files. Make sure the stations you enter have data for the respective years.


The following input files are expected by DegDay:

-input_GDD.txt 

	(Same station, several years. Used to plot the cummulative GDDs and to explore the effect of the base temperature parameter on the calculated GDD)

-Input_MinMax.txt

	(Several stations, same year. Used to produce plots of minimum and maximum temperatures)

-Input_Lin_Reg.txt

	(Same station, several years. Used to fit a linear model to the cummulative GDD data and explore general trends in GDD over time)
	
Examples of these input files are provided. You may modify them as you need.	


#To run the project on your machine

## Clone ths repository
```console
$ cd ~/DirectoryName
(clone the repo)
$ git clone https://github.com/fsfrazao/DegDay.git
$ cd DegDay
```

## Run make
```console
$ Make
```
	* It will generate .pdf report with all the results.



