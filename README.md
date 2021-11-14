# Plover Dictionaries

## Installation:

- linux:
	- symlink from dotfiles
- windows:
	- git clone into the directory:
		- The current solution is just to git clone the whole thing, but that sux because I have to do it twice 

## problems

- I can not simlink from my dotfile plover to the default path for plover configurations in windows
	- /mnt/c/Users/josiah/appdata/Local/plover/plover
- The current solution is just to git clone the whole thing, but that sux because I have to do it twice 
	- once in the dotfiles, and once in this massive directory that I have to navigate to
- possible solutions
	- figure out if there is a way to simlink successfully
	- figure out if there is a way to change the file location to .config/plover
