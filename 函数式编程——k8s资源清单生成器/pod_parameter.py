#Author:Anliu
import json
parameter = {
    "apiVersion":["v1",""],
    "":""
}

with open("parameter_list","w",encoding="utf-8") as f1:
    json.dump(parameter,f1)