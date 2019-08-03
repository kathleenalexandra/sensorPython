import pygatt

adapter = pygatt.GATTToolBackend()

try:
    adapter.start()
    device = adapter.connect('c0:83:43:30:56:4d')
    value = device.char_read("a1e8f5b1-696b-4e4c-87c6-69dfe0b0093b")
finally:
    adapter.stop()

