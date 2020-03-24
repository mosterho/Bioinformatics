###
# open NCBI upload files in the Gridfs format
# write to collections
# This will create various chromosome collections in the
# Genome database. Read the "9606_Genome" collection created by
# the BASH script, write each chromosome as a collection
# while looping through the fsbucket, catch each instance of ">"
# until the next ">" is read

from pymongo import MongoClient
from datetime import datetime, timedelta
import gridfs, re

client = MongoClient('mongodb')
db = client.Genome
fs_forwrite = gridfs.GridFS(db)  # for writing to a new file
fs          = gridfs.GridFSBucket(db)

# begin loop reading through genome colleciton
wrk_tag = False
wrk_filename = ''
wrk_data = ''
#pattern = re.compile(r'>.+?(?<=\n>)', re.DOTALL)
start_time = datetime.now()
print('Starting: ', start_time)

# Retrieve data from "9606_Genome"
fs_datafind = fs.open_download_stream_by_name("9606_Genome")
dataread = fs_datafind.read()

print('dataread from read() is: ', dataread[:1000], 'at: ', datetime.now())

# use a "split" to loop through this single string
# and return a list of strings found
x_decoded = dataread.decode()
print('x_decoded: ', x_decoded[:1000])
#match_object = re.findall(pattern, x_decoded)
match_object = x_decoded.split('>')
for new_list in match_object:
    if new_list != '':
        #print('New_list match object: ', new_list)
        wrk_filename = new_list[0:9]
        wrk_dataforwrite = new_list.encode()
        print('File name: ', wrk_filename, '\ndata: ', wrk_dataforwrite[:100])
        #fs_forwrite.put(wrk_dataforwrite, disable_md5 = True, metadata={ }, filename=wrk_filename)
        fs_forwrite.put(wrk_dataforwrite, metadata={ }, filename=wrk_filename)

end_time = datetime.now()
print('Finished at: ', end_time, '   total time: ', end_time-start_time)
