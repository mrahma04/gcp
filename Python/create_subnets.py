def GenerateConfig(context):
    resources = []

    project = context.env['project']

    for i in range(0, 3):
        resources.append({
            'name': context.env['name'] + '-' + str(i),
            'type': 'compute.v1.subnetwork',
            'properties': {
                'region': context.properties['region'],
                'network': 'projects/{}/global/networks/fox-vpc-1'.format(project),
                'ipCidrRange': '10.{}.0.0/24'.format(str(i)),
                'gatewayAddress': '10.{}.0.1'.format(str(i))
            }
        })

    return {'resources': resources}