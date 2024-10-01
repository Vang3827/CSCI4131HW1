from http.server import BaseHTTPRequestHandler, HTTPServer
import re

listings = [
    {"vehicle 1":"Dodge Challenger","url":"static/html/listing1.html","description":"Longer text for descrption", "category":"coupe", "numeric ID": 1, "Date": "08/20/2024",
     "bids":[
         {"bidder 1":"Carl k", "bid amount":"4,500", "comment":"I would love this car."},{"bidder 2":"Sam Samson", "bid amount":"5,500", "comment":"I just want to use money."}
         ]
    },
    {"vehicle 2":"Ford Mustang","url":"static/html/listing2.html","description":"Longer text for descrption", "category":"coupe", "numeric ID": 2, "Date": "09/15/2024",
     "bids":[
         {"bidder 1":"Luke Lukenson", "bid amount":"2,500", "comment":"Dailer driver right here."},{"bidder 2":"Peter Porker", "bid amount":"6,500", "comment":""}
         ]},
    {"vehicle 3":"Toyota Tundra","url":"https://images.unsplash.com/photo-1621993202323-f438eec934ff?q=80&w=1964&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D","description":"Longer text for descrption", "category":"truck", "numeric ID": 3, "Date": "09/10/2024",
     "bids":[
         {"bidder 1":"Adam Apple", "bid amount":"6,500", "comment":"Work truck."},{"bidder 2":"Ben Benji", "bid amount":"6,500", "comment":"New truck for me."},{"bidder 3":"Cedar Cider", "bid amount":"9,500", "comment":"The Cedar Mobile."}
         ]},
    {"vehicle 4":"Subaru Forester","url":"https://images.unsplash.com/photo-1710171940308-8f9670ecfeda?q=80&w=2071&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D","description":"Longer text for descrption", "category":"suv", "numeric ID": 4, "Date": "09/10/2024",
     "bids":[
         {"bidder 1":"Mike Micheal", "bid amount":"3,500", "comment":""},{"bidder 2":"Justin Time", "bid amount":"4,500", "comment":"Family vehicle."}
         ]}
]

# PUT YOUR GLOBAL VARIABLES AND HELPER FUNCTIONS HERE.
# path = ""
# listing_id =""



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

    return {urlDict}


def render_listing(listing):
    print("in render listing")
    listing_id = int(path[9:])
    print(listing_id)
    newPath = ""

    # if path[9:] != int:
    # return "static/html/404.html"
    
    for dicts in listing:
        if dicts.get("numeric ID") == listing_id:
            newPath = (dicts["url"])
            return newPath
    
    # return (f"{newPath}")
    # return "/static/html/listing.html"
    # return "static\html\listing_example.html"
    
    
    

    


def render_gallery(query, category):
    pass


# Provided function -- converts numbers like 42 or 7.347 to "$42.00" or "$7.35"
def typeset_dollars(number):
    return f"${number:.2f}"


def server(url):
    """
    url is a *PARTIAL* URL. If the browser requests `http://localhost:4131/contact?name=joe#test`
    then the `url` parameter will have the value "/contact?name=joe". So you can expect the PATH
    and any PARAMETERS from the url, but nothing else.

    This function is called each time another program/computer makes a request to this website.
    The URL represents the requested file.

    This function should return two strings in a list or tuple. The first is the content to return
    The second is the content-type.
    """
    # YOUR CODE GOES HERE!
    global path
    path = url.split("?")[0]
    global listing_id
    # print(path)

    if path in "/" or path in "/main":
        return open("static/html/mainpage.html").read(), "text/html"
    elif "/gallery" in path:
        return open("static/html/listings.html").read(), "text/html"
    elif "/listing" in path:
        newPath = render_listing(listings)
        return open(newPath).read(), "text/html"
        # return open(render_listing(listings)).read(), "text/html"
        # print(render_listing(listings))
    else:
        return open("static/html/404.html").read(), "text/html"

# You shouldn't need to change content below this. It would be best if you just left it alone.


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Call the student-edited server code.
        message, content_type = server(self.path)

        # Convert the return value into a byte string for network transmission
        if type(message) == str:
            message = bytes(message, "utf8")

        # prepare the response object with minimal viable headers.
        self.protocol_version = "HTTP/1.1"
        # Send response code
        self.send_response(200)
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

# render_listing(listings)
