# Statements
The heart of any assembly language program are statements. A typical statement in Assembly has the form:

| Label:   | Mnemonic                                    | Operands     | ;comments |
| :------- | ------------------------------------------- | ------------ | --------- |
| Optional | Opcode name or directive name or macro name | zero or more | optional  |

# The Directions 

| Syntax | Format                | Example          | Direction     | Notes                             |
| :----- | --------------------- | ---------------- | ------------- | --------------------------------- |
| AT&T   | `source, destination` | `mov %rsp, %rbp` | `%rsp → %rbp` | Default on most Linux distros     |
| Intel  | `destination, source` | `mov rsp, rbp`   | `rsp ← rbp`   | Preferred on Windows / in IDA Pro |

The direction may vary depending on what syntax does the program use. For example linux toolchain like gdb, gcc, and as may use **AT&T** syntax from **left to right** while some IDE like VsCode and nasm may use **intel** syntax from **right to left.** 

> **the syntax flavour is purely visual.** It does **not** change the actual behavior, execution, or meaning of the code.

Example:
#### AT&T

```
mov %ebx, %ecx
```
#### Intel

```
mov ecx, ebx 
```

Both of these codes copies the contents of register EBX into register ECX.

### Pro tip

> You could actually change the disassembler syntax flavor in most program. for example in gdb, you can change the syntax by typing.

```
# Change flavor to Intel
(gdb) set disassembly-flavor intel

# Change flavor to AT&T
(gdb) set disassembly-flavor att

# Making it persist
$ echo "set disassembly-flavor intel" >> ~/.gdbinit
```
