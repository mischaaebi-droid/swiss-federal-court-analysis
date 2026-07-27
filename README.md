# Project Goal
The goal of this project is to investigate whether the political party affiliation of judges at the Swiss Federal Supreme Court influences their decisions. It also examines whether some judges are stricter or more lenient than others and whether judicial behavior changes over time — for example, whether right-leaning judges have become more restrictive.


# How the Code Works
### Scraping
**[Scraping_Decisions.py](Scraping_Decisions.py)** This code scrapes the court decisions and labels them correctly.
### Structuring, cleaning, merging
1. **[court_decis_data_structuring.ipynb](court_decis_data_structuring.ipynb)** This code extracts information from the court decisions, such as the judges' names, the outcomes of the decisions, and the area of law. The judges' political party affiliations are added from a separate Excel file. The data is then cleaned, checked, and finally saved as a CSV file (and additionally as an Excel file).
2. **[ext_script_decision_match.py](ext_script_decision_match.py)** This is an external extension of [court_decis_data_structuring.ipynb](court_decis_data_structuring.ipynb) from step 2. It classifies the outcomes of the decisions as success or no success. It is imported as a function.
### Analying and calculate results
1. **3-judge-decisions [court_decis_analyse_3er.ipynb](court_decis_analyse_3er.ipynb)** This code analyzes the data of 3-judge-panels and performs the calculations.
2. **5-judge-decisons  [court_decis_analyse_5er.ipynb](court_decis_analyse_5er.ipynb)** This code analyzes the data of 5-judge-panels and performs the calculations.

