import requests
import socket
import json

#check if ip address is valid
def valid_ip(address: str) -> bool:
    try:
        socket.inet_aton(address)
        return True
    except:
        return False

#get ip address location -> (latitude, longitude)
def ip_location(address: str) -> tuple:
    URL = "http://ip-api.com/json/" + address

    res = requests.get(URL)
    data = json.loads(res.content)

    if data["status"] == "success":
        return data["lat"], data["lon"]
    else:
        return "Reserved or N/F"

def main():
    #input ip with validation
    while True:
        IP = input("Enter IP address: ")
        if valid_ip(IP):
            break
    
    print(ip_location(IP))

if __name__ == "__main__":
    main()


