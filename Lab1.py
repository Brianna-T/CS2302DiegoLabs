"""
Tovar, Brianna
CS2302 Aguirre Diego, TA Eduardo
8/29
Lab 1: Option A, Recursion
"""
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import praw

reddit = praw.Reddit(client_id='8n6lGHFZSRqmnQ',
                     client_secret='TH1UO5SIpE24oDZliVmGmDgfR4U',
                     user_agent='my user agent'
                     )


nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()


def get_text_negative_proba(text):
   return sid.polarity_scores(text)['neg']


def get_text_neutral_proba(text):
   return sid.polarity_scores(text)['neu']


def get_text_positive_proba(text):
   return sid.polarity_scores(text)['pos']


def get_submission_comments(url):
    submission = reddit.submission(url=url)
    submission.comments.replace_more()

    return submission.comments

#kept getting nltk.metrics error until fixed, delayed my coding
def main():
    comments = get_submission_comments('https://www.reddit.com/r/learnprogramming/comments/5w50g5/eli5_what_is_recursion/')
    print(comments[0].body)
    print(comments[0].replies[0].body)

    neg = get_text_negative_proba(comments[0].replies[0].body)

    print(neg)
    print("---------------------")#added to separate my code

main()

def process_comments():#traversing replies
    comments = get_submission_comments('https://www.reddit.com/r/learnprogramming/comments/5w50g5/eli5_what_is_recursion/')
    if len(comments)==0:#base case if no info
        return ""
    else:
        count=0
        print(comments[0].replies[count].body)
        
        neg = get_text_negative_proba(comments[0].replies[count].body)#sorting if which one
        pos = get_text_positive_proba(comments[0].replies[count].body)
        neu = get_text_neutral_proba(comments[0].replies[count].body)
        count+=1
        
        print("Negative",neg)
        print("Positive",pos)
        print("Neutral",neu)
        return comments[0].replies[count].body#need to repeat for each reply


process_comments()


#---------------------------------------------

#separated to test

"""
#traversing list of text from Reddit
def process_comments(text):
    if len(text)==0:
        return ""
        
    if get_text_negative_proba(text[0].replies[0].body)<=1: #if reply is closer to neg
        print(get_text_negative_proba(text[0].replies[0].body)+"Negative") #prints when True
        return process_comments(text[0].replies[0+1].body) #returns next reply
        
    if get_text_neutral_proba(text[0].replies[0].body)<=1:
        print(get_text_neutral_proba(text[0].replies[0].body)+"Positive")
        return process_comments(text[0].replies[0+1].body)
        
    if get_text_positive_proba(text[0].replies[0].body)<=1:
        print(get_text_positive_proba(text[0].replies[0].body)+"Neutral")
        return process_comments(text[0].replies[0+1].body)
"""