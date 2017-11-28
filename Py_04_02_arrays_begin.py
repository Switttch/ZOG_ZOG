
# coding: utf-8

# In[ ]:


#ZOG_ZOG
import numpy as np
writer = pd.ExcelWriter('output.xlsx')
df2.to_excel(writer,'Sheet1')
writer.save()
get_ipython().magic('pwd')
df3=pd.DataFrame(df1, columns=['whs', 'div', 'yr', 'mnth', 'salesvalue', 'TAC'])
df3

