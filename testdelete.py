import requests

def main():
    r = requests.delete('http://127.0.0.1:5000/api/students/7')
    print(r.json())

    r = requests.get('http://127.0.0.1:5000/api/students/7')
    print(r.json())



main()
