#!/bin/sh

# Cover art is stored in home directory in .getsong folder.
mkdir "$HOME/.getsong"
mkdir "$HOME/.getsong/cover-art"
mkdir "$HOME/.getsong/scripts"
mkdir "$HOME/.getsong/conf"
touch "$HOME/.getsong/conf/default_output_path"
echo "$HOME/Downloads" > "$HOME/.getsong/conf/default_output_path"
mv CoverArt.py "$HOME/.getsong/scripts"
