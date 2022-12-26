import hashlib

texto = input('Digite algo para gerar o hash: ')

menu = input('Digite o tipo de hash que vc deseja. : SHA1, SHA256, SHA512, MD5 _>>')

resultado = False

match menu:
    case 'SHA1':
        resultado = hashlib.sha1(texto.encode('utf-8'))
    case 'SHA256':
        resultado = hashlib.sha256(texto.encode('utf-8'))
    case 'SHA512':
        resultado = hashlib.sha512(texto.encode('utf-8'))
    case 'MD5':
        resultado = hashlib.md5(texto.encode('utf-8'))


if resultado:
    print(f'o resultado do hashe md5: {resultado.hexdigest()} do texto: {texto}')

else:
    print('comando inválido!')