##Project: Dr. Semmelweis and the Discovery of Handwashing

##Import
import pandas as pd

#Import file
yearly=pd.read_csv("G:\My Drive\Personal Learning\Coding\Project\yearly_deaths_by_clinic.csv")
yearly['proportion_deaths']=yearly['deaths']/yearly['births']
print(yearly)
clinic_1=yearly.loc[yearly["clinic"]=="clinic 1"]
clinic_2=yearly.loc[yearly["clinic"]=="clinic 2"]
print(clinic_1)
print(clinic_2)
ax=clinic_1.plot(x='year',y='proportion_deaths',ylabel='proportion deaths')
clinic_2.plot(x='year',y='proportion_deaths',ax=ax,ylabel='proportion deaths')

#Monthly
monthly=pd.read_csv("G:\My Drive\Personal Learning\Coding\Project\monthly_deaths.csv",parse_dates=["date"])
monthly["proportion_deaths"]=monthly["deaths"]/ monthly["births"]
print(monthly)

handwashing_start = pd.to_datetime('1847-06-01')
before_washing=monthly.loc[monthly['date']>=handwashing_start]
after_washing=monthly.loc[monthly['date']<handwashing_start]
ax=before_washing.plot(x='date',y='proportion_deaths',ylabel='proportion deaths')
after_washing.plot(x='date',y='proportion_deaths',ax=ax,ylabel='proportion deaths')
