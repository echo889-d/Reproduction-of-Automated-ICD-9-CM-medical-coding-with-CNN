# CSE-6250-Project
CSE 6250 Project

Required Packages:
pandas
numpy
sklearn
string
itertools
collections
gensim.models
Levenshtein
pickle (if not rebuilding dictionary from scratch in cell #11)
fasttext
keras
tensorflow

Required Files for Data (From MIMIC-III): 
NOTEEVENTS.csv
DIAGNOSES_ICD.csv

Within the IPYNB file, this is stored in the mimic-iii-clinical-database-1.4 folder.

Pickle dictionary for Word-to-Word Mapping:
mapDictionary.pkl

Instructions and Functionality:
Run the IPYNB file in your local drive with the installed packages. See IPYNB Headers to see functionality of scripts. Code not needed to train the model may be commented out but serve other functionality such as calculation of Data statistics.

Explanation of BoT files:
BoT Base Submission - Base Model used for Table 3 - comparision of ICD-9 rolled-up and full codes which can be easily swapped under the "SET ROLLED UP CODES HERE" section/
For full IC9-Code - use "tokenized["ICD9_CODE"]. For rolled-up codes, used tokenized["ICD9_CODE_primary"]. 
For top 10 codes to be used in comparision to binary classification (Table 5) tokenized["Top_ICD9_Codes"]

BoT Cat 3 Dense Submission  - Code used for Table 4 to augment Base model with Category and further dense layers. Dense Layers can be easily added/moved from the concatenate_3dense function.

BoT Binary Base Submission - Code used for Table 5 to model using binary classification. 

