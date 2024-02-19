import json

with open('sample-data.json') as f:
    data = json.load(f)


print('''
Interface Status 
================================================================================
DN                                                 Description           Speed    MTU 
-------------------------------------------------- --------------------  ------  ------
''', end = "")
           
imdata = data["imdata"]
for i in imdata:
    dn = i["l1PhysIf"]["attributes"]["dn"]
    descr = i["l1PhysIf"]["attributes"]["descr"]
    speed = i["l1PhysIf"]["attributes"]["speed"]
    mtu = i["l1PhysIf"]["attributes"]["mtu"]
    print(f"{dn:50} {descr:20} {speed:7}  {mtu:^6}")
    