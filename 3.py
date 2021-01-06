import json

String_Object = {'make': 'Nokia', 'model': 216, 'color': 'Black'}

print("String_Object : ")
print(String_Object, "\n")

print("JSON data sorted :")
print(json.dumps(String_Object, sort_keys=True, indent=4))
