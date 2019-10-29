---
layout: docs
title: "OpenStack releases"
---

# OpenStack releases

What OpenStack release gets installed by MicroStack can be determined in
advance by issuing the following command:

```bash
snap search microstack
```

The output will display the release. For example, here we see that OpenStack
Stein will be installed:

```no-highlight
Name        Version  Publisher   Notes    Summary
microstack  stein    canonical✓  classic  OpenStack on your laptop
```

There is work underway for more sophisticated OpenStack release management.
