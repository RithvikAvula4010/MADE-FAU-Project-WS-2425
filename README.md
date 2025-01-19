<div align="center">
<h1 align="center"> The Los Angeles Police Department's transition to a NIBRS compliant crime and arrest reporting system


[![License: CC0 1.0 Universal](https://img.shields.io/badge/License-CC0_1.0_Universal-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/legalcode)	  [![Jayvee 0.6.4](https://img.shields.io/badge/Jayvee-0.6.4-yellowgreen.svg)](https://jvalue.github.io/jayvee/docs/dev/intro) [![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3128/) [![CI/CD](https://github.com/prathameshagare02/made-template-WS2425/actions/workflows/data%20pipeline.yml/badge.svg)](https://github.com/prathameshagare02/made-template-WS2425/actions/workflows/data%20pipeline.yml)

</div>

<div style="text-align: justify">
    

### Description
The project investigates crime and arrest data from Los Angeles (2020 2024) associated with the Los Angeles Police Department (LAPD) implementation of the National Incident Based Reporting System (NIBRS). The project analyzes trends of crime by age, gender, and other geographic location in order to locate and address patterns and disparities. Key findings imply that young as well as middle-aged adults are the most heavily involved in committing crimes and getting arrested, but there are really big differences among neighborhoods. The analysis is intended to better design law enforcement strategies, the allocation of resources, and specific targeted interventions that would contribute to the improvement of public safety while tending to a more effective crime prevention system. 

## Question
What is the relationship between the number of reported crimes and arrests made within different age groups in Los Angeles Police Department (LAPD)? Are younger or older age groups more likely to be arrested relative to crime occurrences? 


## Data sources
<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Data Source 1: Crime Data from 2020 to Present (2024)
This dataset shows crime incidents in Los Angeles from 2020 to now. It includes information like the age and gender of people involved, the location of the crime, and a description of what happened. 


* Metadata Context: <https://project-open-data.cio.gov/v1.1/schema/catalog.jsonld>

* License: <http://creativecommons.org/publicdomain/zero/1.0/legalcode>

* Data URL: <https://data.lacity.org/api/views/2nrs-mtv8/rows.csv?accessType=DOWNLOAD>

* Data Type: CSV

### Data Source 2: Arrest Data from 2020 to Present (2024)
This dataset arrest records in Los Angeles from 2020 to now, including details such as arrest date, time, location (latitude/longitude), demographics (age, sex, descent), charge descriptions, and booking information. It provides insights into criminal activity, geographic patterns, and offender profiles. 

* Metadata Context: <https://project-open-data.cio.gov/v1.1/schema/catalog.jsonld>

* License: <http://creativecommons.org/publicdomain/zero/1.0/legalcode>

* Data URL: <https://data.lacity.org/api/views/amvf-fr72/rows.csv?accessType=DOWNLOAD>

* Data Type: CSV

You can find the more details in [**data report**](project/data-report.pdf).

## Data Pipeline
The project uses a structured ETL (Extract, Transform, Load) pipeline method, which is saved in <b><i>/project/automated_pipeline.jv</i></b>. The command <b><i>jayvee project/automated_pipeline.jv</i></b> is used to begin the pipeline.

* The ETL pipeline is build with Jayvee. Jayvee is the Domain-specific language (DSL) to model data pipelines.  Basically, it extracts public datasets including Crime Data from 2020 to Present (2024) and Arrest Data from 2020 to Present (2024).  
* The process of data cleaning only contains records with positive age value and will filter out all invalid entries with negative age records. Gender will also be validated such that only "male" and "female" entries will be accepted for the purposes of data consistency and accuracy. 
* The loaded crime and arrest data will be examined at an analytical level with respect to trends, contiguities, and attributions in between patterns of crime phenomena, different demographic factors, and geographical influences on arrest rates.

#### Run the data pipeline:
To run data pipeline, run the following command

```
  bash project/pipeline.sh
```
#### Running Tests

To run tests, run the following command

```
  bash project/tests.sh
```

## Project Analysis
The Age-wise, Middle-Aged Adults and Young Adults generally experience a load of arrests comparatively, while Children and Old-Aged Adults feature lower figures, presumably pointing towards differences in enforcement or crime types committed. The analysis calls for targeted interventions, improved resource allocation, and age-specific strategies to settle disparities. It will be imperative to improve law enforcement efforts in the less productive regions about building a much more level, effective, and fair system for treating crime across both demographics and regions in its full strength.

You can find the more details in [**analysis report**](project/analysis-report.pdf).

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

</div>

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
