#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 00:35:23 2021

@author: shadabahmed
"""
import re
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
paragraph="""Of course, in one sense, the first essential for a man's being a good citizen is his possession of the home virtues of which we think when we call a man by the emphatic adjective of manly. No man can be a good citizen who is not a good husband and a good father, who is not honest in his dealings with other men and women, faithful to his friends and fearless in the presence of his foes, who has not got a sound heart, a sound mind, and a sound body; exactly as no amount of attention to civil duties will save a nation if the domestic life is undermined, or there is lack of the rude military virtues which alone can assure a country's position in the world. In a free republic the ideal citizen must be one willing and able to take arms for the defense of the flag, exactly as the ideal citizen must be the father of many healthy children. A race must be strong and vigorous; it must be a race of good fighters and good breeders, else its wisdom will come to naught and its virtue be ineffective; and no sweetness and delicacy, no love for and appreciation of beauty in art or literature, no capacity for building up material prosperity can possibly atone for the lack of the great virile virtues.
But this is aside from my subject, for what I wish to talk of is the attitude of the American citizen in civic life. It ought to be axiomatic in this country that every man must devote a reasonable share of his time to doing his duty in the Political life of the community. No man has a right to shirk his political duties under whatever plea of pleasure or business; and while such shirking may be pardoned in those of small cleans it is entirely unpardonable in those among whom it is most common--in the people whose circumstances give them freedom in the struggle for life. In so far as the community grows to think rightly, it will likewise grow to regard the young man of means who shirks his duty to the State in time of peace as being only one degree worse than the man who thus shirks it in time of war. A great many of our men in business, or of our young men who are bent on enjoying life (as they have a perfect right to do if only they do not sacrifice other things to enjoyment), rather plume themselves upon being good citizens if they even vote; yet voting is the very least of their duties, Nothing worth gaining is ever gained without effort. You can no more have freedom without striving and suffering for it than you can win success as a banker or a lawyer without labor and effort, without self-denial in youth and the display of a ready and alert intelligence in middle age. The people who say that they have not time to attend to politics are simply saying that they are unfit to live in a free community.I"""
sentences=nltk.sent_tokenize(paragraph)
ps=PorterStemmer()
from nltk.stem import WordNetLemmatizer
wordnet=WordNetLemmatizer()
corpus=[]
corpus1=[]
for i in range(len(sentences)):
    review=re.sub('[^a-zA-Z]',' ',sentences[i])
    review=review.lower()
    review=review.split()
    review=[ps.stem(word)for word in review if not word  in set(stopwords.words('english'))]
    review=''.join(review)
    corpus.append(review)
    
for i in range(len(sentences)):
     
    review1=re.sub('[^a-zA-Z]',' ',sentences[i])
    review1=review1.lower()
    review1=review1.split()
    review1=[wordnet.lemmatize(word)for word in review1 if not word  in set(stopwords.words('english'))]
    review1=''.join(review1)
    corpus1.append(review1)   
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer()
X=cv.fit_transform(corpus).toarray()
X1=cv.fit_transform(corpus1).toarray()
from sklearn.feature_extraction.text import TfidfVectorizer
cv1=TfidfVectorizer()
X2=cv1.fit_transform(corpus).toarray()