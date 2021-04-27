from flask import Flask
from flask import request, render_template
import json
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/track', methods=['POST', 'GET'])
def track():
    print(json.loads(request.data))
    return 'TRACKING...'

if __name__ == '__main__':
    app.run()
