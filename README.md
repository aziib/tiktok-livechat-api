# Tiktok Live Chat Local Api
make your own local api and fetching from Tiktok Live chat to send to LLM chat.


## Description
this was tested on sillytavern ai live chat extension [https://github.com/aziib/Extension-LiveChat](https://github.com/aziib/Extension-LiveChat)

if you like my code and used it, please support me on ko-fi [https://ko-fi.com/megaaziib](https://ko-fi.com/megaaziib)

your support help me improved on this project.

☢ You will need to take full responsibility for your action ☢

## Requirements
Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)

i'm using python 3.11, don't know if other version will work

make sure you tick check add to path when installing the python

Git: [https://git-scm.com/downloads](https://git-scm.com/downloads)

## Install Manually
1. Clone this repository
```git
git clone https://github.com/aziib/tiktok-livechat-api
```
2. go to the folder and Setup virtual environment
```python
python -m venv venv
```
3. Activate virtual environment (always use this command first when to execute any python scripts)
```python
.\venv\Scripts\activate
```
4. Install requirements
```python
pip install -r requirements.txt
```
5. Go Live on tiktok and then run the fetchingtiktok-testing.py to test fetching the comments, insert your @username and try commenting on tiktok live and see if it also displayed in the cmd or terminal
```python
    python fetchtiktok-testing.py
```
6. if it display correctly, close it and Run fetch-tiktok-live.py and insert your @username , it will fetch the live comments again but also saved it as json file named chat_saved.json. do not close the cmd or terminal, don't open the json file or deleted it until you want to end your stream. (only delete the chat_saved.json file if you want to start new live stream)
```python
    python fetch-tiktok-live.py
```
8. Run app.py to run the API, it will send the chat_saved.json to the api,  it will create local api at port 5006 and then you can get the api calls by type http://127.0.0.1:5006/chat
```python
    python app.py
```
