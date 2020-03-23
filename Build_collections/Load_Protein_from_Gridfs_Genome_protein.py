###
# open NCBI upload files in the Gridfs format
# write to collections

from pymongo import MongoClient
import gridfs, re

client = MongoClient('mongodb')
db = client.Genome_protein
fs_forwrite = gridfs.GridFS(db)  # for writing to a new file
fs          = gridfs.GridFSBucket(db)

#grid_out = fs_datafind.read()
# begin loop reading through genome colleciton
wrk_tag = False
wrk_filename = ''
wrk_data = ''
pattern = re.compile(r'>.._.+(?=\n>)', re.DOTALL)
start_time = datetime.now()
print('Starting: ', start_time)

# Retrieve data from "9606_Genome"
fs_datafind = fs.open_download_stream_by_name("9606_Genome")
dataread = fs_datafind.read()

print('dataread from read() is: ', dataread[:1000], 'at: ', datetime.now())

# use a REGEX "findall" to loop through this single string
# and return a tuple of strings found
x_decoded = dataread.decode()
print('x_decoded: ', x_decoded[:1000])
match_object = re.findall(pattern, x_decoded)
for new_list in match_object:
    #print('New_list match object: ', new_list)
    wrk_filename = new_list[1:10]
    wrk_dataforwrite = new_list.encode()
    print('File name: ', wrk_filename, '\ndata: ', wrk_dataforwrite[:100])
    fs_forwrite.put(wrk_dataforwrite, disable_md5 = True, filename=wrk_filename)

end_time = datetime.now()
print('Finished at: ', end_time, '   total time: ', end_time-start_time)
