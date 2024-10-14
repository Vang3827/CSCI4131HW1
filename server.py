from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib

# PUT YOUR GLOBAL VARIABLES AND HELPER FUNCTIONS HERE.
listings = [
    {"vehicle":"Dodge Challenger","url":"static/html/listing1.html","description":"Longer text for descrption", "category":"small", "numeric ID": 1, "Date": "08/20/2024",
     "bids":[
         {"bidder 1":"Carl k", "bid amount":"4,500", "comment":"I would love this car."},{"bidder 2":"Sam Samson", "bid amount":"5,500", "comment":"I just want to use money."}
         ]
    },
    {"vehicle":"Ford Mustang","url":"static/html/listing2.html","description":"Longer text for descrption", "category":"small", "numeric ID": 2, "Date": "09/15/2024",
     "bids":[
         {"bidder 1":"Luke Lukenson", "bid amount":"2,500", "comment":"Dailer driver right here."},{"bidder 2":"Peter Porker", "bid amount":"6,500", "comment":""}
         ]},
    {"vehicle":"Toyota Tundra","url":"static/html/listing3.html","description":"Longer text for descrption", "category":"truck", "numeric ID": 3, "Date": "09/10/2024",
     "bids":[
         {"bidder 1":"Adam Apple", "bid amount":"6,500", "comment":"Work truck."},{"bidder 2":"Ben Benji", "bid amount":"6,500", "comment":"New truck for me."},{"bidder 3":"Cedar Cider", "bid amount":"9,500", "comment":"The Cedar Mobile."}
         ]},
    {"vehicle":"Toyota RAV4","url":"static/html/listing4.html","description":"Longer text for descrption", "category":"suv", "numeric ID": 4, "Date": "09/10/2024",
     "bids":[
         {"bidder 1":"Mike Micheal", "bid amount":"3,500", "comment":""},{"bidder 2":"Justin Time", "bid amount":"4,500", "comment":"Family vehicle."}
         ]}
]

def checkListDict (query,category):
    print("in ChecklistDict")
    
    vehicleList=[]

    for i in range(len(listings)):
        if(query.lower() in listings[i].get("vehicle").lower()):
            vehicleList.append(listings[i])
    print(vehicleList)
    return vehicleList

def escape_html(str):
    str = str.replace("&", "&amp;")
    str = str.replace('"', "&quot;")

    # you need more.

    return str


def unescape_url(url_str):
    import urllib.parse

    # NOTE -- this is the only place urllib is allowed on this assignment.
    return urllib.parse.unquote_plus(url_str)

def parse_query_parameters(response):
    newStrList=[]

    # Split the query string into key-value pairs
    # key, *val =response.split("&")
    keyValPairs = response.split("&")
    # Initialize a dictionary to store parsed parameters
    urlDict = dict()
    # Iterate over each key-value pair
    # Split the pair by '=' to separate key and value
    for i in keyValPairs:
        newKV = i.split("=")
        
        for j in range(len(newKV)-1):
            newKV[j] = newKV[j].replace("?","")
            newKV[j] = newKV[j].replace("%","#")
            newKV[j] = newKV[j].replace("+"," ")
            newKV[j+1] = newKV[j+1].replace("?","")
            newKV[j+1] = newKV[j+1].replace("%","#")
            newKV[j+1] = newKV[j+1].replace("+"," ")
            newStrList.append((newKV[j], newKV[j+1]))
        
    urlDict=dict(newStrList)
    print(urlDict)
    return urlDict

def render_listing(listing):
    # print("in render listing")
    listing_id = path[9:]
    # print(listing_id)
    newPath = ""
    
    try:
        for dicts in listing:
            if dicts.get("numeric ID") == int(listing_id):
                newPath = (dicts["url"])
                return newPath
    except ValueError:
        return "static/html/404.html","text/html",404
    
    return "static/html/404.html","text/html",404

def render_gallery(query, category):
    print(type(query),query,type(category),category)
    
    galleryList = checkListDict(query,category)
    # name = gallList.get("vehicle")

    listingname = []
    numOfBids = []
    cat = []
    date = []

    for i in range(len(galleryList)):
        listingname.append(galleryList[i].get("vehicle"))
        cat.append(galleryList[i].get("category"))
        numOfBids.append(galleryList[i].get("bids"))
        date.append(galleryList[i].get("Date"))




    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="/main.css">
        <title>Auto Auction</title>
    </head>
    <body>
        <form action="gallery" method="get" class="topnav">
            <a href="/">About</a>
            <a href="/gallery">Gallery</a>
            <input name ="query" type="search" placeholder="Search..">
            <select name="category" id="cars">
                <option>None</option>
                <option value="coupe">Coupe</option>
                <option value="truck">Truck</option>
                <option value="suv">SUV</option>
            </select>
            <input type="submit" value="Submit">
        </form>
        <h1>Query:{query} and Catagory:{category} </h1>
        <p>{listingname}</p>
        <table>
            <table border="1">
        <tr>
            <th>Listing</th>
            <th>Number of Bids</th>
            <th>Top Bid</th>
            <th>Auction Ends</th>
        </tr>
        <tr>
            <td><a href = "/listing/1">{listingname}</a></td>
            <td>{numOfBids}</td>
            <td>{cat}</td>
            <td>{date}</tb>
        </tr>
    </table>
        </table>
    </body>
    </html>
    ""","text/html",200

def server_GET(url: str) -> tuple[str | bytes, str, int]:
    """
    url is a *PARTIAL* URL. If the browser requests `http://localhost:4131/contact?name=joe`
    then the `url` parameter will have the value "/contact?name=joe". (so the schema and
    authority will not be included, but the full path, any query, and any anchor will be included)

    This function is called each time another program/computer makes a request to this website.
    The URL represents the requested file.

    This function should return three values (string or bytes, string, int) in a list or tuple. The first is the content to return
    The second is the content-type. The third is the HTTP Status Code for the response
    """
    # YOUR CODE GOES HERE!
    global path
    path = url.split("?")[0]
    
    print(path)

    if path in "/" or path in "/main":
        return open("static/html/mainpage.html").read(), "text/html",200
    elif "/gallery" in path:
        if "?" in url:
            print(url)
            query = url.split("?")[1]
            print(query)
            return render_gallery(parse_query_parameters(query).get("query"),parse_query_parameters(query).get("category"))
        else:
            return open("static/html/listings.html").read(), "text/html",200
    elif "/listing" in path:
        newPath = render_listing(listings)
        return open(newPath).read(), "text/html",200
    elif "/main.css":
        return open("static/css/main.css").read(), "text/css",200
    else:
        return open("static/html/404.html").read(), "text/html",404
    pass


def server_POST(url: str, body: str) -> tuple[str | bytes, str, int]:
    """
    url is a *PARTIAL* URL. If the browser requests `http://localhost:4131/contact?name=joe`
    then the `url` parameter will have the value "/contact?name=joe". (so the schema and
    authority will not be included, but the full path, any query, and any anchor will be included)

    This function is called each time another program/computer makes a POST request to this website.

    This function should return three values (string or bytes, string, int) in a list or tuple. The first is the content to return
    The second is the content-type. The third is the HTTP Status Code for the response
    """
    return url,"",201

    pass


# You shouldn't need to change content below this. It would be best if you just left it alone.


class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Read the content-length header sent by the BROWSER
        content_length = int(self.headers.get("Content-Length", 0))
        # read the data being uploaded by the BROWSER
        body = self.rfile.read(content_length)
        # we're making some assumptions here -- but decode to a string.
        body = str(body, encoding="utf-8")

        message, content_type, response_code = server_POST(self.path, body)

        # Convert the return value into a byte string for network transmission
        if type(message) == str:
            message = bytes(message, "utf8")

        # prepare the response object with minimal viable headers.
        self.protocol_version = "HTTP/1.1"
        # Send response code
        self.send_response(response_code)
        # Send headers
        # Note -- this would be binary length, not string length
        self.send_header("Content-Length", len(message))
        self.send_header("Content-Type", content_type)
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()

        # Send the file.
        self.wfile.write(message)
        return

    def do_GET(self):
        # Call the student-edited server code.
        message, content_type, response_code = server_GET(self.path)

        # Convert the return value into a byte string for network transmission
        if type(message) == str:
            message = bytes(message, "utf8")

        # prepare the response object with minimal viable headers.
        self.protocol_version = "HTTP/1.1"
        # Send response code
        self.send_response(response_code)
        # Send headers
        # Note -- this would be binary length, not string length
        self.send_header("Content-Length", len(message))
        self.send_header("Content-Type", content_type)
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()

        # Send the file.
        self.wfile.write(message)
        return


def run():
    PORT = 4131
    print(f"Starting server http://localhost:{PORT}/")
    server = ("", PORT)
    httpd = HTTPServer(server, RequestHandler)
    httpd.serve_forever()


run()
