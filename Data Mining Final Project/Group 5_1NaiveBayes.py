import nltk
from nltk import probability
from nltk.corpus import twitter_samples
import numpy as np
import re                                  
import string                             
from nltk.corpus import stopwords          
from nltk.stem import PorterStemmer       
from nltk.tokenize import TweetTokenizer   
import csv
import pandas as pd
from csv import reader
# import sentiment data set and stopwords
nltk.download('twitter_samples')
nltk.download('stopwords')

# assign positive tweets
all_positive_tweets = twitter_samples.strings('positive_tweets.json')
# assign negative tweets
all_negative_tweets = twitter_samples.strings('negative_tweets.json')
# build tokenizer
tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True,
                               reduce_len=True)
# import stopwords
stopwords_english = stopwords.words('english')

punctuations = string.punctuation

stemmer = PorterStemmer()
# remove hyperlinks
def hyperlinks(tweet):
    
    # remove old style retweet text "RT"
    new_tweet = re.sub(r'^RT[\s]+', '', tweet)

    new_tweet = re.sub(r'bit.ly/\S+', '', tweet)

    new_tweet = tweet.strip('[link]') 

    new_tweet = re.sub(r'pic.twitter\S+','', tweet)

    new_tweet = re.sub('(@[A-Za-z]+[A-Za-z0-9-_]+)', '', tweet)
    # remove hyperlinks
    new_tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', new_tweet)

    # remove hashtags
    # only removing the hash # sign from the word
    new_tweet = re.sub(r'#', '', new_tweet)
    
    return new_tweet


# tokenizes the tweet
def tokenize(tweet):
    
    tweet_tokens = tokenizer.tokenize(tweet)
    
    return tweet_tokens

# removes stopwords and punctuation
def rmfluff(tweet_tokens):
    
    tweets_clean = []
    
    for word in tweet_tokens:
        if (word not in stopwords_english and word not in punctuations):
            tweets_clean.append(word)
            
    return tweets_clean
# stem tweets
def stem(tweets_clean):
    
    tweets_stem = []
    
    for word in tweets_clean:
        stem_word = stemmer.stem(word)
        tweets_stem.append(stem_word)
        
    return tweets_stem

# process all methods
def process(tweet):
    
    processed_tweet = hyperlinks(tweet)
    tweet_tokens = tokenize(processed_tweet)
    tweets_clean = rmfluff(tweet_tokens)
    tweets_stem = stem(tweets_clean)
    
    return tweets_stem




# Split Data into Training and Testing data Training gets 8000 Testing gets 2000 assign sentiment value to each value

positiveTest = all_positive_tweets[4000:]
positiveTrain = all_positive_tweets[:4000]
negativeTest = all_negative_tweets[4000:]
negativeTrain = all_negative_tweets[:4000]

train = positiveTrain + negativeTrain
test = positiveTest + negativeTest


# Value of 0 is Negative Tweet 1 is positive
trainSentiment = np.append(np.ones(len(positiveTrain)), np.zeros(len(negativeTrain)))
testSentiment = np.append(np.ones(len(positiveTest)), np.zeros(len(negativeTest)))

## Create Frequency Table that counts how many times word appeared in either positive or negative tweets
def frequencyTable(tweets, sentiment):
    #create dict to hold word frequency
    freqWord = {}

    # Search through key words
    for tweet, sentiment in zip(tweets, sentiment):
        for word in process(tweet):
            couple = (word, sentiment)

            # If word already exists just increment count
            if couple in freqWord:
                freqWord[couple] += 1
            # If not then initialize the value
            else:
                freqWord[couple] = freqWord.get(couple, 1)

    return freqWord

# Build frequency table
frequency = frequencyTable(train, trainSentiment)

def naiveBayesTrain(count, train, trainSentiment):

    # Likelihod of a word being positive or negative
    wordProbability = 0
    # Dictionary holding words probablitity of being positive or negative
    probabilityDict = {}

    # Calculate number of different words
    numWords = set([couple[0] for couple in count.keys()])
    length = len(numWords)

    # Calculate number of positive and negative words in a tweet
    numPos = numNeg = 0
    for couple in count.keys():
        if couple[1] > 0:
            numPos += count[(couple)]
        
        else:
            numNeg += count[(couple)]

    # Calculate number of tweets
    x = trainSentiment.shape[0]
    # Calculate number of positive tweets
    xPos = sum(trainSentiment)
    # Calculate number of negative tweets
    xNeg = x - sum(trainSentiment)
    # Calculate probabliity of word being negative or positive
    wordProbability = np.log(xPos) - np.log(xNeg)

    # For each unique word
    for word in numWords:
        
        # Get Positive and Negative frequency of word
        frequencyPositive = frequency.get((word, 1), 0)
        frequencyNegative = frequency.get((word,0), 0)

        # Calculate probability that word is positive/negative
        probPos = (frequencyPositive + 1) / (numPos + length)
        probNeg = (frequencyNegative + 1) / (numNeg+ length)

        # Fill the probablity dict
        probabilityDict[word] = np.log(probPos / probNeg)

    return wordProbability, probabilityDict

logprior, loglikelihood = naiveBayesTrain(frequency, train, trainSentiment)

def naive_bayes_predict(tweet, wordProbability, probabilityDict):
    # Process the tweet for list of words
    wList = process(tweet)

    # Initialize probability to zero
    p = 0

    # add the probability of sentiment
    p += wordProbability

    # get sentiment probability for each word
    for word in wList:
        if word in probabilityDict:
            p+= loglikelihood[word]
    
    return p

texasSenList = []
texasTweetList = []
texasDf = pd.DataFrame()

texasPositive = 0
texasNegative = 0

negativeCount = 0
errorCount = 0 

for tweet in negativeTest:
    p = naive_bayes_predict(tweet, logprior, loglikelihood)
    print(f'{tweet} -> {p:.2f}')
    if p > 0:
            errorCount += 1
    else:
            negativeCount += 1

print("errors", errorCount)
print("correct", negativeCount)

positiveCount = 0
errorCount1 = 0

for tweet in positiveTest:
    p = naive_bayes_predict(tweet, logprior, loglikelihood)
    #print(f'{tweet} -> {p:.2f}')
    if p < 0:
            errorCount1 += 1
    else:
            positiveCount += 1
print("errors", errorCount1)
print("correct", positiveCount)

print("/////////////////////////////////// Model Success Rate ///////////////////////////////////////////")
errorRate = 9 / 1991
successRate = 100 - errorRate
print("Error Rate", errorRate)
print("Success Rate", successRate)
print("/////////////////////////////////// Model Success Rate ///////////////////////////////////////////")


# runs model predict on twitter data
with open('TexasCleaned.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    reader = csv.reader(read_obj)
    for line in reader:
        p = naive_bayes_predict(str(line), logprior, loglikelihood)
        if p > 0:
            x = "positive"
            texasPositive += 1
        else:
            x = "negative"
            texasNegative +=1
        texasSenList.append(x)
        texasTweetList.append(str(line))
        

texasDf['tweets'] = texasTweetList
texasDf['Sentiment'] = texasSenList
print("/////////////////////////////////// Texas Sentiment Analysis ///////////////////////////////////////////")
print("Positive Tweets", texasPositive)
print("Negative Tweets", texasNegative)
print("Electric Trend Prediction Using Sentiment Analysis: UP")
print("/////////////////////////////////// Texas Sentiment Analysis ///////////////////////////////////////////")


hawaiiSenList = []
hawaiiTweetList = []
hawaiiDf = pd.DataFrame()

hawaiiPositive = 0
hawaiiNegative = 0
# Run this cell to test your function
with open('HawaiiCleaned.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    reader = csv.reader(read_obj)
    for line in reader:
        p = naive_bayes_predict(str(line), logprior, loglikelihood)
        if p > 0:
            x = "positive"
            hawaiiPositive += 1
        else:
            x = "negative"
            hawaiiNegative +=1
        hawaiiSenList.append(x)
        hawaiiTweetList.append(str(line))
        


hawaiiDf['tweets'] = hawaiiTweetList
hawaiiDf['Sentiment'] = hawaiiSenList
print("/////////////////////////////////// Hawaii Sentiment Analysis ///////////////////////////////////////////")
print("Positive Tweets", hawaiiPositive)
print("Negative Tweets", hawaiiNegative)
print("Electric Trend Prediction Using Sentiment Analysis: DOWN")
print("/////////////////////////////////// Hawaii Sentiment Analysis ///////////////////////////////////////////")

idahoSenList = []
idahoTweetList = []
idahoDf = pd.DataFrame()

idahoPositive = 0
idahoNegative = 0
# Run this cell to test your function
with open('IdahoCleaned.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    reader = csv.reader(read_obj)
    for line in reader:
        p = naive_bayes_predict(str(line), logprior, loglikelihood)
        if p > 0:
            x = "positive"
            idahoPositive += 1
        else:
            x = "negative"
            idahoNegative +=1
        idahoSenList.append(x)
        idahoTweetList.append(str(line))
        


idahoDf['tweets'] = idahoTweetList
idahoDf['Sentiment'] = idahoSenList
print("/////////////////////////////////// Idaho Sentiment Analysis ///////////////////////////////////////////")
print("Positive Tweets", idahoPositive)
print("Negative Tweets", idahoNegative)
print("Electric Trend Prediction Using Sentiment Analysis: DOWN")
print("/////////////////////////////////// Idaho Sentiment Analysis ///////////////////////////////////////////")

kansasSenList = []
kansasTweetList = []
kansasDf = pd.DataFrame()

kansasPositive = 0
kansasNegative = 0
# Run this cell to test your function
with open('KansasCleaned.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    reader = csv.reader(read_obj)
    for line in reader:
        p = naive_bayes_predict(str(line), logprior, loglikelihood)
        if p > 0:
            x = "positive"
            kansasPositive += 1
        else:
            x = "negative"
            kansasNegative +=1
        kansasSenList.append(x)
        kansasTweetList.append(str(line))
        


kansasDf['tweets'] = kansasTweetList
kansasDf['Sentiment'] = kansasSenList
print("/////////////////////////////////// Kansas Sentiment Analysis ///////////////////////////////////////////")
print("Positive Tweets", kansasPositive)
print("Negative Tweets", kansasNegative)
print("Electric Trend Prediction Using Sentiment Analysis: DOWN")
print("/////////////////////////////////// Kansas Sentiment Analysis ///////////////////////////////////////////")

louisianaSenList = []
louisianaTweetList = []
louisianaDf = pd.DataFrame()

louisianaPositive = 0
louisianaNegative = 0
# Run this cell to test your function
with open('LouisianaCleaned.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    reader = csv.reader(read_obj)
    for line in reader:
        p = naive_bayes_predict(str(line), logprior, loglikelihood)
        if p > 0:
            x = "positive"
            louisianaPositive += 1
        else:
            x = "negative"
            louisianaNegative +=1
        louisianaSenList.append(x)
        louisianaTweetList.append(str(line))
        


louisianaDf['tweets'] = louisianaTweetList
louisianaDf['Sentiment'] = louisianaSenList
print("/////////////////////////////////// Louisiana Sentiment Analysis ///////////////////////////////////////////")
print("Positive Tweets", louisianaPositive)
print("Negative Tweets", louisianaNegative)
print("Electric Trend Prediction Using Sentiment Analysis: UP")
print("/////////////////////////////////// Louisiana Sentiment Analysis ///////////////////////////////////////////")

arizonaSenList = []
arizonaTweetList = []
arizonaDf = pd.DataFrame()

arizonaPositive = 0
arizonaNegative = 0
# Run this cell to test your function
with open('ArizonaCleaned.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    reader = csv.reader(read_obj)
    for line in reader:
        p = naive_bayes_predict(str(line), logprior, loglikelihood)
        if p > 0:
            x = "positive"
            arizonaPositive += 1
        else:
            x = "negative"
            arizonaNegative +=1
        arizonaSenList.append(x)
        arizonaTweetList.append(str(line))
        


arizonaDf['tweets'] = arizonaTweetList
arizonaDf['Sentiment'] = arizonaSenList
print("/////////////////////////////////// Arizona Sentiment Analysis ///////////////////////////////////////////")
print("Positive Tweets", arizonaPositive)
print("Negative Tweets", arizonaNegative)
print("Electric Trend Prediction Using Sentiment Analysis: UP")
print("/////////////////////////////////// Arizona Sentiment Analysis ///////////////////////////////////////////")

massachusettsSenList = []
massachusettsTweetList = []
massachusettsDf = pd.DataFrame()

massachusettsPositive = 0
massachusettsNegative = 0
# Run this cell to test your function
with open('MassachusettsCleaned.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    reader = csv.reader(read_obj)
    for line in reader:
        p = naive_bayes_predict(str(line), logprior, loglikelihood)
        if p > 0:
            x = "positive"
            massachusettsPositive += 1
        else:
            x = "negative"
            massachusettsNegative += 1
        massachusettsSenList.append(x)
        massachusettsTweetList.append(str(line))
        


massachusettsDf['tweets'] = massachusettsTweetList
massachusettsDf['Sentiment'] = massachusettsSenList
print("/////////////////////////////////// Massachusetts Sentiment Analysis ///////////////////////////////////////////")
print("Positive Tweets", massachusettsPositive)
print("Negative Tweets", massachusettsNegative)
print("Electric Trend Prediction Using Sentiment Analysis: DOWN")
print("/////////////////////////////////// Massachusetts Sentiment Analysis ///////////////////////////////////////////")

utahSenList = []
utahTweetList = []
utahDf = pd.DataFrame()

utahPositive = 0
utahNegative = 0
# Run this cell to test your function
with open('UtahCleaned.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    reader = csv.reader(read_obj)
    for line in reader:
        p = naive_bayes_predict(str(line), logprior, loglikelihood)
        if p > 0:
            x = "positive"
            utahPositive += 1
        else:
            x = "negative"
            utahNegative +=1
        utahSenList.append(x)
        utahTweetList.append(str(line))
        


utahDf['tweets'] = utahTweetList
utahDf['Sentiment'] = utahSenList
print("/////////////////////////////////// UtahSentiment Analysis ///////////////////////////////////////////")
print("Positive Tweets", utahPositive)
print("Negative Tweets", utahNegative)
print("Electric Trend Prediction Using Sentiment Analysis: Down")
print("/////////////////////////////////// Utah Sentiment Analysis ///////////////////////////////////////////")

wisconsinSenList = []
wisconsinTweetList = []
wisconsinDf = pd.DataFrame()

wisconsinPositive = 0
wisconsinNegative = 0
# Run this cell to test your function
with open('WisconsinCleaned.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    reader = csv.reader(read_obj)
    for line in reader:
        p = naive_bayes_predict(str(line), logprior, loglikelihood)
        if p > 0:
            x = "positive"
            wisconsinPositive += 1
        else:
            x = "negative"
            wisconsinNegative +=1
        wisconsinSenList.append(x)
        wisconsinTweetList.append(str(line))
        


wisconsinDf['tweets'] = wisconsinTweetList
wisconsinDf['Sentiment'] = wisconsinSenList
print("/////////////////////////////////// Wisconsin Sentiment Analysis ///////////////////////////////////////////")
print("Positive Tweets", wisconsinPositive)
print("Negative Tweets", wisconsinNegative)
print("Electric Trend Prediction Using Sentiment Analysis: Down")
print("/////////////////////////////////// Wisconsin Sentiment Analysis ///////////////////////////////////////////")

californiaSenList = []
californiaTweetList = []
californiaDf = pd.DataFrame()

californiaPositive = 0
californiaNegative = 0
# Run this cell to test your function
with open('CaliforniaCleaned.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    reader = csv.reader(read_obj)
    for line in reader:
        p = naive_bayes_predict(str(line), logprior, loglikelihood)
        if p > 0:
            x = "positive"
            californiaPositive += 1
        else:
            x = "negative"
            californiaNegative +=1
        californiaSenList.append(x)
        californiaTweetList.append(str(line))
        


californiaDf['tweets'] = californiaTweetList
californiaDf['Sentiment'] = californiaSenList
print("/////////////////////////////////// California Sentiment Analysis ///////////////////////////////////////////")
print("Positive Tweets", californiaPositive)
print("Negative Tweets", californiaNegative)
print("Electric Trend Prediction Using Sentiment Analysis: UP")
print("/////////////////////////////////// California Sentiment Analysis ///////////////////////////////////////////")




#texasSentiment = pd.ExcelWriter('CleanedTexas2020DataFrame.xlsx')
#df.to_excel(texasSentiment, sheet_name='CleanedTexas2020', index = False)
#texasSentiment.close()

    # Iterate over each row in the csv using reader object
   # for row in csv_reader:
        # row variable is a list that represents a row in csv
       # p = naive_bayes_predict(row, logprior, loglikelihood)
        #print(f'{row} -> {p:.2f}')
#     print(f'{tweet} -> {p:.2f} ({p_category})')
