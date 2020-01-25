# --------------
#  Import Libraries
import json
from collections import Counter


#  Read the data of the format .json type and Load dataset
with open(path) as f:
   data=json.load(f)
print(data)

#  Women who got the first Nobel Prize?
women_count=0
for i in range(len(data)):
  if data[i]['Sex']=='Female':
    women_count=women_count+1
print(women_count)

#  How many have come from india?
country_count=0
for i in range(len(data)):
  if data[i]['Birth Country']=='India':
    country_count=country_count+1
print(country_count)

#  Calculate category wise number of prizes for the people who came from India?
category_data=[]
for i in range(len(data)):
  if data[i]['Birth Country']=='India':
    category_data.append(data[i]['Category'])
for category , count in Counter(category_data).most_common():
  print(category,count)

#   Which country has produced the highest number of Nobel winners for category `Chemistry`?
country_data=[]
for i in range(len(data)):
  if data[i]['Category']=='Chemistry':
    country_data.append(data[i]['Birth Country'])
for country , count in Counter(country_data).most_common(1):
  print(country,count)

#  Which Organization won the most nobel prizes in the category "Physics" and "Chemistry" ?
organization_data=[]
for i in range(len(data)):
  if data[i]['Category']=='Physics' or data[i]['Category']=='Chemistry' :
    organization_data.append(data[i]['Organization Name'])
for organization, count in Counter(organization_data).most_common(1):
  print(organization, count)

#  What was the Motivation for awarding the Nobel Prize for Marie Curie, née Sklodowska?
for i in range(len(data)):
  if data[i]['Full Name'] =='Marie Curie, née Sklodowska':
    print(data[i]['Motivation'])


#  In which category people got Noble Prize in the year 1994?
for i in range(len(data)):
  if data[i]['Year']==1994:
    print(data[i]['Prize'])




