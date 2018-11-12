import requests

"""Module to test posting data to the API, Inserts random student data which is then retrieved with a get request"""

def main():
    payload = {"student_id":"6","name":"Declan Costello","year":"4","course":"DT88"}
    r = requests.post('http://127.0.0.1:5000/api/students', data = payload)
    print(r.json())

    r = requests.get('http://127.0.0.1:5000/api/students')
    print(r.json())




main()
