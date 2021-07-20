import requests
import json
import pandas as pd


data=pd.read_csv(r'C:\Users\abhis\OneDrive\Documents\thesisProjectCode\scopus (1).csv')

data_df=pd.DataFrame(data,columns=['DOI','ISSN'])
data_df=data_df.dropna()
data_df=data_df.drop_duplicates(subset=['ISSN'])
data_df['ISSN']=data_df['ISSN'].astype(str)

snip_list=[]
srj_list=[]
citeScore_list=[]
issn_list=[]

for element in data_df['ISSN']:
    base='https://api.elsevier.com/content/serial/title/issn/'
    ap=element
    end='?apikey=ff79f5ec4a6420c9ae1bdf606f9d56e5'
    url=base+ap+end
    print(url)

    myResponse = requests.get(url)

    jsonResponse = myResponse.json()
    
    if "service-error" in jsonResponse:
    
        jsonResponse.pop('service-error', None)
        
    else:
      
        for data in jsonResponse['serial-metadata-response']['entry']:
                        
            if "SNIPList" in data:
                snip=data['SNIPList']['SNIP'][0]['$']
                snip_list.append(snip)
    
            else:
                snip_list.append(0)
                
            if "SJRList" in data:
                srj=data['SJRList']['SJR'][0]['$']
                srj_list.append(srj)
                
            else:
                srj_list.append(0) 
                
            if "citeScoreYearInfoList" in data:
                citeScore=data['citeScoreYearInfoList']['citeScoreCurrentMetric']
                citeScore_list.append(citeScore) 

            else:
                citeScore_list.append(0)    
    
            issn_list.append(element)


venu_data=pd.DataFrame(columns=['issn_details','sjr_details','snip_details','citeScore'])
venu_data['issn_details']=issn_list
venu_data['sjr_details']=srj_list
venu_data['snip_details']=snip_list
venu_data['citeScore']=citeScore_list

