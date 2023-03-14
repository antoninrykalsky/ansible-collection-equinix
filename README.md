# Equinix Ansible Collection
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-equinix.cloud-660198.svg?style=flat)](https://galaxy.ansible.com/equinix/cloud/) 
![Tests](https://img.shields.io/github/actions/workflow/status/equinix-labs/ansible-collection-equinix/integration-tests.yml?branch=main)

The Ansible Collection Equinix contains various plugins for managing Equinix services.

<!--start requires_ansible-->
## Ansible version compatibility

This collection has been tested against following Ansible version **6.7.0**, core version **2.13.8**.

Plugins and modules within a collection may be tested with only specific Ansible versions.
A collection may contain metadata that identifies these versions.
PEP440 is the schema used to describe the versions of Ansible.
<!--end requires_ansible-->

<!--start collection content-->
### Modules

Modules for managing Equinix infrastructure.

Name | Description |
--- | ------------ |
[equinix.cloud.metal_device](./docs/modules/metal_device.md)|Create, update, or delete Equinix Metal devices|
[equinix.cloud.metal_ip_assignment](./docs/modules/metal_ip_assignment.md)|Manage Equinix Metal IP assignments|
[equinix.cloud.metal_project](./docs/modules/metal_project.md)|Manage Projects in Equinix Metal|
[equinix.cloud.metal_reserved_ip_block](./docs/modules/metal_reserved_ip_block.md)|Create/delete blocks of reserved IP addresses in a project.|


### Info Modules

Modules for retrieving information about existing Equinix infrastructure.

Name | Description |
--- | ------------ |
[equinix.cloud.metal_available_ips_info](./docs/modules/metal_available_ips_info.md)|Get list of avialable IP addresses from a reserved IP block|
[equinix.cloud.metal_device_info](./docs/modules/metal_device_info.md)|Select list of Equinix Metal devices|
[equinix.cloud.metal_ip_assignment_info](./docs/modules/metal_ip_assignment_info.md)|Gather IP address assignments for a device|
[equinix.cloud.metal_project_info](./docs/modules/metal_project_info.md)|Gather information about Equinix Metal projects|
[equinix.cloud.metal_reserved_ip_block_info](./docs/modules/metal_reserved_ip_block_info.md)|Gather list of reserved IP blocks|


### Inventory Plugins

Dynamically add Equinix infrastructure to an Ansible inventory.

Name |
--- |
[equinix.cloud.metal_device](./docs/inventory/metal_device.md)|


<!--end collection content-->

## Installation

You can install the Equinix collection with the Ansible Galaxy CLI:

```shell
ansible-galaxy collection install equinix.cloud
```

The Python module dependencies are not installed by `ansible-galaxy`.  They can
be manually installed using pip:

```shell
pip install -r https://raw.githubusercontent.com/equinix-labs/ansible-collection-equinix/main/requirements.txt
```

## Usage
Once the Equinix Ansible collection is installed, it can be referenced by its [Fully Qualified Collection Namespace (FQCN)](https://github.com/ansible-collections/overview#terminology): `equinix.cloud.module_name`.

In order to use this collection, you should have account in the relevant Equinix service. For example you should have an account Equinix Metal to use the `metal_*` plugins.

You can authenticate either by exporting auth tokens as environment variables, or by supplying `*_api_token` attributes to modules. For example, to use `metal_device`, you can export `METAL_AUTH_TOKEN` (or `METAL_API_TOKEN`), or you can supply `metal_auth_token` attribute.

#### Example Playbook
```yaml
---
- name: create Equinix Metal device
  hosts: localhost
  tasks:
    - equinix.cloud.metal_device:
        project_id: "3b516842-c8b1-485e-9f76-c891bd804c5e"
        hostname: "my new device"
        operating_system: ubuntu_20_04
        plan: c3.small.x86
        metro: sv
```

For more information on Ansible collection usage, see [Ansible's official usage guide](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html).

## Examples

Use-case examples for this collection can be found [here](./examples/README.md).

## Licensing

GNU General Public License v3.0.

See [COPYING](COPYING) to see the full text.