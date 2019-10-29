---
layout: docs
title: "Clustering"
---

# Clustering

<div class="p-notification--information">
  <p class="p-notification__response">
    <span class="p-notification__status">Note:</span>
    The clustering feature is currently offered as a tech preview.
  </p>
</div>

Clustering allows you to install MicroStack on several machines ("nodes") and
create an OpenStack cloud by combining the nodes together. At this time the
cloud roles that can be assigned to each node are *control* and *compute*.
These respectively translate to the cloud's control plane and data plane. A
cloud can consist of a single control node and multiple compute nodes.

The setup of nodes must be done from a freshly installed MicroStack snap. See
the [Installation and Quickstart][install] page for how to install MicroStack.

<div class="p-notification--information">
  <p class="p-notification__response">
    <span class="p-notification__status">Note:</span>
    At this time, clustering requires the snap installation to use the `--edge`
    channel.
  </p>
</div>

## Control node

On the machine designated as the control node, begin initialisation:

```bash
sudo microstack.init
```

An interactive session will follow. Here is a sample:

```no-highlight
Do you want to setup clustering? (yes/no) [default=no] > yes
2019-10-29 13:32:17,834 - microstack_init - INFO - Configuring clustering ...
What is this machines' role? (control/compute) > control
Please enter a cluster password > *******
Please re-enter password > *******
Please enter the ip address of the control node [default=10.246.114.34] > ENTER
```

You're done. Now wait for the process to finish. It can take between 9 and 15
minutes depending on the resources available on the host system.

Take note of the IP address that was discovered for the local system. You will
need it when it comes time to add a compute node.

<div class="p-notification--information">
  <p class="p-notification__response">
    <span class="p-notification__status">Note:</span>
    The control node must have completed its initialisation phase prior to the
    addition of any compute nodes.
  </p>
</div>

## Compute nodes

On the machine designated as a compute node, begin initialisation:

```bash
sudo microstack.init
```

Like before, an interactive session will follow, but this time the 'compute'
role will be selected:

```no-highlight
Do you want to setup clustering? (yes/no) [default=yes] > yes
2019-10-29 13:43:29,425 - microstack_init - INFO - Configuring clustering ...
What is this machines' role? (control/compute) > compute
Please enter a cluster password > *******
Please re-enter password > *******
Please enter the ip address of the control node [default=10.20.20.1] > 10.246.114.34
Please enter the ip address of this node [default=10.246.114.25] > ENTER
```

The initialisation process for a compute node is much shorter than that of a
control node. It can take as little as 45 seconds.

## Cluster verification

Once the cluster is set up you can perform a verification of it by launching a
test instance based on the CirrOS image. The instance will be created on a
compute node which the control node sees as an availability zone.

The command to use is the same as in the non-clustered case except that option
``--availability-zone`` is added. The name of the AZ is based on the hostname
of the target compute node (here 'node-urey'):

```bash
microstack.launch cirros --name test --availability-zone nova:node-urey
```

The output will provide the instance's floating IP address (here 10.20.20.157).

So to SSH to the instance:

```bash
ssh -i ~/.ssh/id_microstack cirros@10.20.20.157
```


<!-- LINKS -->

[install]: index
