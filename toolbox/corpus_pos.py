#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from text_tool import textPurger
from ArticutAPI import Articut
import json

accountDICT = json.load(open("account.info",encoding="utf-8"))
articut = Articut(username=accountDICT["username"],apikey=accountDICT["apikey"])

def purge_pos_loc_zai(startLine, lastLine):
    purgedDICT = {}
    with open("../corpus/Sketch Engine 在.txt", encoding="utf-8") as f:
        lines = ''.join(f.readlines())
        rawLIST = textPurger(lines).split("\n")
        purgedLIST = []
        [purgedLIST.append(x) for x in rawLIST if x not in purgedLIST]
        #print(purgedLIST)
    with open("../purged corpus/loc_zai_purged.txt", 'w', encoding = "utf-8") as g:
        for j in range(startLine, lastLine):#4539
            #print(purgedLIST[j])
            #purgedDICT['{}'.format(purgedLIST[j])] = ''.join(articut.parse(purgedLIST[j])['result_pos'])
            #print(purgedDICT)
            #g.write(''.join(articut.parse(purgedLIST[j])['result_pos'])+"\n")
        #json.dump(purgedDICT,g, ensure_ascii=False)
            g.write(purgedLIST[j]+"\n"+''.join(articut.parse(purgedLIST[j])['result_pos'])+"\n")
            print(j)
    #print(purgedDICT)

if __name__ == "__main__":
    purge_pos_loc_zai(5,4539)