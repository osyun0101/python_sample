import flask
from flask import request
import json
import my_text

app = flask.Flask(__name__)
port_num = 8888

@app.route('/', methods=['GET'])
def index():
    with open('index.html', 'rb') as fp:
        return fp.read()
    
@app.route('/api', methods=['GET'])
def api():
    q = request.args.get('q', '')
    if q == '':
        return "{'LANELS': '空です', 'per': 0}"
    print('q=', q)
    data = my_text.check_tf(q)
    label, per, n = data
    return json.dumps({'LABELS': label, 'predict': per, 'no': n})
    
    
if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=port_num)