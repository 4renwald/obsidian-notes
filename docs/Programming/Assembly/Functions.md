
| **Command**                                                       | **Description**               |
| ----------------------------------------------------------------- | ----------------------------- |
| `cat /usr/include/x86_64-linux-gnu/asm/unistd_64.h \| grep write` | Locate `write` syscall number |
| `man -s 2 write`                                                  | `write` syscall man page      |
| `man -s 3 printf`                                                 | `printf` libc man page        |

**Syscall Calling Convention**

1. Save registers to stack
2. Set its syscall number in `rax`
3. Set its arguments in the registers
4. Use the `syscall` assembly instruction to call it

**Function Calling Convention**

1. `Save Registers` on the stack (_`Caller Saved`_)
2. Pass `Function Arguments` (_like syscalls_)
3. Fix `Stack Alignment`
4. Get Function's `Return Value` (_in `rax`_)

**Link external functions**
nasm -f elf64 solution.s &&  ld solution.o -o solution -lc --dynamic-linker /lib64/ld-linux-x86-64.so.2 && ./solution