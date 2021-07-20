from pybliometrics.scopus import PlumXMetrics
import pandas as pd
import numpy as np

#ff79f5ec4a6420c9ae1bdf606f9d56e5

data=pd.read_csv(r'C:\Users\abhis\OneDrive\Documents\thesisProjectCode\scopus.csv')

data_df=pd.DataFrame(data,columns=['DOI'])
data_df=data_df.dropna()
data_df['DOI']=data_df['DOI'].astype(str)

#data_df=data_df.set_index('DOI')

summary_data=pd.DataFrame(columns=['capture_details','socialmedia_details','citation_details','usage_details',
                                   'mention_details'])

summary_data=pd.concat([summary_data,data_df])
summary_data=summary_data.set_index('DOI')

def get_plumx_data(a):
    plum = PlumXMetrics(a, id_type='doi')
    return plum


for i, row in summary_data.iterrows():
    
    b=i
    print(row[0])
    plum=get_plumx_data(b)
   
    if plum.capture == None:
     print("data unavailable")
     row[0]=0                              

    else:
        t_cap=pd.DataFrame(plum.capture)
        t1=t_cap['total'].sum()
        row[0]=t1
        
        print("data available")

    if plum.social_media == None:
        print("data unavailable")
        row[3]=0                              

    else:        
        t_social=pd.DataFrame(plum.social_media)
        t2=t_social['total'].sum()
        row[3]=t2
 
        
        print("data available")
    
    
    if plum.citation == None:
        print("data unavailable")
        row[1]=0                              

    else:
        t_cite=pd.DataFrame(plum.citation)
        t3=t_cite['total'].sum()
        row[1]=t3
        print("data available")

    if plum.usage == None:
        
        print("data unavailable")
        row[4]=0                             

    else:
        t_usage=pd.DataFrame(plum.usage)
        t4=t_usage['total'].sum()
        row[4]=t4
        print("data available")

    if plum.mention == None:
        
        print("data unavailable")
        row[2]=0                              

    else:
        t_mention=pd.DataFrame(plum.mention)
        t5=t_mention['total'].sum()
        row[2]=t5
        print("data available")


