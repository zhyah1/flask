from flask import Flask, send_file ,render_template
import subprocess
app = Flask(__name__)

@app.route('/')
def index():

    return send_file('index1.html')
@app.route('/work_p')
def work():

    output = subprocess.check_output(['python', 'test.py'], text=True)

    return send_file('index1.html')

if __name__ == '__main__':
    app.run(debug=True)

