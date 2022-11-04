Hello and welcome to ftype. It is an experimental idea to take text from the clipboard and display on the terminal like a kind of typewriter or a futuristic style display.

v0.01 - Figuring out how to use git.
Making first commit from laptop
Copied main code
Changed text delay from 0.04 to 0.06 for ease of reading - but ideally this should be set by user.

Future:
This may be taken further to be an online version eventually but at the moment, it's just a training ground for me learning to code and using git. Who knows what it may develop into... if anything.

DESCRIPTION:

Currently, what should happen is when the program is run, the user is prompted for text (the option to use what is on clipboard will be added later). Text is entered and then the screen is cleared and then text displayed letter by letter with a little clicky sound (bell.wav) until the end of the input. I have included pauses for full stops (periods) and commas.


ISSUES:

Currently, the program has to be run by specifying to python not to cache (python3 -u ftype.py) otherwise all the sounds are played... then all the code is dumped at once.

Also, Something seems to be breaking the program before all the text has been displayed an dumping the remainder as commands on the screen instead of within the program. I think this may be related to certain characters being recognised by python as special characters. I have already written code to deal with linebreaks. Maybe a good test for this would be to push through every unicode character and see which breaks it and which don't then create rules for these characters.

When text ends, we need a few newlines so that the command prompt does not display on the same line as the end of the text... or maybe a question "Do you want to add more text or exit"

No "simpleaudio" module on windows' version of python - seems to work on linux.

Entering a single space " " kills the program - string index out of range. Seems to be when a space is at the end of the string.


FUTURE FEATURES

Request input for speed of text (pause variable for time.sleep)