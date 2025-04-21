#Importing libraries
import time #Not used currently, used for old ngrok start process
import webbrowser #For automatically opening the ngrok URL in the default web browser on script run
from flask import Flask
from flask import render_template
import csv #For reading 'airports.csv'

#Importing libaries so ngrok can work on MacOS for development
import os
import certifi
os.environ['SSL_CERT_FILE'] = certifi.where()

from pyngrok import ngrok

import subprocess
import requests

#Endof importing libraries

#Defining Constants
AUTH_TOKEN = "2n9HhWvL2Bba7GmJ3amVYZjDkED_2dMRdEGFY1oWnf3ZemkiC"
DEV_PAGE_AUTO_OPEN = True #Set if you want page to auto open when program is ran
 
#Endof defining Constants


# Setting of Authtoken for ngrok
ngrok.set_auth_token(AUTH_TOKEN)

# Function to start ngrok
def start_ngrok():
    # Use pyngrok to create a tunnel to port 5000 with TLS (HTTPS) enabled
    tunnel = ngrok.connect(5001, bind_tls=True)
    public_url = tunnel.public_url

    # Print the ngrok tunnel URL to the console
    print(" * ngrok tunnel URL:", public_url)

    # Return the public URL for use elsewhere in the script
    return public_url




app = Flask(__name__)

@app.route('/')
def index():
    # Temporary simple route to test the Flask app
    return render_template('index.html')



if __name__ == "__main__":
    # Calls start_ngrok() to start the ngrok tunnel and get the public URL
    public_url = start_ngrok()
    # Prints the public URL to the console
    print(" * App at:", public_url)
    if DEV_PAGE_AUTO_OPEN:
        #Open the public URL in the default web browser
        webbrowser.open(public_url)
    # Bind on 0.0.0.0 so ngrok can forward traffic directly
    app.run(host="0.0.0.0",port=5001, debug=True, use_reloader=False)


'''
    Old code for ngrok process

    # Start the ngrok process with subprocess, specifying that ngrok should tunnel HTTP traffic to port 5000
    ngrok_process = subprocess.Popen(['ngrok', 'http', '5000'])
    # Delay the script for 4 seconds to allow ngrok time to initialize and start the tunnel
    time.sleep(4)
    # Fetch the ngrok tunnel information using an HTTP GET request to ngrok's local API
    response = requests.get('http://localhost:4040/api/tunnels')
    # Parse the JSON response to get the details of the tunnel
    tunnel_info = response.json()
    # Extract the public URL where the ngrok tunnel is accessible
    public_url = tunnel_info['tunnels'][0]['public_url']
    '''