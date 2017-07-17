#!/usr/bin/python
# -*- coding: utf-8 -*-
# AutoDownloader files of server
# Data: 17/07/2017
# Desenvolvedor: Rúben Silva

# Imports

import sys
import os

#########

def converter(link, fileType):
	padrao = 'wget -r -l 1 -nd -nH -A '
	downloader = padrao + fileType + ' ' + link
	return downloader
	
def ajuda():
		return """
USAGE:  python AutoDownloader.py [Extensão do Ficheiro] [Server]
		
        Ex:
        python AutoDownloader.py pdf http://127.0.0.1 
	python AutoDownloader.py docx https://127.0.0.1 
"""

#########

if len(sys.argv) > 1:
	if sys.argv[1] == '-h':
		print ajuda()
		sys.exit(0)

print """
+-----------------------------------------------------+
|                    AutoDownloader                   |
+-----------------------------------------------------+
                      Rúben Silva 
"""

try:
	fileType = sys.argv[1]
	link = sys.argv[2]
	downloader = converter(link, fileType)
	print(downloader)

except:
	print ajuda()
	sys.exit(0)

try:
	os.system(downloader)

except:
	print ('Não foi possivel aceder ao servidor ou não existem arquivos com essa extensão no servidor')
	sys.exit(0)
	
