#!/bin/bash
#PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/myUser/scripts
. ~/.virtualenvs/wallpaper/bin/activate


# virtualenv is now active, which means your PATH has been modified.
# Don't try to run python from /usr/bin/python, just run "python" and
# let the PATH figure out which version to run (based on what your
# virtualenv has configured).
echo "Begining!"
python /home/danielmxli/mintpaper/mintpaper-script.py
echo "Done!"