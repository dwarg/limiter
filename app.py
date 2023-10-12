from flask import Flask, request
from flask_limiter import Limiter
import yaml
import os

app = Flask(__name__)
limiter = Limiter(app, default_limits=["5 per minute"], headers_enabled=True)
ip_addresses = []

@app.route('/', methods=['GET'])
@limiter.limit("2 per minute") # Set a rate limit of 2 requests per minute
def get_ip_address():
    ip = request.remote_addr
    ip_addresses.append(ip)

    accept_header = request.headers.get('Accept', 'text/plain')
    if 'text/html' in accept_header:
        return f"<h1>Your IP address is {ip}</h1>"
    elif 'application/xml' in accept_header:
        return f"<ip><address>{ip}</address></ip>",  {'Content-Type': 'application/xml'}
    elif 'application/yaml' in accept_header:
        return yaml.dump({'ip': {'address': ip}}), {'Content-Type': 'application/yaml'}
    else:
        return f"Your IP address is {ip}", {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))