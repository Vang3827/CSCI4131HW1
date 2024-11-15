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
    {"vehicle":"Dodge Challenger","url":"https://images.unsplash.com/photo-1632686341369-8a7991237930?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D","description":"Longer text for descrption", "category":"small", "numeric ID": 1, "Date": "08/20/2024",
     "bids":[
         {"bidder 1":"Carl k", "bid amount":4500, "comment":"I would love this car."},{"bidder 2":"Sam Samson", "bid amount":5500, "comment":"I just want to use money."}
         ]
    },
    {"vehicle":"Ford Mustang","url":"https://images.unsplash.com/photo-1610378985708-ac6de045f9f3?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D","description":"Longer text for descrption", "category":"small", "numeric ID": 2, "Date": "09/15/2024",
     "bids":[
         {"bidder 1":"Luke Lukenson", "bid amount":2500, "comment":"Dailer driver right here."},{"bidder 2":"Peter Porker", "bid amount":6500, "comment":""}
         ]},
    {"vehicle":"Toyota Tundra","url":"https://images.unsplash.com/photo-1621993202323-f438eec934ff?q=80&w=1964&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D","description":"Longer text for descrption", "category":"truck", "numeric ID": 3, "Date": "09/10/2024",
     "bids":[
         {"bidder 1":"Adam Apple", "bid amount":6500, "comment":"Work truck."},{"bidder 2":"Ben Benji", "bid amount":7500, "comment":"New truck for me."},{"bidder 3":"Cedar Cider", "bid amount":9500, "comment":"The Cedar Mobile."}
         ]}
]
newListing =[]
bids =[{"id": 0, "name": "", "amount": "0"}]
message_list = [
    {"id": 1, "author": "system", "message": "test message one"},
    {"id": 2, "author": "system", "message": "test message two"},
]
        
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
    
    if query == "" and category =="":

        tablestr = ""
        listingname = ""
        numOfBids = 0
        cat = ""
        date = ""
        dataid = 0
        url =""
        timerid = 0

        for i in range(len(listings)):
            maxbid = 0

            for j in range(len(listings[i]["bids"])):
                numOfBids = numOfBids + 1

                if listings[i]["bids"][j]["bid amount"] > maxbid:
                    maxbid = listings[i]["bids"][j]["bid amount"]

            listingname = listings[i].get("vehicle")
            cat = listings[i].get("category")
            date = listings[i].get("Date")
            dataid += 1
            timerid +=1
            print("dataID: ", dataid, "timerId: ", timerid)
            url = listings[i].get("url")
            tablestr = tablestr + """
                    <tr id="tableRow" class="box">
                    <td id='imgData"""+str(dataid)+"""'
                        data-image="""+url+""">
                        <a href='/listing/"""+str(dataid)+"""'>"""+listingname+"""</a>
                    </td>
                    <td>"""+str(numOfBids)+"""</td>
                    <td>$ """+str(maxbid)+"""</td>
                    <td id=timer"""+str(timerid)+"""'>"""+date+"""</td>
                    <td><input data-id= """+str(dataid)+""" class = "bidButton" type="button" id="delete" value="delete"></td>
                </tr>
            """

        return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="/main.css">
            <title>Auto Auction</title>
            <script defer src="/table.js">
            </script>
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
                <h1 class="listingh">Auto Auction list</h1>
            <div class="listingColumn">
                <div class="tableContainer">
                    <table border="1">
                        <tr>
                            <th>Listing</th>
                            <th>Number of Bids</th>
                            <th>Top Bid</th>
                            <th>Auction Ends</th>
                        </tr>
                        {tablestr}
                    </table>
                </div>
                <div class="sideOfTable" id="imgPreview">
                </div>
            </div>
        </body>
        </html>
    """,200,{"Content-Type": "text/html"}
    else:
        galleryList = checkListDict(query,category)
        # name = gallList.get("vehicle")

        listingname = []
        numOfBids = []
        cat = []
        date = []

        for i in range(len(galleryList)):
            print("for loop to append")
            listingname.append(galleryList[i].get("vehicle"))
            print(listingname.append(galleryList[i].get("vehicle")))
            # cat.append(galleryList[i].get("category"))
            # numOfBids.append(galleryList[i].get("bids"))
            # date.append(galleryList[i].get("Date"))

            

        return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="/main.css">
            <title>Auto Auction</title>
            <script defer src="/table.js">
            </script>
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
                return render_gallery("","")
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
        if path =="/api/place_bid":
            print("In /api/place_bid POST")
            if request_headers.get("Content-Type", "") != "application/json":
                # checking if the headers look right.
                response_body = json.dumps({"message": "invalid or missing content type!"})
                status = 400
                response_headers["Content-Type"] = "application/json"
            else:
                try:
                    # attempt parsing and processing. Errors here should be caused by bad json, and treated as such.
                    request_body = json.loads(request_body)
                    #
                    print("In else --> try ",request_body)
                    name = str(request_body.get("bidder_name", ""))
                    amount = str(request_body.get("bid_amount",""))
                    comments = str(request_body.get("comment", ""))
                    bid_Id = str(request_body.get("listing_id", ""))
                    if len(name) == 0 or len(amount) == 0:
                        response_body = json.dumps(
                            {"mising body"}
                        )
                        status = 400
                        response_headers["Content-Type"] = "application/json"
                    else:
                        # Come back
                        # 
                        print("Else statement In right place ",request_body)

                        next_id = 1 + max(bid["id"] for bid in bids)
                        bids.append(
                            {"bidder_name": name, "bid_amount": amount, "id": next_id, "comment":comments, "bid_Id":bid_Id}
                        )
                        response_body = json.dumps({"message": "ok"})
                        status = 200
                        response_headers["Content-Type"] = "application/json"
                        print("The bids: ",bids)
                except Exception as e:
                    print(e)
                    response_body = json.dumps(
                        {"message": "body could not be parsed as json!"}
                    )
                    status = 400
                    response_headers["Content-Type"] = "application/json"
        elif path == "/api/delete_listing":
            print("In /api/delete_listing ")
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

