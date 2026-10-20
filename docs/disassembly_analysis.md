# Disassembly Analysis

The assembly code implements a loop that calculates the sum of numbers from 1 to 10.

## Reconstructed Python Code

```python
acc = 0      # -4(%rbp)
i = 1        # -8(%rbp)

while i <= 10:   # .L2: cmpl $10, -8(%rbp); jle .L3
    acc += i     # .L3: movl -8(%rbp), %eax; addl %eax, -4(%rbp)
    i += 1       # addl $1, -8(%rbp)

# The result (sum) is now in acc (eax)
