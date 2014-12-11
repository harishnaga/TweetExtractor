# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 01:07:03 2014

@author: HARI
"""
#To get the textblob classifier please goto following link https://textblob.readthedocs.org/en/latest/

from textblob.classifiers import NaiveBayesClassifier #Importing NBC from textbolb classifier
import numpy as np # importing numpy library as np
import matplotlib.pyplot as plt # importing matplotlib library as plt
import re # importing regular expression library
import csv # importing Csv library



with open('Train2.csv', 'r') as fp:
    cl = NaiveBayesClassifier(fp, format="csv") #Training the data using naive bayes classifier
    
with open('Prostatecancer1.csv') as csvfile: # Opening the file which have to be classified 
    csv_f=csv.reader(csvfile, delimiter=' ')
    f = open('Prostatecancer.txt','a')
    aw = open('Pcawareness.txt','a')
#    ad = open('bcadvice.txt','a')
#    n = open('bcnews.txt','a')
#    s = open('bcstatistics.txt','a')
#    q= open('bcquestion.txt','a')
#    o = open('bcother.txt','a')

    for row in csv_f:
        line = ' '.join(row)
        text= ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",line).split()) # regular expression for deleting http link @ # from tweet
        tlabel=(cl.classify(text))
        aw.write(str(text+','+' '+tlabel +'\n'))
        f.write(str(tlabel+'\n'))
        
#        if str(tlabel) == 'Awareness':
#            aw.write(str(text+' '))
#            aw.write(str(tlabel+'\n'))
            
      #count of appearance of labels in the classified data  
        
    hl =open('Prostatecancer.txt','r')
    awcount = 0
    adcount = 0
    ncount = 0
    scount = 0
    ocount = 0
    qcount = 0
    
    for line in hl:
        if line.split(' ')[0].rstrip() == "Awareness":
            awcount += 1   
        if line.split(' ')[0].rstrip() == "Advice":
            adcount += 1 
        if line.split(' ')[0].rstrip() == "News":
            ncount += 1 
        if line.split(' ')[0].rstrip() == "Statistics":
            scount += 1 
        if line.split(' ')[0].rstrip() == "Other":
            ocount += 1 
        if line.split(' ')[0].rstrip() == "Question":
            qcount += 1 
   
    count =(awcount,adcount,ncount,scount,ocount,qcount)
    print count 
    # this part of code is used to do a bar plot of the data
    n_groups = 6
    count_label = count
    std_label = (2, 3, 4, 1, 2, 4)
    fig, ax = plt.subplots()

    index = np.arange(n_groups)
    bar_width = 1

    opacity = 0.4
    error_config = {'ecolor': '0.3'}

    rects = plt.bar(index, count_label, bar_width,
                 alpha=opacity,
                 color='b',
                 yerr=std_label,
                 error_kw=error_config,
                 label='Tweet Label')
    plt.xlabel('TweetLabel')
    plt.ylabel('Number of tweets')
    plt.title('Tweet Distribution for ProStateCancer')
    plt.xticks(index+0.5, ('Awareness', 'Advice', 'News', 'Statistics', 'Other','Question'))
    plt.legend()

    plt.tight_layout()
    plt.show()
