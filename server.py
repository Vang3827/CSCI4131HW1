from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib  # Only for parse.unquote and parse.unquote_plus.
import json
import base64
from typing import Union, Optional
import re
import datetime
import time
# If you need to add anything above here you should check with course staff first.

# Provided helper function. This function can help you implement rate limiting
rate_limit_store = []

# My global variables here 
numericID = 0
bidnumericID = 0
listingBool = False
bidBool = False
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
newListing =[]
bids =[{"id": 0, "name": "", "amount": "0"}]
message_list = [
    {"id": 1, "author": "system", "message": "test message one"},
    {"id": 2, "author": "system", "message": "test message two"},
]

# My helper functions
# def postFunc(body):
#     # TODO: Need to Max current numeric ID and add 1
#     global numericID
#     newParams = parse_query_parameters(body)
#     add_new_listing(newParams)
    
#     if listingBool == True:
#         numericID += 1
#         newParams["numeric ID"] = numericID
#         newListing.append(newParams)
#         print(newListing)
#         return open("static/html/create_success.html").read(),200,{"Content-Type": "text/html"}
#     else:
#         print("In false postFunch listingBool is--->",listingBool)
#         return open("static/html/create_fail.html").read(),404,{"Content-Type": "text/html"}

# def postBidFunc(body):
#     # TODO: Need to Max current numeric ID and add 1
#     global bidnumericID
#     newParams = parse_query_parameters(body)
#     add_new_bid(newParams)
    
#     if bidBool == True:
#         bids.append(newParams)
#         print(bids)
#         return open("static/html/create_success.html").read(),200,{"Content-Type": "text/html"}
#     else:
#         print("In false postFunch listingBool is--->",bidBool)
#         return open("static/html/create_fail.html").read(),404,{"Content-Type": "text/html"}
        
def postAPI(body,contentType):
    print("In postAPI func")
    print(body,contentType)

    if len(body) == 0:
        return 400
    else:
        newBody = json.loads(body)
        print(newBody)
    

def add_new_listing(params):
    global listingBool
    print("In add_new_listing(params)")
    print((params.values() == ""))
        
    if "" in params.values():
        listingBool = False
        print("in false listingBool = ",listingBool)
        print(params)
        return listingBool
    else:
        listingBool = True
        print("In true so listingBool = ",listingBool)
        print(params)
        return listingBool

def add_new_bid(params):
    global bidBool
    print("In add_new_listing(params)")
    print((params.values() == ""))
        
    if "" in params.values():
        bidBool = False
        print("in false listingBool = ",bidBool)
        print(params)
        return bidBool
    else:
        bidBool = True
        print("In true so listingBool = ",bidBool)
        print(params)
        return bidBool

def checkListDict (query,category):
    print("in ChecklistDict")
    
    vehicleList=[]

    for i in range(len(listings)):
        if(query.lower() in listings[i].get("vehicle").lower()):
            vehicleList.append(listings[i])
    print(vehicleList)
    return vehicleList
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
        return "static/html/404.html",404,{"Content-Type": "text/html"}
    
    return "static/html/404.html",404,{"Content-Type": "text/html"}

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
    """,200,{"Content-Type": "text/html"}


def pass_api_rate_limit() -> tuple[bool, int | None]:
    """This function will keep track of rate limiting for you.
    Call it once per request, it will return how much delay would be needed.
    If it returns 0 then process the request as normal
    Otherwise if it returns a positive value, that's the number of seconds
    that need to pass before the next request"""
    from datetime import datetime, timedelta

    global rate_limit_store
    # you may find it useful to change these for testing, such as 1 request for 3 seconds.s
    RATE_LIMIT = 4  # requests per second
    RATE_LIMIT_WINDOW = 10  # seconds
    # Refresh rate_limit_store to only "recent" times
    rate_limit_store = [
        time
        for time in rate_limit_store
        if datetime.now() - time <= timedelta(seconds=RATE_LIMIT_WINDOW)
    ]
    if len(rate_limit_store) >= RATE_LIMIT:
        return (
            RATE_LIMIT_WINDOW - (datetime.now() - rate_limit_store[0]).total_seconds()
        )
    else:
        # Add current time to rate_limit_store
        rate_limit_store.append(datetime.now())
        return 0


def escape_html(str):
    # this i s a bare minimum for hack-prevention.
    # You might want more.
    str = str.replace("&", "&amp;")
    str = str.replace('"', "&quot;")
    str = str.replace("<", "&lt;")
    str = str.replace(">", "&gt;")
    str = str.replace("'", "&#39;")
    return str


def unescape_url(url_str):
    import urllib.parse

    # NOTE -- this is the only place urllib is allowed on this assignment.
    return urllib.parse.unquote_plus(url_str)


def parse_query_parameters(response):
    print("This is our initial response ", response)
    parseResponse =[]
    charPlacement =""

    for char in response:
        if char == '&':
            # Only add '&' if it's not the same as the previous character
            if charPlacement != '&':
                parseResponse.append('&')
        elif char == '=':
            # Only add '=' if it's not the same as the previous character
            if charPlacement != '=':
                parseResponse.append('=')
        else:
            # For all other characters, just append them
            parseResponse.append(char)
        
        # Update prev_char to the current character
        charPlacement = char
    parseResponse = "".join(parseResponse)
    print("New response: ",parseResponse)

    pairs = parseResponse.split("&")
    print("This is the .split pairs ", pairs)


    parsed_params = {}
    print(pairs)

    for pair in pairs:
        key = unescape_url(pair.split("=")[0])
        print("this is the key ",key)
        value = unescape_url(pair.split("=")[1])
        print("This is the value ",value)
        parsed_params[key] = value
        print(parsed_params)

    return parsed_params


def typeset_dollars(number):
    return f"${number:.2f}"


# The method signature is a bit "hairy", but don't stress it -- just check the documentation below.
# NOTE some people's computers don't like the type hints. If so replace below with simply: `def server(method, url, body, headers)`
# The type hints are fully optional in python.
def server(
    request_method: str,
    url: str,
    request_body: Optional[str],
    request_headers: dict[str, str],
) -> tuple[Union[str, bytes], int, dict[str, str]]:
    """
    `method` will be the HTTP method used, for our server that's GET, POST, DELETE, and maybe PUT
    `url` is the partial url, just like seen in previous assignments
    `body` will either be the python special `None` (if the body wouldn't be sent (such as in a GET request))
         or the body will be a string-parsed version of what data was sent.
    headers will be a python dictionary containing all sent headers.

    This function returns 3 things:
    The response body (a string containing text, or binary data)
    The response code (200 = ok, 404=not found, etc.)
    A _dictionary_ of headers. This should always contain Content-Type as seen in the example below.
    """
    # feel free to delete anything below this, so long as the function behaves right it's cool.
    # That said, I figured we could give you some starter code...
    global bids
    response_body = None
    status = 200
    response_headers = {}
    global path
    print(url)
    path = url.split("?")[0]
    
    if request_method == "GET":
        if path in "/" or path in "/main":
            return open("static/html/mainpage.html").read(),200,{"Content-Type": "text/html"}
        elif "/gallery" in path:
            if "?" in url:
                print(url)
                query = url.split("?")[1]
                print(query)
                return render_gallery(parse_query_parameters(query).get("query"),parse_query_parameters(query).get("category"))
            else:
                return open("static/html/listings.html").read(),200,{"Content-Type": "text/html"}
        elif "/listing" in path:
            newPath = render_listing(listings)
            return open(newPath).read(),200,{"Content-Type": "text/html"}
        elif "/create" == path:
            return open("static/html/create.html").read(),200,{"Content-Type": "text/html"}
        elif "/main.css" == path:
            return open("static/css/main.css").read(),200,{"Content-Type": "text/css"}
        # elif "/new_listing" == path:
        #     return open("static/js/new_listing.js").read(),200,{"Content-Type": "text/javascript"}
        elif "/bid.js" == path:
            return open("static/js/bid.js").read(),200,{"Content-Type": "text/javascript"}
        elif "/new_listing.js"== path:
            return open("static/js/new_listing.js").read(),200,{"Content-Type": "text/javascript"}
        elif "/table.js" == path:
            return open("static/js/table.js").read(),200,{"Content-Type": "text/javascript"}
        else:
            return open("static/html/404.html").read(),404,{"Content-Type": "text/html"} 
    elif request_method == "POST": 
        # if path == "/create":
            # If request_body is empty, or request_header for content type is missing OR does not indicate that json content was sent  (application/json) then an error 400 should be returned.
            #body does not matter in this case and can be empty
            # return postFunc(request_body)
        if path =="/api/place_bid":
            print(response_body)
            print("In /api/place_bid POST")
            # if request_headers.get("Content-Type", "") != "application/json":
            #     # checking if the headers look right.
            #     response_body = json.dumps({"message": "invalid or missing content type!"})
            #     status = 400
            #     response_headers["Content-Type"] = "application/json"
            # else:
            #     try:
            #         # attempt parsing and processing. Errors here should be caused by bad json, and treated as such.
            #         request_body = json.loads(request_body)
            #         # I'm being super-paranoid here -- forcing whatever is input to be a string even if it wasn't originally.
            #         name = str(request_body.get("name", ""))
            #         amount = str(request_body.get("amount",""))
            #         comments = str(request_body.get("comments", ""))
            #         if len(name) == 0 or len(amount) == 0:
            #             response_body = json.dumps(
            #                 {"mising body"}
            #             )
            #             status = 400
            #             response_headers["Content-Type"] = "application/json"
            #         else:
            #             next_id = 1 + max(bid["id"] for bid in bids)
            #             bids.append(
            #                 {"name": name, "amount": amount, "id": next_id, "comments":comments}
            #             )
            #             response_body = json.dumps({"message": "ok"})
            #             status = 200
            #             response_headers["Content-Type"] = "application/json"
            #     except Exception as e:
            #         print(e)
            #         response_body = json.dumps(
            #             {"message": "body could not be parsed as json!"}
            #         )
            #         status = 400
            #         response_headers["Content-Type"] = "application/json"
        else:
            return open("static/html/create_fail.html").read(),404,{"Content-Type": "text/html"}
    
    # Parse URL -- this is probably the best way to do it. Delete if you want.
    parameters = None
    if "?" in url:
        url, parameters = url.split("?", 1)

    # To help you get rolling... the 404 page will probably look like this.
    # Notice how we have to be explicit that "text/html" should be the value for
    # header: "Content-Type" now instead of being returned directly.
    # I am sorry that you're going to have to do a bunch of boring refactoring.
    response_body = open("static/html/404.html").read()
    status = 404
    response_headers["Content-Type"] = "text/html; charset=utf-8"





    return response_body, status, response_headers



# You shouldn't need to change content below this. It would be best if you just left it alone.


class RequestHandler(BaseHTTPRequestHandler):
    def c_read_body(self):
        # Read the content-length header sent by the BROWSER
        content_length = int(self.headers.get("Content-Length", 0))
        # read the data being uploaded by the BROWSER
        body = self.rfile.read(content_length)
        # we're making some assumptions here -- but decode to a string.
        body = str(body, encoding="utf-8")
        return body

    def c_send_response(self, message, response_code, headers):
        # Convert the return value into a byte string for network transmission
        if type(message) == str:
            message = bytes(message, "utf8")

        # Send the first line of response.
        self.protocol_version = "HTTP/1.1"
        self.send_response(response_code)

        # Send headers (plus a few we'll handle for you)
        for key, value in headers.items():
            self.send_header(key, value)
        self.send_header("Content-Length", len(message))
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()

        # Send the file.
        self.wfile.write(message)

    def do_POST(self):
        # Step 1: read the last bit of the request
        try:
            body = self.c_read_body()
        except Exception as error:
            # Can't read it -- that's the client's fault 400
            self.c_send_response(
                "Couldn't read body as text", 400, {"Content-Type": "text/plain"}
            )
            raise

        try:
            # Step 2: handle it.
            message, response_code, headers = server(
                "POST", self.path, body, self.headers
            )
            # Step 3: send the response
            self.c_send_response(message, response_code, headers)
        except Exception as error:
            # If your code crashes -- that's our fault 500
            self.c_send_response(
                "The server function crashed.", 500, {"Content-Type": "text/plain"}
            )
            raise

    def do_GET(self):
        try:
            # Step 1: handle it.
            message, response_code, headers = server(
                "GET", self.path, None, self.headers
            )
            # Step 3: send the response
            self.c_send_response(message, response_code, headers)
        except Exception as error:
            # If your code crashes -- that's our fault 500
            self.c_send_response(
                "The server function crashed.", 500, {"Content-Type": "text/plain"}
            )
            raise

    def do_DELETE(self):
        # Step 1: read the last bit of the request
        try:
            body = self.c_read_body()
        except Exception as error:
            # Can't read it -- that's the client's fault 400
            self.c_send_response(
                "Couldn't read body as text", 400, {"Content-Type": "text/plain"}
            )
            raise

        try:
            # Step 2: handle it.
            message, response_code, headers = server(
                "DELETE", self.path, body, self.headers
            )
            # Step 3: send the response
            self.c_send_response(message, response_code, headers)
        except Exception as error:
            # If your code crashes -- that's our fault 500
            self.c_send_response(
                "The server function crashed.", 500, {"Content-Type": "text/plain"}
            )
            raise


def run():
    PORT = 4131
    print(f"Starting server http://localhost:{PORT}/")
    server = ("", PORT)
    httpd = HTTPServer(server, RequestHandler)
    httpd.serve_forever()


run()

