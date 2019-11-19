---
layout: docs
title: "Pro tips"
---

# Pro tips

This page consists of a collection of tips and optional configurations that may
improve your experience with MicroStack.

## Try a different version, or a beta, or a daily build

Snaps are published in [channels](https://snapcraft.io/docs/channels) which are made up of a track (or major version), and an expected level of stability. Try          `snap info microstack` to see what versions are currently published. You can run:

```bash
sudo snap refresh --channel=latest/beta microstack
```

or

```bash
sudo snap refresh --channel=1.11/stable microstack
```

to get the required version.

## Kernel tweaks

OpenStack can potentially run a lot of processes and open a lot of network
connections. For a busy deployment, here are some suggested kernel settings for
your host:

```bash
echo fs.inotify.max_queued_events=1048576 | sudo tee -a /etc/sysctl.conf
echo fs.inotify.max_user_instances=1048576 | sudo tee -a /etc/sysctl.conf
echo fs.inotify.max_user_watches=1048576 | sudo tee -a /etc/sysctl.conf
echo vm.max_map_count=262144 | sudo tee -a /etc/sysctl.conf
echo vm.swappiness=1 | sudo tee -a /etc/sysctl.conf
sudo sysctl -p
```

## Client alias

Create an alias to remove the need to type the `microstack.` prefix when using
the `openstack` CLI client:

```bash
sudo snap alias microstack.openstack openstack
```

## Custom DNS

The DNS server used by cloud instances is 1.1.1.1 ([Cloudflare][cloudfare]). To
change this default create the file
`/var/snap/microstack/common/etc/neutron/dhcp_agent.ini` and add the following:

```no-highlight
[DEFAULT]
interface_driver = openvswitch
dhcp_driver = neutron.agent.linux.dhcp.Dnsmasq
enable_isolated_metadata = True
dnsmasq_dns_servers = <nameserver-ip>
```

Substitute in your chosen server IP address and save the file.

Now restart the MicroStack services:

```bash
sudo systemctl restart snap.microstack.*
```

## Disabling MicroStack

You can save system resources by disabling MicroStack when it's not in use:

```bash
sudo snap disable microstack
```

To re-enable:

```bash
sudo snap enable microstack
```

## Accessing Horizon on a remote server

If you've installed MicroStack on a remote server you can use SSH local port
forwarding to access Horizon:

```bash
sudo ssh -i <ssh-key> -N -L 8001:10.20.20.1:80 <user>@<server-ip>
```

Then point your browser at: `http://localhost:8001`.


<!-- LINKS -->

[cloudfare]: https://www.cloudflare.com/dns
