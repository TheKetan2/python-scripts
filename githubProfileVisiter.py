# install requests with "pip install requests"
import requests
import time
# your profile badge url
url = "https://camo.githubusercontent.com/59ad8f917b0bca65844d04a632ec72a2c89ff391d37cf6a913411ba8c2f1da4f/68747470733a2f2f76697369746f722d62616467652e6c616f62692e6963752f62616467653f706167655f69643d7468656b6574616e32"

while True:
    time.sleep(1)
    print("visiting page...")
    requests.get(url)
    
