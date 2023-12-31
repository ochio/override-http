import json
import subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer

import browsers
from browsers.osx import OSX_BROWSER_BUNDLE_LIST

default_browser_bundle_id = subprocess.getoutput(cmd="sh getDefaultBrowser.sh")


class CustomHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.send_header("Access-Control-Allow-Credentials", "true")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With, Content-type")

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write("hello".encode())

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        data = json.loads(self.rfile.read(int(self.headers["content-length"])).decode("utf-8"))
        print(data)
        html_context = "完了"
        self.wfile.write(html_context.encode())

        open_with_default_browser(
            default_browser_bundle_id=default_browser_bundle_id,
            url=data["destination"],
        )


def open_with_default_browser(default_browser_bundle_id, url):
    for browser, bundle_id, version_string in OSX_BROWSER_BUNDLE_LIST:
        if default_browser_bundle_id.lower() == bundle_id.lower():
            browsers.launch(browser, url=url)


def main():
    server_address = ("localhost", 8080)
    httpd = HTTPServer(server_address, CustomHTTPRequestHandler)
    httpd.serve_forever()


if __name__ == "__main__":
    main()
