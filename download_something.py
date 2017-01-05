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
    url = 'http://my_url'
    filename, headers = urlretrieve(url, reporthook=progress)
    print('Download finished')
    print('File in :', filename)
