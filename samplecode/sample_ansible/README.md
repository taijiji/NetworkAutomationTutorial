# Prepare
```
pip3 install ansible
```

For junos
```
pip3 install junos-eznc
ansible-galaxy install Juniper.junos
```

# result

```
$ ansible-playbook -i hosts junos_show_1.yaml

PLAY [vsrx1] ********************************************************************************************************************************

TASK [Get basic information] ****************************************************************************************************************
ok: [192.168.33.3]

TASK [show model name] **********************************************************************************************************************
ok: [192.168.33.3] => {
    "ansible_net_model": "firefly-perimeter"
}

TASK [show serial number] ****************


***************************************************************************************************
ok: [192.168.33.3] => {
    "ansible_net_serialnum": "83f144ddd4f7"
}

TASK [show version] *************************************************************************************************************************
ok: [192.168.33.3] => {
    "ansible_net_version": null
}

PLAY RECAP **********************************************************************************************************************************
192.168.33.3               : ok=4    changed=0    unreachable=0    failed=0
```

```
$ ansible-playbook -i hosts junos_show_2.yaml

PLAY [vsrx1] ********************************************************************************************************************************

TASK [send command "show version"] **********************************************************************************************************
ok: [192.168.33.3]

TASK [show result of "show version"] ********************************************************************************************************
ok: [192.168.33.3] => {
    "result.stdout_lines": [
        [
            "Hostname: vsrx",
            "Model: firefly-perimeter",
            "JUNOS Software Release [12.1X47-D15.4]"
        ]
    ]
}

PLAY RECAP **********************************************************************************************************************************
192.168.33.3               : ok=2    changed=0    unreachable=0    failed=0
```


# Reference
- http://docs.ansible.com/ansible/latest/junos_facts_module.html#return-values
# junos_get_facts vs junos_facts?
- junos_get_facts
    - http://junos-ansible-modules.readthedocs.io/en/1.3.1/junos_get_facts.html
- junos_facts
    - http://docs.ansible.com/ansible/latest/junos_facts_module.html
    - http://junos-ansible-modules.readthedocs.io/en/2.0.1/juniper_junos_facts.html