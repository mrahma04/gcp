def GenerateConfig(context):
    resources = []

    project_id = context.env['project']

    resources.append({
        'name': 'vpc-1',
        'type': 'compute.v1.network',
        'properties': {
            "autoCreateSubnetworks": False,
            "routingConfig": {
                "routingMode": "REGIONAL"
            }
        }
    })

    return {'resources': resources}