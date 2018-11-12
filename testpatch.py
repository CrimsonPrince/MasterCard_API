import requests

def main():
    r = requests.put('http://127.0.0.1:5000/api/students/1', data = {

    "student_id": "1",
    "name": "Ryan Fields",
    "year": "2",
    "course": "DT18"
    })
    print(r.json())

    r = requests.get('http://127.0.0.1:5000/api/students/1')
    print(r.json())




main()
