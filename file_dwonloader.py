import requests
import wget
api_token = "5414212374:AAGBm69kU555CJ_lYbQeS1GRentMRp5Bu-E"
get_update = requests.get(f"https://api.telegram.org/bot{api_token}/getUpdates").json()
files = []
for mas in get_update['result']:
    if "document" in mas["message"] :
        files.append({"file_name": str(mas["message"]["document"]["file_name"]),"file_id":str(mas["message"]["document"]["file_id"])})
print("whoce file by enter number : ")
for f_ile in files:
    print(f"{files.index(f_ile)} - {f_ile['file_name']}")
num_file = int(input(" enter file number : "))
get_file = requests.get(
    f"https://api.telegram.org/bot{api_token}/getFile?file_id={files[num_file]['file_id']}").json()

url = f'https://api.telegram.org/file/bot{api_token}/{get_file["result"]["file_path"]}'
filename = wget.download(url,out=files[num_file]['file_name'])