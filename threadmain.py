from flask import Flask, send_file
import threading

app1 = Flask(__name__)
app2 = Flask(__name__)

# Define routes for app1
@app1.route('/')
def index_app1():
    return send_file('index1.html')

# Define routes for app2
@app2.route('/')
def index_app2():
    return send_file('index2.html')

def run_app1():
    app1.run(host='0.0.0.0', port=5001)

def run_app2():
    app2.run(host='0.0.0.0', port=5002)

if __name__ == "__main__":
    thread1 = threading.Thread(target=run_app1)
    thread2 = threading.Thread(target=run_app2)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
