#!/usr/bin/env python3

from jjcli import *
import yaml

docs = glob("ComUM/*.md")
#print(f"Nos: {len(docs)}")
cl = clfilter("")
cl.args = sorted(docs)

out = open("corpus-comum.txt", "w", encoding="utf-8")
for txt in cl.text():
    #print(txt[:100])
    for meta, body in re.findall('---(.*?)---(.*)', txt, flags = re.S):
        print(f"@ {cl.filename()}\n", body, file = out)

