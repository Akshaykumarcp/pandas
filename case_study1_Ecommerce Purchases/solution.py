import pandas as pd

ecommerce = pd.read_csv('Ecommerce Purchases')

#total rows and columns
ecommerce.shape
#OR
ecommerce.info()

#average purchase of Price
ecommerce['Purchase Price'].mean()

#highest and lowest price
ecommerce['Purchase Price'].max()
ecommerce['Purchase Price'].min()

#how many people has english 'en' as their language of choice
len(ecommerce[ecommerce['Language'] == 'en'])
#OR
ecommerce[ecommerce['Language']=='en']['Language'].count()

#total people having job title of "Lawyer"
len(ecommerce[ecommerce['Job'] == 'Lawyer'])
#OR
ecommerce[ecommerce['Job']=='Lawyer'].info()
#OR
ecommerce[ecommerce['Job']=='Lawyer']['Job'].count()
#OR
len(ecommerce[ecommerce['Job']=='Lawyer'].index)

#total people made purchases during AM and PM
len(ecommerce[ecommerce['AM or PM'] == 'AM'])
len(ecommerce[ecommerce['AM or PM'] == 'PM'])
#OR
ecommerce['AM or PM'].value_counts()

#5 most common job titles
ecommerce['Job'].value_counts().head(5)

#someone made purchase from Lot:"90 WT", what was the purchase price for the transaction
ecommerce[ecommerce['Lot'] =="90 WT"]['Purchase Price']

#email of person with credit card no : 4926535242672853
ecommerce[ecommerce['Credit Card']==4926535242672853]['Email']

#people with American express as credit card provider and made purchase above $95
len(ecommerce[(ecommerce['CC Provider'] == 'American Express') & (ecommerce['Purchase Price'] > 95)])
#OR
ecommerce[(ecommerce['CC Provider'] == 'American Express') & (ecommerce['Purchase Price'] > 95)].count()

#credit card that expires in 2025
sum(ecommerce['CC Exp Date'].apply(lambda exp:exp[3:]=='25'))
#OR
ecommerce[ecommerce['CC Exp Date'].apply(lambda exp:exp[3:]=='25')].count()

#top 5 email providers/hosts

ecommerce['Email'][0].split('@')[1]

ecommerce['Email'].apply(lambda email:email.split('@')[1]).value_counts().head(5)
ecommerce.columns


