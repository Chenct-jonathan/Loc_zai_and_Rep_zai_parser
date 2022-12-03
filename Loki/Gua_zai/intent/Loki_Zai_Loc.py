#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Zai_Loc

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

import json
import os

DEBUG_Zai_Loc = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_asNoun":["@","《","》","「","」","『","』","【","】","（","）"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Zai_Loc:
        print("[Zai_Loc] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "在台灣":
        resultDICT["Zai"].append("Loc")

    if utterance == "在東方320公里外":
        resultDICT["Zai"].append("Loc")

    if utterance == "在浴室":
        resultDICT["Zai"].append("Loc")

    if utterance == "在福建省中":
        resultDICT["Zai"].append("Loc")

    if utterance == "在科學機構":
        resultDICT["Zai"].append("Loc")

    return resultDICT