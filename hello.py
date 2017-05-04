def app(environ, start_response):
    d = environ['QUERY_STRING'].split("&")
    status='200 OK'
    headers = [
        ('Content-type', 'text/plain')
    ]
    start_response(status, headers)
    body = ""
    for k in d:
        body += k + b"\n"
    return [body]
