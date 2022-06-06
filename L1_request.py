import requests

def main():
    # response = requests.get("http://www.google.com")
    response = requests.get("https://www.djangoproject.com/start/")
    print("Status code: ",response.status_code)
    print("Status code: ",response.headers['Referrer-Policy'])
    print("Status code: ",response.text)

def connect2api():
    pa={'access_key':'vwi7jgmwf2p7ew9st6jj69vtczlrgysqc8er13ef66i48s2f5znmw8a6gq33'}
    response = requests.get("https://metals-api.com/api/latest",params=pa)
    print(f'\ncurrent gold rate is {response.json()["rates"]["XAU"]} {response.json()["base"]} {response.json()["unit"]}')






if __name__=='__main__':
    # main()
    connect2api()
