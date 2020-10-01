def GenerateConfig(context):
    resources = []

    project = context.env["project"]
    zone = context.properties["zone"]
    instance_name = "gcp-vm-" + context.env["project"]
    machine_type = context.properties["machineType"]
    
    resources.append({
        "name": instance_name,
        "type": "compute.v1.instances",
        "properties": {
            "zone": zone,
            "machineType": "zones/{}/machineTypes/{}".format(zone, machine_type),
            "disks": [{
                "boot": True,
                "autoDelete": True,
                "initializeParams": {
                    "diskName": "boot-disk-" + instance_name,
                    "sourceImage": "projects/debian-cloud/global/images/debian-10-buster-v20200910",
                    "diskType": "projects/{}/zones/{}/diskTypes/pd-standard".format(project, zone),
                    "diskSizeGb": "10",
                }
            }],
            "networkInterfaces": [{
                "subnetwork": context.properties["nic1-subnet"],
                "accessConfigs": [{
                    "name": "External NAT",
                    "type": "ONE_TO_ONE_NAT",
                    "networkTier": "STANDARD"
                }]
            }]
        }
    })

    return {"resources": resources}