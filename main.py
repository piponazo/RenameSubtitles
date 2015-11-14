#Approach using glob does not work (and I do not know why)

from os import listdir
import os
import glob
import sys
import os.path
import argparse

def searchVideoFilesWithSubtitles(path):
    """
    Keyword arguments:
    path  -- Directory that will be analyzed recursively
    Return values:
    dictSrts  -- dictionary with video files as keys and srt files as values
    rootPaths -- root paths for each entry in the dictionary
    """
    dictSrts = {}
    rootPaths= []

    for root, dirs, files in os.walk(path):
        for mkv in files:
            if mkv.endswith(".mkv"):
                for srt in os.listdir(root):
                    if srt.endswith(".srt"):
                        dictSrts[mkv] = srt
                        rootPaths.append(root)

    return (dictSrts, rootPaths)

def renameSrts(dictSrts, rootPaths):
    """
    TODO - perform renaming in other function. This one should only return a dictionary with the old
    file name and the new one.

    Keyword arguments:
    dictSrts  -- dictionary with video files as keys and srt files as values
    rootPaths -- root paths for each entry in the dictionary
    """
    mkvs = dictSrts.keys()
    srts = dictSrts.values()
    for i in xrange(len(rootPaths)-1):
        mkvName = mkvs[i].split(".mkv")[0]
        srtName = srts[i].split(".srt")[0]
        if mkvName != srtName :
            oldSrt = rootPaths[i] + "/" + srts[i]
            newSrt = rootPaths[i] + "/" + mkvName + ".srt"
            print "Renaming " + srts[i] + " to " + mkvName + ".srt"
            print oldSrt
            print newSrt
            os.rename(oldSrt, newSrt)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Match names of srt files with video files.')
    parser.add_argument('-p', '--path', dest='path', action='store', required=True,
                       help='Path where the script will process in recursive way')
    args = parser.parse_args()

    if not os.path.exists(args.path):
        print "Given path doesn't exist: " + args.path
        sys.exit()

    dictSrts, rootPaths = searchVideoFilesWithSubtitles(args.path)
    renameSrts(dictSrts, rootPaths)

