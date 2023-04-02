import cv2
import mediapipe as mp
import numpy as np
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean


def extract_keypoints(video_file):
    cap = cv2.VideoCapture(video_file)
    mp_pose = mp.solutions.pose
    mp_drawing = mp.solutions.drawing_utils
    pose = mp_pose.Pose()

    keypoints_list = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(image)

        if results.pose_landmarks:
            keypoints = []
            for lm in results.pose_landmarks.landmark:
                print(lm)
                keypoints.extend([lm.x, lm.y])
            keypoints_list.append(keypoints)

        if cv2.waitKey(5) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

    return np.array(keypoints_list)


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
    score = 100 * (1 - (avg_distance / max_possible_distance))

    return score


video1 = "jj_6s.mp4"
video2 = "jj_side_6s.mp4"
score = compare_videos(video1, video2)

print(f"The similarity score between the two videos is: {score:.2f}")