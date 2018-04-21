# -*- coding: utf-8

import hashlib
import sys
import os

def hash(fname, handler):
    with open(fname, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            handler.update(chunk)
    return handler.hexdigest()

target_dir = sys.argv[1]
for filename in os.listdir(target_dir):
    if filename.endswith('.md5') or filename.endswith('.sha1'):
        continue
    filepath = target_dir + os.path.sep + filename
    md5file = filepath + '.md5'
    sha1file = filepath + '.sha1'
    with open(md5file, 'w+') as out:
        out.write(hash(filepath, hashlib.md5()).lower())
    with open(sha1file, 'w+') as out:
        out.write(hash(filepath, hashlib.sha1()).lower())

print 'FINISH!'