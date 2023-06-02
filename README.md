# SpotWrap
### A graphical wrapper for Spotdl and Savify
### Gallery
### How to use
Paste your spotify song/album/playlist link to the search bar, hit enter,
then you can select the output type and the quality you want. Then simply click on Download.
### How to compile using pyinstaller and auto-py-to-exe
First you have to install the dependencies using pip, I recommend using a virtual environment
```bash
python -m venv venv
```
Then you have to activate the virtual environment:
- on windows : 
```bash
venv\Scripts\activate
```
- on linux:
```bash
source venv/bin/activate
```

Then you have to install the dependencies using pip
```bash 
pip install -r requirements.txt
```
Then you have to compile the python file using pyinstaller:
Screenshot of all the options to use: ![Screenshot](assets/images/how_to_bundle_spotwrap.png)
Then you have to add the pip package's `pykakasi` directory to the output directory of auto-py-to-exe for it to work.