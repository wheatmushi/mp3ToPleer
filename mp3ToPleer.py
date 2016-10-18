import os
import shutil

music = u"F:/Music (s)"
pleer = u"F:/_PLEER"

for artist in os.listdir(music):
    mus_art_path = os.path.join(music,artist)
    plr_art_path = os.path.join(pleer,artist)
    for album in os.listdir(mus_art_path):
        if album[1:5] != u"flac":
            if not os.path.isdir(plr_art_path):
                os.mkdir(plr_art_path)
            mus_alb_path = os.path.join(music,artist,album)
            plr_alb_path = os.path.join(pleer,artist,album)
            if os.path.isdir(mus_alb_path):
                shutil.copytree(mus_alb_path, plr_alb_path)

folders = [x[0] for x in os.walk(pleer)]
for i in folders:
    if i[-7:] == u"Artwork":
        print i
        shutil.rmtree(i)
