## Synopsis

**GymTax** is a scripting language interpreted developed in Python using a dialect of the EBNF notation. With Text-to-Speech support for both PC and Android Smartphones with Python installed, it allows you to turn virtually any device into your **personal trainer**.

Achieve the best experience with QPython installed on your Android smartphone and bluetooth sport earphone(s).

The current syntax abstracts a typical gym session, which usually is made of a *warmup* phase, an *activity*/*circuits* phase, and a *cool down* phase. Such phases are fully customisable with the specification of exercises and announcements.

In the future the syntax will add native support for Interval Training. For the time being, the syntax is flexible enough to manually incorporate this kind of training in your GymTax scripts.

## Script Example

A typical (almost minimalistic) script would look something like this.

~~~~
SESSION 'Test session'

  enter warmup
    exercise 'test warmup exercise 01'                                 1m  9s
    rest                                                               2m
    announce 'test warmup announce 01'                                    15s

  enter activity
    announce 'test announcement 01'

  enter circuits rotate
    station
      'squats'
      'power lounges'

    station
      'station 2 exercise 1'
      'station 2 exercise 2'

    run 2

    exercise 'burpess'                                                    20s

    run 2

  enter cooldown
    exercise 'test exercise 02'

start
~~~~

The parser is case-insensitive so you can use upper and lower case letters as you like. The numbers appearing to the right specify the duration of the corresponding events. When no duration is explicitly given a default of 1 minute and 15 seconds is used for exercises and rests respectively.

## Motivation

This project came to be the moment I left the University of Glasgow Sports and Recreation centre, which offer a great Supercircuits class, almost unique. This project is an attempt to fill the gap when going to gyms which do not provide what one is really looking for.

## Installation

GymTax depends on **parsimonious**, the library used to parse the grammar and generate the GymTax script parser. Install it with

`sudo pip install parsimonious`

Then clone this Git repository wherever you like, and run

`python gymtax.py`

for further instructions.

## License

GPLv3.
