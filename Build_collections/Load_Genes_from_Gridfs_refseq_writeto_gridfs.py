
## There is no practical application for this program,
## other than learning how to write to a GridFS system.

## this will read the multiple refseqgene files uploaded from
## the NCBI files. This will combine the 22 files in GridFS format into one
## GridFS file as "refseqgene".

## to read a GridFS "bucket":
## 1. create the GridIN object (GridFSBucket spec)
## 2. perform a "find" (in this case, will read all 22 files)
## 3. loop through the "find" object,
## 4. perform a "read" on the "find" (actually a single file) object.
## 5. perform a "decode" on the binary data to convert it to a string data type

## the following will create a new bucket, no additional steps needed
## to write to a GridFS bucket (file):
## 1. create the GridIN object (GridFSBucket spec), but specify a new bucket name ('fs' is default)
## 2. open a stream to write to the file (open_upload_stream)
## 3. perform an "encode" to convert string data to binary
## 4. perform a "write" to the stream object
## 5. perform a close() to the stream object to ensure all writes are complete

import sys
from pymongo import MongoClient
import gridfs, re

client = MongoClient('mongodb')
db = client.refseqgene
fs_forread  = gridfs.GridFSBucket(db)
fs_forwrite = gridfs.GridFSBucket(db, bucket_name='refseqgene')  # for writing to a new file

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
