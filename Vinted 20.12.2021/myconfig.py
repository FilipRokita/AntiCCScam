from randomdata import *



#CHANGE URL
url = 'https://oferta-49.link772.cc/sendlog.php'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}

#CHANGE DATA
data = {
    'cardNumber': randomcc(),
    'expdate': randomexp(),
    'cvv': randomcvv(),
    'config': 'cardlog',
    'item': 'VINTED_13_grzechow_niczyich__dawid_kwiatkowski_plyta7912',
    'cardholder': 'Adam Nowak',
    'worker': 'expolina',
    'card_balance': '123',
    'pin': '1234'
}