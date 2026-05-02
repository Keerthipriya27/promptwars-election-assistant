import requests
try:
    res = requests.post('http://127.0.0.1:5000/chat', json={'message': 'how to vote'})
    print(res.json())
except Exception as e:
    print(e)
