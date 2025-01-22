<div align="center">
<h1 align="center"> Interplay Between Electricity Generation and Sales in NewYork: Correlations and Key Insights 


[![License: CC0 1.0 Universal](https://img.shields.io/badge/License-CC0_1.0_Universal-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/legalcode)	  [![Jayvee 0.6.4](https://img.shields.io/badge/Jayvee-0.6.4-yellowgreen.svg)](https://jvalue.github.io/jayvee/docs/dev/intro) [![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3128/)

<br><img src="data/DALL·E 2025-01-22 23.06.51 - An artistic illustration of electricity flowing from various power plants (nuclear, solar, wind, and coal) represented visually with glowing, color-co.webp" width="1000" height="500">

</div>

---

## **Overview**
The report explores the connection between electricity generation and consumption over the past several decades. It examines trends in electricity production across different fuel types and its utilization in residential, commercial, and transportation sectors, identifying key patterns and relationships. The insights aim to support strategic decision-making in energy planning and infrastructure development, striving to achieve an optimal balance between energy supply and demand during a period of significant energy transition.

---

## **Research Question**
How are changes in electricity generation across fuels affecting consumption patterns in various sectors, and what can we learn to optimize energy planning and infrastructure in the course of the transition?  

---

## **Data Sources**

### **Crime Data (2020–2024)**
- **Details**: Electricity Sales by Sector.
- **Data URL**: [Electricity Sales by Sector csv](https://catalog.data.gov/dataset/electricity-sales-by-sector-gwh-beginning-1980-1f109/resource/65764672-4abb-4bcf-bd76-3eba55f77315. )  

### **Arrest Data (2020–2024)**
- **Details**:  Electricity Generation by Fuel Type.
- **Data URL**: [ Electricity Generation by Fuel Type csv](https://catalog.data.gov/dataset/electric-generation-by-fuel-type-gwh-beginning-1960/resource/df1528d1-bdd0-4594-8ef8-793b298cfdd5. )  

For more details, refer to the [**Data Report**](project/data-report.pdf).

---

## **ETL Pipeline Overview**
The ETL pipeline is built with **Jayvee**, a Domain-Specific Language (DSL) for data pipelines. It extracts, cleans, and processes crime and arrest data, ensuring it is accurate and follows privacy rules. The final output is stored in a SQLite file, making it easy to use for analysis and reporting.

### **Pipeline Process**
1. **Extraction**:  Focuses on getting some raw data from online sources. The URLs of the datasets "Electricity Sales by Sector" and "Electricity Generation by Fuel Type" are identified, and the data is retrieved through HTTP requests. The datasets are saved locally in a specific directory (./data/raw_csv/) as CSV files to enable access for further process .  
2. **Transformation**:  focuses on cleaning, preparing, and merging of data for analysis. The raw CSV data files are imported using pandas, and info is merged using the common Year column in outer join format to retain all data entries.  
3. **Loading**: ensures that all processed data is kept safe for future analysis. The formed dataset is carried to a SQLite database (GenerationVsSales.sqlite), under the table ElectricityData. Data insertion is checked by querying the database, inspecting for records if the storage and integration have worked properly. .  

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
- **Verdict**: A high correlation is an indication of a strong linear relationship: In other words, a correlation coefficient equal to 0.973 implies that there is a very strong linear relationship between total electricity generation and total electricity sales, meaning electricity generation grows with increasing sales almost proportionally and vice versa. .  


Detailed insights are available in the [**Analysis Report**](project/analysis-report.pdf).

---



