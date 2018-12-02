from geoloc import addressToDistance

privacyOrders = [] #for users who desire privacy
generalOrders = [] #for users who do not need privacy

#slits the user information string, allowing for manipulation of user input info
def userParse(user):
    return user.split('-')

#returns the day for the user's order
def dateParse(date):
    dateInfo = date.split(':')
    return dateInfo[2]

#adds the user info string to the appropriate order list
def addToOrderList(userInfo):
    privacy = userInfo[2]

    if (privacy == '0'):
        privacyOrders.append(userInfo)
        privacyOrders.sort()
    else:
        generalOrders.append(userInfo)
        generalOrders.sort()

#extracts the order
def order(orderList, today):
    for order in orderList:
        date = order[0]
        day = dateParse(date)

        privacy = order[2]


        #'order' all of today's orders
        if (day == today):
            print('ordering day ' + today +
                  ': \n\t' + ', '.join(orderList.pop(0)))
            print("\n\n")

def lumpedOrders(orderList, today):
    lumpedOrderList = []

    listLength = len(orderList)
    for i in range(0, listLength - 1):
        if (orderList[i][4] == orderList[i+1][4] or
            orderList[i][4] == orderList[i-1][4]):
            lumpedOrderList.append(orderList[i])
        if (i == listLength - 2):
            if (orderList[i+1][4] == orderList[0][4]):
                lumpedOrderList.append(orderList[i+1])

    return lumpedOrderList



'''
user1 = '2018:11:20-1.23-0-product1-123 Test Street, City, CA'
user2 = '2018:11:22-3.534-0-product2-456 Test Street, City, CA'
user3 = '2018:11:24-0.2342-0-product1-789 Test Street, City, CA'
user4 = '2018:11:2-10.234212-0-product1-654 Test Street, City, CA'
user5 = '2018:11:2-10.234212-1-product2-654 Test Street, City, CA'
user6 = '2018:11:2-10.234212-1-product3-654 Test Street, City, CA'

userList = [user1, user2, user3, user4, user5, user6]

for user in userList:
    userInfo = userParse(user)
    addToOrderList(userInfo)


#print(privacyOrders)
#print(generalOrders)

lumpedOrderList = lumpedOrders(generalOrders, '2')
addressList = []
for order in lumpedOrderList:
    addressList.append(order[4])

for order in generalOrders:
    date = order[0]
    day = dateParse(date)

    if (day == '2'):
        addressList.append(order[4])

print (list(set(addressList)))
'''
