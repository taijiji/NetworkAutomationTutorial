# Vagrant + IOSXRv

# Download IOSXRv
1. get Cisco ID and Key for IOSXRv beta.
  https://xrdocs.github.io/getting-started/steps-download-iosxr-vagrant
1. install vagrant box

```
% mkdir ~/ios-xr-vagrant
% cd ios-xr-vagrant
% BOXURL="https://devhub.cisco.com/artifactory/appdevci-release/XRv64/latest/iosxrv-fullk9-x64.box"
% curl -u YOUR-CCO-ID:YOUR-API-KEY $BOXURL --output ./iosxrv-fullk9-x64.box
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 1690M  100 1690M    0     0  2748k      0  0:10:29  0:10:29 --:--:-- 4876k
```

1. 

```
vagrant box add iosxrv ./iosxrv-fullk9-x64.box
```



# Reference
- https://qiita.com/Mabuchin/items/22992f157f301d63b715


