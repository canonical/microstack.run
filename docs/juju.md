---
layout: docs
title: "Using Juju"
---

# Using Juju


## Install Juju

```bash
sudo snap install juju --classic
```

## Generate image metadata for Juju

Juju needs to know how to find metadata for the images necessary for
provisioning machines. For private clouds such as OpenStack this is done via
*Simplestreams*. 

First decide on a Ubuntu release and region. Here we'll use Ubuntu 18.04 LTS
(Bionic) and a region of 'localhost'. Start by importing a Bionic image into
the cloud:

```bash
OS_SERIES=bionic
REGION=localhost
IMAGE_ID=$(curl http://cloud-images.ubuntu.com/$OS_SERIES/current/$OS_SERIES-server-cloudimg-amd64.img | \
microstack.openstack image create \
--public --container-format=bare --disk-format=qcow2 \
-f value -c id $OS_SERIES)
```

The image's ID will be stored in variable `IMAGE_ID`. You can also list
OpenStack images (and their IDs) in the usual way:

```bash
microstack.openstack image list
```

Next, generate the metadata:

```bash
mkdir ~/simplestreams
juju metadata generate-image -d ~/simplestreams -i $IMAGE -s $OS_SERIES -r $REGION -u http://10.20.20.1:5000/v3
```

See [Cloud image metadata][juju-cloud-image-metadata] in the Juju documentation
for background information.

## Add the cloud to Juju

Create a cloud definition file, say `microstack.yaml`, for the OpenStack cloud
(notice the region of 'localhost'):

```yaml
clouds:
    microstack:
      type: openstack
      auth-types: [access-key,userpass]
      regions:
        localhost:
           endpoint: http://10.20.20.1:5000/v3
```

Now add the cloud by referencing that file:

```bash
juju add-cloud microstack -f microstack.yaml
```

The command `juju clouds --local` should now list the cloud.

## Add the cloud credentials to Juju

Source a file to have the shell pick up credential information:

```bash
source /var/snap/microstack/common/etc/microstack.rc
```

Now supply that information to Juju:

```bash
juju autoload-credentials
```

An interactive session will ensue where you will need to select the
OpenStack credentials that the command has located. Here is an example:

```no-highlight
Looking for cloud and credential information locally...

1. LXD credential "localhost" (new)
2. openstack region "<unspecified>" project "admin" user "admin" (new)
3.  (new)
Select a credential to save by number, or type Q to quit: 2

Select the cloud it belongs to, or type Q to quit [microstack]: ENTER

Saved openstack region "<unspecified>" project "admin" user "admin" to cloud microstack

1. LXD credential "localhost" (new)
2. openstack region "<unspecified>" project "admin" user "admin" (new)
3.  (new)
Select a credential to save by number, or type Q to quit: Q
```

Added credentials can be inspected with:

```bash
juju credentials --show-secrets --format yaml
```

## Create the Juju controller

Create the Juju controller:

```bash
juju bootstrap \
--config network=test \
--config external-network=external \
--config use-floating-ip=true \
--metadata-source ~/simplestreams \
microstack microstack
```
 
Refer to [ ][ ] for information on the options used in the above command.

## Deploy a Kubernetes workload

<!-- LINKS -->

[juju-cloud-image-metadata]: https://jaas.ai/docs/cloud-image-metadata
