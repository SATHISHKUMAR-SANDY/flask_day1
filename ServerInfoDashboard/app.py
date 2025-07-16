from flask import Flask,request
import socket
import os 
import platform

app = Flask(__name__)


@app.route('/')
def system_info():

    host_name =socket.gethostname()
    local_ip = socket.gethostbyname(host_name)

    port =request.host.split(":")[1]if ":" in  request.host else "default"

    flask_env = os.environ.get('FLASK_ENV','NOT SET')

    os_info = platform.system()+""+platform.release()

    return f"""
<h1>System Information</h1>
    <ul>
        <li><b>Local IP Address:</b> {local_ip}</li>
        <li><b>Port:</b> {port}</li>
        <li><b>Environment:</b> {flask_env}</li>
        <li><b>OS:</b> {os_info}</li>
        <li><a href='/status' >See Debuf status Click here</a></li>
    </ul>



"""

@app.route('/status')
def status():
    if app.debug:
        return "<h1>Debug Mode is ON"
    else:
        return "<h1>Debug mode is off</h1>"

if __name__ =='__main__':
    app.run(debug=True,port=8000)