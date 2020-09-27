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
