from bluepy import btle
 
print "Connecting..."
dev = btle.Peripheral("c0:83:47:30:5a:4d")
 
print "Services..."
for svc in dev.services:
	print str(svc)
