import pandas
import matplotlib.pyplot as plt
import numpy as np

''' 
The following is the starting code for path1 for data reading to make your first step easier.
'dataset_1' is the clean data for path1.
'''
dataset_1 = pandas.read_csv('NYC_Bicycle_Counts_2016_Corrected.csv')
dataset_1['Brooklyn Bridge']      = pandas.to_numeric(dataset_1['Brooklyn Bridge'].replace(',','', regex=True))
dataset_1['Manhattan Bridge']     = pandas.to_numeric(dataset_1['Manhattan Bridge'].replace(',','', regex=True))
dataset_1['Queensboro Bridge']    = pandas.to_numeric(dataset_1['Queensboro Bridge'].replace(',','', regex=True))
dataset_1['Williamsburg Bridge']  = pandas.to_numeric(dataset_1['Williamsburg Bridge'].replace(',','', regex=True))
dataset_1['Williamsburg Bridge']  = pandas.to_numeric(dataset_1['Williamsburg Bridge'].replace(',','', regex=True))

dataset_1['Total'] = pandas.to_numeric(dataset_1['Total'].replace(',', '', regex=True))


print(dataset_1.to_string()) #This line will print out your data

brook_bridge = dataset_1['Brooklyn Bridge']
man_bridge = dataset_1['Manhattan Bridge']
queen_brdige = dataset_1['Queensboro Bridge']
will_bridge = dataset_1['Williamsburg Bridge']

days = len(will_bridge)
averages = []

averages.append(sum(brook_bridge) / days)
averages.append(sum(man_bridge) / days)
averages.append(sum(queen_brdige) / days)
averages.append(sum(will_bridge) / days)

# finding the minimum value
#print(averages)
succ_bridge = min(averages)
#print(averages.index(succ_bridge))

if averages.index(succ_bridge) == 0:
    succ_bridge = 'Brooklyn Bridge'

elif averages.index(succ_bridge) == 1:
    succ_bridge = 'Manhattan Bridge'

elif averages.index(succ_bridge) == 2:
    succ_bridge = 'Queensboro Bridge'

elif averages.index(succ_bridge) == 3:
    succ_bridge = 'Williamsburg Bridge'



##problem 2 & 3 code below
lowtemp = dataset_1['Low Temp']
minimumlow = int(min(lowtemp))
maximumlow = int(max(lowtemp))
ranglow = maximumlow - minimumlow

hightemp = dataset_1['High Temp']
minimumhigh = int(min(hightemp))
maximumhigh = int(max(hightemp))
ranghigh = maximumhigh - minimumhigh

weather = dataset_1['Precipitation']
maxweather = int(max(weather))
minweather = int(min(weather))
rangweather = maxweather - minweather
dataset_1['weather'] = (pandas.to_numeric(dataset_1['Precipitation'].replace(',', '', regex=True)) - minweather) / rangweather



ppl = dataset_1['Total']
minimumppl = int((min(ppl)))
maximumppl = int((max(ppl)))
rangppl = maximumppl - minimumppl

dataset_1['traffic'] = (pandas.to_numeric(dataset_1['Total'].replace(',', '', regex=True)) - minimumppl) / rangppl
norm = dataset_1['traffic']

dataset_1['lowtemps'] = (pandas.to_numeric(dataset_1['Low Temp'].replace(',', '', regex=True))  - minimumlow) / ranglow
dataset_1['hightemps'] = (pandas.to_numeric(dataset_1['High Temp'].replace(',', '', regex=True))  - minimumhigh) / ranghigh

dataset_1.plot(x='Date', y=['lowtemps', 'traffic'])
plt.title('Low Temps & Traffic Throughout the Year')
plt.xlabel('Date')
plt.ylabel('Normalized Low Temps and Traffic')
plt.show()

dataset_1.plot(x='Date', y=['hightemps', 'traffic'])
plt.title('High Temps & Traffic Throughout the Year')
plt.xlabel('Date')
plt.ylabel('Normlaized High Temps and Traffic')
plt.show()


dataset_1.plot.bar(x='Date', y=['lowtemps', 'traffic'])
plt.title('Low Temps and Traffic Throughout the Year')
#plt.xlablel('Date')
plt.ylabel('Normalized Low Temps and Traffic')
plt.show()



corrl_weathertotraffic = dataset_1['Precipitation'].corr(dataset_1['traffic'])
#print(corrl)
corrl_lowtotraffic = dataset_1['lowtemps'].corr(dataset_1['traffic'])
#print(corrl)
corrl_hightotraffic = dataset_1['hightemps'].corr(dataset_1['traffic'])
#print(corrl)


mondays = []
tuesdays = []
wednesdays = []
thursdays = []
fridays = []
saturdays = []
sundays = []
for i in range(len(ppl)):
    if i%7 == 0:
        fridays.append(dataset_1['Total'][i])

    elif i%7 == 1:
        saturdays.append(dataset_1['Total'][i])

    elif i%7 == 2:
        sundays.append(dataset_1['Total'][i])

    elif i%7 == 3:
        mondays.append(dataset_1['Total'][i])

    elif i%7 == 4:
        tuesdays.append(dataset_1['Total'][i])

    elif i%7 == 5:
        wednesdays.append(dataset_1['Total'][i])

    elif i%7 == 6:
        thursdays.append(dataset_1['Total'][i])


dayavgs = []
print('Avgerages based on days:')
friavg = sum(fridays) / len(fridays)
dayavgs.append(friavg)
print('Friday: ', friavg)
satavg = sum(saturdays) / len(saturdays)
dayavgs.append(satavg)
print('Saturday: ', satavg)
sunavg = sum(sundays) / len(sundays)
dayavgs.append(sunavg)
print('Sunday: ', sunavg)
monavg = sum(mondays) / len(mondays)
dayavgs.append(monavg)
print('Monday: ', monavg)
tuesavg = sum(tuesdays) / len(tuesdays)
dayavgs.append(tuesavg)
print('Tuesday: ', tuesavg)
wedavg = sum(wednesdays) / len(wednesdays)
dayavgs.append(wedavg)
print('Wednesday: ', wedavg)
thuravg = sum(thursdays) / len(thursdays)
dayavgs.append(wedavg)
print('Thursday: ', thuravg)


plt.plot(dayavgs)
plt.xlabel('Days')
plt.ylabel('Average traffic')
plt.title('Average Traffic vs Days of the Week')
plt.show()



new_column = []
for j in range(len(ppl)):
    new_column.append(j%7)


#print(new_column)
dataset_1['Day Values'] = new_column

#print(dataset_1.to_string())


corr_daystotraffic = dataset_1['Day Values'].corr(dataset_1['traffic'])
#print(corrl)
print('============================================================')
print('Calculated Correlation Values:')
print('Correlation between weather and bridge traffic: ', corrl_weathertotraffic)
print('Correlation between low temps and bridge traffic: ', corrl_lowtotraffic)
print('Correlation between high temps and bridge traffic: ', corrl_hightotraffic)
print('Correlation between days of the week and bridge traffic: ', corr_daystotraffic)




###attempting to fit them


regression = np.polyfit(dataset_1['Date'], dataset_1['traffic'], deg=2)


# print(dataset_1.to_string())


