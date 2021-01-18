#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Text1 = """The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you."""


# In[ ]:


Text2 = """The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you."""


# In[ ]:


#A common set of contracting words was used from the link below.
#https://gist.github.com/nealrs/96342d8231b75cf4bb82
cList = {
  "ain't": "am not",
  "aren't": "are not",
  "can't": "cannot",
  "can't've": "cannot have",
  "'cause": "because",
  "could've": "could have",
  "couldn't": "could not",
  "couldn't've": "could not have",
  "didn't": "did not",
  "doesn't": "does not",
  "don't": "do not",
  "hadn't": "had not",
  "hadn't've": "had not have",
  "hasn't": "has not",
  "haven't": "have not",
  "he'd": "he would",
  "he'd've": "he would have",
  "he'll": "he will",
  "he'll've": "he will have",
  "he's": "he is",
  "how'd": "how did",
  "how'd'y": "how do you",
  "how'll": "how will",
  "how's": "how is",
  "I'd": "I would",
  "I'd've": "I would have",
  "I'll": "I will",
  "I'll've": "I will have",
  "I'm": "I am",
  "I've": "I have",
  "isn't": "is not",
  "it'd": "it had",
  "it'd've": "it would have",
  "it'll": "it will",
  "it'll've": "it will have",
  "it's": "it is",
  "let's": "let us",
  "ma'am": "madam",
  "mayn't": "may not",
  "might've": "might have",
  "mightn't": "might not",
  "mightn't've": "might not have",
  "must've": "must have",
  "mustn't": "must not",
  "mustn't've": "must not have",
  "needn't": "need not",
  "needn't've": "need not have",
  "o'clock": "of the clock",
  "oughtn't": "ought not",
  "oughtn't've": "ought not have",
  "shan't": "shall not",
  "sha'n't": "shall not",
  "shan't've": "shall not have",
  "she'd": "she would",
  "she'd've": "she would have",
  "she'll": "she will",
  "she'll've": "she will have",
  "she's": "she is",
  "should've": "should have",
  "shouldn't": "should not",
  "shouldn't've": "should not have",
  "so've": "so have",
  "so's": "so is",
  "that'd": "that would",
  "that'd've": "that would have",
  "that's": "that is",
  "there'd": "there had",
  "there'd've": "there would have",
  "there's": "there is",
  "they'd": "they would",
  "they'd've": "they would have",
  "they'll": "they will",
  "they'll've": "they will have",
  "they're": "they are",
  "they've": "they have",
  "to've": "to have",
  "wasn't": "was not",
  "we'd": "we had",
  "we'd've": "we would have",
  "we'll": "we will",
  "we'll've": "we will have",
  "we're": "we are",
  "we've": "we have",
  "weren't": "were not",
  "what'll": "what will",
  "what'll've": "what will have",
  "what're": "what are",
  "what's": "what is",
  "what've": "what have",
  "when's": "when is",
  "when've": "when have",
  "where'd": "where did",
  "where's": "where is",
  "where've": "where have",
  "who'll": "who will",
  "who'll've": "who will have",
  "who's": "who is",
  "who've": "who have",
  "why's": "why is",
  "why've": "why have",
  "will've": "will have",
  "won't": "will not",
  "won't've": "will not have",
  "would've": "would have",
  "wouldn't": "would not",
  "wouldn't've": "would not have",
  "y'all": "you all",
  "y'alls": "you alls",
  "y'all'd": "you all would",
  "y'all'd've": "you all would have",
  "y'all're": "you all are",
  "y'all've": "you all have",
  "you'd": "you had",
  "you'd've": "you would have",
  "you'll": "you will",
  "you'll've": "you you will have",
  "you're": "you are",
  "you've": "you have"
}


# In[ ]:


#A common list of stop word was used from the link below.
#https://gist.github.com/sebleier/554280

stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]


# In[ ]:


def textSimilarity(Text1, Text2):
    
    Text1 = Text1.lower()
    Text2 = Text2.lower()
    
    #replacing characters from text
    Text1 = Text1.replace('.', '').replace(',', '')
    Text2 = Text2.replace('.', '').replace(',', '')
    
    #splitting the text based on space
    splitList = []
    for i in Text1.split(" "):
        splitList.append(i)
    #saving the splitted text into dictionary
    splitDict = {}
    for i in range(len(splitList)):
        splitDict[i] = splitList[i]
        
    #removing contracting words in 1st sentence
    for key, value in splitDict.items():
        #print(splitDict[key])
        if splitDict[key] in cList.keys():
            #print(splitDict[key])
            #print(cList[splitDict[key]])
            splitDict[key] = cList[splitDict[key]]
            
    #removing the stop words. Dictionary is used insdide a list to avoid RuntimeError: dictionary changed size during iteration
    for key, value in list(splitDict.items()):
        if splitDict[key] in stopwords:
            #print(splitDict[key])
            del splitDict[key]
    
    splitList2 = []
    for i in Text2.split(" "):
        splitList2.append(i)
        
    splitDict2 = {}
    for i in range(len(splitList2)):
        splitDict2[i] = splitList2[i]
    
    #removing contracting words in 2nd sentence
    for key, value in splitDict2.items():
        if splitDict2[key] in cList.keys():
            splitDict2[key] = cList[splitDict[key]]
            
    #removing the stop words. Dictionary is used insdide a list to avoid RuntimeError: dictionary changed size during iteration
    for key, value in list(splitDict2.items()):
        if splitDict2[key] in stopwords:
            #print(splitDict2[key])
            del splitDict2[key]
    
    #exact match along with position of the words
    count = 0
    for key, value in splitDict.items():
        if splitDict[key] == splitDict2[key]:
            count = count + 1
            if count == len(splitDict):
                print("1")
                return 1
        else:
            print("0")
            return '0'
            break
            


# In[ ]:


textSimilarity(Text1, Text2)


# In[ ]:




