import json

info = 'sample-data.json'
with open(info, "r") as file:
    data = json.load(file)
sorts=data["imdata"]
