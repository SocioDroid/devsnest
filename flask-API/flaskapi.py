import flask
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

serverData = []
@app.route('/', methods=['GET'])
def home():
    return '''
    <h1>Devsnest FLASK API</h1>
    <ul>
    <li>Add a string here: /add/string<br></li>
    <li>Concat all the submitted strings: <url>/concat</li>
    <ul>
    '''

@app.route('/add', methods=['POST'])
@app.route('/add/<string:ip_str>', methods=['GET', 'POST'])
def addStringUsingGet(ip_str=None):
    if request.method == "GET":
        serverData.append(ip_str)
        return 'The string {} has been saved in the server!'.format(serverData[-1])    
    elif request.method == "POST":
        req_data = request.get_json(force=True)
        serverData.append(req_data['string'])
        return 'The string {} has been saved in the server!'.format(serverData[-1])    


@app.route('/concat', methods=['GET'])
def concatString():
    return ' '.join(serverData)
app.run()