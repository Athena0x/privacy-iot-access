import requests

def request_access(user, resource):
    response = requests.post("http://localhost:5000/auth", json={"user": user, "resource": resource})
    return response.json()

if __name__ == "__main__":
    print(request_access("device_1", "sensor_data"))
