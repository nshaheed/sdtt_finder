from music21 import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join

# op76 = converter.parse('haydn-op76-3-02.mxl')
# op76chords = op76.chordify().flat.getElementsByClass('Chord') # no measure info here, could be an issue
# op76chords = op76.chordify() # no measure info here, could be an issue

# determine whether the outer notes of the chord are tritones
def outerTritone(chrd):
    top = max(chrd.pitches)
    bottom = min(chrd.pitches)
    # interv = interval.Interval(chrd[len(chrd)-1],chrd[0]).simpleName # reduce to simple interval
    interv = interval.Interval(top,bottom).simpleName # reduce to simple interval
    tritone = interval.Interval('a4').simpleName # both apparently need to be simple to compare
    if interv == tritone:
        return True
    else:
        return False

# onlyOuter = filter(outerTritone, op76chords) # template, need to get interval have it be dim 4th

def descSecond(interv):
    # print 'INTERVAL:',interv.niceName, interv.direction
    if (interv.name == 'm2' or interv.name == 'M2') and interv.direction == -1:
        return True
    else:
        return False

# when outertritone is found:
# tritone flag = true
# curr bass = set
# curr tritone = set
# once bass note changes -> set to false

def analyzePiece(piece_title):
    piece = piece_title[0]
    title = piece_title[1]
    if piece is not None:
        # if piece.metadata is not None and piece.metadata.title is not None:
        #     print 'analyzing ' + piece.metadata.title
        # else:
        #     print 'analyzing'
        print 'analyzing ' + title
        # print 'analyzing piece'
        chords = piece.chordify()

        saw_tt = False
        tt_bass = None
        tt_sop  = None
        tt_chord = None # the chord where the tritone appears
        potential_sub_tt = []

        for thisChord in chords.recurse().getElementsByClass('Chord'):
            curr_bass = thisChord[-1]
            curr_sop = thisChord[0]

            if saw_tt:
                curr_sop_int = interval.Interval(tt_sop,curr_sop)
                if curr_bass.pitch != tt_bass.pitch:
                    saw_tt = False
                elif descSecond(curr_sop_int) : # the sop resolved down by a second
                    saw_tt = False
                    potential_sub_tt.append((tt_chord.measureNumber, tt_chord.beatStr, tt_chord))
                    print(tt_chord.measureNumber, tt_chord.beatStr, tt_chord)

            else:
                if outerTritone(thisChord):
                    saw_tt   = True
                    tt_chord = thisChord
                    tt_bass  = curr_bass
                    tt_sop   = curr_sop
                    # print(thisChord.measureNumber, thisChord.beatStr, thisChord)

        # return (piece.metadata.title, potential_sub_tt)
        return potential_sub_tt
    else:
        print "got none"

# print 'parsing chorales'
# chorales = map(lambda x: corpus.parse('bwv' + str(x)), range(250,439)) # go through all chorales
# chorales = map(lambda x: corpus.parse('bwv' + str(x)), range(250,439)) # go through all chorales

# sdtts = map(analyzePiece,chorales)
print 'analyzing...'

# bach chorales...
# sdtts = map(analyzePiece,corpus.chorales.Iterator(1,371))
# sdtts_title = zip(corpus.chorales.Iterator(1,371,returnType='filename'),sdtts)
# sdtts_title = filter(lambda x: len(x[1]) > 0,sdtts_title)

# schumann
def analyzeComposer(composer):
    print 'analyzing ' + composer
    paths = corpus.getComposer(composer)
    works = map(corpus.parse,paths)
    # titles = map(lambda x: x.metadata.title, works)
    titles = paths
    titles_works = zip(works,titles)
    # sdtts = map(analyzePiece,works)
    sdtts = map(analyzePiece,titles_works)
    sdtts_title = zip(titles, sdtts)
    return filter(lambda x: len(x[1]) > 0, sdtts_title)

def printInstance(instance):
    print '| | ', instance, '|'

def printResults(sdtts):
    print 'RESULTS'
    for work in sdtts:
        print '|', work[0], '|'
        map(printInstance, work[1])

# schumann = analyzeComposer('schumann')
# # schumann = analyzePiece(corpus.parse
# printResults(schumann)

# mozart = analyzeComposer('mozart')
# printResults(mozart)

def analyzePalestrina(composer):
    print 'analyzing ' + composer
    paths = corpus.getComposer(composer)
    paths = paths[286:]
    works = map(corpus.parse,paths)
    # titles = map(lambda x: x.metadata.title, works)
    titles = paths
    titles_works = zip(works,titles)
    # sdtts = map(analyzePiece,works)
    sdtts = map(analyzePiece,titles_works)
    sdtts_title = zip(titles, sdtts)
    return filter(lambda x: len(x[1]) > 0, sdtts_title)

# palestrina = analyzeComposer('palestrina')
palestrina = analyzePalestrina('palestrina')
printResults(palestrina)

def analyzeFilePath(path):
    paths = [f for f in listdir(path) if isfile(join(path, f))]
    # print onlyfiles
    paths = map(lambda x: path + x, paths)
    print paths
    print 'parsing paths'
    works = map(converter.parse,paths)
    # titles = map(lambda x: x.metadata.title, works)
    titles = paths
    titles_works = zip(works,titles)
    # sdtts = map(analyzePiece,works)
    print 'analyzing pieces'
    sdtts = map(analyzePiece,titles_works)
    sdtts_title = zip(titles, sdtts)
    return filter(lambda x: len(x[1]) > 0, sdtts_title)

# corpus.addPath('haydn_quartets/')

# haydn = analyzeFilePath('haydn_quartets/')
# printResults(haydn)

# print 'RESULTS'
# print_title sdtts
# for x in sdtts_title:
    # results = map((x.measureNumber, x.beatStr, x.chord),x[1])
    # print x[0], x[1]
# result = analyzePiece()
# print map(lambda x: (x.measureNumber, x.beatStr, x), result)

# the example is at the 59th indx of op76chords

# hchords = op76.chordify()
# t2 = hchords.flat.getElementsByClass('Chord')
