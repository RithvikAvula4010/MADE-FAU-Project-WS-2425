# The Los Angeles Police Department's transition to a NIBRS compliant crime and arrest reporting system
The project investigates crime and arrest data from Los Angeles (2020 2024) associated with the Los Angeles Police Department (LAPD) implementation of the National Incident Based Reporting System (NIBRS). The project analyzes trends of crime by age, gender, and other geographic location in order to locate and address patterns and disparities. Key findings imply that young as well as middle-aged adults are the most heavily involved in committing crimes and getting arrested, but there are really big differences among neighborhoods. The analysis is intended to better design law enforcement strategies, the allocation of resources, and specific targeted interventions that would contribute to the improvement of public safety while tending to a more effective crime prevention system. 

## Question
What is the relationship between the number of reported crimes and arrests made within different age groups in Los Angeles Police Department (LAPD)? Are younger or older age groups more likely to be arrested relative to crime occurrences? 


## Datasources
<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Crime Data from 2020 to Present (2024)
This dataset shows crime incidents in Los Angeles from 2020 to now. It includes information like the age and gender of people involved, the location of the crime, and a description of what happened. 


* Metadata Context: <https://project-open-data.cio.gov/v1.1/schema/catalog.jsonld>

* Data URL: <https://data.lacity.org/api/views/2nrs-mtv8/rows.csv?accessType=DOWNLOAD>

* Data Type: CSV

### Datasource2: Arrest Data from 2020 to Present (2024)
This dataset arrest records in Los Angeles from 2020 to now, including details such as arrest date, time, location (latitude/longitude), demographics (age, sex, descent), charge descriptions, and booking information. It provides insights into criminal activity, geographic patterns, and offender profiles. 

* Metadata Context: <https://project-open-data.cio.gov/v1.1/schema/catalog.jsonld>

* Data URL: <https://data.lacity.org/api/views/amvf-fr72/rows.csv?accessType=DOWNLOAD>

* Data Type: CSV

## Project Work
Your data engineering project will run alongside lectures during the semester. We will ask you to regularly submit project work as milestones, so you can reasonably pace your work. All project work submissions **must** be placed in the `project` folder.

### Exporting a Jupyter Notebook
Jupyter Notebooks can be exported using `nbconvert` (`pip install nbconvert`). For example, to export the example notebook to HTML: `jupyter nbconvert --to html examples/final-report-example.ipynb --embed-images --output final-report.html`


## Exercises
During the semester you will need to complete exercises using [Jayvee](https://github.com/jvalue/jayvee). You **must** place your submission in the `exercises` folder in your repository and name them according to their number from one to five: `exercise<number from 1-5>.jv`.

In regular intervals, exercises will be given as homework to complete during the semester. Details and deadlines will be discussed in the lecture, also see the [course schedule](https://made.uni1.de/).

### Exercise Feedback
We provide automated exercise feedback using a GitHub action (that is defined in `.github/workflows/exercise-feedback.yml`). 

To view your exercise feedback, navigate to Actions → Exercise Feedback in your repository.

The exercise feedback is executed whenever you make a change in files in the `exercise` folder and push your local changes to the repository on GitHub. To see the feedback, open the latest GitHub Action run, open the `exercise-feedback` job and `Exercise Feedback` step. You should see command line output that contains output like this:

```sh
Found exercises/exercise1.jv, executing model...
Found output file airports.sqlite, grading...
Grading Exercise 1
	Overall points 17 of 17
	---
	By category:
		Shape: 4 of 4
		Types: 13 of 13
```
