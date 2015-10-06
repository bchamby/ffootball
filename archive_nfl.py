########################
# Author: Brad Chamberlain
# Summary: Moves NFL fantasy data to archive folder.
########################

import time

files = [
'nfl_dst.html'
'nfl_k.html'
'nfl_qb.html'
'nfl_rb.html'
'nfl_te.html'
'nfl_wr.html'
]

CurrentDate = time.strftime("%Y-%m-%d")

for file in files:
    shutil.move("./output" + file, "./output" + file + currentTime)

#print (time.strftime("%Y-%m-%d"))
