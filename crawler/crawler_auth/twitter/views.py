from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.http import HttpResponse
from .models import Twitter_Target
from django.contrib.auth import authenticate, login as authorize, logout as deauth
from bs4 import BeautifulSoup
import requests
import json
import twint
import nest_asyncio
from django.http import JsonResponse
from django.http import HttpResponse
from django.db import models
# from django_countries.fields import CountryField
import subprocess
import asyncio
from .tasks import asd


# Create your views here.

def twitterIndex(request):

    return render(request, 'twitter/index.html')





#this submits the target coompletely for future screeninfg
def submitTarget(request):
    target_type = request.POST['target_type']
    target_platform = request.POST['target_platform']
    twitter_username=request.POST['twitter_username']
    submission_date=request.POST['submission_date']
    target_scheduling=request.POST['target_scheduling']
    #got all variables 
    #save them to database
    target=Twitter_Target(target_type=target_type,target_platform=target_platform,
                          twitter_username=twitter_username,submission_date=submission_date,
                          target_scheduling=target_scheduling)
    target.save()
    r=asd.delay(twitter_username)
    #databse save complete
    
    return render(request,'twitter/index.html')









def tweets_keyword(request):
    # tweets= subprocess.run('twint -u maliksblr92',shell=True,capture_output=True,text=True)
    # tweets_text=tweets.stdout;
    username = request.POST['twitter_username']
    keyword = request.POST['search_tag']
    tweets = getTweets(username, keyword)
    return render(request, 'twitter/dump_tweets.html', {'tweets': tweets,})


def fullProfile(request):
    username = request.POST['twitter_username']
    tweets = getTweets_all(username)
    userProfile = getProfile(username)
    followers_list=getFollowers(username)
    following_list=getFollowing(username)

    return render(request, 'twitter/dump_tweets.html', {'tweets': tweets, 'userProfile': userProfile, 'followers_list': followers_list,'following_list':following_list})



def getFollowersList(request):
    username = request.POST['twitter_username']
    followers_list=getFollowers(username)
    return render(request, 'twitter/dump_followers.html', { 'followers_list': followers_list})




def getFollowingList(request):
    username = request.POST['twitter_username']
    following_list=getFollowing(username)
    return render(request, 'twitter/dump_following.html', { 'following_list': following_list})



# username limit
def getTweets_all(_username):
    tweets_list = []
    c = twint.Config()
    # c.Username = "maliksblr92"
    c.Username = _username
    # c.Limit = limit
    c.Store_object = True  # this is what you need
    c.Hide_output = True

    tweet_text = []
    tweet_id = []
    tweet_date_timestamp = []
    tweet_timestamp = []
    tweet_userid = []
    tweet_username = []
    tweet_tweet_name = []
    tweet_time_zone = []
    tweet_replies_count = []
    tweet_retweet_count = []
    tweet_link = []
    tweet_like_count = []
    tweet_retweet_status = []
    tweet_quote_url = []

    twint.run.Search(c)
    tweets = twint.output.tweets_list
    for tweet in tweets:
        tweet_text.append(format(tweet.tweet))
        tweet_id.append(format(tweet.id))
        tweet_date_timestamp.append(format(tweet.datestamp))
        tweet_timestamp.append(format(tweet.timestamp))
        tweet_userid.append(format(tweet.user_id_str))
        tweet_username.append(format(tweet.username))
        tweet_tweet_name.append(format(tweet.name))
        tweet_time_zone.append(format(tweet.timezone))
        tweet_replies_count.append(format(tweet.replies_count))
        tweet_retweet_count.append(format(tweet.retweets_count))
        tweet_like_count.append(format(tweet.likes_count))
        tweet_link.append(format(tweet.link))
        tweet_retweet_status.append(format(tweet.retweet))
        tweet_quote_url.append(format(tweet.quote_url))
    dic = []
    for item in zip(tweet_text, tweet_id, tweet_date_timestamp, tweet_timestamp, tweet_userid, tweet_username, tweet_tweet_name, tweet_time_zone, tweet_replies_count, tweet_retweet_count, tweet_link, tweet_like_count, tweet_retweet_status, tweet_quote_url):

        dic.append({
            'tweet_text': item[0],
            'tweet_id': item[1],
            'tweet_date_timestamp': item[2],
            'tweet_timestamp': item[3],
            'tweet_userid': item[4],
            'tweet_username': item[5],
            'tweet_tweet_name': item[6],
            'tweet_time_zone': item[7],
            'tweet_replies_count': item[8],
            'tweet_retweet_count': item[9],
            'tweet_link': item[10],
            'tweet_like_count': item[11],
            'tweet_retweet_status': item[12],
            'tweet_quote_url': item[13],
        })

    return dic


# username limit and keyword
def getTweets(_username, keyword):
    tweets_list = []
    c = twint.Config()
    # c.Username = "maliksblr92"
    c.Username = _username
    c.Search = keyword
    # c.Limit = limit
    c.Store_object = True  # this is what you need
    c.Hide_output = True

    tweet_text = []
    tweet_id = []
    tweet_date_timestamp = []
    tweet_timestamp = []
    tweet_userid = []
    tweet_username = []
    tweet_tweet_name = []
    tweet_time_zone = []
    tweet_replies_count = []
    tweet_retweet_count = []
    tweet_link = []
    tweet_like_count = []
    tweet_retweet_status = []
    tweet_quote_url = []

    twint.run.Search(c)
    tweets = twint.output.tweets_list
    for tweet in tweets:
        tweet_text.append(format(tweet.tweet))
        tweet_id.append(format(tweet.id))
        tweet_date_timestamp.append(format(tweet.datestamp))
        tweet_timestamp.append(format(tweet.timestamp))
        tweet_userid.append(format(tweet.user_id_str))
        tweet_username.append(format(tweet.username))
        tweet_tweet_name.append(format(tweet.name))
        tweet_time_zone.append(format(tweet.timezone))
        tweet_replies_count.append(format(tweet.replies_count))
        tweet_retweet_count.append(format(tweet.retweets_count))
        tweet_like_count.append(format(tweet.likes_count))
        tweet_link.append(format(tweet.link))
        tweet_retweet_status.append(format(tweet.retweet))
        tweet_quote_url.append(format(tweet.quote_url))
    dic = []
    for item in zip(tweet_text, tweet_id, tweet_date_timestamp, tweet_timestamp, tweet_userid, tweet_username, tweet_tweet_name, tweet_time_zone, tweet_replies_count, tweet_retweet_count, tweet_link, tweet_like_count, tweet_retweet_status, tweet_quote_url):

        dic.append({
            'tweet_text': item[0],
            'tweet_id': item[1],
            'tweet_date_timestamp': item[2],
            'tweet_timestamp': item[3],
            'tweet_userid': item[4],
            'tweet_username': item[5],
            'tweet_tweet_name': item[6],
            'tweet_time_zone': item[7],
            'tweet_replies_count': item[8],
            'tweet_retweet_count': item[9],
            'tweet_link': item[10],
            'tweet_like_count': item[11],
            'tweet_retweet_status': item[12],
            'tweet_quote_url': item[13],
        })

    return dic

# single profile return


def getProfile(_username):
    # nest_asyncio.apply()
    asyncio.set_event_loop(asyncio.new_event_loop())
    c = twint.Config()
    # c.Username = "maliksblr92"
    c.Username = _username
    c.Store_object = True
    user = {'id': ''}
    twint.run.Lookup(c)
    u = twint.output.users_list
    user['id'] = format(u[0].id)
    user['name'] = u[0].name
    user['username'] = u[0].username
    user['bio'] = u[0].bio
    user['location'] = u[0].location
    user['join_date'] = u[0].join_date
    user['join_time'] = u[0].join_time
    user['tweets'] = u[0].tweets
    user['following'] = u[0].following
    user['followers'] = u[0].followers
    user['avatar'] = u[0].avatar
    user['followers'] = u[0].followers
    user['background_image'] = u[0].background_image
    return user

 # scrap twitter user followers


def getFollowers(username):
    

    nest_asyncio.apply()
    c = twint.Config()
    c.Username = username
    c.User_full = True
    c.Store_object = True
    c.Hide_output = True
    twint.run.Followers(c)
    user_lists = twint.output.users_list

    id = []
    name = []
    username = []
    bio = []
    location = []
    url = []
    join_date = []
    join_time = []
    tweets = []
    following = []
    followers = []
    avatar = []
    private = []
    verified = []
    likes = []
    media = []


    for user in user_lists:
        id.append(user.id)
        name.append(user.name)
        username.append(user.username)
        bio.append(user.bio)
        location.append(user.location)
        url.append(user.url)
        join_date.append(user.join_date)
        join_time.append(user.join_time)
        tweets.append(user.tweets)
        following.append(user.following)
        followers.append(user.followers)
        avatar.append(user.avatar)
        private.append(user.is_private)
        verified.append(user.is_verified)
        likes.append(user.likes)
        media.append(user.media_count)

    dic = []

    for item in zip(id, name, username, bio, location, url, join_date, join_time, tweets, following, followers, avatar, private, verified, likes, media):

        dic.append({
            'id': item[0],
            'name': item[1],
            'username': item[2],
            'bio': item[3],
            'location': item[4],
            'url': item[5],
            'join_date': item[6],
            'join_time': item[7],
            'tweets': item[8],
            'following': item[9],
            'followers': item[10],
            'avatar': item[11],
            'private': item[12],
            'verified': item[13],
            'likes': item[14],
            'media': item[15],


    })
    print(len(dic))
    return dic 



def getFollowing(username):
    

    nest_asyncio.apply()
    c = twint.Config()
    c.Username = username
    c.User_full = True
    c.Store_object = True
    c.Hide_output = True
    twint.run.Following(c)
    user_lists = twint.output.users_list

    id = []
    name = []
    username = []
    bio = []
    location = []
    url = []
    join_date = []
    join_time = []
    tweets = []
    following = []
    followers = []
    avatar = []
    private = []
    verified = []
    likes = []
    media = []


    for user in user_lists:
        id.append(user.id)
        name.append(user.name)
        username.append(user.username)
        bio.append(user.bio)
        location.append(user.location)
        url.append(user.url)
        join_date.append(user.join_date)
        join_time.append(user.join_time)
        tweets.append(user.tweets)
        following.append(user.following)
        followers.append(user.followers)
        avatar.append(user.avatar)
        private.append(user.is_private)
        verified.append(user.is_verified)
        likes.append(user.likes)
        media.append(user.media_count)

    dic = []

    for item in zip(id, name, username, bio, location, url, join_date, join_time, tweets, following, followers, avatar, private, verified, likes, media):

        dic.append({
            'id': item[0],
            'name': item[1],
            'username': item[2],
            'bio': item[3],
            'location': item[4],
            'url': item[5],
            'join_date': item[6],
            'join_time': item[7],
            'tweets': item[8],
            'following': item[9],
            'followers': item[10],
            'avatar': item[11],
            'private': item[12],
            'verified': item[13],
            'likes': item[14],
            'media': item[15],


    })
    print(len(dic))
    return dic 