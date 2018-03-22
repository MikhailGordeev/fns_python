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

print(random_uuid)
qrscan = get_qr_data('qr.png')



# Fiscal storage (Номер фискального накопителя - ФН)
FN = "8710000100955536"
# Fiscal document number (Номер фискального документа - ФД)
FD = "151034"
# Fiscal sign (Подпись фискального документа - ФП)
FS = "196397073"
