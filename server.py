from flask import Flask, request
import socket
import json
import requests

app = Flask(__name__)

DRONES = []

@app.route('/')
def hello_world():
    return 'drone scenario drone manager'

@app.route('/api/ip')
def get_ip():
    h_name = socket.gethostname()
    IP_addres = socket.gethostbyname(h_name)
    return json.dumps({
        "host_name": h_name,
        "ip": IP_addres
    })

@app.route('/api/drone/list', methods=['GET'])
def get_device_list():
    return json.dumps(DRONES)

@app.route('/api/drone/add', methods=['POST', 'PUT'])
def add_drone():
    target_url = request.get_json()
    DRONES.append(target_url['url'])
    add_drone(target_url['url'])
    return "ok"


@app.route('/api/drone/remove', methods=['POST', 'PUT'])
def remove_drone():
    target_url = request.get_json()
    remove_drone(DRONES[target_url])
    DRONES.remove(target_url['url'])
    return "ok"

def add_drone(id):
    pass

def remove_drone(id):
    pass

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)