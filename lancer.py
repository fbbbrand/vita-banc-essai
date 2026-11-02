import http.server, socketserver, webbrowser, os, threading
os.chdir(os.path.dirname(os.path.abspath(__file__)))
PORT = 8080
threading.Timer(0.8, lambda: webbrowser.open(f"http://localhost:{PORT}/")).start()
with socketserver.TCPServer(("127.0.0.1", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
    print(f"Banc d'essai VITA sur http://localhost:{PORT}/  (Ctrl+C pour arrêter)")
    httpd.serve_forever()
