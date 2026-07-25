How the Code Works
Scraping_Decisions.py: This code scrapes the court decisions and labels them correctly.
court_decis_data_structuring.ipynb: This code extracts information from the court decisions, such as the judges' names, the outcomes of the decisions, and the area of law. The judges' political party affiliations are added from a separate Excel file. The data is then cleaned, checked, and finally saved as a CSV file (and additionally as an Excel file).
ext_script_decision_match.py: This is an external extension of court_decis_data_structuring.ipynb from step 2. It classifies the outcomes of the decisions as success or no success.
court_decis_analyse.ipynb: This code analyzes the data and performs the calculations.

