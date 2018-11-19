from flask import Flask, request

app = Flask(__name__)

products = []
addresses = []
delays = []
privacies = []

@app.route('/', methods=['GET', 'POST'])
def form_example():
    #if request.method == 'POST':
        if request.form.get('submit') == 'Submit':
            product = request.form.get('product').encode("utf-8")
            address = request.form.get('address').encode("utf-8")
            delay=request.form['option1'].encode("utf-8")
            privacy=request.form['option2'].encode("utf-8")

            products.append(product)
            addresses.append(street)
            delays.append(delay)
            privacies.append(privacy)

        print(products)
        print(delays)
        print(privacies)
        
        if request.form.get('submit') == 'Stop':
            return "thank you for shopping with us"

        return '''<form method="POST">
                  Product: <input type="text" name="product"><br>
                  Address: <br>
                    Street: <input type="text" name="street"><br>
                    City: <input type="text" name="city"><br>
                    State: <input type="text" name="state"><br>
                    Zip:<input type="text" name="zip"><br>
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
