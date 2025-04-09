from nudenet import NudeDetector

detector = NudeDetector()

def check_image(target_url):
    results = detector.detect(target_url)
    explicit_classes = [
        'FEMALE_GENITALIA_EXPOSED', 'MALE_GENITALIA_EXPOSED',
        'BUTTOCKS_EXPOSED', 'FEMALE_BREAST_EXPOSED', 'ANUS_EXPOSED'
    ]

    is_nude = any([det['class'] in explicit_classes for det in results])
    return results,is_nude

###### DETECTION USING URL

# import requests
# import os
# from nudenet import NudeDetector

# def download_and_detect(image_url, save_path="C:/Users/bpmch/OneDrive/Desktop/python/ignition_hack/TEST.jpg"):
#     """
#     1. Downloads an image from a URL
#     2. Saves it to disk
#     3. Runs nudity detection
#     4. Returns results and keeps the saved file
#     """
#     # 1. Download the image
#     response = requests.get(image_url)
#     response.raise_for_status()  # Raise error if download fails
    
#     # 2. Save to disk
#     with open(save_path, "wb") as f:
#         f.write(response.content)
#     print(f"Image saved to: {os.path.abspath(save_path)}")
    
#     # 3. Initialize detector
#     detector = NudeDetector()
    
#     # 4. Detect nudity using the saved file
#     results = detector.detect(save_path)
    
#     # 5. Define explicit classes
#     explicit_classes = {
#         "FEMALE_GENITALIA_EXPOSED",
#         "MALE_GENITALIA_EXPOSED",
#         "BUTTOCKS_EXPOSED",
#         "FEMALE_BREAST_EXPOSED",
#         "ANUS_EXPOSED"
#     }
    
#     # 6. Check for nudity
#     is_nude = any(det["class"] in explicit_classes for det in results)
    
#     return is_nude, results, save_path

# # Example Usage
# if __name__ == "__main__":
#     # Test image URL (replace with your target URL)
#     test_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQw5pgbYRrPDicMehJ3HWyEeU7VI2ltBAse4Q&s"
    
#     try:
#         is_nude, details, saved_path = download_and_detect(test_url)
#         print(f"Nudity detected: {is_nude}")
#         print("Detailed results:", details)
#         print(f"Image saved at: {saved_path}")
#     except Exception as e:
#         print(f"Error: {e}")