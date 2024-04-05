import os
def san(ffile,sfile):
    if os.path.exists(ffile):
        with open(ffile, 'r') as f:
            with open(sfile, 'w') as q:
                q.write(f.read())
