# Prepare for IOSXRv
You can get CCO ID and API Key
- https://xrdocs.github.io/getting-started/steps-download-iosxr-vagrant


```
$ BOXURL="https://devhub.cisco.com/artifactory/appdevci-release/XRv64/6.1.2/iosxrv-fullk9-x64.box"

$ curl -u your-cco-id:API-KEY $BOXURL --output ~/iosxrv-fullk9-x64.box

$ vagrant box add --name IOS-XRv ~/iosxrv-fullk9-x64.box
```

# How to build

```
cd NetworkAutomationTutorial/vagrant

$ vagrant init

...


$ vagrant status

Current machine states:

vsrx1                     running (virtualbox)
iosxrv1                   running (virtualbox)

This environment represents multiple VMs. The VMs are all listed
above with their current state. For more information about a specific
VM, run `vagrant status NAME`.
```

# Login router

## vSRX router

```
$ vagrant ssh vsrx1

--- JUNOS 12.1X47-D15.4 built 2014-11-12 02:13:59 UTC

root@vsrx%

root@vsrx% cli

root@vsrx>

root@vsrx> show version
Hostname: vsrx
Model: firefly-perimeter
JUNOS Software Release [12.1X47-D15.4]
```

## IOSXRv router
```
ssh -p 2223 vagrant@localhost

Password: vagrant # default

RP/0/RP0/CPU0:ios#

RP/0/RP0/CPU0:ios#show version
Tue Jan 16 19:34:36.098 UTC

Cisco IOS XR Software, Version 6.2.1.23I
Copyright (c) 2013-2016 by Cisco Systems, Inc.

Build Information:
 Built By     : jwu
 Built On     : Mon Nov 21 00:33:58 PST 2016
 Build Host   : iox-ucs-005
 Workspace    : /auto/iox-ucs-005-san1/nightly/xr-dev_16.11.20C/iosxrv-x64
 Version      : 6.2.1.23I
 Location     : /opt/cisco/XR/packages/

cisco IOS XRv x64 () processor
System uptime is 8 minutes
```

# Reference
## English article
- [XR toolbox, Part 1 : IOS-XR Vagrant Quick Start](https://xrdocs.github.io/application-hosting/tutorials/iosxr-vagrant-quickstart)

## Japanese article
- [Vagrantでfireflyを動かしたら自動化開発が捗った話](https://qiita.com/taijijiji/items/501a4d671106240fbd2c)
- [IOS-XRv Vagrantを試してみた](https://qiita.com/Mabuchin/items/22992f157f301d63b715)