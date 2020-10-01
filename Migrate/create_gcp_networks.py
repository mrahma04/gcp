def GenerateConfig(context):
    resources = []

    resources.append({
        "name": context.env["name"],
        "type": "compute.v1.network",
        'properties': {
            "autoCreateSubnetworks": False,
            "routingConfig": {
                "routingMode": "REGIONAL"
            }
        }
    })

    return {'resources': resources}