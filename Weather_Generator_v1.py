import datetime
import requests
import os
import random
import sys

class weather:
    
    def __init__(self,start_date):
        #print('class Initiated')
        self.loc = ''
        self.position = ''
        self.local_time = ''
        self.condition = ''
        self.temperature = ''
        self.pressure = ''
        self.humidity = ''
        self.location_list = []
        self.start_date = start_date
        self.location_list = None
        with open('My_Data/Locations.txt') as f:
            self.location_list = [line.strip() for line in f]
        #print(self.location_list)
        
    def location_data(self,location):
        
        url_geo_code = 'https://maps.googleapis.com/maps/api/geocode/json?sensor=false&address='
        url_elevation = 'https://maps.googleapis.com/maps/api/elevation/json?locations='
        #print("url's set")
        while True :
            location_info = {'location': location}
            #print('sucessful location')
            #print(location_info['location'])
            geo_info = requests.get(url_geo_code+location+'&key=AIzaSyC2vRJb6df3t1sHbc24bPe7tosYzy0HR3A')
            #print(geo_info.status_code)
            loc_geo_info = geo_info.json()
            if loc_geo_info.get('results') != [] :
                break
        
        if loc_geo_info.get('results'):
            for loc_geo_info_results in loc_geo_info.get('results'):
                latlong = loc_geo_info_results.get('geometry','').get('location','')
                #print('sucessful latlong')
                location_info['lat'] = latlong.get('lat','')
                #print('sucessful lat')
                location_info['lng'] = latlong.get('lng','')
                #print('sucessful lng')
                #print(url_elevation , str(location_info['lat']) , str(location_info['lng']), "&key='AIzaSyB7ifjtSnY4jXlsk_PXiTFPz9dch5FbjFA'")
                #print("request_elevattion started")
                request_elevation = requests.get(url_elevation + str(location_info['lat']) + ',' + str(location_info['lng']) + '&key=AIzaSyC2vRJb6df3t1sHbc24bPe7tosYzy0HR3A').json()
                #print(request_elevation)
                if request_elevation.get('results'):
                    for request_elevation_results in request_elevation.get('results'):
                        location_info['elev'] = request_elevation_results.get('elevation', '')
                        #print('sucessful elev')
                        break
                    break
        
        all_weather_data = []
        
        for date_offset in range(0,365,30):
            #print(location)
            location_data = {}
            #print(location_data)
            location_data['loc'] = location_info['location']
            location_data['lat'] = location_info['lat']
            location_data['lng'] = location_info['lng']
            location_data['elevation'] = location_info['elev']
            new_date = self.start_date + datetime.timedelta(date_offset)
            location_data['time'] = new_date.isoformat()
            location_data['humidity'] = random.randint(15,90)
            location_data['pressure'] = random.randint(200,800)
            location_data['temp'] = random.randint(-8,50)
            if location_data['temp'] >= 0 and location_data['humidity'] > 75:
                location_data['condition'] = "Rain"
            elif location_data['temp'] >= 0 and location_data['humidity'] < 75:
                location_data['condition'] = "Sunny"
            elif location_data['temp'] <= 0:
                location_data['condition'] = "Snow"
            else:
                location_data['condition'] = ""
            
            all_weather_data.append(location_data)
        

        for l in all_weather_data:
            out_data = ''
            self.loc = l['loc']
            #print(loc)
            self.position = str(l['lat']) + ',' + str(l['lng'])  + ',' + str(l['elevation'])
            #print(position)
            self.local_time = str(l['time'])
            #print(local_time)
            self.condition = l['condition']
            if l['temp'] > 0 :
                self.temperature = '+' + str(l['temp'])
            else:
                self.temperature = str(l['temp'])
            self.pressure = l['pressure']
            self.humidity = l['humidity']
            out_data = str(self.loc) + '|' + str(self.position) + '|' + str(self.local_time) +'|' + str(self.condition) + '|' + str(self.temperature)  + '|' + str(self.pressure)  + '|' + str(self.humidity) 
            print(out_data)
    
    def weather_data(self):
        
        for location in self.location_list:
            #print(location)
            self.location_data(location)
            
        

if __name__ == '__main__':
    start_date = datetime.datetime(1989, 3, 24)
    location_weather = weather(start_date)
    location_weather.weather_data()
