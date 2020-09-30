Python templates for Google Cloud Deployment Manager must have the following two components:

* A method called GenerateConfig(context) or generate_config(context)
* Method must return a dictionary

```
def generate_config(context):

    resources = []

    resources.append({
        'name': ''
        'type': ''
        'properties': {}
    })

    return {'resources': resources}

```

Get a quick list of available types in your region ([Link to full list](https://cloud.google.com/deployment-manager/docs/configuration/supported-resource-types))

`gcloud deployment-manager types list`