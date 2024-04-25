'''
 Creer un programme qui permet de convertir 
 une vidéo MP4 en MP3
'''
# utiliser la bibliotheque moviepy
import moviepy.editor as mp

my_clip=mp.VideoFileClip(r"4C.mp4")
my_clip.audio.write_audiofile(r"4C.mp3")