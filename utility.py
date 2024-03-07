import re
import pandas as pd
from IPython.display import display


def clean_skills(inp):
    """Clean skill strings"""
    inp_list = str(inp).strip(',').split(', ')
    inp_list = [i.lower() for i in inp_list if i.strip()]
    return inp_list


def check_job_title(i):
    """Bin job titles"""
    i = i.strip().lower()
    if re.search(r'.*data.*engineer.*', i):
        return 'data engineer'
    elif re.search(r'.*data.*specialist.*', i):
        return 'data engineer'

    elif re.search(r'.*data.*scientist.*', i):
        return 'data scientist'

    elif re.search(r'.*data.*analyst.*', i):
        return 'data analyst'

    elif re.search(r'.*business.*analyst.*', i):
        return 'business analyst'

    elif re.search(r'.*database.*engineer.*', i):
        return 'database administrator'
    elif re.search(r'.*database.*admin.*', i):
        return 'database administrator'

    elif re.search(r'.*data.*architect.*', i):
        return 'data architect'
    elif re.search(r'.*architect.*data.*', i):
        return 'data architect'

    elif re.search(r'.*machine.*learning.*engineer.*', i):
        return 'machine learning engineer'
    elif re.search(r'.*ml.*engineer.*', i):
        return 'machine learning engineer'
    elif re.search(r'.*mlop.*engineer.*', i):
        return 'machine learning engineer'
    elif re.search(r'.*engineer.*machine.*learning.*', i):
        return 'machine learning engineer'
    elif re.search(r'.*mlop.*engineer.*', i):
        return 'machine learning engineer'

    elif re.search(r'.*software.*engineer.*', i):
        return 'software engineer'
    elif re.search(r'.*software.*developer.*', i):
        return 'software engineer'

    elif re.search(r'.*tech.*lead.*', i):
        return 'tech/data lead'
    elif re.search(r'.*data.*lead.*', i):
        return 'tech/data lead'

    elif re.search(r'.*manager.*', i):
        return 'manager'

    elif re.search(r'.*head.*', i):
        return 'c-suite'
    elif re.search(r'.*president.*', i):
        return 'c-suite'
    elif re.search(r'.*superintendent.*', i):
        return 'c-suite'
    elif re.search(r'.*director.*', i):
        return 'c-suite'

    else:
        return 'others'


def init_jobs():
    job_summary = pd.read_csv('linkedin_csv/job_summary.csv')
    job_postings = pd.read_csv('linkedin_csv/job_postings.csv')
    job_skills = pd.read_csv('linkedin_csv/job_skills.csv')
    merged_df = pd.merge(job_summary, job_postings, on='job_link')
    merged_df = pd.merge(merged_df, job_skills, on='job_link')
    display(len(merged_df))
    return merged_df


METHO = """Comparing Hirability for:
- base `{}`
- `{}` plus {} random sampled skills without replacement
- `{}` plus {} unique skills recommended by fim with highest lift
"""


CASE = """Skillset: {}
Hirability: {}%
Jobs available: {}/{}
Applying in all {} {} jobs, you are likely to get into {}
"""


VALID = """Result:
- {} % Hirability (base)
- {} % Hirability (stochastic)
- {} % Hirability (fim)

Hirability increase better in fim case compared to stochastic case!
"""