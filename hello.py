def app(environ, start_response):
    d = dict(x.split("=") for x in environ['QUERY_STRING'].split("&"))
    status='200 OK'
    headers = [
        ('Content-type', 'text/plain')
    ]
    start_response(status, headers)
    body = ""
    for k in d.keys():
        body += k + b"=" + d[k] + b"\n"
    return [body]
