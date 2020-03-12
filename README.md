# Openstack workload monitoring tool
## Description
This solution allows to prepare test workload within environment and monitor instances availability during scheduled operations such as ceph or contrail upgrades.

By default ansible playbook creates one basic monitor VM that has prometheus, alertmanager and alerta as docker compose services at the top of itself. In addition it generates dedicated count of dummy VMs with prometheus exporter that used as monitoring goals to check the instances availability.

![Architecture diagram](docs/architecture_diagram.png?raw=true "Architecture diagram")

## Installation
### Install pip requirements
```sh
# git clone https://github.com/dpovolotskiy/openstack-workload-monitoring
# cd openstack-workload-monitoring
# virtualenv .venv
# . .venv/bin/activate
# pip install -r requirements.txt

```
### Prepare clouds.yaml
You need to fill up and put `clouds.yaml` file to root project folder. Content example:
```yaml
clouds:
  devstack:
    auth:
      auth_url: http://192.168.122.10:35357/
      project_name: demo
      username: demo
      password: 0penstack
    region_name: RegionOne
  ds-admin:
    auth:
      auth_url: http://192.168.122.10:35357/
      project_name: admin
      username: admin
      password: 0penstack
    region_name: RegionOne
  infra:
    cloud: rackspace
    auth:
      project_id: 275610
      username: openstack
      password: xyzpdq!lazydog
    region_name: DFW,ORD,IAD
    interface: internal
```
More information about `clouds.yaml` you may find in the [official documentation]( https://docs.openstack.org/python-openstackclient/pike/configuration/index.html).

### Prepare images
You need to generate master/slave images and upload it to cloud.
```sh
# ./diskimage-builder/build-master-image.sh
# ./diskimage-builder/build-slave-image.sh
```
When the generation is finished, the images will be available in the following path **diskimage-builder/images/**.

### Set up variables for roles


## Usage
From root project folder execute:
```sh
# ansible-playbook -i hosts main.yaml
```
