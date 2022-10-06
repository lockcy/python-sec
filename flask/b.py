import pickle
import sys
# import secret
#
# print("secret变量的值为:" + secret.secret_key)
# opcode = b'''c__main__
# secret
# (S'secret_key'
# S'Hack!!!'
# db.'''
# fake = pickle.loads(opcode)
#
# print("secret变量的值为:" + fake.secret_key)

for i in sys.modules:
    print(i)

import marshal
import builtins

a = getattr(builtins, "eval")
print(a("2+2"))

# print(getattr(sys.modules["os"], "system"))
# print(getattr(sys.modules[chr(111)+"s"], "system"))
# import nt
# nt.system("calc")