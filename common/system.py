from common.exceptions import NotAllowMachineType

SYSTEM_DISALLOW_CHARS = {
    'WINDOWS': []
}


def _add_system_disallow_chars(machine: str, char: str, replace: str):
    if machine not in SYSTEM_DISALLOW_CHARS.keys():
        raise NotAllowMachineType(f'Machine "{machine}" is disallowed.')

    SYSTEM_DISALLOW_CHARS[machine].append({'char': char, 'replace': replace})


_add_system_disallow_chars('WINDOWS', '*', '_MULTIPLY_')
_add_system_disallow_chars('WINDOWS', '/', '_')
_add_system_disallow_chars('WINDOWS', '\\', '_')
_add_system_disallow_chars('WINDOWS', ':', '_')
_add_system_disallow_chars('WINDOWS', '?', '_')
_add_system_disallow_chars('WINDOWS', '"', '_')
_add_system_disallow_chars('WINDOWS', '>', '_LARGER_')
_add_system_disallow_chars('WINDOWS', '<', '_LESS_')
_add_system_disallow_chars('WINDOWS', '|', '_')
