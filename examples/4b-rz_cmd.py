"""
SPDX-FileCopyrightText: 2022 wingdeans <wingdeans@protonmail.com>
SPDX-License-Identifier: LGPL-3.0-only
"""

import rizin

core = rizin.core or rizin.RzCore()

def say_hello():
    print("hello from python")
    return True
core.register_group("u", "A custom group for user-defined commands")
core.register_command("uh", say_hello)

def print_function_info(fn: rizin.RzAnalysisFunction):
    print("name:", fn.name)
    print("number of xrefs from:", fn.get_xrefs_from().length())
    print("number of xrefs to:", fn.get_xrefs_to().length())
    return True
core.register_command("uf", print_function_info)

core.prompt_loop()
