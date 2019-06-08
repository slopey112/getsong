# getsong
This is a command line utility that pulls songs from youtube. DISCLAIMER: This script only works on Unix-like operating systems, so it will NOT work on Windows.

## Installation
First, clone this repo from github.
```
$ git clone https://github.com/slopey112/getsong.git
```
You may also need to download a few dependencies, listed below:
```
eyed3, youtube-dl, id3v2
```
Next, navigate to the downloaded directory and execute the setup wizard.
```
$ chmod +x setup.sh
$ ./setup.sh
```
After that, it is recommended to move the `getsong` script to somewhere on your path. It is also recommended to move the script to your local `bin` directory, as `getsong` depends on your home folder.

Installation is now complete. You may choose to delete the cloned repo along with the setup wizard.

## Usage
`getsong` requires three arguments and two optional arguments.
```
getsong [-g genre] [-o output path] title artist album
```
For example, to download DNA by Kendrick Lamar from the album DAMN.:
```
$ getsong DNA 'Kendrick Lamar' DAMN.
```
By default, `getsong` downloads to your home Downloads directory, but you can change this by entering the following command, replacing DEFAULT_PATH with the path of your choice.
```
$ echo DEFAULT_PATH > ~/.getsong/conf/default_output_path
```
