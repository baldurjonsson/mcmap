import os
import ftplib
import zipfile

import settings


def download_world():
    with ftplib.FTP(settings.FTP_HOST, settings.FTP_USER, settings.FTP_PASS) as ftp:
        with open(settings.FTP_FILENAME, 'wb') as f:
            ftp.retrbinary('RETR ' + settings.FTP_FILENAME, f.write)


def unzip_world():
    with zipfile.ZipFile(settings.FTP_FILENAME, 'r') as zip:
        zip.extractall()


def main():
    os.chdir(settings.DATA_DIR)
    download_world()
    unzip_world()


if __name__ == '__main__':
    main()
