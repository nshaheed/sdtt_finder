# sdtt_finder
music21 script to look for subdominant tritones (SdTTs)

This script requies Python 2.7, and the music21 library to be installed.

To run, first clone the repository:

```
git clone https://github.com/nshaheed/sdtt_finder.git
```

To search an individual work in the music21 corpus:

```
python sdtt_finder.py work schumann/opus41no1/movement1.mxl
```

To search all works in the music21 corpus by a composer:

```
python sdtt_finder.py composer schumann
```

If you have a directory of music21 parsable score files (such as .krn files) you can analyze the
entire directy with

```
python sdtt_finder.py filepath haydn_quartets/
```

Example output:

```
$ python sdtt_finder.py composer schumann

['sdtt_finder.py', 'composer', 'schumann']
analyzing the works of schumann
analyzing /home/nshaheed/anaconda2/lib/python2.7/site-packages/music21/corpus/schumann/dichterliebe_no2.xml
analyzing /home/nshaheed/anaconda2/lib/python2.7/site-packages/music21/corpus/schumann/opus41no1/movement1.mxl
{'beat': '1', 'title': u'/home/nshaheed/anaconda2/lib/python2.7/site-packages/music21/corpus/schumann/opus41no1/movement1.mxl', 'chord': <music21.chord.Chord B4 D4 G#3 F2>, 'measure': 11}
{'beat': '2 1/2', 'title': u'/home/nshaheed/anaconda2/lib/python2.7/site-packages/music21/corpus/schumann/opus41no1/movement1.mxl', 'chord': <music21.chord.Chord B4 D4 G#3 F2>, 'measure': 11}
analyzing /home/nshaheed/anaconda2/lib/python2.7/site-packages/music21/corpus/schumann/opus41no1/movement2.mxl
analyzing /home/nshaheed/anaconda2/lib/python2.7/site-packages/music21/corpus/schumann/opus41no1/movement3.mxl
analyzing /home/nshaheed/anaconda2/lib/python2.7/site-packages/music21/corpus/schumann/opus41no1/movement4.xml
analyzing /home/nshaheed/anaconda2/lib/python2.7/site-packages/music21/corpus/schumann/opus41no1/movement5.mxl
{'beat': '2', 'title': u'/home/nshaheed/anaconda2/lib/python2.7/site-packages/music21/corpus/schumann/opus41no1/movement5.mxl', 'chord': <music21.chord.Chord E5 D4 F4 C4 B-2 F3>, 'measure': 114}
{'beat': '2', 'title': u'/home/nshaheed/anaconda2/lib/python2.7/site-packages/music21/corpus/schumann/opus41no1/movement5.mxl', 'chord': <music21.chord.Chord A4 B-3 F3 G3 E-2 B-2>, 'measure': 118}
analyzing /home/nshaheed/anaconda2/lib/python2.7/site-packages/music21/corpus/schumann/opus48no2.mxl
-------------------------------
Potential Subdominant Tritones:
-------------------------------
/home/nshaheed/anaconda2/lib/python2.7/site-packages/music21/corpus/schumann/opus41no1/movement1.mxl
	Chord:   <music21.chord.Chord B4 D4 G#3 F2>
	Measure: 11
	Beat:    1

	Chord:   <music21.chord.Chord B4 D4 G#3 F2>
	Measure: 11
	Beat:    2 1/2

/home/nshaheed/anaconda2/lib/python2.7/site-packages/music21/corpus/schumann/opus41no1/movement5.mxl
	Chord:   <music21.chord.Chord E5 D4 F4 C4 B-2 F3>
	Measure: 114
	Beat:    2

	Chord:   <music21.chord.Chord A4 B-3 F3 G3 E-2 B-2>
	Measure: 118
	Beat:    2

```
