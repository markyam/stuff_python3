from urllib.request import urlretrieve

def progress(blk_reads, blk_size, total_size):
    if not blk_reads:
        print('Starting download')
        return None

    if total_size < 0:
        #Taille totale du fichier inconnue
        print('{:8d} / ??? octets downloaded'.format(blk_reads * blk_size))
    else:
        #Taille totale du fichier connue
        print('{:8d} / {:8d} octets downloaded'.format(blk_reads * blk_size, total_size))

    return None

if __name__ == '__main__':
    url = 'http://storage.sbg1.cloud.ovh.net/v1/AUTH_f3d9da6ae8ad466f99fe51489414ceeb/bb5-images/'
    filename, headers = urlretrieve(url + '077/312570c48b4d9636ee63015ae64f8.jpg', reporthook=progress)
    print('Download finished')
    print('File in :', filename)
