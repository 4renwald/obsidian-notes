
| **Instruction**                     | **Description**                                                                             | **Example**                                             |
| ----------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| **Data Movement**                   |                                                                                             |                                                         |
| `mov`                               | Move data or load immediate data                                                            | `mov rax, 1` -> `rax = 1`                               |
| `lea`                               | Load an address pointing to the value                                                       | `lea rax, [rsp+5]` -> `rax = rsp+5`                     |
| `xchg`                              | Swap data between two registers or addresses                                                | `xchg rax, rbx` -> `rax = rbx, rbx = rax`               |
| **Unary Arithmetic Instructions**   |                                                                                             |                                                         |
| `inc`                               | Increment by 1                                                                              | `inc rax` -> `rax++` or `rax += 1` -> `rax = 2`         |
| `dec`                               | Decrement by 1                                                                              | `dec rax` -> `rax--` or `rax -= 1` -> `rax = 0`         |
| **Binary Arithmetic Instructions**  |                                                                                             |                                                         |
| `add`                               | Add both operands                                                                           | `add rax, rbx` -> `rax = 1 + 1` -> `2`                  |
| `sub`                               | Subtract Source from Destination (_i.e `rax = rax - rbx`_)                                  | `sub rax, rbx` -> `rax = 1 - 1` -> `0`                  |
| `imul`                              | Multiply both operands                                                                      | `imul rax, rbx` -> `rax = 1 * 1` -> `1`                 |
| **Bitwise Arithmetic Instructions** |                                                                                             |                                                         |
| `not`                               | Bitwise NOT (_invert all bits, 0->1 and 1->0_)                                              | `not rax` -> `NOT 00000001` -> `11111110`               |
| `and`                               | Bitwise AND (_if both bits are 1 -> 1, if bits are different -> 0_)                         | `and rax, rbx` -> `00000001 AND 00000010` -> `00000000` |
| `or`                                | Bitwise OR (_if either bit is 1 -> 1, if both are 0 -> 0_)                                  | `or rax, rbx` -> `00000001 OR 00000010` -> `00000011`   |
| `xor`                               | Bitwise XOR (_if bits are the same -> 0, if bits are different -> 1_)                       | `xor rax, rbx` -> `00000001 XOR 00000010` -> `00000011` |
| **Loops**                           |                                                                                             |                                                         |
| `mov rcx, x`                        | Sets loop (`rcx`) counter to `x`                                                            | `mov rcx, 3`                                            |
| `loop`                              | Jumps back to the start of `loop` until counter reaches `0`                                 | `loop exampleLoop`                                      |
| **Branching**                       |                                                                                             |                                                         |
| `jmp`                               | Jumps to specified label, address, or location                                              | `jmp loop`                                              |
| `jz`                                | Destination **equal to Zero**                                                               | `D = 0`                                                 |
| `jnz`                               | Destination **Not equal to Zero**                                                           | `D != 0`                                                |
| `js`                                | Destination **is Negative**                                                                 | `D < 0`                                                 |
| `jns`                               | Destination **is Not Negative** (i.e. 0 or positive)                                        | `D >= 0`                                                |
| `jg`                                | Destination **Greater than** Source                                                         | `D > S`                                                 |
| `jge`                               | Destination **Greater than or Equal** Source                                                | `D >= S`                                                |
| `jl`                                | Destination **Less than** Source                                                            | `D < S`                                                 |
| `jle`                               | Destination **Less than or Equal** Source                                                   | `D <= S`                                                |
| `cmp`                               | Sets `RFLAGS` by subtracting second operand from first operand (_i.e. first - second_)      | `cmp rax, rbx` -> `rax - rbx`                           |
| **Stack**                           |                                                                                             |                                                         |
| `push`                              | Copies the specified register/address to the top of the stack                               | `push rax`                                              |
| `pop`                               | Moves the item at the top of the stack to the specified register/address                    | `pop rax`                                               |
| **Functions**                       |                                                                                             |                                                         |
| `call`                              | push the next instruction pointer `rip` to the stack, then jumps to the specified procedure | `call printMessage`                                     |
| `ret`                               | pop the address at `rsp` into `rip`, then jump to it                                        | `ret`                                                   |
