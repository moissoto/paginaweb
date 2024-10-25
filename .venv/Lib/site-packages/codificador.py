from base64 import b64decode,b64encode

def encode64(txtArea:str)->str:
    texto_bites = txtArea.encode('ascii')
    message = b64encode(texto_bites)
    messageb64 = message.decode('ascii')
    return messageb64

def decode64(txtArea:str)->str:
    texto_bites = txtArea.encode('ascii')
    message = b64decode(texto_bites)
    messageb64 = message.decode('ascii')
    return messageb64
