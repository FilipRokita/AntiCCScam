from randomdata import *



#CHANGE URL
url = 'https://www.example.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}

#CHANGE DATA
data = {
    'cc': randomcc(),
    'exp': randomexp(),
    'cvv': randomcvv(),
    'cardholder': 'John Smith',
}