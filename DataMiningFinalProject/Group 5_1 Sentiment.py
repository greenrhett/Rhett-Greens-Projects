import twint
import pandas as pd
import numpy as np
import csv
from nltk.stem.wordnet import WordNetLemmatizer
import re
import nltk

import gensim
import nltk
# remove NA values so as not to skew data
texasTweets_df = pd.read_csv("Texas2021test.csv")
hawaiiTweets_df = pd.read_csv("Hawaii2021test.csv")
idahoTweets_df = pd.read_csv("Idaho2021test.csv")
kansasTweets_df = pd.read_csv("Kansas2021test.csv")
louisianaTweets_df = pd.read_csv("Louisiana2021test.csv")
arizonaTweets_df = pd.read_csv("Arizona021test.csv")
massachusettsTweets_df = pd.read_csv("Massachusetts2021test.csv")
utahTweets_df = pd.read_csv("Utah2021test.csv")
wisconsinTweets_df = pd.read_csv("Wisconsin2021test.csv")
californiaTweets_df = pd.read_csv("California2021test.csv")

texasTweets_df.dropna(axis='columns', inplace=True)
hawaiiTweets_df.dropna(axis='columns', inplace=True)
idahoTweets_df.dropna(axis='columns', inplace=True)
kansasTweets_df.dropna(axis='columns', inplace=True)
louisianaTweets_df.dropna(axis='columns', inplace=True)
arizonaTweets_df.dropna(axis='columns', inplace=True)
massachusettsTweets_df.dropna(axis='columns', inplace=True)
utahTweets_df.dropna(axis='columns', inplace=True)
wisconsinTweets_df.dropna(axis='columns', inplace=True)
californiaTweets_df.dropna(axis='columns', inplace=True)
## keep only columns needed for data model
texasTweets_df1 = texasTweets_df[['tweet']]
hawaiiTweets_df1 = hawaiiTweets_df[['tweet']]
idahoTweets_df1 = idahoTweets_df[['tweet']]
kansasTweets_df1 = kansasTweets_df[['tweet']]
louisianaTweets_df1 = louisianaTweets_df[['tweet']]
arizonaTweets_df1 = arizonaTweets_df[['tweet']]
massachusettsTweets_df1 = massachusettsTweets_df[['tweet']]
utahTweets_df1 = utahTweets_df[['tweet']]
wisconsinTweets_df1 = wisconsinTweets_df[['tweet']]
californiaTweets_df1 = californiaTweets_df[['tweet']]
# define a string of punctuation symbols
punctuation = '!"$%&\'()*+,-./:;<=>?[\\]^_`{|}~•@'
## drop duplicates that may skew data
texasTweets_df1.drop_duplicates(inplace=True, subset="tweet")
hawaiiTweets_df1.drop_duplicates(inplace=True, subset="tweet")
idahoTweets_df1.drop_duplicates(inplace=True, subset="tweet")
kansasTweets_df1.drop_duplicates(inplace=True, subset="tweet")
louisianaTweets_df1.drop_duplicates(inplace=True, subset="tweet")
arizonaTweets_df1.drop_duplicates(inplace=True, subset="tweet")
massachusettsTweets_df1.drop_duplicates(inplace=True, subset="tweet")
utahTweets_df1.drop_duplicates(inplace=True, subset="tweet")
wisconsinTweets_df1.drop_duplicates(inplace=True, subset="tweet")
californiaTweets_df1.drop_duplicates(inplace=True, subset="tweet")

## preprocessing
#Takes a string and removes web links from it
def removeLinks(tweet):
    tweet = re.sub(r'http\S+', '', tweet)   # remove http links
    tweet = re.sub(r'bit.ly/\S+', '', tweet)  # remove bitly links
    tweet = tweet.strip('[link]')   # remove [links]
    tweet = re.sub(r'pic.twitter\S+','', tweet) #remove pictures
    return tweet
#Takes a string and removes retweet and @user information
def removeUsers(tweet):
    tweet = re.sub('(RT\s@[A-Za-z]+[A-Za-z0-9-_]+)', '', tweet)  # remove re-tweet
    tweet = re.sub('(@[A-Za-z]+[A-Za-z0-9-_]+)', '', tweet)  # remove tweeted at
    return tweet
#Takes a string and removes any hash tags
def removeHashtags(tweet):
    tweet = re.sub('(#[A-Za-z]+[A-Za-z0-9-_]+)', '', tweet)  # remove hash tags
    return tweet    
#Takes a string and removes AUDIO/VIDEO tags or labels
def removeAudioVideo(tweet):
    tweet = re.sub('VIDEO:', '', tweet)  # remove 'VIDEO:' from start of tweet
    tweet = re.sub('AUDIO:', '', tweet)  # remove 'AUDIO:' from start of tweet
    return tweet
#Returns lemmatization of a token to make it easier to model the data making the words more conisistent
def lemmatize(token):
    return WordNetLemmatizer().lemmatize(token, pos='v')
#Returns tokenized representation of words in lemma form excluding stopwords
def tokenize(tweet):
    result = []
    for token in gensim.utils.simple_preprocess(tweet):
        if token not in gensim.parsing.preprocessing.STOPWORDS \
                and len(token) > 2:  # drops words with less than 3 characters
            result.append(lemmatize(token))
    return result   
# call the preprocessing methods to clean the data and tokenize into lemma format
def preprocessTweet(tweet):
    tweet = removeUsers(tweet)
    tweet = removeLinks(tweet)
    tweet = removeHashtags(tweet)
    tweet = removeAudioVideo(tweet)
    tweet = tweet.lower()  # make lower case so as not to trip up the model
    tweet = re.sub('[' + punctuation + ']+', ' ', tweet)  # strip punctuation
    tweet = re.sub('\s+', ' ', tweet)  # remove double spacing
    tweet = re.sub('([0-9]+)', '', tweet)  # remove numbers
    tweet_token_list = tokenize(tweet)  # apply lemmatization and tokenization
    tweet = ' '.join(tweet_token_list)
    return tweet
# call preprocessing methods
def tokenizeTweets(df):
    df['tweets'] = df['tweet'].str.lower().apply(preprocessTweet)
    num_tweets = len(df)
    print('Number of Tweets cleaned and tokenized : {}'.format(num_tweets))
    return df
# tokenize tweets
texasCleanData = tokenizeTweets(texasTweets_df1)
hawaiiCleanData = tokenizeTweets(hawaiiTweets_df1)
idahoCleanData = tokenizeTweets(idahoTweets_df1)
kansasCleanData = tokenizeTweets(kansasTweets_df1)
louisianaCleanData = tokenizeTweets(louisianaTweets_df1)
arizonaCleanData = tokenizeTweets(arizonaTweets_df1)
massachusettsCleanData = tokenizeTweets(massachusettsTweets_df1)
utahCleanData = tokenizeTweets(utahTweets_df1)
wisconsinCleanData = tokenizeTweets(wisconsinTweets_df1)
californiaCleanData = tokenizeTweets(californiaTweets_df1)

# make spreadsheets
texasCleanData['tweets'].to_csv('TexasCleaned.csv', index = False)
cleanTexas = pd.ExcelWriter('CleanedTexasDataFrame.xlsx')
texasCleanData['tweets'].to_excel(cleanTexas, sheet_name='CleanedTexas', index = False)
cleanTexas.close()

hawaiiCleanData['tweets'].to_csv('HawaiiCleaned.csv', index = False)
cleanHawaii = pd.ExcelWriter('CleanedHawaiiDataFrame.xlsx')
hawaiiCleanData['tweets'].to_excel(cleanHawaii, sheet_name='CleanedHawaii', index = False)
cleanHawaii.close()

idahoCleanData['tweets'].to_csv('IdahoCleaned.csv', index = False)
cleanIdaho = pd.ExcelWriter('CleandedIdahoDataFrame.xlsx')
idahoCleanData['tweets'].to_excel(cleanIdaho, sheet_name='CleanedIdaho', index = False)
cleanIdaho.close()

kansasCleanData['tweets'].to_csv('KansasCleaned.csv', index = False)
cleanKansas = pd.ExcelWriter('CleandedKansasDataFrame.xlsx')
kansasCleanData['tweets'].to_excel(cleanKansas, sheet_name='CleanedKansas', index = False)
cleanKansas.close()

louisianaCleanData['tweets'].to_csv('LouisianaCleaned.csv', index = False)
cleanLouisiana = pd.ExcelWriter('CleandedLouisianaDataFrame.xlsx')
louisianaCleanData['tweets'].to_excel(cleanLouisiana, sheet_name='CleanedLouisiana', index = False)
cleanLouisiana.close()

arizonaCleanData['tweets'].to_csv('ArizonaCleaned.csv', index = False)
cleanArizona = pd.ExcelWriter('CleandedArizonaDataFrame.xlsx')
arizonaCleanData['tweets'].to_excel(cleanArizona, sheet_name='CleanedArizona', index = False)
cleanArizona.close()

massachusettsCleanData['tweets'].to_csv('MassachusettsCleaned.csv', index = False)
cleanMassachusetts = pd.ExcelWriter('CleandedMassachusettsDataFrame.xlsx')
massachusettsCleanData['tweets'].to_excel(cleanMassachusetts, sheet_name='CleanedMassachusetts', index = False)
cleanMassachusetts.close()

utahCleanData['tweets'].to_csv('UtahCleaned.csv', index = False)
cleanUtah = pd.ExcelWriter('CleandedUtahDataFrame.xlsx')
utahCleanData['tweets'].to_excel(cleanUtah, sheet_name='CleanedUtah', index = False)
cleanUtah.close()

wisconsinCleanData['tweets'].to_csv('WisconsinCleaned.csv', index = False)
cleanWisconsin = pd.ExcelWriter('CleandedWisconsinDataFrame.xlsx')
wisconsinCleanData['tweets'].to_excel(cleanWisconsin, sheet_name='CleanedWisconsin', index = False)
cleanWisconsin.close()

californiaCleanData['tweets'].to_csv('CaliforniaCleaned.csv', index = False)
cleanCalifornia = pd.ExcelWriter('CleandedCaliforniaDataFrame.xlsx')
californiaCleanData['tweets'].to_excel(cleanCalifornia, sheet_name='CleanedCalifornia', index = False)
cleanCalifornia.close()