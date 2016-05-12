# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server

from  newhello import application

httpd = make_server('', 9000, application)
print("Server HTTP on port 9000")

httpd.serve_forever()

