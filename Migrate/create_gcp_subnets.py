def GenerateConfig(context):
    resources = []

    resources.append({
        "name": context.env["name"],
        "type": "compute.v1.subnetwork",
        "properties": {
            "region": context.properties["region"],
            "network": context.properties["network"],
            "ipCidrRange": "10.1.0.0/24",
            "gatewayAddress": "10.1.0.1"
        }
    })

    return {"resources": resources}