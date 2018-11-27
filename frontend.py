from flask import Flask, request
import time

app = Flask(__name__)

full_list = []
products = []
addresses = []
delays = []
privacies = []
dates = []
full_dates=[]
i = 0

@app.route('/', methods=['GET', 'POST'])
def frontend():
        global i
        if request.form.get('submit') == 'Submit':
            product = request.form.get('product').encode("utf-8")
            address = request.form.get('address').encode("utf-8")
            delay=request.form['option1'].encode("utf-8")
            privacy=request.form['option2'].encode("utf-8")

            date_year = int(float(time.strftime('%Y', time.localtime(time.time()))))
            date_month = int(float(time.strftime('%m', time.localtime(time.time()))))
            date_day = int(float(time.strftime('%d', time.localtime(time.time()))))
                
            products.append(product)
            addresses.append(address)
            delays.append(delay)
            privacies.append(privacy)
            dates.append([date_year, date_month, date_day])

        if i>0 and request.form["submit"] == "Submit":
                if delays[i-1] == "yes, for one day":
                        dates[i-1][2] += 1
                elif delays[i-1] == "yes, for two days":
                        dates[i-1][2] += 2
                if privacies[i-1] == "yes, please!":
                        privacies[i-1] = 1
                elif privacies[i-1] == "no, I prefer my privacy":
                        privacies[i-1] = 0
                
                full_dates.append(str(dates[i-1][0]) + ":" + str(dates[i-1][1]) + ":" + str(dates[i-1][2]))
                full_list.append(full_dates[i-1] + "-" + "PLACEHOLDER" + "-" + str(privacies[i-1]) + "-" + products[i-1] + "-" + addresses[i-1])
        
        i += 1
        
        if request.form.get('submit') == 'Stop':
            return "Thank you for shopping with us!" 

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


        return full_list

if __name__ == '__main__':
    app.run(host="localhost")
