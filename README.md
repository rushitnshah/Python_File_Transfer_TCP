# Transferring files over TCP using Pythong

Client/Server Python codes for enabling file transfer over TCP/IP.

## Steps to run sample code
1. Run `python server.py` and copy address displayed 
	`>>''_addr_''<<`
2. Run `pyhon client.py`
3. Paste address in client window.
4. In server window, enter the file path (including filename) for the file to be transferred from the client to the server
5. In client window, enter the file path (including filename) to save to save the incoming file on the client side.

Done!

IMPORTANT NOTES (Updated regularly):
1. This code works over a network too. Enter the appropriate IP address when indicated.
2. Larger files like images may get corrupted during the transfer. In case of such unsuccessfull transfer, adjust the buffer size ``buffsize``.
