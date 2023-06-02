import requests
import json
import  json
import csv
import random
import xml.etree.ElementTree as ET
import pandas as pd

# 定义要生成的 CSV 文件名和广州市经纬度范围
filename = ""
lat_range = [22.467, 23.214]
lon_range = [113.098, 113.651]

# 创建包含50个随机位置数据的列表
locations = []
for i in range(50):
    lat = round(random.uniform(lat_range[0], lat_range[1]), 4)
    lon = round(random.uniform(lon_range[0], lon_range[1]), 4)
    locations.append({"name": "Location {}".format(i+1), "lat": lat, "lon": lon})

# 创建 CSV 文件并写入位置数据
with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["name", "latitude", "longitude"]) # 写入标题行
    for loc in locations:
        writer.writerow([loc["name"], loc["lat"], loc["lon"]]) # 写入每个位置的名称、纬度和经度坐标

print("CSV file {} has been generated successfully.".format(filename))




#获取高德地图经纬度
def def_address(n):
    # 获取农讲所经纬度的 URL
    address=n
    key=''
    #url = 'https://restapi.amap.com/v3/geocode/regeo?key={}&location=113.269137,23.135366&poitype=&radius=1000&extensions=all&batch=false&roadlevel=0'
    url=f'https://restapi.amap.com/v3/geocode/geo?address={address}&output=XML&key={key}'
    print(url)

    response = requests.get(url)
    print(response.text)
    if response.status_code == 200:
        try:
            root = ET.fromstring(response.text)
            print(root)
            geocode = root.find('geocodes').find('geocode')
            lnglat = geocode.find('location').text
            address = geocode.find('formatted_address').text
            level=geocode.find('level').text
            print('标签：',level)
            print('农讲所地址：', address)
            print('农讲所经纬度：', lnglat)
        except AttributeError:  # 捕获缺少“location”元素的异常
            print('Error: 缺少“location”元素')
    else:
        print('Error:', response.status_code)







import  os
path='C:/Users/xunyi/Desktop/移动/卜蜂莲花cgi'   #需要获取的地址
f=os.listdir(path)
print(f)
for i in f:
    #print(i.replace('的CGI.csv',''))
    name=i.replace('的CGI.csv','')
    print(name)
    def_address(name)