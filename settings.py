from decouple import config
FTP_HOST = config('FTP_HOST', '')
FTP_USER = config('FTP_USER', '')
FTP_PASS = config('FTP_PASS', '')
FTP_FILENAME = config('FTP_FILENAME', 'world.zip')
DATA_DIR = config('DATA_DIR', 'data')
