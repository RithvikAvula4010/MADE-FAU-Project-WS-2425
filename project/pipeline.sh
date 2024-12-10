#!/bin/bash
#Automated feed extraction is slow, so avoid running it via the JV file.
#Data Extraction taking too much time to extract the data (approx 20 to 30 min), hence do not execute the pipeline.
jayvee project/automated_pipeline.jv
