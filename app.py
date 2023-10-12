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
    
@app.route('/list', methods=['GET'])
def list_ip_addresses():
    return {'ip_addresses': ip_addresses}, {'Content-Type': 'application/json'}

@app.errorhandler(404)
def not_found_error(error):
    return '404 Error: Page not found', 404

@app.errorhandler(500)
def internal_error(error):
    return '500 Error: Internal server error', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))