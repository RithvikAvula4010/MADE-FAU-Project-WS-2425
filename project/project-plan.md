# Project Plan

## Title
<!-- Give your project a short title. -->
The Los Angeles Police Department's transition to an NIBRS-compliant crime and arrest reporting system

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
What is the relationship between the number of reported crimes and arrests made within different age 
groups in Los Angeles Police Department (LAPD)? Are younger or older age groups more likely to be 
arrested relative to crime occurrences? 


## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
The Los Angeles Police Department (LAPD) is working toward an upgrade of their present crime and arrest records' system into one that meets the new requirements of the Federal Bureau of Investigation, known as the National Incident-Based Reporting System (NIBRS). These new standards cover a nationwide scope concerning making data on crimes more consistent, accurate, and specific. Not only will this include input from the community on trends of crime affecting Los Angeles, but also in the future, it will include individuals beyond their immediate surroundings. 

At the moment, while LAPD builds this new system, the public will have sight of information only from the old one. To make the records the more accurate during this transition period, the department has switched from updating crime reports each week to updates every other week. 


## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Crime Data from 2020 to Present(2024)
* Metadata Context: https://project-open-data.cio.gov/v1.1/schema/catalog.jsonld
* Metadata Catalog ID: 	https://data.lacity.org/data.json
* License: 	http://creativecommons.org/publicdomain/zero/1.0/legalcode
* Data URL: https://data.lacity.org/api/views/2nrs-mtv8/rows.csv?accessType=DOWNLOAD
* Data Type: CSV

##### Datasource Description:
This dataset shows crime incidents in Los Angeles from 2020 to now. It includes information like the age and gender of people involved, the location of the crime, and a description of what happened.

### Datasource2: Arrest Data from 2020 to Present(2024)
* Metadata Context: https://project-open-data.cio.gov/v1.1/schema/catalog.jsonld
* Metadata Catalog ID: 	https://data.lacity.org/data.json
* License: 	http://creativecommons.org/publicdomain/zero/1.0/legalcode
* Data URL: https://data.lacity.org/api/views/amvf-fr72/rows.csv?accessType=DOWNLOAD
* Data Type: CSV

##### Datasource Description:
This dataset arrest records in Los Angeles from 2020 to now, including details such as arrest date, time, location (latitude/longitude), demographics (age, sex, descent), charge descriptions, and booking information. It provides insights into criminal activity, geographic patterns, and offender profiles. 

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Explore Datasets [#1][i1]
2. ...

[i1]: https://github.com/prathameshagare02/made-template-WS2425/issues/1
