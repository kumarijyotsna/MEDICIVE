from app.api import medcive
from flask import render_template,make_response
from flask import Flask, request, redirect, url_for

import googlemaps 

#-------API 4-------#
#-----entering user's location-------#
@medcive.route("/location",methods=['POST','GET'])
def location():
        return render_template("map.html")

#------getting suggestion for nearest hospitals-------#
@medcive.route("/map_med",methods=['POST','GET'])
def map_doc():
        add=request.form["add"] #getting address entered by user in form
        gmaps = googlemaps.Client(key='APP_KEY') #connecting to google client
        geocode_result = gmaps.geocode(add)
        lat_lng=[(float(d['geometry']['location']['lat']), float(d['geometry']['location']['lng'])) for d in geocode_result] #extracting latitude and longitude using the address enetered by user
        map_data=gmaps.places(query="hospital", location=lat_lng[0]) #getting the name of hospitals near the address entered by user
        result=map_data["results"]
        result=[[str(res['name']),str(res['formatted_address'])] for res in result]
        return render_template("location.html", res=result)

