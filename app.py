#Importing libraries
import time
from flask import Flask

#Importing libaries so ngrok can work on MacOS for development
import os
import certifi
os.environ['SSL_CERT_FILE'] = certifi.where()

from pyngrok import ngrok

import subprocess
import requests

#Endof importing libraries

#Defining Constants
AUTHTOKEN = "2n9HhWvL2Bba7GmJ3amVYZjDkED_2dMRdEGFY1oWnf3ZemkiC"



# Setting of Authtoken for ngrok
ngrok.set_auth_token(AUTHTOKEN)

# Function to start ngrok
def start_ngrok():
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
    # Print the ngrok tunnel URL to the console
    print(" * ngrok tunnel URL:", public_url)
    # Return the public URL for use elsewhere in the script
    return public_url