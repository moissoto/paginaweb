import gzip,shutil

archivo = 'Comprobante_Seguros23377132.pdf'

with open(archivo, 'rb') as f_in:
    with gzip.open('Comprobante_Seguros23377132.gz', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)