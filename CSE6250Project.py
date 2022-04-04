import pandas as pd
import numpy as np
import sklearn as sk
import string
import itertools
from collections import Counter
diaglist=["250"]

def extractData():
    noteEvents=pd.read_csv("mimic-iii-clinical-database-1.4/NOTEEVENTS.csv")
    noteEvents=noteEvents[["HADM_ID","TEXT","DESCRIPTION"]]
    diagnosis = pd.read_csv("mimic-iii-clinical-database-1.4/DIAGNOSES_ICD.csv")
    diagnosis = diagnosis[["HADM_ID","SUBJECT_ID","ICD9_CODE"]]

    #Group Diagnosis into 1 list per admission
    diagnosisGrouped = diagnosis.groupby(["SUBJECT_ID","HADM_ID"])["ICD9_CODE"].apply(list).reset_index()

    def checkdiagnosis(x):
        for code in x:
            if str(code)[0:3]=="250":
                return True
        return False

    #filter
    admissionswithDiabetes = diagnosisGrouped[diagnosisGrouped["ICD9_CODE"].apply(lambda x: checkdiagnosis(x))]

    patlist=admissionswithDiabetes["SUBJECT_ID"].tolist()
    HADMlist=admissionswithDiabetes["HADM_ID"].tolist()

    combineddf=noteEvents.merge(admissionswithDiabetes, on="HADM_ID")
    filtereddf=combineddf

    #filteredNotes = noteEvents[noteEvents["HADM_ID"].apply(lambda x: x in HADMlist)]
    filtereddf=filtereddf[filtereddf["TEXT"].apply(lambda x: len(x)>0])
    combineddf.to_csv("PreFilteredData.csv")
    return filtereddf

    #406190 expected count per paper

# Preprocessing instructions
# (1) Punctuation characters, except for the apostrophe, are converted to whitespace
# (2) Digits are replaced by the character ’d’
# (3) All characters are converted to lowercase
# (4) The report is split at whitespace characters
def preProcesstext(filtereddf):
    processeddf=filtereddf.copy()
    spacestring=" "*len(string.punctuation.replace("'",""))
    dstring="d"*len(string.digits)
    processeddf["TEXT"]=processeddf["TEXT"].apply(lambda x: x.translate(str.maketrans(string.punctuation.replace("'",""),spacestring)))
    processeddf["TEXT"] = processeddf["TEXT"].apply(lambda x: x.translate(str.maketrans(string.digits,dstring)))
    processeddf["TEXT"] = processeddf["TEXT"].apply(lambda x: x.lower())
    processeddf["TEXT"] = processeddf["TEXT"].apply(lambda x: x.split())
    wordslist=processeddf["TEXT"].tolist()
    flatlist=list(itertools.chain(*wordslist))
    wordset=set(flatlist)
    wordDict=Counter(flatlist)
    wordDict5orMore= dict(filter(lambda x: x[1] >=5, wordDict.items())) #53229
    wordDictLessThan5 = dict(filter(lambda x: x[1] <=5, wordDict.items()))
    pass

    #162784 tokens to 53229 unique tokens post Levenshtein





if __name__ == '__main__':
    filtereddf = extractData()
    preprocesseddf = preProcesstext(filtereddf)

