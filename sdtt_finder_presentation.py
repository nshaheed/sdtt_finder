import sys
import itertools

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
