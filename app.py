# uwsgi --http :8080 --wsgi-file app.py --callable app --master

import os
import zunzuncito

document_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'API/')

versions = ['v0', 'v1', 'v2']

routes = [
    # ('/.*', 'default'),
    ('/teste', 'test_get', 'GET'),
    ('/teste', 'test_post', 'POST'),
    ('/teste', 'test_put', 'PUT')
]

app = zunzuncito.ZunZun(document_root, versions, routes, debug=False)
