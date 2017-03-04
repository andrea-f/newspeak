import re
from typing import List


def gen_regexp(reg_type: str, members: List[str]) -> str:
    members_joined = '|'.join(members)
    reg_types = {
        'exact': '^(%s)$',
        'prefix': '^(%s)\w+',
        'suffix': '\w+(%s)$',
    }
    if not reg_type in reg_types:
        raise ValueError("No such type %s" % reg_type)

    return re.compile(reg_types[reg_type] % members_joined)

