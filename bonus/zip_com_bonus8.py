import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    i = pathlib.Path(dest_dir, 'compress.zip')
    with zipfile.ZipFile(i, 'w') as archive:
        for fp in filepaths:
            fp = pathlib.Path(fp)
            archive.write(fp, arcname=fp.name)


if __name__ == "__main__":
    make_archive(filepaths=['bonus1.py', 'bonus2.py'], dest_dir='dest')
