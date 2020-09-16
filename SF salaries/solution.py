# Goal --> Explore San Francisco city employee salary data

"""
Exploration Ideas
To help get you started, here are some data exploration ideas:

How have salaries changed over time between different groups of people?
How are base pay, overtime pay, and benefits allocated between different groups?
Is there any evidence of pay discrimination based on gender in this dataset?
How is budget allocated based on different groups and responsibilities?
"""

import pandas as pd

salaries = pd.read_csv('dataset/14_827864_bundle_archive/Salaries.csv')

#how many entries
salaries.info()

#average basepay ?
#BasePay is object type.
#lets convert to float

salaries['BasePay'].astype(float)
#ValueError: could not convert string to float: 'Not Provided'

salaries['BasePay'].mean()
#TypeError: unsupported operand type(s) for +: 'float' and 'str'

#highest amount of overtimepay ?
salaries['OvertimePay'].max()

#job title of JOSEPH DRISCOLL
salaries[salaries['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']

#how much does JOSEPH DRISCOLL make ?
salaries[salaries['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits']

#highest paid person
salaries[salaries['TotalPayBenefits'] == salaries['TotalPayBenefits'].max()]['EmployeeName']
#OR
salaries.loc[salaries['TotalPayBenefits'].idxmax()]

#name of lowest paid person
salaries[salaries['TotalPayBenefits'] == salaries['TotalPayBenefits'].min()]['EmployeeName']
#OR
salaries.iloc[salaries['TotalPayBenefits'].argmin()]

#average TotalPay of all employees per year
year = salaries['Year']=='2011'
salaries[salaries['BasePay'].mean()].where(year,inplace=True) #haven't cross checked due type error
#OR
salaries.groupby('Year').mean()['TotalPay']

#unique job titles
salaries['JobTitle'].nunique()

#top 5 most common jobs
salaries['JobTitle'].value_counts().head(5)

#job title represented by only 1 person
sum(salaries['JobTitle'].value_counts() == 1)

#total people having Chief in job title
def chief(title):
    if "chief" in title.lower().split():
        return True
    else:
        return False

chief('chief executive officer') # for testing
sum(salaries['JobTitle'].apply(lambda x: chief(x)))

#correlation between JobTitle and TotalPayBenefits
salaries[['JobTitle','TotalPayBenefits']].corr()

#correlation between length ofJobTitle and TotalPayBenefits
salaries['JobTitleLen'] = salaries['JobTitle'].apply(len)

salaries[['JobTitleLen','TotalPayBenefits']].corr()