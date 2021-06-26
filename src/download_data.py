
# USAGE
# python download_data.py
#
# dependencies: 
#   wget
#
# AIM:
# Download the protein interactions to create a network analysis for the posterior analysis

import wget

url = "https://stringdb-static.org/download/protein.links.v11.0/9606.protein.links.v11.0.txt.gz"
path = 'data/'
wget.download(url,out = path)
