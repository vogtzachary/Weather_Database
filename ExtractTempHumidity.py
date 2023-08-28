# Purpose: Extract temperature, humidity data from weather database into CSV file
# Run BuildWeatherDB.py to build weather database before running this program

import sqlite3

#convert Celsius temperature to Fahrenheit
def convertCtoF(tempC):
    return (tempC*9.0/5.0) + 32.0

# File names for database and output file
dbFile = "weather.db"
output_file_name='formatdata'

# Connect to and query weather database and
conn = sqlite3.connect(dbFile)

# Create cursor to execute SQL commands
cur = conn.cursor()
selectCmd = """ SELECT temperature, relativeHumidity FROM observations
                ORDER BY timestamp; """
cur.execute(selectCmd)
allRows = cur.fetchall()
# Limit the number of rows output to half
rowCount = len(allRows)//2 # double slash does integer division
rows = allRows[rowCount:]
rows2 = allRows[:rowCount]
rows_list = [rows, rows2]


count = 1
#write data to output file
for i in rows_list:
    with open(output_file_name + str(count) + ".csv","w+") as outf:
        outf.write('Celsius,Fahrenheit,Humidity')
        outf.write('\n')
        for row in i:
            tempC = row[0]
            if tempC is None:       # Handle missing temperature value
                continue
            else:
                tempF = convertCtoF(tempC)
                outf.write(str(tempC)+',')
                outf.write(str(tempF)+',')
            humidity = row[1]
            if humidity is None:   # Handle missing humidity value
                outf.write('\n')
            else:
                outf.write(str(humidity)+'\n') # Print data to file separated by commas
    count += 1