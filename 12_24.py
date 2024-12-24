# import json

# x = {
#     "name":"John",
#     "age": 30,
#     "married": True,
#     "divorced": False,
#     "pets": ("Ann","Billy"),
#     "pets": None,
#     "cars": [
# {"model": "BMW 230", "mpg": }
#     ]
# }


# import re   
# s = 'My 2 favourite numbers are 8 and 10'
# lst = re.findall('[0-9]+', s)   
# print(lst) 


# import re  
# s = 'Hello from shubhamg199630@gmail.com to priya@yahoo.com about the meeting @2PM'
# lst = re.findall('\S+@\S+', s)     
# print(lst) 

# import re  
# s = 'Hello from 99857575 to 57565757 about the meeting 984848747'
# lst = re.findall(r'\b\d{8}\b', s)     
# print(lst) 


import re  
s = 'Hello my name is Taivanbat and my phone number is 99378809 and 123456789  АБ12345678'
lst = re.findall(r'\b[А-ЯӨҮ]{2}\d{8}\b', s)     
print(lst) 



