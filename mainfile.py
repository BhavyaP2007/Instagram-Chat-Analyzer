import json
import pandas as pd
from pathlib import Path
root_dir = Path(__file__).parent
root_dir = str(root_dir).replace("\\","/")
import detect_image,detect_video,detect_text
toxic_messages = pd.DataFrame(columns=['ChatWith', 'Message', 'Type_of_message', 'Type_of_message_score','Remark']) 
toxic_photos = pd.DataFrame(columns=['ChatWith', 'photo_path']) 
toxic_videos = pd.DataFrame(columns=['ChatWith', 'video_path'])  
def check_data(d):
    messages_data = {"sender":[],"message":[]}
    person = d["participants"][0]["name"]
    for i in d["messages"]:
        if "content" in list(i.keys()):
            messages_data["sender"].append(i["sender_name"])
            messages_data["message"].append(i["content"])
    
    df = pd.DataFrame(data=messages_data)  
    for i in df["message"]:
        message_type = detect_text.checktext(i)
        type_of_message = []
        type_of_message_score = []
        for k,v in message_type.items():
            if v>=0.7:
                type_of_message.append(k)
                type_of_message_score.append(v)
                if v<0.8:
                    remark = "Consider softening the tone for a more respectful conversation."
                elif v<0.9:
                    remark="This text includes toxic language that could be offensive or disrespectful."
                else:
                    remark="This message contains extremely harmful or abusive language."      
        if len(type_of_message)>=1:       
            return [person,i,type_of_message,type_of_message_score,remark] 
        else:
            pass        

def zip_check(dir_of_people):
    for person_folder in Path(dir_of_people).iterdir():
        for json_file in person_folder.glob("*.json"):
            json_file = str(json_file).replace("\\","/")
            f = open(str(json_file))
            d = json.load(f)
            text_data = check_data(d)
            if text_data is not None:
                toxic_messages.loc[len(toxic_messages)]=text_data
        photos_dir = str(person_folder).replace("\\","/")+"/photos"
        for photo in Path(photos_dir).glob("*.*"):
            if photo.suffix.lower() in [".jpg", ".jpeg", ".png", ".bmp", ".gif"]:   
                a,b = detect_image.check_image(str(photo).replace("\\","/"))  
                if b:
                    file = open(str(person_folder).replace("\\","/")+"/message_1.json")
                    data_of_file = json.load(file)
                    person = data_of_file["participants"][0]["name"]
                    toxic_photos.loc[len(toxic_photos)] = [person,photo]
        video_dir = str(person_folder).replace("\\","/")+"/videos"
        for video in Path(video_dir).glob("*.*"):
            if video.suffix.lower() in [".mp4", ".avi", ".mov"]:   
                b = detect_video.check_video(str(video).replace("\\","/"),root_dir+"temp.jpg")  
                if b==True:
                    file = open(str(person_folder).replace("\\","/")+"/message_1.json")
                    data_of_file = json.load(file)
                    person = d["participants"][0]["name"]
                    toxic_videos.loc[len(toxic_videos)] = [person,str(video)]  
    return [toxic_messages,toxic_photos,toxic_videos]                 