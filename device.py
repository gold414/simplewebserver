from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
        <title>Device <Table></Table></title>
    </head>

    <body>
       <center><h1 >Product Specification(25017581)</h1>
       <table border="1" cellpadding="10" cellspacing="2">
            <tr bgcolor="lightcoral">
                <th>S.No.</th>
                <th>Device name</th>
                <th>Storage</th>
                <th>Ram</th>
                <th>Processor</th>
            </tr>
            <tr bgcolor="lightblue">
                <td>1</td>
                <td>Acer</td>
                <td>1 TB</td>
                <td>16 GB</td>
                <td>intel i5</td>
            </tr>
            <tr bgcolor="lightblue">
                <td>2</td>
                <td>Lenovo</td>
                <td>2 TB</td>
                <td>8 GB</td>
                <td>intel i3</td>
            </tr>
            <tr bgcolor="lightblue">
                <td>3</td>
                <td>Hp</td>
                <td>1 TB</td>
                <td>16 GB</td>
                <td>amd 5</td>
            </tr>
            <tr bgcolor="lightblue">
                <td>4</td>
                <td>Asus</td>
                <td>2 TB</td>
                <td>32 GB</td>
                <td>intel i9</td>
            </tr>
            <tr bgcolor="lightblue">
                <td>5</td>
                <td>Apple</td>
                <td>1 TB</td>
                <td>16 GB</td>
                <td>intel i5</td>
        </table></center>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()