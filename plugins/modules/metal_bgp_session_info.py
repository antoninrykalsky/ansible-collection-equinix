#!/usr/bin/python
# -*- coding: utf-8 -*-

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# DOCUMENTATION, EXAMPLES, and RETURN are generated by
# ansible_specdoc. Do not edit them directly.

DOCUMENTATION = '''
author: Equinix DevRel Team (@equinix) <support@equinix.com>
description: Gather information about Equinix Metal resources
module: metal_bgp_session_info
notes: []
options:
  device_id:
    description:
    - ID of the device to which the BGP session belongs
    required: false
    type: str
  project_id:
    description:
    - ID of project to which BGP session belongs
    required: false
    type: str
requirements: null
short_description: Gather information about BGP session
'''
EXAMPLES = '''
- name: Gather information about all resources in parent resource
  hosts: localhost
  tasks:
  - equinix.cloud.metal_resource_info:
      parent_resource_id: 2a5122b9-c323-4d5c-b53c-9ad3f54273e7
'''
RETURN = '''
resources:
  description: Found resources
  returned: always
  sample:
  - "[\n  {\n    \"address_family\": \"ipv6\",\n    \"default_route\": true,\n   \
    \ \"device_id\": \"b068984f-f7d9-43a2-aa45-de04dcf4fe06\",\n    \"id\": \"03912bd6-a158-47ad-8bc7-c93df338fe0d\"\
    \n  }\n]"
  type: dict
'''

# End

from ansible.module_utils._text import to_native
from ansible_specdoc.objects import SpecField, FieldType, SpecReturnValue
import traceback

from ansible_collections.equinix.cloud.plugins.module_utils.equinix import (
    EquinixModule,
    getSpecDocMeta,
)

module_spec = dict(
    device_id=SpecField(
        type=FieldType.string,
        description=['Find BGP sessions by device ID.'],
    ),
    project_id=SpecField(
        type=FieldType.string,
        description=['Find BGP sessions by project ID.'],
    ),
)

specdoc_examples = ['''
- name: Gather information about all BGP sessions in a project
  hosts: localhost
  tasks:
      - equinix.cloud.metal_resource_info:
          parent_resource_id: 2a5122b9-c323-4d5c-b53c-9ad3f54273e7
''', '''
''',
                    ]

result_sample = ['''[
  {
    "address_family": "ipv6",
    "default_route": true,
    "device_id": "b068984f-f7d9-43a2-aa45-de04dcf4fe06",
    "id": "03912bd6-a158-47ad-8bc7-c93df338fe0d"
  }
]''',
]

SPECDOC_META = getSpecDocMeta(
    short_description="Gather information BGP sessions in Equinix Metal",
    description=(
        'Gather information BGP sessions in Equinix Metal. You can fetch it by device ID or project ID.'
    ),
    examples=specdoc_examples,
    options=module_spec,
    return_values={
        "resources": SpecReturnValue(
            description='Found resources',
            type=FieldType.dict,
            sample=result_sample,
        ),
    },
)


def main():
    module = EquinixModule(
        argument_spec=SPECDOC_META.ansible_spec,
        is_info=True,
    )
    try:
        module.params_syntax_check()

        if 'project_id' in module.params:
            return_value = {'resources': module.get_list("metal_bgp_session_by_project")}
        else:
            return_value = {'resources': module.get_list("metal_bgp_session")}

    except Exception as e:
        tr = traceback.format_exc()
        module.fail_json(msg=to_native(e), exception=tr)
    module.exit_json(**return_value)


if __name__ == '__main__':
    main()
