#!/usr/bin/python
# -*- coding: utf-8 -*-

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# DOCUMENTATION, EXAMPLES, and METAL_PROJECT_ARGS are generated by
# ansible_specdoc. Do not edit them directly.

DOCUMENTATION = ""
EXAMPLES = ""
RETURN = ""

from ansible.module_utils._text import to_native
import traceback

from ansible_collections.equinix.cloud.plugins.module_utils.equinix import (
    EquinixModule,
    get_diff,
    getSpecDocMeta,
)

from ansible_specdoc.objects import (
    SpecField,
    FieldType,
    SpecReturnValue,
)

MUTABLE_ATTRIBUTES = [
    'tags',
    'description',
]

specdoc_examples = [
    """
- name: Create a new reserved IP block in metro "sv"
  hosts: localhost
  tasks:
  - equinix.cloud.metal_reserved_ip_block:
      project_id: 2a5122b9-c323-4d5c-b53c-9ad3f54273e7
      type: public_ipv4
      quantity: 1
      metro: "sv"
""", """
- name: Create a new global reserved IP block (no metro)
  hosts: localhost
  tasks:
  - equinix.cloud.metal_reserved_ip_block:
      project_id: 2a5122b9-c323-4d5c-b53c-9ad3f54273e7
      type: global_ipv4
      quantity: 1
""",
]


result_sample = ['''
{
    "address_family": 4,
    "changed": true,
    "customdata": {},
    "details": "",
    "id": "6d94f567-6cf5-4536-8216-7dc96e1585dd",
    "management": false,
    "metro": "sv",
    "netmask": "255.255.255.255",
    "network": "145.40.67.3",
    "project_id": "fd554070-70b6-420d-b3f8-7ed8438862d5",
    "public": true,
    "quantity": 1,
    "tags": [
        "t1",
        "t2"
    ],
    "type": "public_ipv4"
}
''']

module_spec = dict(
    id=SpecField(
        type=FieldType.string,
        description=['UUID of the reserved IP block'],
    ),
    type=SpecField(
        type=FieldType.string,
        description=['The type of IP address to list'],
        choices=['public_ipv4', 'public_ipv6', 'private_ipv4', 'global_ipv4', 'vrf'],
    ),
    quantity=SpecField(
        type=FieldType.integer,
        description=['The number of IP addresses to reserve'],
    ),
    details=SpecField(
        type=FieldType.string,
        description=['Details about the reserved IP block'],
    ),
    metro=SpecField(
        type=FieldType.string,
        description=['The metro where the reserved IP block will be created'],
    ),
    customdata=SpecField(
        type=FieldType.string,
        description=['Custom data to associate with the reserved IP block'],
    ),
    comments=SpecField(
        type=FieldType.string,
        description=['Comments to associate with the reserved IP block'],
    ),
    vrf_id=SpecField(
        type=FieldType.string,
        description=[
            'The ID of the VRF in which this VRF IP Reservation is created.',
            'The VRF must have an existing IP Range that contains the requested subnet.',
        ],
    ),
    project_id=SpecField(
        type=FieldType.string,
        description=['The ID of the project to which the reserved IP block will be assigned'],
    ),
    tags=SpecField(
        type=FieldType.list,
        description=['Tags to associate with the reserved IP block'],
    ),
)

SPECDOC_META = getSpecDocMeta(
    short_description=(
        "Create/delete blocks of reserved IP addresses in a project."
    ),
    description=(
        "When a user provisions first device in a facility, Equinix "
        "Metal API automatically allocates IPv6/56 and private IPv4/25 "
        "blocks. The new device then gets IPv6 and private IPv4 addresses "
        "from those block. It also gets a public IPv4/31 address. Every new "
        "device in the project and facility will automatically get IPv6 "
        "and private IPv4 addresses from these pre-allocated blocks. The "
        "IPv6 and private IPv4 blocks can't be created, only imported. "
        "With this resource, it's possible to create either public IPv4 "
        "blocks or global IPv4 blocks."

    ),
    examples=specdoc_examples,
    options=module_spec,
    return_values={
        "metal_reserved_ip_block": SpecReturnValue(
            description='The module object',
            type=FieldType.dict,
            sample=result_sample,
        ),
    },
)


def main():
    argument_spec = dict(
        state=dict(type='str', default='present', choices=['present', 'absent']),
        id=dict(type='str'),
        wait_for_state=dict(type='str', choices=['pending', 'created']),

        type=dict(type='str', choices=['global_ipv4', 'public_ipv4', 'vrf']),
        quantity=dict(type='int'),
        details=dict(type='str'),
        metro=dict(type='str'),
        customdata=dict(type='str'),
        comments=dict(type='str'),
        vrf_id=dict(type='str'),
        network=dict(type='str'),
        cidr=dict(type='int'),
    )
    module = EquinixModule(
        # argument_spec=argument_spec,
        argument_spec=SPECDOC_META.ansible_spec,
        required_one_of=[['id', 'project_id']],
        required_by=dict(project_id=['quantity', 'type']),
        required_if=[
            ['type', 'vrf', ['vrf_id', 'cidr', 'network']],
            ['type', 'public_ipv4', ['metro']]
        ],
    )

    state = module.params.get("state")
    changed = False

    try:
        module.params_syntax_check()
        if module.params.get("id"):
            tolerate_not_found = state == "absent"
            fetched = module.get_by_id("metal_ip_reservation", tolerate_not_found)
        else:
            module.params['types'] = [module.params.get('type')]
            fetched = module.get_one_from_list(
                "metal_ip_reservation",
                ["type", "metro"],
            )

        if fetched:
            module.params['id'] = fetched['id']
            if state == "present":
                diff = get_diff(module.params, fetched, MUTABLE_ATTRIBUTES)
                if diff:
                    fetched = module.update_by_id(diff, "metal_ip_reservation")
                    changed = True

            else:
                module.delete_by_id("metal_ip_reservation")
                changed = True
        else:
            if state == "present":
                fetched = module.create("metal_ip_reservation")
                if 'id' not in fetched:
                    module.fail_json(msg="UUID not found in metal_reserved_ip_block creation response")
                changed = True
            else:
                fetched = {}
    except Exception as e:
        tb = traceback.format_exc()
        module.fail_json(msg="Error in metal_reserved_ip_block: {0}".format(to_native(e)),
                         exception=tb)

    fetched.update({'changed': changed})
    module.exit_json(**fetched)


if __name__ == '__main__':
    main()