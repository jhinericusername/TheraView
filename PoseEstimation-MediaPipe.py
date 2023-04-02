import cv2
import mediapipe as mp
import numpy as np
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean
import math
import json


def extract_keypoints(video_file):
    
    cap = cv2.VideoCapture(video_file)
    mp_pose = mp.solutions.pose
    mp_drawing = mp.solutions.drawing_utils
    pose = mp_pose.Pose()

    angles_list = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(image)



        if results.pose_landmarks:

            angles = []

            # Find point values for specific connected groups of joints
            x1 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x
            y1 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y
            x2 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].x
            y2 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].y
            x3 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x
            y3 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y
            
            # Take differences between the different points to find 2D vector x and y components
            x_diff_1 = x2 - x1
            x_diff_2 = x2 - x3
            y_diff_1 = y2 - y1
            y_diff_2 = y2 - y3

            # determine the angle between the 2 vectors
            dot = x_diff_1*x_diff_2 + y_diff_1*y_diff_2      # dot product between [x1, y1] and [x2, y2]
            det = x_diff_1*y_diff_2 - y_diff_1*x_diff_2      # determinant
            angle = math.atan2(det, dot)  # atan2(y, x) or atan2(sin, cos)
            angles.append(math.degrees(angle)/180)

            # Find point values for specific connected groups of joints
            x1 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].x
            y1 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].y
            x2 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x
            y2 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y
            x3 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].x
            y3 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].y
            
            # Take differences between the different points to find 2D vector x and y components
            x_diff_1 = x2 - x1
            x_diff_2 = x2 - x3
            y_diff_1 = y2 - y1
            y_diff_2 = y2 - y3

            # determine the angle between the 2 vectors
            dot = x_diff_1*x_diff_2 + y_diff_1*y_diff_2      # dot product between [x1, y1] and [x2, y2]
            det = x_diff_1*y_diff_2 - y_diff_1*x_diff_2      # determinant
            angle = math.atan2(det, dot)  # atan2(y, x) or atan2(sin, cos)
            angles.append(math.degrees(angle)/180)

            # Find point values for specific connected groups of joints
            x1 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].x
            y1 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].y
            x2 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].x
            y2 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].y
            x3 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].x
            y3 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].y
            
            # Take differences between the different points to find 2D vector x and y components
            x_diff_1 = x2 - x1
            x_diff_2 = x2 - x3
            y_diff_1 = y2 - y1
            y_diff_2 = y2 - y3

            # determine the angle between the 2 vectors
            dot = x_diff_1*x_diff_2 + y_diff_1*y_diff_2      # dot product between [x1, y1] and [x2, y2]
            det = x_diff_1*y_diff_2 - y_diff_1*x_diff_2      # determinant
            angle = math.atan2(det, dot)  # atan2(y, x) or atan2(sin, cos)
            angles.append(math.degrees(angle)/180)

            # Find point values for specific connected groups of joints
            x1 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].x
            y1 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].y
            x2 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].x
            y2 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].y
            x3 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].x
            y3 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].y
            
            # Take differences between the different points to find 2D vector x and y components
            x_diff_1 = x2 - x1
            x_diff_2 = x2 - x3
            y_diff_1 = y2 - y1
            y_diff_2 = y2 - y3

            # determine the angle between the 2 vectors
            dot = x_diff_1*x_diff_2 + y_diff_1*y_diff_2      # dot product between [x1, y1] and [x2, y2]
            det = x_diff_1*y_diff_2 - y_diff_1*x_diff_2      # determinant
            angle = math.atan2(det, dot)  # atan2(y, x) or atan2(sin, cos)
            angles.append(math.degrees(angle)/180)

            # Find point values for specific connected groups of joints
            x1 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].x
            y1 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].y
            x2 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].x
            y2 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].y
            x3 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].x
            y3 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y
            
            # Take differences between the different points to find 2D vector x and y components
            x_diff_1 = x2 - x1
            x_diff_2 = x2 - x3
            y_diff_1 = y2 - y1
            y_diff_2 = y2 - y3

            # determine the angle between the 2 vectors
            dot = x_diff_1*x_diff_2 + y_diff_1*y_diff_2      # dot product between [x1, y1] and [x2, y2]
            det = x_diff_1*y_diff_2 - y_diff_1*x_diff_2      # determinant
            angle = math.atan2(det, dot)  # atan2(y, x) or atan2(sin, cos)
            angles.append(math.degrees(angle)/180)

            # Find point values for specific connected groups of joints
            x1 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].x
            y1 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].y
            x2 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].x
            y2 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y
            x3 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].x
            y3 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].y
            
            # Take differences between the different points to find 2D vector x and y components
            x_diff_1 = x2 - x1
            x_diff_2 = x2 - x3
            y_diff_1 = y2 - y1
            y_diff_2 = y2 - y3

            # determine the angle between the 2 vectors
            dot = x_diff_1*x_diff_2 + y_diff_1*y_diff_2      # dot product between [x1, y1] and [x2, y2]
            det = x_diff_1*y_diff_2 - y_diff_1*x_diff_2      # determinant
            angle = math.atan2(det, dot)  # atan2(y, x) or atan2(sin, cos)
            angles.append(math.degrees(angle)/180)

            # Find point values for specific connected groups of joints
            x1 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].x
            y1 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].y
            x2 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].x
            y2 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].y
            x3 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE].x
            y3 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE].y
            
            # Take differences between the different points to find 2D vector x and y components
            x_diff_1 = x2 - x1
            x_diff_2 = x2 - x3
            y_diff_1 = y2 - y1
            y_diff_2 = y2 - y3

            # determine the angle between the 2 vectors
            dot = x_diff_1*x_diff_2 + y_diff_1*y_diff_2      # dot product between [x1, y1] and [x2, y2]
            det = x_diff_1*y_diff_2 - y_diff_1*x_diff_2      # determinant
            angle = math.atan2(det, dot)  # atan2(y, x) or atan2(sin, cos)
            angles.append(math.degrees(angle)/180)

            # Find point values for specific connected groups of joints
            x1 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].x
            y1 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].y
            x2 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE].x
            y2 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE].y
            x3 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE].x
            y3 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE].y
            
            # Take differences between the different points to find 2D vector x and y components
            x_diff_1 = x2 - x1
            x_diff_2 = x2 - x3
            y_diff_1 = y2 - y1
            y_diff_2 = y2 - y3

            # determine the angle between the 2 vectors
            dot = x_diff_1*x_diff_2 + y_diff_1*y_diff_2      # dot product between [x1, y1] and [x2, y2]
            det = x_diff_1*y_diff_2 - y_diff_1*x_diff_2      # determinant
            angle = math.atan2(det, dot)  # atan2(y, x) or atan2(sin, cos)
            angles.append(math.degrees(angle)/180)

            # Find point values for specific connected groups of joints
            x1 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x
            y1 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y
            x2 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].x + results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x
            y2 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y + results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y
            x3 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].x
            y3 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y
            
            # Take differences between the different points to find 2D vector x and y components
            x_diff_1 = x2 - x1
            x_diff_2 = x2 - x3
            y_diff_1 = y2 - y1
            y_diff_2 = y2 - y3

            # determine the angle between the 2 vectors
            dot = x_diff_1*x_diff_2 + y_diff_1*y_diff_2      # dot product between [x1, y1] and [x2, y2]
            det = x_diff_1*y_diff_2 - y_diff_1*x_diff_2      # determinant
            angle = math.atan2(det, dot)  # atan2(y, x) or atan2(sin, cos)
            angles.append(math.degrees(angle)/180)

            angles_list.append(angles)

        if cv2.waitKey(5) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

    return np.array(angles_list)


def dtw_mapping(video1_keypoints, video2_keypoints):
    distance, path = fastdtw(
        video1_keypoints, video2_keypoints, dist=euclidean)
    return distance, path


def compare_videos(video1, video2):
    video1_keypoints = extract_keypoints(video1)
    video2_keypoints = extract_keypoints(video2)

    distance, path = dtw_mapping(video1_keypoints, video2_keypoints)

    total_frames = len(path)
    avg_distance = distance / total_frames

    # Normalize the score to a range of 1-100
    max_possible_distance = np.sqrt(2)

    print(max_possible_distance)
    print(avg_distance)
    print(path)

    total_error = 0

    for pair in path:
        y1 = video1_keypoints[pair[0]] 
        y2 = video2_keypoints[pair[1]]
        error = abs(y2 - y1)
        total_error += error

    average_error = (total_error / total_frames) * 50

    print(distance)
    print(average_error)

    total_average_error = 0
    most_error = -1
    most_error_index = -1
    least_error = 101
    least_error_index = -1
    for i in range(len(average_error)):
        if (most_error < average_error[i]):
            most_error = average_error[i]
            most_error_index = i
        if (least_error > average_error[i] and i != 8):
            least_error = average_error[i]
            least_error_index = i
        total_average_error += average_error[i]
    
    total_average_error = total_average_error / len(average_error)
    
    score = 100 - (total_average_error) * (total_average_error) / 10

    if score < 0:
        score = 0

    return score, least_error_index, most_error_index

def joint_from_index(argument):
    switcher = {
        0: "Right Arm",
        1: "Right Shoulder",
        2: "Right Hip",
        3: "Right Leg",
        4: "Left Arm",
        5: "Left Shoulder",
        6: "Left Hip",
        7: "Left Leg",
        8: "Head"
    }

    # get() method of dictionary data type returns
    # value of passed argument if it is present
    # in dictionary otherwise second argument will
    # be assigned as default value of passed argument
    return switcher.get(argument, "ERROR")


video1 = "jj_6s.mp4"
video2 = "armstretch_6s.mp4"
score, least_error_index, most_error_index = compare_videos(video1, video2)

    
best_attribute = joint_from_index(least_error_index)
worst_attribute = joint_from_index(most_error_index)

print(f"The similarity score between the two videos is: {score:.2f}")



dict = {
    "score": score,
    "best_attribute": best_attribute,
    "worst_attribute": worst_attribute,
    "best_attribute_": least_error_index,
    "worst_attribute_": most_error_index
}

print(dict)

# Serializing json
json_object = json.dumps(dict, indent=4)
 
# Writing to sample.json
with open("analysis_output.json", "w") as outfile:
    outfile.write(json_object)
