# Weather_Data
This weather data is generated for Given list of cities


Create a toy simulation of the environment (taking into account things like atmosphere, topography, geography, oceanography, or similar) that evolves over time

Environment
Python 3.5.2 |Enthought, Inc. (x86_64)| (default, Mar  2 2017, 16:37:47) [MSC v.1900 64 bit (AMD64)]


Project Structure
My_Data : this is the folder which contains input data related to this script (Locations.txt)


Instructions to run :

1. Please keep all the locations in My_Data/Locations.txt
2. Please change the path in python to your directory where My_Data folder is present
3. run the script by typing below in the python prompt
	python Weather_Generator.py
4. Please change the Google API Key to get the latitute and logitude and elevation ( Each Key only supports limited requestes per day)

	
Output :

1. Output is | (pipe) delimited format
2. output is in the format of 

Location | Position | Local time | Conditions | Temperature | Pressure | Relative humidity

Where
• Location is an optional label describing one or more positions,
• Position is a comma-separated triple containing latitude, longitude, and elevation in metres above sea level,
• Local time is an ISO8601 date time,
• Conditions is either Snow, Rain, Sunny,
• Temperature is in °C,
• Pressure is in hPa, and
• Relative humidity is a %.

Sample Output

Sydney|-33.86,151.21,39|2015-12-23T05:02:12Z|Rain|+12.5|1004.3|97
Melbourne|-37.83,144.98,7|2015-12-24T15:30:55Z|Snow|-5.3|998.4|55
Adelaide|-34.92,138.62,48|2016-01-03T12:35:37Z|Sunny|+39.4|1114.1|12



To Generate the Same Result using Python Class Objects :
Please use the Weather_Generator_v1.py

Note all the above mentioned Instructions to Run will apply.

execution :
python Weather_Generator_v1.py
