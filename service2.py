import requests
//replace the url in below statement with the url that you get 
// after running the service1.py
response=requests.get("http://0.0.0.0:5000") 
print (response.text)
