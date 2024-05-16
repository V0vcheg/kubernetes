from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import os

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        
        api_key = os.getenv("API_KEY", "no-api-key")
        message = f"Hello from Order-Service using API key: {api_key}"
        self.wfile.write(message.encode('utf-8'))
        
        logging.info(f"Received request using API key: {api_key}")

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=3001):
    log_file_path = '/var/log/user.log'
    logging.basicConfig(level=logging.INFO, filename=log_file_path, 
                        format='%(asctime)s - %(message)s', 
                        datefmt='%Y-%m-%d %H:%M:%S')

    logging.info(f'Starting httpd server on port {port}')
    
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == '__main__':
    run()
