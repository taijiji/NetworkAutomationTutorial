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

root@vsrx> 
root@vsrx> show interfaces terse
Interface               Admin Link Proto    Local                 Remote
ge-0/0/0                up    up
ge-0/0/0.0              up    up   inet     10.0.2.15/24
gr-0/0/0                up    up
ip-0/0/0                up    up
lsq-0/0/0               up    up
lt-0/0/0                up    up
mt-0/0/0                up    up
sp-0/0/0                up    up
sp-0/0/0.0              up    up   inet
                                   inet6
sp-0/0/0.16383          up    up   inet     10.0.0.1            --> 10.0.0.16
                                            10.0.0.6            --> 0/0
                                            128.0.0.1           --> 128.0.1.16
                                            128.0.0.6           --> 0/0
ge-0/0/1                up    up
ge-0/0/1.0              up    up   inet     10.0.1.1/24
dsc                     up    up
gre                     up    up
ipip                    up    up
irb                     up    up
lo0                     up    up
lo0.16384               up    up   inet     127.0.0.1           --> 0/0
lo0.16385               up    up   inet     10.0.0.1            --> 0/0
                                            10.0.0.16           --> 0/0
                                            128.0.0.1           --> 0/0
                                            128.0.0.4           --> 0/0
                                            128.0.1.16          --> 0/0
lo0.32768               up    up
lsi                     up    up
mtun                    up    up
pimd                    up    up
pime                    up    up
pp0                     up    up
ppd0                    up    up
ppe0                    up    up
st0                     up    up
tap                     up    up
vlan                    up    down
```

## IOSXRv router
```
$ ssh -p 2223 vagrant@localhost

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


RP/0/RP0/CPU0:ios#
RP/0/RP0/CPU0:ios#show ipv4 interface brief

Tue Jan 16 19:49:58.980 UTC

Interface                      IP-Address      Status          Protocol Vrf-Name
GigabitEthernet0/0/0/0         unassigned      Shutdown        Down     default
MgmtEth0/RP0/CPU0/0            10.0.2.15       Up              Up       default
```

# add configuration for general use

## vSRX

```
edit

set system root-authentication plain-text-password
set system login user user1 class super-user
set system login user user1 authentication plain-text-password

set security zones security-zone trust interfaces ge-0/0/1
set security zones security-zone trust interfaces ge-0/0/1.0 host-inbound-traffic system-services all
set system time-zone Asia/Tokyo

set system services netconf ssh

delete security policies
set security forwarding-options family mpls mode packet-based
set security forwarding-options family inet6 mode packet-based
```


# Reference
## English article
- [XR toolbox, Part 1 : IOS-XR Vagrant Quick Start](https://xrdocs.github.io/application-hosting/tutorials/iosxr-vagrant-quickstart)

## Japanese article
- [Vagrantでfireflyを動かしたら自動化開発が捗った話](https://qiita.com/taijijiji/items/501a4d671106240fbd2c)
- [IOS-XRv Vagrantを試してみた](https://qiita.com/Mabuchin/items/22992f157f301d63b715)