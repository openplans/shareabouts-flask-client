import requests

from flask import request


def proxy_view(url, requests_args=None):
    """
    Forward as close to an exact copy of the request as possible along to the
    given url.  Respond with as close to an exact copy of the resulting
    response as possible.

    If there are any additional arguments you wish to send to requests, put
    them in the requests_args dictionary.
    """
    requests_args = (requests_args or {}).copy()
    headers = dict(request.headers)  # Maybe?

    if 'headers' not in requests_args:
        requests_args['headers'] = {}
    if 'data' not in requests_args:
        requests_args['data'] = request.data
    if 'params' not in requests_args:
        requests_args['params'] = request.args

    # Explicitly set content-length request header, as some servers will
    # want it and complain without it.
    headers['Content-Length'] = unicode(len(requests_args['data']))
    requests_args['headers'].update(headers)

    response = requests.request(request.method, url, **requests_args)

    # Certain response headers should NOT be just tunneled through.  These are
    # they.  For more info, see:
    # http://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html#sec13.5.1
    #
    # Note that, although content-encoding is not listed among the hop-by-hop
    # headers, it can cause trouble as well.  Just let the server set the value
    # as it should be.
    proxy_headers = {}
    hop_by_hop = ['connection', 'keep-alive', 'proxy-authenticate',
                  'proxy-authorization', 'te', 'trailers', 'transfer-encoding',
                  'upgrade', 'content-encoding']
    for key, value in response.headers.iteritems():
        if key.lower() in hop_by_hop: continue
        proxy_headers[key] = value

    proxy_response = (
        response.content,
        response.status_code,
        proxy_headers)

    return proxy_response
