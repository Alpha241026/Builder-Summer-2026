########## REQUESTS ########## :-



Requests is a simple HTTP library for Python.


In requests, calling requests.get(url) sends the question, and whatever it returns is the answer - packaged as one object, not just a string. Thus, the thing you get back isn't the data itself, it's a container holding the data plus metadata about how it arrived.


Think about what a real answer to a question includes beyond just the answer: did it succeed, what kind of thing is this, in what language, and what's the actual content. That's exactly the four things you're pulling off the response object:

-> response.status_code - did it even succeed? This is the server's one-word verdict. 200-range = good, 400-range = you asked wrong, 500-range = server broke.

-> response.headers - metadata about the answer, not the answer itself. content-type telling you "this is JSON" is like an envelope telling you what's inside before you open it.

-> response.encoding - how the raw bytes were turned into text (usually utf-8).

-> response.text - the raw string body. If the server sent back HTML or plain text, this is what you'd read.

-> response.json() - same body as .text, but parsed into an actual Python dict/list. This is a method (has ()), not an attribute, because it's doing work - converting a JSON string into real Python data structures you can index into (data['name'], data['repos'][0]).


The pattern that repeats everywhere; once this clicks, every future API call is the same shape:

Build the request (URL + method + maybe params/headers/body)
Fire it -> get a response object back
Check .status_code first
Pull the shape of data you need (.json() almost always, for any modern API)


To install requests, run:
py -m pip install requests python-dotenv


[Note that command specific notes are mentioned in comments in requests_prac.py] 


General notes :-


Verb idempotency (ties to: GET/POST/PUT/DELETE lines)

GET, PUT, DELETE are idempotent — calling once or many times leaves the same end state (safe to retry automatically).
POST is not idempotent — calling it twice creates two things. This is why GET is "the safe one" and POST needs care around retries.


Status code categories (ties to: print(r.status_code) / the if r.status_code == 200 block)

2xx = success · 3xx = redirected (see r.history) · 4xx = client's fault (bad request) · 5xx = server's fault (like the 503 hit earlier).
Checking the hundreds-digit lets you branch logic without hardcoding every exact code.


Why timeouts exist (ties to: requests.get('https://github.com/', timeout=0.001))

Without a timeout, a hung server means your program waits forever — no built-in giving-up point.
In real systems, one un-timed-out slow call can cascade into everything else hanging too.


Statelessness and auth (ties to: the headers / custom-verb lines, even though auth itself wasn't run)

HTTP has no memory between requests — the server forgets you instantly unless you resend proof (auth headers, tokens, cookies) every single time.
This is a deliberate scaling tradeoff, not a flaw: statelessness is what lets any server handle any request.


Sessions save real cost (ties to: the s = requests.Session() block)

TCP handshake + TLS negotiation (connection setup) is expensive relative to sending small data.
A Session reuses the same connection across calls to the same host, skipping that setup cost each time.


Custom verbs work because HTTP doesn't validate them (ties to: the requests.request('MKCOL', ...) line)

The verb is just a word in the request text — the protocol itself doesn't enforce a fixed list.
Whether it does anything depends entirely on whether the server has code written to handle that verb — sending is trivial, meaningful handling isn't.






########## DOTENV ########## :-



python-dotenv reads key-value pairs from a .env file and can set them as environment variables.


This way, secrets/config never get hardcoded in code (and never get pushed to GitHub,
since .env is in .gitignore).


.env file (plain text, key=value) -> load_dotenv() reads it and injects into os.environ -> os.getenv("KEY") pulls it back out in code.


dotenv_values(".env") is the alternative that returns a dict without touching
os.environ - not used here, but exists for advanced config management.






########## GitHub CLI API ########## :-



Simple Python script using real GitHub public api and requests library to fetch info of a username and print the fields in a structured, human readable manner.


Flow: GET request -> check status_code -> only parse .json() if the request succeeded -> pull specific fields from the parsed dict.


Status codes handled:

- 200: success, parse and print fields (name, email, bio, public_repos,
  followers, following)

- 403: rate limit exceeded (GitHub allows 60 unauthenticated requests/hour)

- else: treated as user not found (matches GitHub's 404 for missing users)


Research method: hit https://api.github.com/users/<real-username> and https://api.github.com/users/<fake-username> directly in browser first, to see real response shapes before writing any code.






########## Full REST API - Client + Flask Server ########### :-



Flask is the server-side mirror of requests - instead of building outbound requests, you register handlers that wait and react to incoming ones.


Core pattern: @app.route(path, methods=[...]) + a function = "when a request matching this path+verb arrives, run this code and return its result as the response body." jsonify() converts Python dicts/lists into JSON responses -
the server-side mirror of .json() parsing on the client.


Data is a plain in-memory Python list of dicts (no database) - resets on every server restart, which also happens automatically on every file save because of debug=True. Real persistence will come with PostgreSQL (Phase II).


Verbs implemented (flask_server.py), each its own route+function on /books (or /books/<int:id> where a specific record is targeted):

- GET /books - returns the full list via jsonify(books)
- POST /books - reads request.get_json(), appends new record, returns 201
- PATCH /books/<id> - loops to find matching id, updates only fields present
  in the incoming body (checked via "field" in data before assigning) -
  true partial update, not a full overwrite like PUT would be
- DELETE /books/<id> - loops to find matching id, books.remove(rec), returns
  confirmation or 404 if not found
- QUERY /books - custom/experimental method (mentioned below)


Status codes used: 200 (success/read), 201 (created), 404 (not found).
4xx = client's fault, 5xx = server's fault, 2xx = success - same category system from the requests notes, now used from the server side.


Known limitations (noted honestly, not fixed - out of scope for this demo):

- No schema validation on POST body (a malformed request would still get
  appended as-is)
- Server assigns nothing automatically; client computes next id via
  max(existing ids)+1 before POSTing



---- QUERY method (RFC 10008) ----

RFC 10008, published June 2026, defines QUERY as a new HTTP method - the first new standard method since PATCH in 2010. It's "GET with a body":
safe and idempotent like GET (read-only, no side effects, repeatable), but carries a JSON body like POST - solving the real problem where complex filters don't fit cleanly in a URL query string, without falsely implying a write operation the way POST-for-search does.

As of writing, no major public API implements QUERY server-side yet, so this demo builds BOTH sides - a Flask server that manually registers the QUERY method, and a client that sends it - to prove the full round trip, rather than pretending to hit a live implementation that doesn't exist.

Server: registering a custom/new verb is no different from any other - methods=["QUERY"] works exactly like methods=["GET"] would, since Flask/ Werkzeug don't restrict method names to a fixed list (same lesson as requests' Custom Verbs section, now from the server side).

Filtering logic: loops through books, sets a per-book "matches" flag, independently checked (not chained if/elif) against each optional filter key (category, min_price, max_price, min_stock) - order-independent, easy to extend with more filters later, and "in filters" checks mean a
missing filter key never wrongly disqualifies a book.

Client: requests has no .query() shortcut (library predates the RFC), so the general-purpose requests.request("QUERY", url, json=filters) is used instead - the same underlying function .get()/.post()/etc. all wrap around, just called directly with the verb as a string argument.