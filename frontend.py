from flask import Flask, request, Response
import time
from geoloc import addressToDistance
from algo import userParse, dateParse, addToOrderList, order, lumpedOrders
from createPath import Path
import folium
import googlemaps

app = Flask(__name__)

#all the lists we will later need
full_list = []
products = []
addresses = []
delays = []
privacies = []
dates = []
full_dates=[]
ListOfToday = ["9500 Gilman Drive, La Jolla, CA"] #make sure we begin at base
i = 0
gmaps = googlemaps.Client(key='AIzaSyAZ5896c7UzrpG99I_PCdlFBebE0jpAlVM')

@app.route('/', methods=['GET', 'POST'])
def frontend():
        global i
        global ListOfToday
        #with each user submittion, record their responses
        if request.form.get('submit') == 'Submit':
            product = request.form.get('product').encode("utf-8")
            address = request.form.get('address').encode("utf-8")
            delay=request.form['option1'].encode("utf-8")
            privacy=request.form['option2'].encode("utf-8")

            #timestamp
            date_year = int(float(time.strftime('%Y', time.localtime(time.time()))))
            date_month = int(float(time.strftime('%m', time.localtime(time.time()))))
            date_day = int(float(time.strftime('%d', time.localtime(time.time()))))

            #lists of all users' preferences                
            products.append(product)
            addresses.append(address)
            delays.append(delay)
            privacies.append(privacy)
            dates.append([date_year, date_month, date_day])

            address1 = "9500 Gilman Drive, La Jolla, CA" #base

        if i>0 and request.form["submit"] == "Submit":
                #change the timestamp of those willing to delay
                if delays[i-1] == "yes, for one day":
                        dates[i-1][2] += 1
                elif delays[i-1] == "yes, for two days":
                        dates[i-1][2] += 2
                if privacies[i-1] == "yes, please!":
                        privacies[i-1] = 1
                elif privacies[i-1] == "no, I prefer my privacy":
                        privacies[i-1] = 0

                #find distances between base and all addresses
                distance = addressToDistance(address1, addresses[i-1])

                #create long string of the information gathered
                full_dates.append(str(dates[i-1][0]) + ":" + str(dates[i-1][1]) + ":" + str(dates[i-1][2]))
                full_list.append(full_dates[i-1] + "-" + str(distance) + "-" + str(privacies[i-1]) + "-" + products[i-1] + "-" + addresses[i-1])

        i += 1
        privacyOrders = [] #for users who desire privacy
        generalOrders = [] #for users who do not need privacy

        #create order lists per each day
        for user in full_list:
                userInfo = userParse(user)
                privacy = userInfo[2]

                if (privacy == '0'):
                        privacyOrders.append(userInfo)
                        privacyOrders.sort()
                else:
                        generalOrders.append(userInfo)
                        generalOrders.sort()

        #we will now show the path of all general orders modified to be on the third of december
        #as in, all orders that were either made (i) on the first of december and agreed to delay in two days;
                                                #(ii) on the second of december and agreed to delay in one day;
                                                ##(iii) on the third of december
        
        lumpedOrderList = lumpedOrders(generalOrders, '3')
        addressList = []
        for order in lumpedOrderList:
                addressList.append(order[4])

        for order in generalOrders:
                date = order[0]
                day = dateParse(date)

                if (day == '3'):
                        addressList.append(order[4])

        if request.form.get('submit') == 'Stop': #when user stops shopping

                ListOfToday.extend(list(set(addressList)))
                ListOfToday.append("9500 Gilman Drive, La Jolla, CA") #make sure at the end, comes back to base
                
        #organize path:
                points = Path(ListOfToday) #list of coordinates in the order of shortest path
                
                lat = []
                Long = []

                #find coordinates of all of today's orders
                for m in range(len(ListOfToday)):
                        loc = gmaps.geocode(ListOfToday[m])
                        lat.append(loc[0]['geometry']['location']['lat'])
                        Long.append(loc[0]['geometry']['location']['lng'])

                #map base, all addresses and their products, and the shortest path
                mapit = folium.Map(location=[lat[0], Long[0]], zoom_start=12)
                for k in range(len(lat)):
                        if k == 0 or k == (len(lat)-1):
                                folium.Marker(location=[lat[0], Long[0]], icon = folium.Icon(color='red')).add_to( mapit )
                        else:
                                folium.Marker(location=[lat[k], Long[k]]).add_to( mapit )
                folium.PolyLine(points).add_to(mapit)
                mapit.save('/Users/durstido/Desktop/map4.html') #change to save it on your own desktop

                return "Thank you for shopping with us!"

        #returning the structure of our html website to local host below
        return '''<form method="POST">
                  Product: <input type="text" name="product"><br>
                  Address (street, city, state): <input type="text" name="address"><br>
                  Would you be willing to delay your shipping? <br>
                  <input type="radio" name="option1" value="yes, for one day">yes, for one day<br>
                  <input type="radio" name="option1" value="yes, for two days">yes, for two days<br>
                  <input type="radio" name="option1" value="not today">no<br>
                  Would you be willing to share your box with another product, in order to reduce the amount of boxes shipped? <br>
                  <input type="radio" name="option2" value="yes, please!">yes, please!<br>
                  <input type="radio" name="option2" value="no, I prefer my privacy">no, I prefer my privacy<br>
                  <input type="submit" name="submit" value="Submit">
                  <input type="submit" name="submit" value="Stop"><br>
              </form>'''

if __name__ == '__main__':
    app.run(host="localhost")


