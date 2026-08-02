website: https://mischaaebi-droid.github.io/swiss-federal-court-analysis/

# Project Goal
The goal of this project is to investigate whether the political party affiliation of judges at the Swiss Federal Supreme Court influences their decisions. It also examines whether some judges are stricter or more lenient than others and whether judicial behavior changes over time — for example, whether right-leaning judges have become more restrictive.

# Results (brief overview)
The results show clear differences between left-wing and right-wing judges. Panels with a left-wing majority are more likely to approve criminal appeals, while right-wing majorities are more likely to rule in favor of claimants in administrative law cases. The data also show a striking imbalance: panels made up only of right-wing judges are 79 times more common than panels made up only of left-wing judges. This is surprising because it does not reflect the overall balance of judges or political parties and may indicate a problem with how judges are assigned to panels (see publication).

# How the Code Works
### Scraping
**[Scraping_Decisions.py](Scraping_Decisions.py)** This code scrapes the court decisions and labels them correctly.
### Structuring, cleaning, merging
1. **[court_decis_data_structuring.ipynb](court_decis_data_structuring.ipynb)** This code extracts information from the court decisions, such as the judges' names, the outcomes of the decisions, and the area of law. The judges' political party affiliations are added from a separate Excel file. The data is then cleaned, checked, and finally saved as a CSV file (and additionally as an Excel file).
2. **[ext_script_decision_match.py](ext_script_decision_match.py)** This is an external extension of [court_decis_data_structuring.ipynb](court_decis_data_structuring.ipynb) from step 2. It classifies the outcomes of the decisions as success or no success. It is imported as a function.
### Analying and calculate results
1. **3-judge-decisions [court_decis_analyse_3er.ipynb](court_decis_analyse_3er.ipynb)** This code analyzes the data of 3-judge-panels and performs the calculations.
2. **5-judge-decisons  [court_decis_analyse_5er.ipynb](court_decis_analyse_5er.ipynb)** This code analyzes the data of 5-judge-panels and performs the calculations.

# Challenges

Scraping the court decisions and labeling them systematically was not difficult. However, two parts of the project turned out to be major challenges.

1. **Extracting judges' names**

The hardest part was extracting the judges' names from the decisions. The names are not separated by HTML tags or stored in tables. Instead, they appear in text blocks with many different formats: sometimes separated by commas, sometimes not, sometimes with titles such as Judge or Ms. Miller.

I used regular expressions (regex) to identify the names. Each pattern required a different regex, and in the end I had dozens of them. The same approach was needed to extract other information from the decisions.

To improve accuracy, I wrote a separate test script that automatically found decisions where names had not been extracted correctly. This made it much easier to identify missing patterns and add new regex rules.

2. **Responsive graphics**

The second challenge was making the visualization responsive. If a graphic is fairly complex, adapting it to different screen sizes takes much longer than expected. In my case, making the charts responsive almost doubled the development time.
