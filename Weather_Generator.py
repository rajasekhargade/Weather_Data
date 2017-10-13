import datetime
import requests
import os
import random
import sys

os.environ['TZ'] = 'UTC'

def loc_info(location_list):
    
    url_geo_code = 'https://maps.googleapis.com/maps/api/geocode/json?sensor=false&address='
    url_elevation = 'https://maps.googleapis.com/maps/api/elevation/json?locations='

    loc_info_list = []

    for location in location_list:
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

        loc_info_list.append(location_info)
        #print(loc_info_list)

    return loc_info_list

def weather_condition(loc_data):
    if loc_data['temp'] >= 0 and loc_data['humidity'] > 75:
        loc_data['condition'] = "Rain"
    elif loc_data['temp'] >= 0 and loc_data['humidity'] < 75:
        loc_data['condition'] = "Sunny"
    elif loc_data['temp'] <= 0:
        loc_data['condition'] = "Snow"
    else:
        loc_data['condition'] = ""
    return loc_data['condition']


def weather_data(loc_list,start_date):
    
    all_weather_data = []
    for location in loc_list:
        for date_offset in range(0,365,30):
            #print(location)
            location_data = {}
            #print(location_data)
            location_data['loc'] = location['location']
            location_data['lat'] = location['lat']
            location_data['lng'] = location['lng']
            location_data['elevation'] = location['elev']
            new_date = start_date + datetime.timedelta(date_offset)
            location_data['time'] = new_date.isoformat()
            location_data['humidity'] = random.randint(15,90)
            location_data['pressure'] = random.randint(200,800)
            location_data['temp'] = random.randint(-8,50)
            location_data['cond'] = weather_condition(location_data)
            all_weather_data.append(location_data)
            #print(all_weather_data)
    return all_weather_data    

def output_data(location_weather_data):
    #print("started")
    output_data = []
    for l in location_weather_data:
        out_data = ''
        loc = l['loc']
        #print(loc)
        position = str(l['lat']) + ',' + str(l['lng'])  + ',' + str(l['elevation'])
        #print(position)
        local_time = str(l['time'])
        #print(local_time)
        condition = l['cond']
        if l['temp'] > 0 :
            temperature = '+' + str(l['temp'])
        else:
            temperature = str(l['temp'])
        pressure = l['pressure']
        humidity = l['humidity']
        out_data = str(loc) + '|' + str(position) + '|' + str(local_time) +'|' + str(condition) + '|' + str(temperature)  + '|' + str(pressure)  + '|' + str(humidity) 
        print(out_data)
        output_data.append(out_data)
        #print(output_data)
    return output_data
    
if __name__ == '__main__':
    location_list = None
    with open('My_Data/Locations.txt') as f:
        location_list = [line.strip() for line in f]

    location_info_list = loc_info(location_list)
    #print(location_info_list)
    #location_info_list=[{'elev': 99.28376007080078, 'lng': 79.7399875, 'location': 'Andhra Pradesh', 'lat': 15.9128998}, {'elev': 533.9525756835938, 'lng': 94.7277528, 'location': 'Arunachal Pradesh', 'lat': 28.2179994}, {'elev': 198.1753540039062, 'lng': 92.9375739, 'location': 'Assam', 'lat': 26.2006043}, {'elev': 68.76460266113281, 'lng': 85.31311939999999, 'location': 'Bihar', 'lat': 25.0960742}, {'elev': 279.1519165039062, 'lng': 81.8661442, 'location': 'Chhattisgarh', 'lat': 21.2786567}, {'elev': 104.106575012207, 'lng': 74.12399599999999, 'location': 'Goa', 'lat': 15.2993265}, {'elev': 292.5394897460938, 'lng': 71.1923805, 'location': 'Gujarat', 'lat': 22.258652}, {'elev': 217.25, 'lng': 76.085601, 'location': 'Haryana', 'lat': 29.0587757}, {'elev': 2197.066162109375, 'lng': 77.17339009999999, 'location': 'Himachal Pradesh', 'lat': 31.1048294}, {'elev': 5549.93408203125, 'lng': 76.57617139999999, 'location': 'Jammu and Kashmir', 'lat': 33.778175}, {'elev': 412.9102783203125, 'lng': 85.2799354, 'location': 'Jharkhand', 'lat': 23.6101808}, {'elev': 651.4623413085938, 'lng': 75.7138884, 'location': 'Karnataka', 'lat': 15.3172775}, {'elev': 53.64788818359375, 'lng': 76.2710833, 'location': 'Kerala', 'lat': 10.8505159}, {'elev': 331.314208984375, 'lng': 78.6568942, 'location': 'Madhya Pradesh', 'lat': 22.9734229}, {'elev': 505.10400390625, 'lng': 75.7138884, 'location': 'Maharashtra', 'lat': 19.7514798}, {'elev': 776.8121948242188, 'lng': 93.90626879999999, 'location': 'Manipur', 'lat': 24.6637173}, {'elev': 1527.630859375, 'lng': 91.366216, 'location': 'Meghalaya', 'lat': 25.4670308}, {'elev': 598.346435546875, 'lng': 92.9375739, 'location': 'Mizoram', 'lat': 23.164543}, {'elev': 1333.762329101562, 'lng': 94.5624426, 'location': 'Nagaland', 'lat': 26.1584354}, {'elev': 123.0769271850586, 'lng': 85.0985236, 'location': 'Odisha', 'lat': 20.9516658}, {'elev': 223.6012573242188, 'lng': 75.34121789999999, 'location': 'Punjab', 'lat': 31.1471305}, {'elev': 344.2458190917969, 'lng': 74.21793260000001, 'location': 'Rajasthan', 'lat': 27.0238036}, {'elev': 837.9268798828125, 'lng': 88.5122178, 'location': 'Sikkim', 'lat': 27.5329718}, {'elev': 138, 'lng': 78.6568942, 'location': 'Tamil Nadu', 'lat': 11.1271225}, {'elev': 405.2203979492188, 'lng': 79.01929969999999, 'location': 'Telangana', 'lat': 18.1124372}, {'elev': 64.91964721679688, 'lng': 91.9881527, 'location': 'Tripura', 'lat': 23.9408482}, {'elev': 117.3600921630859, 'lng': 80.9461592, 'location': 'Uttar Pradesh', 'lat': 26.8467088}, {'elev': 2189.307861328125, 'lng': 79.01929969999999, 'location': 'Uttarakhand', 'lat': 30.066753}, {'elev': 26.83669471740723, 'lng': 87.8549755, 'location': 'West Bengal', 'lat': 22.9867569}, {'elev': 86.1482162475586, 'lng': 92.6586401, 'location': 'Andaman and Nicobar Islands', 'lat': 11.7400867}, {'elev': 348.65283203125, 'lng': 76.7794179, 'location': 'Chandigarh', 'lat': 30.7333148}, {'elev': 52.30442810058594, 'lng': 73.0169135, 'location': 'Dadra and Nagar Haveli', 'lat': 20.1808672}, {'elev': 9.618703842163086, 'lng': 72.8397317, 'location': 'Daman and Diu', 'lat': 20.428283}, {'elev': 218.0439605712891, 'lng': 77.10249019999999, 'location': 'Delhi', 'lat': 28.7040592}, {'elev': -1833.188232421875, 'lng': 72.78463359999999, 'location': 'Lakshadweep', 'lat': 10.3280265}, {'elev': 439.2325439453125, 'lng': 78.92553199999999, 'location': 'Puducherry', 'lat': 13.801001}]
    #print(location_info_list)
    loc_weather_data = weather_data(location_info_list, datetime.datetime(1989, 3, 24))
    #print(loc_weather_data)
    final_weather_data = output_data(loc_weather_data)
    
    
    
    