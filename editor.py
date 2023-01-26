from moviepy.editor import *


#lets add a class to organize the code
class Edit:
    def __init__(self, v_path, m_path):
        #add the video path and the audio path
        self.video = v_path
        self.audio = m_path
    #function to add audio to a video
    def add_audio(self):
        self.clip = VideoFileClip(self.video)

        self.clip_duration = self.clip.duration

        self.audioclip = AudioFileClip(self.audio)#.set_duration(self.clip_duration)

        self.new_audioclip = CompositeAudioClip([self.audioclip])
    #adding a logo
    def add_logo(self, path):
        self.path = path
        self.logo = (ImageClip(self.path)
          .set_duration(self.clip_duration)
          .resize(height=50)
          .margin(right=8, top=8, opacity=0)
          .set_pos(("right","bottom")))
    def combine(self):
        self.clip = VideoFileClip(self.video)
        self.clip2 = VideoFileClip(self.audio)
        self.final_clip = concatenate_videoclips([self.clip,self.clip2])
    def save(self):
        #self.final_clip = self.clip.set_audio(self.new_audioclip)
        self.final_clip.write_videofile("output/output.mp4")


new = Edit("C:/Users/Mustapha - FreeTime/Desktop/Everything/output/temp/output.mp4","C:/Users/Mustapha - FreeTime/Documents/Bandicam/result.avi")
new.combine()
new.save()
