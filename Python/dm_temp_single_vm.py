def generate_config(context):
    resources = []
    resources.append({
        'name': 'temp-instance-1',
        'type': 'compute.v1.instance',
        'properties': {
            'zone': 'us-central-1a',
            'machinteType': '/zones/us-central1-a/machineTypes/n1-standard-1',
            'disks': [{
                'deviceName': 'boot',
                'type': 'PERSISTENT',
                'boot': True,
                'autoDelete': True,
                'initializeParams': {
                    'sourceImage': 'projects/debian-cloud/global/images/family/debian-9'
                }
            }],
            'networkInterfaces': [{
                'network': 'global/networks/default'
            }]
        }
    })

    return {'resources': resources}