# Jetstream Machine Ansible playbooks

## Full airavata stack

NOTE: These will currently fail in this repo as-cloned!

NORE: ssh.cfg will point to the wrong ssh key!

TWO THINGS ARE MISSING:
1. A working clouds.yaml file (see below in the single-server instance).
2. A copy of *all* the roles from airvata/dev-tools/ansible/roles

The playbook `all_build.yml` should build a complete stack of airavata servers.

Currently, it depends on Jetstream (an OpenStack cloud service), both creating VMs and deploying software to them.

Call it via: `ansible-playbook -i inventory all_build.yml`

Testing is still needed to be sure that this creates a complete, working stack!

The configuration is still off - creating a new user in the PGA, for example, sends a user request to testdrive.airavata.org...

##Single Machine Example:

This is currently a simple set of playbooks to create a single virtual machine in Jetstream.
You will probably have to install the shade libraries.

It should work via

`ansible-playbook pga_host.yml`

This will both initialize a private network, with public router, 
and create a new instance based on a 'm1.small' image.
 
I don't have the file 'clouds.yaml' included in this public repo, which is a necessity. 

It is equivalent to the openrc.sh - may be included later as a vault.

The basic format looks like:

```
clouds:
 tacc:
  auth: 
   username: value
   auth_url: value
   project_name: value
   password: value 
  user_domain_name: value
  project_domain_name: value
  identity_api_version: 3
```

Now with dynamic inventory (openstack.py).

The variables and hosts have been pulled from the main set of 
ansible playbooks in 

airavata/dev-tools/ansible

because some of the pga-config depends on other hosts. 

As more per-host playbooks are added, these can be removed. 

The pga role was also directly copied from the main ansible script 
location, to demonstrate a single-command build of the pga from
absolute scratch,  with dynamic inventory.
No more manual instance creation!

The complete build can be run via:
`ansible-playbook -i inventory pga_build.yml`
