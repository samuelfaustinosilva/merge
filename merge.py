#!/usr/bin/env python
# coding: utf-8

# ### Bibliotecas 

# In[5]:


import pandas as pd


# ### Carregamento de dados

# In[7]:


acessos = pd.read_excel('compras_e_acessos.xlsx', sheet_name='acessos')


# In[8]:


acessos


# In[9]:


compras = pd.read_excel('compras_e_acessos.xlsx', sheet_name='compras')


# In[10]:


compras


# ### Merge

# #### SQL JOIN: Usuários que tem acessos E comrpas, trazendo também as informações de ambas as tabelas

# In[11]:


inner_join = acessos.merge(compras, how='inner', on='user_id')


# In[12]:


inner_join


# #### SQL LEFT JOIN: Usuários que têm acessos, mas também queremos trazer o total de compras, caso tenham feito

# In[16]:


left_join = acessos.merge(compras, how='left', on='user_id')


# In[17]:


left_join


# #### SQL RIGHT JOIN: Usuários que tem compras, mas também trazer o total de acessos, caso tenham feito

# In[18]:


right_join = acessos.merge(compras, how='right', on='user_id')


# In[19]:


right_join


# #### SQL FULL JOIN: Usuários que tem acessos OU compras, trazendo as informações de âmbos, caso existam

# In[23]:


full_join = acessos.merge(compras, how='outer', on='user_id')


# In[24]:


full_join


# In[ ]:




