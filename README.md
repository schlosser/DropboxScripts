Dropbox Scripts
===============

Scripts that seek to simply Dropbox user experience, with a focus on photo organization for 
use with [Dropbox Camera Upload][1].

I use these scripts in conjunction with my [Food Journal WordPress Post Generator][2].

###Organize Photos

This script puts all photo files in its directory in folders based on date metadata.

Run this script by running the command `$ python Organize_Photos.py` in the directory with 
the photos.

###Flatten Photo Folders

This script removes all photos organized using `Organize_Photos.py` and places them in the
same directory as this script, remove the folders.

Run this script by running the command `$ python Flatten_Photo_Folders.py` in the directory with 
the photos.

###Scramble

This script scrambles and zips together photo folders created by `Organize_Photos.py` for easy
transport.

Run this script by running the command `$ python Scramble.py` in the directory with 
the photos and entering `1` or `2` as prompted to scramble or unscramble respectively.


[1]: https://www.dropbox.com/help/289/en
[2]: https://github.com/danrschlosser/FoodJournal/
