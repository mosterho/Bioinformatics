
## There is no practical application for this program,
## other than learning how to write to a GridFS system.

import sys
from pymongo import MongoClient
import gridfs, re

client = MongoClient('mongodb')
db = client.refseqgene
#fs_forwrite_filesys = gridfs.GridFS(db, collection='refseqgene')
fs_forwrite = gridfs.GridFSBucket(db, bucket_name='refseqgene')  # for writing to a new file
fs_forread  = gridfs.GridFSBucket(db)
fs_forwrite_gridin = fs_forwrite.open_upload_stream('refseqgene')

first_read = False

for fs_find in fs_forread.find({}):
    fs_read = fs_find.read()
    print('fs_read: ', fs_read[:100])
    #
    fs_read_decode = fs_read.decode()
    fs_read_decode_splits = fs_read_decode.split("\n")
    for x_read in fs_read_decode_splits:
        if(x_read[:1] == ">"):
            if(first_read is True):
                Nucleotide_encoded = write_data.encode()
                fs_forwrite_gridin.write(Nucleotide_encoded)
                #print('accession: ', accession_nbr, 'gene abbrev: ', gene_abbrev, 'description: ', description)
            else:
                first_read = True
            write_data = x_read
            #print('write_data: ', write_data)
        else:
            write_data += x_read
    Nucleotide_encoded = write_data.encode()
    fs_forwrite_gridin.write(Nucleotide_encoded)
    #print('accession: ', accession_nbr, 'gene abbrev: ', gene_abbrev, 'description: ', description)
fs_forwrite_gridin.close()
