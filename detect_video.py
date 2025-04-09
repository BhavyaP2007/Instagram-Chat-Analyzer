import cv2
from nudenet import NudeDetector

detector = NudeDetector()


def check_video(video_path,temp_path):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % 10 == 0:  # Process every 10th frame (to speed up)
            # Save frame temporarily
            frame_path = temp_path
            cv2.imwrite(frame_path, frame)

            # Run nude detection
            results = detector.detect(frame_path)

            # result format: {'temp_frame.jpg': {'safe': 0.2, 'unsafe': 0.8}}
            explicit_classes = [
            'FEMALE_GENITALIA_EXPOSED', 'MALE_GENITALIA_EXPOSED',
            'BUTTOCKS_EXPOSED', 'FEMALE_BREAST_EXPOSED', 'ANUS_EXPOSED']

            is_nude = any([det['class'] in explicit_classes for det in results])

            if is_nude:
                return is_nude


        frame_count += 1

xyz =5

