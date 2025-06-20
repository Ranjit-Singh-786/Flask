import requests
api_url = "http://192.168.0.48:1073/addmodifycamerasettings/save-empcam-details"

# JSON data you want to send
sample_data = {
"indId": "56",
"cameraId": "78",
"empcamDirection": "fghfgh",
"empcamInout": "fghfh",
"empcamRemark": "ewfrs",
"empcamDt": "23/09/2023",
"empcamTime": "23/09/2023 16:27:53"}

sample_data["indId"] = None 
sample_data["cameraId"] = "1" 
sample_data["empcamDt"] = "12/10/2025" 
sample_data["empcamTime"] = "10:25:23" 
sample_data['empcamDirection'] = None 
sample_data["empcamRemark"] = None 
sample_data["empcamInout"] = None 
if __name__ == '__main__':
    response = requests.post(api_url, json=sample_data)
    print("Successsfully sent the data : ",response.status_code)


