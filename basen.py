import base64
string = "0123456789abcdefghijklmnoppqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
var1 = string.encode('ascii')
print(var1)
var1bytes = base64.b64encode(var1)
print(var1bytes)
decoded = var1bytes.decode('ascii')
print(decoded)

# b'0123456789abcdefghijklmnoppqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# b'MDEyMzQ1Njc4OWFiY2RlZmdoaWprbG1ub3BwcXJzdHV2d3h5ekFCQ0RFRkdISUpLTE1OT1BRUlNUVVZXWFla'
# MDEyMzQ1Njc4OWFiY2RlZmdoaWprbG1ub3BwcXJzdHV2d3h5ekFCQ0RFRkdISUpLTE1OT1BRUlNUVVZXWFla
#
# Process finished with exit code 0