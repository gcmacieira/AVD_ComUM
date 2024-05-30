
#### COMUM

titulos.txt: #objetivo      #Como construo esse objetivo e de quem ele depende
	python3 extraicom.py 

corpus-comum.txt: extrai-body.py
	python3 extrai-body.py

corpus-anotado.txt: corpus-comum.txt  anota.py  # a prtir do corpus UMS e da script anota,cria um corpus anotado #este objetivo depende destes dois ficheiros
	python3 anota.py corpus-comum.txt

# cálculo de frequência de verbos no nosso corpus e que, potencialmente, fosse descrevendo
verbos.txt: corpus-anotado.txt contaverbos.py
	python3 contaverbos.py corpus-anotado.txt 

propn.txt: corpus-anotado.txt contapropn.py
	python3 contapropn.py corpus-anotado.txt

loc.txt: corpus-anotado.txt contaloc.py
	python3 contaloc.py corpus-anotado.txt




#### NOS

titulosNos.txt: #objetivo      #Como construo esse objetivo e de quem ele depende
	python3 extraicom2.py 

corpus-nos.txt: extraibodynos.py
	python3 extraibodynos.py

corpus-anotadonos.txt: corpus-nos.txt  anotanos.py  # a prtir do corpus UMS e da script anota,cria um corpus anotado #este objetivo depende destes dois ficheiros
	python3 anotanos.py corpus-nos.txt

# cálculo de frequência de verbos no nosso corpus e que, potencialmente, fosse descrevendo
verbosnos.txt: corpus-anotadonos.txt contaverbosnos.py
	python3 contaverbosnos.py corpus-anotadonos.txt 

propnnos.txt: corpus-anotadonos.txt contapropnos.py
	python3 contapropnos.py corpus-anotadonos.txt

locnos.txt: corpus-anotadonos.txt contalocnos.py
	python3 contalocnos.py corpus-anotadonos.txt