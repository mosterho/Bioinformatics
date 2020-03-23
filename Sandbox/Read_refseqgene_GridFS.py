
##
## read from full refseqgene GridFS file.

## This short program works, shows how to read from
## a single GridFS bucket. Note this needs a "find"
## in order to work, may be a different way to do this.

import sys
from pymongo import MongoClient
import gridfs

client = MongoClient('mongodb')
db = client.refseqgene
fsforread = gridfs.GridFSBucket(db, bucket_name='refseqgene')

for fsforread_find in fsforread.find({}):
    fsforread_read = fsforread_find.read()
    print('Should only be one of these from read():', fsforread_read[:100])
    fsforread_read_split = fsforread_read.split(b'>')
    for i in fsforread_read_split:
        print(i[:100])
        pass
