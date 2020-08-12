import requests
import json

ip_address = "13.126.204.3"
port = "5000"
data = ['All #GOP candidates want to reduce taxes while #Huckabee wants to legalize prostitution and drugs so we can tax it. #GOPDebate']


url = 'http://{0}:{1}/predict/'.format(ip_address, port)

json_data = json.dumps(data)
header = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
response = requests.post(url, data=json_data, headers = header)
print(response, response.text)