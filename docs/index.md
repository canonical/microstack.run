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

Begin by installing MicroStack via a [snap][microstack-snap]. Here we use the
default `--beta` channel but, as with any snap, channels `--stable`,
`--candidate` and `--edge` are also available (in principle):

```bash
sudo snap install microstack --beta --classic
```

<div class="p-notification--information">
  <p class="p-notification__response">
    <span class="p-notification__status">Note:</span>
    At time of writing, MicroStack has been assured to run bug-free only on
    Ubuntu 18.04 LTS.
  </p>
</div>

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

Configure OpenStack in this way:

```bash
sudo microstack.init --auto
```

This configured and started services. It also created the database, networks,
an image, several flavors, ICMP/SSH security groups, and an SSH keypair (called
'microstack'). These can be viewed with the standard client commands. For
example:

```bash
microstack.openstack network list
```

Output:

```no-highlight
+--------------------------------------+----------+--------------------------------------+
| ID                                   | Name     | Subnets                              |
+--------------------------------------+----------+--------------------------------------+
| 92763cdb-8543-445a-973a-952a1483506d | external | 18cef02a-03ba-448f-9d11-59dfd28f12b0 |
| b7d73bd0-f12d-4446-99e9-7e6c18b657fe | test     | 50540f94-ca00-40a1-8faa-4e0408369f36 |
+--------------------------------------+----------+--------------------------------------+
```

MicroStack comes with the convenient instance launcher ``microstack.launch``
that uses default values for network, image, flavor, and SSH key. It also sets
up a floating IP address.

To launch an instance named 'test' that uses the CirrOS image:

```bash
microstack.launch cirros --name test
```

The instance's public IP address will be shown in the resulting output:

```no-highlight
Server test launched! (status is BUILD)

Access it with `ssh -i $HOME/.ssh/id_microstack` <username>@10.20.20.202
```

Access that instance using the default SSH key (the CirrOS image comes with a
'cirros' user account):

```bash
ssh -i ~/.ssh/id_microstack cirros@10.20.20.202
```

<div class="p-notification--positive">
  <p class="p-notification__response">
    <span class="p-notification__status">Pro tip:</span>
    The CirrOS image user account 'cirros' has a default password of
    'gocubsgo'. It can be useful if you have trouble logging in with a key.
  </p>
</div>

The ``microstack.launch`` command also supports arguments ``--key``,
``--flavor``, ``--image``, and ``--net-id``. You may need to create objects
using the standard client if non-default values are used. You can, of course,
replace the command entirely with ``microstack.openstack server create``.

### Horizon

The Horizon dashboard lives here:

`http://10.20.20.1`

and its default credentials are:

```no-highlight
username: admin
password: keystone
```

### Next steps

This Quickstart has shown you how simple it is to get started with MicroStack.
You can now go on to perform native OpenStack operations such as importing boot
images; creating keypairs, networks, and cloud flavors. See the [OpenStack
documentation][openstack-docs].

<!-- LINKS -->

[microstack-snap]: https://snapcraft.io/microstack
[openstack-cirros]: https://docs.openstack.org/image-guide/obtain-images.html#cirros-test
[openstack-docs]: https://docs.openstack.org/
