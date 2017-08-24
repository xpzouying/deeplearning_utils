# -*- coding: utf-8 -*-


'''Processing

    Author: zouying (xpzouying@gmail.com)

1. rotate 90, 180, 270
2. flip
3. mirror

'''


import os
import argparse


from PIL import Image, ImageOps


IGNORE_FILES = ['.DS_Store']
SUPPORT_IMGS_FORMAT = ('.jpg', '.jpeg', '.bmp')


parser = argparse.ArgumentParser()
parser.add_argument('--dir', '-d', required=True, help='image dir')


def process_file(base, f):
    '''process file

    '''
    valid_ext = f.endswith(SUPPORT_IMGS_FORMAT)
    if not valid_ext:
        return

    file_basename, file_ext = os.path.splitext(f)
    f_rotate90 = file_basename + '_90' + file_ext
    f_rotate90_mirror = file_basename + '_90_mirror' + file_ext
    f_rotate90_flip = file_basename + '_90_fip' + file_ext
    f_rotate180 = file_basename + '_180' + file_ext
    f_rotate180_mirror = file_basename + '_180_mirror' + file_ext
    f_rotate180_flip = file_basename + '_180_fip' + file_ext
    f_rotate270 = file_basename + '_270' + file_ext
    # f_rotate270_mirror = file_basename + '_270_mirror' + file_ext
    # f_rotate270_flip = file_basename + '_270_fip' + file_ext

    full_path = os.path.join(base, f)
    img = Image.open(full_path)

    img90 = img.rotate(90, expand=1)
    img90.save(os.path.join(base, f_rotate90))
    ImageOps.mirror(img90).save(os.path.join(base, f_rotate90_mirror))
    ImageOps.flip(img90).save(os.path.join(base, f_rotate90_flip))

    img180 = img.rotate(180, expand=1)
    img180.save(os.path.join(base, f_rotate180))
    ImageOps.mirror(img180).save(os.path.join(base, f_rotate180_mirror))
    ImageOps.flip(img180).save(os.path.join(base, f_rotate180_flip))

    img270 = img.rotate(270, expand=1)
    img270.save(os.path.join(base, f_rotate270))
    # rotate_270_mirror is same as rotate_90_flip
    # ImageOps.mirror(img270).save(os.path.join(base, f_rotate270_mirror))
    # rotate_270_flip is same as rotate_90_mirror
    # ImageOps.flip(img270).save(os.path.join(base, f_rotate270_flip))


def process_dir(dir):
    sub_dirs = os.listdir(dir)

    for f in sub_dirs:
        # ignore filter
        if f in IGNORE_FILES:
            print('ignore file: ', f)
            continue

        full_path = os.path.join(dir, f)
        # ignore link
        if os.path.islink(full_path):
            print('ignore link: ', f)
            continue

        # if f is FILE
        if os.path.isfile(full_path):
            print('find file: ', f)
            process_file(dir, f)

        # if f is DIR
        if os.path.isdir(full_path):
            print('find dir: ', f)
            sub_path = os.path.join(dir, f)
            process_dir(sub_path)


def main():
    '''main function

    '''

    args = parser.parse_args()

    imgs_dir = args.dir
    imgs_dir = os.path.expanduser(imgs_dir)

    process_dir(imgs_dir)


if __name__ == '__main__':
    main()
