# find newest pictures or movies


import os
from operator import itemgetter, attrgetter
from datetime import datetime


def find_newpics(dir, number, extension):
    """
    returns a list of filenames, newest first - function makes chdir
    parameter:
    dir = string, directory in which should be searched e.g. "/etc/...."
    number = number of newest files which should be given back e.g. 3
    extension = what kind of file is look for e.g. ".jpg",
    keep in mind: function has Problems if there are blanks in filename,
    should not matter here because there are only generated filenames without
    """
    
    newestfiles = []
    # go to directory
    os.chdir(dir)
    # get all filenames in directory
    files = os.listdir('.')
    # give stat information of all files in a list - using a generator
    # mind: stat has problems with blanks in filename, should not matter here
    stats = [os.stat(f) for f in files]
    # get time of last content change, should also work when newly created
    mtimes = [stat.st_mtime for stat in stats]
    # print(mtimes)
    # combine filenname and corresponding ctime
    combine = zip(files,mtimes)
    # sort files, key = time, newest first
    combine = sorted(combine, key=itemgetter(1), reverse=True)
    # print(combine)
    counter = 0
    for n in combine:
        # print(n[0], "Datum Uhrzeit:", datetime.fromtimestamp(n[1])  )
        # only return files with .extension - for example
        # only number of filenames is returned
        if n[0].endswith(extension) and counter < number:
            counter += 1
            # print(counter)
            newestfiles.append(n[0])
    # print(newestfiles)
    return newestfiles





