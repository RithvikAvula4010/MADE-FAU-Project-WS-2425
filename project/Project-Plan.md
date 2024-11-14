
# Project Plan

## Title

Relationship between the type of fuel used in electricity generation and electricity consumption in various sectors over time.

## Main Question

1. How does the type of fuel used for electricity generation correlate with electricity consumption across different sectors over time?

## Description

This project allows you to explore the relationship between generation sources and sector-specific consumption patterns, potentially highlighting trends in energy demand by sector and shifts in fuel type reliance. It could also offer insights into how changes in fuel types (like renewable energy increases or coal decreases) have impacted electricity availability and consumption in residential, commercial, industrial, and other sectors.

## Datasources

### Datasource1: Electricity Sales by Sector
•	Metadata URL: https://catalog.data.gov/dataset/electricity-sales-by-sector-gwh-beginning-1980-1f109/resource/65764672-4abb-4bcf-bd76-3eba55f77315
•	Data URL: https://catalog.data.gov/dataset/electricity-sales-by-sector-gwh-beginning-1980-1f109/resource/65764672-4abb-4bcf-bd76-3eba55f77315
•	Data Type: CSV

This dataset is available in data.gov contains all the data related to electricity sales by sector in US

### Datasource2: Electricity Generation by Fuel Type
•	Metadata URL: https://catalog.data.gov/dataset/electric-generation-by-fuel-type-gwh-beginning-1960/resource/df1528d1-bdd0-4594-8ef8-793b298cfdd5
•	Data URL: https://catalog.data.gov/dataset/electric-generation-by-fuel-type-gwh-beginning-1960/resource/df1528d1-bdd0-4594-8ef8-793b298cfdd5
•	Data Type: CSV

This dataset is available in data.gov contains all the data related to electricity generation by fuel type in US

## Work Packages

1. 	Prior to conducting correlation analysis, we will preprocess both datasets by cleaning unwanted columns and ensuring consistency in datatypes and year #1
2.	Make the working pipeline to get curated data #2
3.	Plot EDA trends of Electricity generation over years. Using these parameters we will try to find the impact regarding the consumption in particular sectors#3
