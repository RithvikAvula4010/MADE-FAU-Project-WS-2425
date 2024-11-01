# Project Plan

## Title
<!-- Give your project a short title. -->
The Los Angeles Police Department's transition to an NIBRS-compliant crime and arrest reporting system

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. In comparison to the prior system, what effects has the implementation of the NIBRS-compliant reporting system had on the accuracy and quality of LAPD's crime and arrest data?
2. What patterns in crime categories and incident sites have LAPD documented since 2020, and are these patterns different under the new NIBRS system?
3. What is the impact on data reliability for public usage and decision-making of the regularity and consistency of LAPD data updates (weekly, bi-weekly, and possible interruptions)?


## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
To comply with the FBI's National Incident-Based Reporting System (NIBRS) regulations, which seek to standardize the gathering of crime and arrest data across the country, the Los Angeles Police Department (LAPD) will introduce a new Records Management System. The community will gain better insights into local crime trends as a result of this move to NIBRS-only data, which will increase the accuracy, detail, and accessibility of Los Angeles crime data.

As LAPD works to create the new NIBRS-compatible datasets, users will initially only see occurrences that were logged in the retiring system during the transition. In an effort to preserve data accuracy, the department temporarily switched from weekly to bi-weekly updates due to recent problems providing crime data updates.



## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Crime Data from 2020 to Present(2024)
* Metadata Context: https://project-open-data.cio.gov/v1.1/schema/catalog.jsonld
* Metadata Catalog ID: 	https://data.lacity.org/data.json
* License: 	http://creativecommons.org/publicdomain/zero/1.0/legalcode
* Data URL: https://data.lacity.org/api/views/2nrs-mtv8/rows.csv?accessType=DOWNLOAD
* Data Type: CSV

##### Datasource Description:
Crime incidents in Los Angeles from 2020 to the present are displayed in this dataset. Since the data is derived from paper reports, a few minor mistakes might exist. For privacy reasons, addresses are only listed to the closest hundred blocks, and location data is displayed as (0°, 0°) if it is missing. Users can post comments or questions, and the data is as accurate as possible.

### Datasource2: Arrest Data from 2020 to Present(2024)
* Metadata Context: https://project-open-data.cio.gov/v1.1/schema/catalog.jsonld
* Metadata Catalog ID: 	https://data.lacity.org/data.json
* License: 	http://creativecommons.org/publicdomain/zero/1.0/legalcode
* Data URL: https://data.lacity.org/api/views/amvf-fr72/rows.csv?accessType=DOWNLOAD
* Data Type: CSV

##### Datasource Description:
This dataset displays arrests that have occurred in Los Angeles since 2020. There may be minor errors because the data is derived from paper reports. Location data is displayed as (0.0000°, 0.0000°) if it is absent, and addresses are only displayed by the closest hundred blocks for privacy reasons. People can leave comments or ask questions, and the information is as accurate as possible.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Example Issue [#1][i1]
2. ...

[i1]: https://github.com/jvalue/made-template/issues/1
