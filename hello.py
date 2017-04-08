def wsgi_app(environ, start_response):
    d = environ['QUERY_STRING'].split('=')
    status='200 OK'
    headers = [
        ('Content-type', 'text/plain')
    ]
    start_response(status, headers)
    return [d]
