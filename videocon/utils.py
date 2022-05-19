import moviepy.editor as mp
from moviepy.editor import VideoFileClip
from moviepy.editor import *
import cv2

def send_admin_mail(form_file_data,form_choice_data):
  if str(form_choice_data) == "GIF":
            file = str(form_file_data)
            clip = VideoFileClip(file)
            clip.write_gif("mygif.gif",fps=1) # This line of code convert gif
        
  elif str(form_choice_data) == "AUDIO":
      file = str(form_file_data)
      video = VideoFileClip(file)
      audio = video.audio                  # This line of code converting video file to audio file
      audio.write_audiofile("MyAudio.mp3") # This line of code for saving (.mp3) file
      # audio.save()

  elif str(form_choice_data) == "Image":
      file = str(form_file_data)
      vidcap = cv2.VideoCapture(file)
      time_skips = float(12000)
      success,image = vidcap.read()
      count = 0
      while success:
          # cv2.imshow("Output",image)     -----> this line of code to show video window on run time / but not working properly
          cv2.imwrite("frame%d.jpg" % count, image)  # save image as jpg
          vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*time_skips)) 
          # cv2.imshow("MYVIDEO.mp4",image)            
          success,image = vidcap.read()
          # print('Read a new frame: ', success)
          count +=1