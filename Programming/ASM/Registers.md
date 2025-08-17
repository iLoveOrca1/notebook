Aight, I ain't gonna waste your time. Here's the cheatsheet:

| Register | Typical Use         | Think of it as...          |
| -------- | ------------------- | -------------------------- |
| `EAX`    | Main math/storage   | Calculator result box      |
| `EBX`    | Index or base       | Extra pocket               |
| `ECX`    | Loop counter        | Countdown timer            |
| `EDX`    | Math partner        | Second calculator box      |
| `ESP`    | Stack top           | Hand holding the top plate |
| `EBP`    | Stack base          | Marker in the stack        |
| `ESI`    | Source address      | Address where we read from |
| `EDI`    | Destination address | Address where we write to  |


# Registers

Registers are a small memory or a storage inside your **CPU** who works super fast. Think of it like a quick pocket that your cpu use to keep some important stuff while it's working.

The Intel registers are broken down in several categories. They include 
- General registers
- Segment registers
- Index/Pointer registers 
- Flags registers

# General Register

In general register when using a 64 bit processor, the register starts with the letter R. In 32 bit, it starts with the letter E. And in 16 bit processor, it doesn't have any prefix with only two letter. 

| REG | Bits   |
| :-- | :----- |
| RAX | 64 Bit |
| EAX | 32 Bit |
| AX  | 16 Bit |

Here Above are the example

The prefix just means that the register can hold up to their respective size. In 64 architecture a 16 bit register may still be appear but not the other way around.

# Types of General Register

| Registers   | 64-Bit | 32-Bit | 16-Bit | 8-Bit H/L |
| :---------- | ------ | ------ | ------ | --------- |
| Accumulator | `RAX`  | `EAX`  | `AX`   | `AH/AL`   |
| Counter     | `RCX`  | `ECX`  | `CX`   | `CH/CL`   |
| Data        | `RDX`  | `EDX`  | `DX`   | `DH/DL`   |
| Base        | `RBX`  | `EBX`  | `BX`   | `BH/BL`   |

> Note: These are the actual order so its not abcd but acdb

---

- **Accumulator register**
	It is usually used to place the return value of a function but can be used for other purposes. Often used for **calculations** and storing **results.**

- **Counter register**
	Used to **count** things. Especially useful in **loops** (e.g., "do this 5 times").

- **Data register**
	Usually used to store temporary data in operations. Often holds data related to `EAX`. Sometimes used in division or I/O operations.

- **Base register**
	Used as the base pointer for **memory access**. We subtract or add an offset to the value of this register to access variables. Can be used for anything, but often used for indexing or storing base addresses.




# 🧭 Pointer Register

These registers are used to mark the end or start of a region of memory to allow a program keeping track of elements such as location of variables or the top of the stack, which are essential to manipulate data in memory.

| Pointers          | 64-Bit | 32-Bit | 16-Bit |
| :---------------- | ------ | ------ | ------ |
| Stack             | `RSP`  | `ESP`  | `SP`   |
| Instruction       | `RIP`  | `EIP`  | `IIP`  |
| Base              | `RBP`  | `EBP`  | `BP`   |
| Source Index      | `RSI`  | `ESI`  | `SI`   |
| Destination Index | `RDI`  | `EDI`  | `DI`   |


- **Stack Pointer**
	Points to the **top of the stack**, like the last plate in a stack of dishes. Used for function calls.
	
	Whenever we create a local variable, this pointer changes to allow space to that variable. For example, if we create an variable that takes 4 bytes, the stack pointer moves 4 bytes to make room for that new variable.

- **Instruction Pointer**
	Indicates the current instruction that the program is executing. If we make this register pointing to an address, the program will execute the code at that address.

- **Base Pointer**
	Indicates the beginning of the stack frame of a function. The stack frame is a region of memory in which we place data, such as local variables, from a specific function. To access a local variable from a function, we take the address of the base pointer and subtract an offset.

- **Destination Index**
	Generally used for copying chunks of memory, that can be strings or arrays.

- **Source Index**
	Similar purpose to the previous register (Destination index register).