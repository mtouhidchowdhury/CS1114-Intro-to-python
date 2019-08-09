'''

M. Touhid Chowdhury
CS 1114
mtc405
N14108583

Note: Used updated windows file
First function cleans the data and makes new file with just city, date, high temp, low temp, and precipitation
Second Function converts farenheit to celsius
third function converts inch to centimeter
fourth function uses the last two function to convert the cleaned data into metric units
the last function takes the metric file and a year and prints the average of the highests and the lowests 
'''


# Part A
def clean_data(complete_weather_filename, cleaned_weather_filename):
    weather = open(complete_weather_filename, "r")
    cleaned = open(cleaned_weather_filename, "w")
    headers_line = weather.readline()#remove header line

    print("City", "Date","High Temp", "Low Temp", "precipitation", sep = ",",file = cleaned) #new header
    #loop through file and print into new file only desired information
    #convert any alpha into 0 
    for curr_line in weather:
        curr_line = curr_line.strip()
        curr_list = curr_line.split(',')
        city = curr_list[0]
        date = curr_list[1]
        highTemp = curr_list[2]
        lowTemp = curr_list[3]
        precip = curr_list[8]
        if highTemp.isalpha():
            highTemp = 0
        if lowTemp.isalpha():
            lowTemp = 0
        if precip.isalpha():
            precip = 0 
            
        print(city, date, highTemp, lowTemp, precip, sep = ",", file = cleaned)
    #close files after completing 
    cleaned.close()
    weather.close()
    print('done')
    


# Part B
def f_to_c(f_temperature):
    #convert farenheit to celsius
    celsius = (float(f_temperature)-32)*(5/9)
    return celsius

def in_to_cm(inches):
    #convert inches to centimeter
    centimeter = float(inches) * 2.54
    return centimeter

def convert_data_to_metric(imperial_weather_filename, metric_weather_filename):
    #convert all data to metric
    imperial = open(imperial_weather_filename, "r")
    metric = open(metric_weather_filename, "w")
    headline = imperial.readline()
    print("city", "date","highTemp", "lowTemp", "precipitation", sep = ",", file = metric)
    for curr_line in imperial:
        curr_line = curr_line.strip()
        curr_list = curr_line.split(',')
        city = curr_list[0]
        date = curr_list[1]
        highTemp = f_to_c(curr_list[2])
        lowTemp = f_to_c(curr_list[3])
        precip = in_to_cm(curr_list[4])
        print(city, date, highTemp, lowTemp, precip, sep = ",", file = metric)

    metric.close()
    imperial.close()
    print("done")

#Part C
def print_average_temps_per_month(city, weather_filename, unit_type):
# prints average highs and lows in each month for the given city
    file = open(weather_filename, 'r')
    headline = file.readline()
    counterMonths= [0,0,0,0,0,0,0,0,0,0,0,0] #keep track of how many times each month occur
    valuesForHigh = [0,0,0,0,0,0,0,0,0,0,0,0]# keeps track of the highs of every month
    valuesForLow =[0,0,0,0,0,0,0,0,0,0,0,0] #keep track of the lows of every month 
    countMetric = 0
    countImperial = 0 
    print("Average temperatures for ", city, ":")
    for curr_line in file:
        curr_line.strip()
        curr_list = curr_line.split(',')
        cityFile = curr_list[0]
        date = curr_list[1]
        highTemp = curr_list[2]
        lowTemp = curr_list[3]
        monthDayYearList = date.split('/')
        if cityFile == city:
            for number in range(0,13):
                if monthDayYearList[0] == str(number):
                    valuesForHigh [number-1] += float(highTemp)
                    valuesForLow[number-1] += float(lowTemp)
                    counterMonths[number-1] += 1
    #list of months to print
    month =["January", "February", "March", "April","May", "June", "July","August","September", "October", "November", "December"]
    if unit_type == "imperial":
        for appearance in counterMonths:
            print(month[countMetric],":",round(valuesForHigh[countMetric]/appearance,3),"F High",round(valuesForLow[countMetric]/appearance,3), "F low")  
            countMetric +=1 
    if unit_type == "metric":
        for appearance in counterMonths:
            print(month[countImperial],":",round(valuesForHigh[countImperial]/appearance,3),"C High",round(valuesForLow[countImperial]/appearance,3), "C low")  
            countImperial +=1
    file.close()
    



#Part D
def highest_and_Lowest(metric_weather_file, year): 
    # Write a function that tells you which year had how much average high tempt and low tempt for the available data
    # assume that the unit is metric
    # assume that all the data has the complete year for the years available (2010-2015)
    # assume user will put a year thats in the file
    # Use the metric file that you created in previous function
    file = open(metric_weather_file, "r")
    header = file.readline()
    highest = 0
    lowest = 0
    occur = 0
    yearsAvailable = [2010,2011,2012,2013,2014,2015]
    for curr_line in file:
        curr_line = curr_line.strip()
        curr_list = curr_line.split(',')
        cityFile = curr_list[0]
        date = curr_list[1]
        highTemp = curr_list[2]
        lowTemp = curr_list[3]
        monthDayYearList = date.split('/')
        
        if str(monthDayYearList[2]) == str(year):
            lowest += float(lowTemp)
            highest += float(highTemp)
            occur += 1
    if occur > 0:
        print("The average of the lowest temperatures of the year",year,"is", round(lowest/occur, 2),"C", "\n"\
              "and average of the highest temperatures is", round(highest/ occur, 2),"C")
    else:
        print("THE YEAR IS NOT AVAILABLE")

def main():
    print ("Running Part A")
    clean_data("weatherwindows.csv", "weather in imperial.csv")
    
    print ("Running Part B")
    convert_data_to_metric("weather in imperial.csv", "weather in metric.csv")
    
    print ("Running Part C")
    print_average_temps_per_month("San Francisco", "weather in imperial.csv", "imperial")
    print_average_temps_per_month("New York", "weather in metric.csv", "metric")
    print_average_temps_per_month("San Jose", "weather in imperial.csv", "imperial")

    print ("Running Part D")
    highest_and_Lowest("weather in metric.csv", 2011)  
main()
