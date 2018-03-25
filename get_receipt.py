import uuid
from qrscanner import get_qr_data
from furl import furl
import requests
import re
import datetime
from auth import phone, pin

#
# Place .netrc in home directory with format "machine proverkacheka.nalog.ru login {you phone number} password {pin from sms}"
#
# Place your receipt photo with QR code in project root directory
# Receipt QR code
qr_file = 'qr.png'

# Random device ID
dev_id = str(uuid.uuid4()).replace('-', '')
# DeviceID
dev_os = 'Adnroid 4.4.4'
# Protocol version
proto = '2'
# Client version
client = '1.4.1.3'
# User agent
uagent = 'okhttp/3.0.1'
# Base URL
base = 'https://proverkacheka.nalog.ru:9999'

f = furl('/?{}'.format(get_qr_data(qr_file)[0].decode("utf-8")))

# Fiscal storage (Номер фискального накопителя - ФН)
fn = f.args['fn']
# Fiscal document number (Номер фискального документа - ФД)
fd = f.args['i']
# Fiscal sign (Подпись фискального документа - ФП)
fp = f.args['fp']

headers = {
    'Device-Id': dev_id,
    'Device-OS': dev_os,
    'Version': proto,
    'ClientVersion': client,
    'User-Agent': uagent
}

data_request = [
  ('fiscalSign', fp),
  ('sendToEmail', 'no'),
]

request_receipt = "%s/v1/inns/*/kkts/*/fss/%s/tickets/%s" % (base, fn, fd)

response = requests.get(request_receipt, headers=headers, params=data_request, auth=(phone, pin)).json()


n = 0
total_sum = response['document']['receipt']['totalSum'] * 0.01

try:
    user = response['document']['receipt']['user']
    print(user)
except KeyError:
    # Key is not present
    pass
try:
    retail_place_address = response['document']['receipt']['retailPlaceAddress']
    print(retail_place_address)
except KeyError:
    # Key is not present
    pass
try:
    user_inn = response['document']['receipt']['userInn']
    print('ИНН {}\n'.format(user_inn))

except KeyError:
    # Key is not present
    pass
print(datetime.datetime(*map(int, re.split('[^\d]', response['document']['receipt']['dateTime']))).strftime('%d.%m.%Y %H:%M'))
print('Чек № {}'.format(response['document']['receipt']['requestNumber']))
try:
    shift_number = response['document']['receipt']['shiftNumber']
    print('Смена № {}'.format(shift_number))
except KeyError:
    # Key is not present
    pass
print('Кассир {}'.format(response['document']['receipt']['operator']))
print('Приход')
print('-------------------------------------------------------------------')
print('№  Название                              Цена    Кол.    Сумма')
for i in response['document']['receipt']['items']:
    n += 1
    price = i['price'] * 0.01
    sum = i['sum'] * 0.01
    print('{}  {}   {:,.2f}       {}      {:,.2f}'.format(n, i['name'], price, i['quantity'], sum))
print('-------------------------------------------------------------------')
print('Итого: {:,.2f}'.format(total_sum))