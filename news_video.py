import requests
import json

class VideoGenerator:
    def __init__(self,api_key):
        self.api_key = api_key 

    def generate_video(self,text,img_url):
        url = "https://api.d-id.com/talks"

        payload = {
                "script":{
                    "type":"text",
                    "subtitles":"false",
                    "provider":{
                        "type":"microsoft",
                        "voice_id":"en-US-JennyNeural"
                    },
                    "ssml":"false",
                    "input":text
                },
                "config":{
                    "stitch":"true",
                    "fluent":"false",
                    "pad_audio":"0.0"
                },
                "source_url":img_url
            } 
        headers = {
                "accept":"application/json",
                "content-type":"application/json",
                "authorization":self.api_key

            }
        resp = requests.post(url,json=payload,headers=headers)
        _resp = json.loads(resp.text)
        print(_resp)
        while _resp['status'] != "created":
                resp = requests.post(url,json=payload,headers=headers)
                _resp = json.loads(resp.text)

        talk_id = json.loads(resp.text)['id']
        talk_url = f"{url}/{talk_id}"
    
        headers = {
                "accept":"application/json",
                "authorization":self.api_key
            }    

        resp = requests.get(talk_url,headers=headers)
        video_response = json.loads(resp.text)
        while video_response["status"] != "done":
                resp = requests.get(talk_url,headers=headers)
                video_response = json.loads(resp.text)

        return video_response['result_url']
    
    
