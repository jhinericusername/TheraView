import json
import os

# system
import sys, subprocess

# File names
video_file_name = "input_video.mp4"
output_json_file_name = "final_result.json"

if __name__ == "__main__":

    print("Starting pose estimation on video under openpose/videos/input_video.mp4")

    os.chdir(os.getcwd() + '/openpose')

    command = os.getcwd() + "/bin/OpenPoseDemo.exe"

    hands = False
    
    if hands:
        command += " --hands"

    command += " --video " + os.getcwd() + "\\videos\\" + video_file_name
 
    command += " --write_json " + os.getcwd() + "\\output_jsons\\" + output_json_file_name

    subprocess.run(command, shell=True)