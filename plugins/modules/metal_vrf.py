#!/usr/bin/python
# -*- coding: utf-8 -*-

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# DOCUMENTATION, EXAMPLES, and RETURN are generated by
# ansible_specdoc. Do not edit them directly.

DOCUMENTATION = '''
author: Equinix DevRel Team (@equinix) <support@equinix.com>
description: Create a VRF in a metro, with IP ranges that you want the VRF to route
  and forward.
module: metal_vrf
notes: []
options:
  description:
    description:
    - Description of the VRF.
    required: false
    type: str
  id:
    description:
    - UUID of the VRF.
    required: false
    type: str
  ip_ranges:
    description:
    - All IPv4 and IPv6 Ranges that will be available to BGP Peers. IPv4 addresses
      must be /8 or smaller with a minimum size of /29. IPv6 must be /56 or smaller
      with a minimum size of /64. Ranges must not overlap other ranges within the
      VRF.
    required: false
    type: list
  local_asn:
    description:
    - The 4-byte ASN set on the VRF.
    required: false
    type: int
  metro:
    description:
    - Metro ID or Code where the VRF will be deployed.
    required: false
    type: str
  name:
    description:
    - User-supplied name of the VRF, unique to the project.
    required: false
    type: str
  project_id:
    description:
    - Project ID where the VRF will be deployed.
    required: false
    type: str
requirements: null
short_description: Manage a VRF resource in Equinix Metal
'''
EXAMPLES = '''
- name: Create new Equinix Metal VRF
  hosts: localhost
  tasks:
  - equinix.cloud.metal_vrf:
      name: example-vrf
      description: VRF with ASN 65000 and a pool of address space that includes 192.168.100.0/25
      metro: da
      local_asn: 65000
      ip_ranges:
      - 192.168.100.0/25
      - 192.168.200.0/25
      project_id: your_project_id_here
'''
RETURN = '''
metal_vrf:
  description: The module object
  returned: always
  sample:
  - "\n{\n    \"changed\": false,\n    \"description\": \"Test VRF with ASN 65000\"\
    ,\n    \"id\": \"f4a7863c-fcbf-419c-802c-3c6d3ad9529e\",\n    \"ip_ranges\": [\n\
    \        \"192.168.100.0/25\",\n        \"192.168.200.0/25\"\n    ],\n    \"local_asn\"\
    : 65000,\n    \"metro\": {\n        \"href\": \"/metal/v1/locations/metros/108b2cfb-246b-45e3-885a-bf3e82fce1a0\"\
    ,\n        \"id\": \"108b2cfb-246b-45e3-885a-bf3e82fce1a0\"\n    },\n    \"name\"\
    : \"ansible-integration-test-vrf-6yww6pyz\",\n    \"project_id\": \"9934e474-04a1-46a3-842b-5f3dc0ed0eba\"\
    \n}\n"
  type: dict
'''

# End of generated documentation


from ansible.module_utils._text import to_native
from ansible_specdoc.objects import (
    SpecField,
    FieldType,
    SpecReturnValue,
)
import traceback

from ansible_collections.equinix.cloud.plugins.module_utils.equinix import (
    EquinixModule,
    get_diff,
    getSpecDocMeta,
)


module_spec = dict(
    id=SpecField(
        type=FieldType.string,
        description="UUID of the VRF.",
        required=False,
    ),
    description=SpecField(
        type=FieldType.string,
        description=['Description of the VRF.'],
        required=False,
    ),
    name=SpecField(
        type=FieldType.string,
        description=['User-supplied name of the VRF, unique to the project.'],
    ),
    metro=SpecField(
        type=FieldType.string,
        description=['Metro ID or Code where the VRF will be deployed.'],
    ),
    local_asn=SpecField(
        type=FieldType.integer,
        description=['The 4-byte ASN set on the VRF.'],
        required=False,
        editable=True,
    ),
    ip_ranges=SpecField(
        type=FieldType.list,
        description=[
            'All IPv4 and IPv6 Ranges that will be available to BGP Peers. '
            'IPv4 addresses must be /8 or smaller with a minimum size of /29. '
            'IPv6 must be /56 or smaller with a minimum size of /64. '
            'Ranges must not overlap other ranges within the VRF.'
        ],
        required=False,
        editable=True,
    ),
    project_id=SpecField(
        type=FieldType.string,
        description=['Project ID where the VRF will be deployed.'],
    ),
)


specdoc_examples = [
    '''
- name: Create new Equinix Metal VRF
  hosts: localhost
  tasks:
    - equinix.cloud.metal_vrf:
        name: "example-vrf"
        description: "VRF with ASN 65000 and a pool of address space that includes 192.168.100.0/25"
        metro: "da"
        local_asn: 65000
        ip_ranges:
          - "192.168.100.0/25"
          - "192.168.200.0/25"
        project_id: "your_project_id_here"
''',
]

result_sample = ['''
{
    "changed": false,
    "description": "Test VRF with ASN 65000",
    "id": "f4a7863c-fcbf-419c-802c-3c6d3ad9529e",
    "ip_ranges": [
        "192.168.100.0/25",
        "192.168.200.0/25"
    ],
    "local_asn": 65000,
    "metro": {
        "href": "/metal/v1/locations/metros/108b2cfb-246b-45e3-885a-bf3e82fce1a0",
        "id": "108b2cfb-246b-45e3-885a-bf3e82fce1a0"
    },
    "name": "ansible-integration-test-vrf-6yww6pyz",
    "project_id": "9934e474-04a1-46a3-842b-5f3dc0ed0eba"
}
''']

MUTABLE_ATTRIBUTES = [
    k for k, v in module_spec.items() if v.editable
]

SPECDOC_META = getSpecDocMeta(
    short_description='Manage a VRF resource in Equinix Metal',
    description=(
        'Create a VRF in a metro, with IP ranges that you want the VRF to route and forward.'
    ),
    examples=specdoc_examples,
    options=module_spec,
    return_values={
        "metal_vrf": SpecReturnValue(
            description='The module object',
            type=FieldType.dict,
            sample=result_sample,
        ),
    },
)


def main():
    module = EquinixModule(
        argument_spec=SPECDOC_META.ansible_spec,
        required_one_of=[("name", "id")],
    )

    state = module.params.get("state")
    changed = False

    try:
        module.params_syntax_check()

        state = module.params.get("state")

        if module.params.get("id"):
            tolerate_not_found = state == "absent"
            fetched = module.get_by_id("metal_vrf", tolerate_not_found)
        else:
            fetched = module.get_one_from_list(
                "metal_vrf",
                ["name"],
            )

        if fetched:
            module.params['id'] = fetched['id']
            if state == "present":
                diff = get_diff(module.params, fetched, MUTABLE_ATTRIBUTES)
                if diff:
                    fetched = module.update_by_id(diff, "metal_vrf")
                    changed = True

            else:
                module.delete_by_id("metal_vrf")
                changed = True
        else:
            if state == "present":
                fetched = module.create("metal_vrf")
                if 'id' not in fetched:
                    module.fail_json(msg="UUID not found in resource creation response")
                changed = True
            else:
                fetched = {}
    except Exception as e:
        tb = traceback.format_exc()
        module.fail_json(msg="Error in metal_vrf: {0}".format(to_native(e)),
                         exception=tb)

    fetched.update({'changed': changed})
    module.exit_json(**fetched)


if __name__ == '__main__':
    main()
