import requests

def main():
    r = requests.get('http://127.0.0.1:5000/api/students')
    print(r.json())

    r = requests.get('http://127.0.0.1:5000/api/students/1')
    print(r.json())



main()
