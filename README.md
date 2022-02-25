# HW-Data-ETL
Data processing of ETL

Step1: <br>
&emsp;&emsp; 1. &ensp; Filter data by __lineItem/UsageAccountId__, __lineItem/UsageType__, __product/ProductName__ and __lineItem/LineItemType__.<br>
&emsp;&emsp; 2. &ensp; Find the index of filtered data.<br>

Step2: <br>
&emsp;&emsp; 1. &ensp; Change the value of __lineItem/UnblendedRate__, __lineItem/UnblendedCost__ and __lineItem/LineItemDescription__ with specific value in json.<br>
&emsp;&emsp; 2. &ensp; Create output folder and split the .csv by __lineItem/UsageAccountId__, and save in .zip.
