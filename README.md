<div align="center">
<h1 align="center"> The Los Angeles Police Department's transition to a NIBRS compliant crime and arrest reporting system


[![License: CC0 1.0 Universal](https://img.shields.io/badge/License-CC0_1.0_Universal-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/legalcode)	  [![Jayvee 0.6.4](https://img.shields.io/badge/Jayvee-0.6.4-yellowgreen.svg)](https://jvalue.github.io/jayvee/docs/dev/intro) [![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3128/) [![CI/CD](https://github.com/prathameshagare02/made-template-WS2425/actions/workflows/data%20pipeline.yml/badge.svg)](https://github.com/prathameshagare02/made-template-WS2425/actions/workflows/data%20pipeline.yml)

<br><img src="https://github.com/prathameshagare02/made-template-WS2425/blob/main/data/crimepng.jpg" width="1000" height="500">

</div>

---

## **Overview**
This project explores crime and arrest data in Los Angeles (2020–2024) during the Los Angeles Police Department’s (LAPD) transition to a **National Incident-Based Reporting System (NIBRS)**. Our goal is to analyze crime trends by **age, gender, and geography**, providing insights to enhance **law enforcement strategies, resource allocation**, and targeted interventions for improved public safety.

---

## **Research Question**
What is the relationship between the number of reported crimes and arrests made within different age groups in Los Angeles Police Department (LAPD)? Are younger or older age groups more likely to be arrested relative to crime occurrences? 

---

## **Data Sources**

### **Crime Data (2020–2024)**
- **Details**: Crime incidents, including age, gender, crime location, and descriptions.  
- **License**: [Public Domain](http://creativecommons.org/publicdomain/zero/1.0/legalcode)  
- **Data URL**: [Crime Data CSV](https://data.lacity.org/api/views/2nrs-mtv8/rows.csv?accessType=DOWNLOAD)  

### **Arrest Data (2020–2024)**
- **Details**: Arrest records with demographics, location, charges, and booking info.  
- **License**: [Public Domain](http://creativecommons.org/publicdomain/zero/1.0/legalcode)  
- **Data URL**: [Arrest Data CSV](https://data.lacity.org/api/views/amvf-fr72/rows.csv?accessType=DOWNLOAD)  

For more details, refer to the [**Data Report**](project/data-report.pdf).

---

## **ETL Pipeline Overview**
The ETL pipeline is built with **Jayvee**, a Domain-Specific Language (DSL) for data pipelines. It extracts, cleans, and processes crime and arrest data, ensuring it is accurate and follows privacy rules. The final output is stored in a SQLite file, making it easy to use for analysis and reporting.

### **Pipeline Process**
1. **Extraction**: Fetch crime and arrest datasets.  
2. **Transformation**: Filter invalid entries (e.g., negative ages, invalid genders).  
3. **Loading**: Store cleaned data for analysis.  

To run the pipeline:
```bash
bash project/pipeline.sh
```

To run tests:
```bash
bash project/tests.sh
```

---

## **Analysis Summary**
- **Age Groups**: Young adults (17–30) and middle-aged adults (31–45) are most involved in crimes and arrests.  
- **Safer Areas**: Devonshire and West Valley.  
- **High-Crime Areas**: Central, Olympic, Southwest, Mission, Rampart.

#### **Recommendations**
- Focus resources on high-crime areas.  
- Target interventions for young and middle-aged adults. 
- Use community programs and predictive tools for prevention.

Detailed insights are available in the [**Analysis Report**](project/analysis-report.pdf).

---

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


---

## **License**
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.


