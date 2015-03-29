#!/usr/bin/env python
from gi.repository import Gio
import os
import re
name = "file:////home/danielmxli/mintpaper/Mt. Fuji (Japan) under the Milky Way  by Yuga Kurita. 1600x1068.jpg"
print(name)
new_name = re.escape(name)
print(new_name)
os.system("gsettings set org.gnome.desktop.background picture-uri %s" % new_name)
# settings = Gio.Settings.new("org.cinnamon.desktop.background")
# settings.set_string("picture-uri", "file:///home/daniemxli/mintpaper/test.jpg")