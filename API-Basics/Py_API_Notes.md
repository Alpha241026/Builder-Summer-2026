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