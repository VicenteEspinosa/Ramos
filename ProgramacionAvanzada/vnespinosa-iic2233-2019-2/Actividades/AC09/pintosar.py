def reparar_comunicacion(ruta):
    chunks = []
    with open(ruta, 'rb') as bytes_file:
        bytes_a = bytes(bytes_file)
        for i in range(0, len(bytes_a), 16):
            chunk = bytes_file[i:i + 16]
            chunks.append[chunk]
    for chunk in chunks:
        pivote = int(chunk[0])
        del chunk[0]
        for byte in chunk:
            if byte.isdigit():
                if byte >= pivote:
                    chunk.remove(byte)

    with open('Docengelion.bmp', 'wb') as bytes_file:
        pass
        # Guardar los bytes arreglados

if __name__ == '__main__':
    try:
        reparar_comunicacion('EVA.xdc')
        print("PINTOSAR201: Comunicacion con pilotos ESTABLE")
    except Exception as error:
        print(f'Error: {error}')
        print("PINTOSAR301: CRITICO pilotos incomunicados DESCONEXION INMINENTE")
