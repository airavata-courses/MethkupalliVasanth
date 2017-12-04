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
 




# Work for Assignment-5, including the openrc.sh file or using vault to encrypt either the .sh file or the cloud.yaml file

To take the credentials directly from the user for using the jetstream(tacc) for openstack, we can use one of the two methods to source the credentials. The first method is to directly source the .sh file downloaded from the API Access from the dashboard. Which is a crude and often unsafe method because it has all the passwords and open to attacks.

Instead we go with using the cloud.yml file mentioned below, a sample included in the main directory. We need to fill the details using openrc.sh file which we download from the API Access.

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


However, after filling the values in the clouds.yaml file we need to use vault for securing it. Following are the commands that need to be run, for encrypting the file, we will be using vault by ansible to achieve that. It has to be remembered that encryption can be performed on few sets of file formats like .yml and .json files only.

This command is used to create an encrypted yml file, which asks for a password interactively. 
`ansible-vault create clouds.yml`

This command is used to run for decrypting the file and using the yml file.  
`ansible-playbook clouds.yml --ask-vault-pass'



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
