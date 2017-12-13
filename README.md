goodreads books importer
=========

Python script to bulk-upload my google play books to goodreads:
- given json list of book titles, whether from google books or elsewhere, and a target shelf in goodreads 
- script will parse for best match in goodreads given the title
- result is the books will be added to the goodreads shelf

#### Usage

- `pip install -r requirements.txt`
- get goodreads api key and secret
- `touch config.json` and add keys following `config.json.example`
- get input data (list of book titles to upload) and save as json file to INPUT_TITLES_PATH
  - TODO add helper/alfred workflow to fetch from google books api
- `python main.py` 

Todo:
- FIX: this seems to be failing because the goodreads lib has not updated to Oauth2 