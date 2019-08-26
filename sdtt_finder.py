import sys
import itertools
from os import listdir
from os.path import isfile, join

from music21 import *

def analyzePiece(piece, title):
    """ analyze a piece to find all potential subdominant tritones. """
    if piece is not None:
        print 'analyzing ' + title
        chords = piece.chordify()

        outer_tt = False
        tt_bass = None
        tt_soprano  = None
        tt_chord = None # the chord where the outer tritone appears
        potential_sdtt = []

        # iterate through every harmony looking for a tritone between outer voices
        # and the soprano resolving down
        for current_chord in chords.recurse().getElementsByClass('Chord'):
            current_bass_note = current_chord[-1]
            current_soprano_note = current_chord[0]

            if outer_tt:
                current_soprano_note_interval = interval.Interval(tt_soprano,current_soprano_note)
                if current_bass_note.pitch != tt_bass.pitch:
                    outer_tt = False
                # the soprano resolves down by a second, indicating a potential SdTT
                elif descSecond(current_soprano_note_interval) :
                    outer_tt = False
                    potential_sdtt.append({
                        'measure': tt_chord.measureNumber,
                        'beat': tt_chord.beatStr,
                        'chord': tt_chord,
                        'title': title,
                    })
                    print potential_sdtt[-1]
            # indicate that the current bass note forms a tritone with the soprano voice
            elif outerTritone(current_chord):
                outer_tt   = True
                tt_chord   = current_chord
                tt_bass    = current_bass_note
                tt_soprano = current_soprano_note

        return potential_sdtt
    else:
        print >> sys.stderr, '%s did not contain any score data' % (title)

def outerTritone(chrd):
    """ determine whether the outer notes of the chord form a tritone. """
    top = max(chrd.pitches)
    bottom = min(chrd.pitches)
    interv = interval.Interval(top,bottom).simpleName # reduce to simple interval
    tritone = interval.Interval('a4').simpleName # both intervals need to be simple to compare
    return interv == tritone

def descSecond(interv):
    """ check if an interval is a descending second. """
    return (interv.name == 'm2' or interv.name == 'M2') and interv.direction == -1

def analyzeComposer(composer):
    """ analyze all the works of a composer available in the music21 corpus.

    Parameters
    ----------
    composer : string
           The name of the composer
    """
    print 'analyzing the works of ' + composer

    # get the file paths of all of a composer's works
    paths = corpus.getComposer(composer)
    works = map(corpus.parse,paths)
    titles = paths

    # find any possible instances of the SdTT
    sdtts = []
    for work, title in zip(works, titles):
        sdtts.append(analyzePiece(work, title))

    return filter(lambda x: len(x) > 0, sdtts)

def analyzeFilePath(path):
    """ analyze all files in the given directory (e.g. /music/haydn_quartets/).

    Parameters
    ----------
    path : string
           The filepath containing files to analyze (e.g. /music/haydn_quartets/)
    """
    filenames = [f for f in listdir(path) if isfile(join(path, f))]
    paths = map(lambda filename: path + filename, filenames)
    print 'parsing all files in file path'
    works = map(converter.parse,paths)

    titles = paths

    print 'analyzing pieces'
    # find any possible instances of the sdtt
    sdtts = []
    for work, title in zip(works, titles):
        sdtts.append(analyzePiece(work, title))

    return filter(lambda x: len(x) > 0, sdtts)

def printResults(works):
    """ pretty print the potential SdTTs. """

    print '-------------------------------'
    print 'Potential Subdominant Tritones:'
    print '-------------------------------'

    for work in works:
        print work[0]['title']
        for sdtt in work:
            print '\tChord:   {0}'.format(sdtt['chord'])
            print '\tMeasure: {0}'.format(sdtt['measure'])
            print '\tBeat:    {0}\n'.format(sdtt['beat'])

# haydn = analyzeFilePath('haydn_quartets/')
# printResults(haydn)

schumann = analyzeComposer('schumann')
print schumann
printResults(schumann)


# dir, composer, work
