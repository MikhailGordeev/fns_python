import uuid
from qrscanner import get_qr_data
from furl import furl


# Random device ID
random_uuid = str(uuid.uuid4()).replace('-', '')
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

f = furl('/?{}'.format(get_qr_data('qr.png')))
fn = f.args['fn']
fd = f.args['i']
fs = f.args['fp']

