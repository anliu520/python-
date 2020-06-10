#Author:Anliu
import yaml,json
dict_moder = {
    'apiVersion': None,
    'kind': None,
    'metadata': {
        'name': None,
        'labels':
            {
                "key01": "valume1",
                "key02": "valume2"
            }
    },
    'spec':
        {
            'containers': [{'name': None,
                            'image': None
                            }]
        }
}

with open("parameter_list","r",encoding="utf-8") as f2:
    apiversion = json.load(f2)
    print(apiversion["apiVersion"])

with open("pod.yaml","r",encoding="utf-8") as f1:
    text  = yaml.load(f1,Loader=yaml.FullLoader)

    text["apiVersion"] = input("%s>>>:" %apiversion["apiVersion"])
    #text["kind"] = "deployment"
    text["kind"] = input("kind  >>>:")
    text["metadata"]["name"] = "anliu"
    print(text["metadata"]["labels"])
    labels =  text["metadata"]["labels"]
    labels.update({"app":"myapp-opd","version":"v3"})

    text["spec"]["containers"][0]["name"] = "myapp"
    text["spec"]["containers"][0]["images"] = "images"

#print(text)
with open("pod_test.yaml","w",encoding="utf-8") as f2:
    yaml.dump(text,f2)



