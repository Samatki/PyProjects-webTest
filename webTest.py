from sys import argv
import httplib as h

x = argv[1]

conn = h.HTTPConnection(x)
conn.request("GET","/")
y = conn.getresponse()

if 200<=y.status and y.status<400:
	z = 'OK'
else:
	z= 'BAD REQUEST'


print x, ' *** ', z,'\n\t', y.status, '  ***  ', y.reason
