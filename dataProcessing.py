import pandas as pd
import zipfile
import os

with zipfile.ZipFile('data/cur.zip','r') as zip:
    with zip.open('output.csv') as file:
        df = pd.read_csv(file, low_memory=False)
        
        # condition1
        filt = (df['lineItem/UsageAccountId'] == 467262080079) & (df['lineItem/UsageType'] == 'EU-DataTransfer-Out-Bytes') & (df['product/ProductName'] == 'Amazon CloudFront') & (df['lineItem/LineItemType'] == 'Usage')
        UnblendedRate = 0.05
        df.loc[filt, ['lineItem/UnblendedRate']] = UnblendedRate
        modify = df['Unnamed: 0'].loc[filt]
        for i in modify:
            df.loc[df['Unnamed: 0'] == i, ['lineItem/UnblendedCost']] = df['lineItem/UsageAmount'].loc[df['Unnamed: 0'] == i] * UnblendedRate
            originStr = df['lineItem/LineItemDescription'].loc[df['Unnamed: 0'] == i].to_string()
            split = originStr.split("per")
            s = "$0.05" + split[-1]
            df.loc[df['Unnamed: 0'] == i, ['lineItem/LineItemDescription']] = s
   
        # condition2
        filt2 = (df['lineItem/UsageAccountId'] == 467262080079) & (df['lineItem/UsageType'] == 'AU-DataTransfer-Out-Bytes') & (df['product/ProductName'] == 'Amazon CloudFront') & (df['lineItem/LineItemType'] == 'Usage')
        UnblendedRate2 = 0.033
        df.loc[filt2, ['lineItem/UnblendedRate']] = UnblendedRate2
        modify = df['Unnamed: 0'].loc[filt2]
        for i in modify:
            df.loc[df['Unnamed: 0'] == i, ['lineItem/UnblendedCost']] = df['lineItem/UsageAmount'].loc[df['Unnamed: 0'] == i] * UnblendedRate2
            originStr = df['lineItem/LineItemDescription'].loc[df['Unnamed: 0'] == i].to_string()
            split = originStr.split("per")
            s = "$0.033" + split[-1]
            df.loc[df['Unnamed: 0'] == i, ['lineItem/LineItemDescription']] = s
        

        # split data by UsageAccountId, create output folder and save zip in it
        os.mkdir('output')
        os.chdir('output')
        accounts = df['lineItem/UsageAccountId'].unique()
        for account in accounts:
            newDf = df[df['lineItem/UsageAccountId'] == account]
            newDf = newDf.drop(['Unnamed: 0'], axis=1)
            newDf.reset_index(inplace=True, drop=True)
            newDf.to_csv(f'{account}.csv.zip', compression='zip')           
            os.rename(f'{account}.csv.zip', f'{account}.zip')


