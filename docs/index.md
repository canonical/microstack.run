---
layout: docs
title: "Installation and Quickstart"
---

# Installation and Quickstart

MicroStack speedily installs OpenStack on a single machine. Supported services
are currently Glance, Horizon, Keystone, Neutron, and Nova.

<div class="p-notification--information">
  <p class="p-notification__response">
    <span class="p-notification__status">Requirements:</span>
    You will need at least 2 CPUs, 8 GiB of memory, and 100 GiB of disk space.
  </p>
</div>

## Installation

Begin by installing MicroStack. It is installed with a [snap][microstack-snap]:

```bash
sudo snap install microstack --classic
```

The standard `openstack` client is also installed, and is invoked like so:

```bash
microstack.openstack <command>
```

## Quickstart

The purpose of the Quickstart guide is to confirm that the cloud is in working
order. The following can all be done within 10 to 15 minutes depending on your
machine:

- configure OpenStack automatically
- launch an instance based on the [CirrOS][openstack-cirros] image (with
  floating IP address)
- SSH to the instance

Let's begin.

**Configure** OpenStack in this way:

<!--
Revisit the configuration step (interactive?)
-->

```bash
sudo microstack.init --auto
```

This configured and started services. It also created the database, networks,
an image, several flavors, ICMP/SSH security groups, and an SSH keypair.

**Launch** an instance named 'test':

```bash
microstack.launch test
```

The instance's public IP address will be shown in the resulting output. For
example:

```no-highlight
--------------------------------------+------+--------+------------------------------------+--------+---------+
| ID                                   | Name | Status | Networks                           | Image  | Flavor  |
+--------------------------------------+------+--------+------------------------------------+--------+---------+
| 80a2bf1b-5ad2-4cd1-af25-3bb325711acb | test | ACTIVE | test=192.168.222.109, 10.20.20.202 | cirros | m1.tiny |
+--------------------------------------+------+--------+------------------------------------+--------+---------+
```

**Access** that instance using the auto-generated SSH key:

```bash
ssh -i ~/.ssh/id_microstack cirros@10.20.20.202
```

### Horizon

The Horizon dashboard lives here:

`http://10.20.20.1`

and its default credentials are:

```no-highlight
username: admin
password: keystone
```

### Additional instances

The initialisation process creates an SSH keypair called 'microstack'. This can
be confirmed with:

```bash
microstack.openstack keypair list
```

Sample output:

```no-highlight
+------------+-------------------------------------------------+
| Name       | Fingerprint                                     |
+------------+-------------------------------------------------+
| microstack | 17:94:f6:b8:e2:81:4d:4d:c8:56:c7:00:3a:2f:f1:fd |
+------------+-------------------------------------------------+
```

<div class="p-notification--information">
  <p class="p-notification__response">
    <span class="p-notification__status">Note:</span>
    If a keypair is not used with instances based on the CirrOS image, password
    authentication can be tried. This image sets up a user account of 'cirros'
    with a password of 'gocubsgo'.
  </p>
</div>

Instances can be created with the CirrOS image in this way:

```bash
microstack.openstack server create --flavor m1.small --nic net-id=test --key-name=microstack --image cirros <instance-name>
```

Assign the instance a floating IP address in the usual way:

```bash
ALLOCATED_FIP=$(microstack.openstack floating ip create -f value -c floating_ip_address external)
microstack.openstack server add floating ip <instance-name> $ALLOCATED_FIP
```

And then SSH:

```bash
ssh -i ~/.ssh/id_microstack cirros@$ALLOCATED_FIP
```

### Next steps

This Quickstart has shown you how quick and simple it is to get started with
MicroStack. You can now go on to perform native OpenStack operations such as
importing boot images; creating keypairs, networks, and cloud flavors.

<!-- LINKS -->

[microstack-snap]: https://snapcraft.io/microstack
[openstack-cirros]: https://docs.openstack.org/image-guide/obtain-images.html#cirros-test
