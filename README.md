# Steps to install 

## Conda installation 

#### create environment  
`conda env create -f environment.yml`

#### update environment 
`conda env create -f environment.yml`

####  activate (air_env) environment
`conda activate air_env`

####  PIP installation

`virtualenv air_env`

`source air_env/bin/activate`

`pip3 install -r requirements.txt`

###  Start application

`python run.py`
 Type 'http:\localhost:5000` in the browser 

## Notes

* Need internet connection the application to work. css and api calls uses  calls to web
* css is extracted from www.w3schools.com/w3css/ and used in this sample 
* Generated plots are saved as images and displayed in dashboard
* Functions are made generic as much as possible and modularised 

## Performance improvement 

#### Request library 
Api Calls were really slow especially lyrics api. Requests  has one major drawback: it is synchronous. Calling requests.get("http://example.org") blocks the program until the HTTP server replies completely. With limit of 20 lyrics using  `request.get()` method  it took between **20-25 secs** . 

#### asyncio and aiohttp 
Starting with version 3.5, Python offers asynchronicity as its core using asyncio. The aiohttp library provides an asynchronous HTTP client built on top of asyncio. This library allows sending requests in series but without waiting for the first reply to come back before sending the new one. In contrast to HTTP pipelining, aiohttp sends the requests over multiple connections in parallel, avoiding the ordering issue explained earlier
asyncio is often a perfect fit for IO-bound and high-level structured network code.
With limit of 20 lyrics using  `asyncio and aiohttp` method  it took between **6-9 secs** . 

## Types of plots in dashboard 
* Statics
    * Maximum number of words in a Song
    * Mean Words 
    * Median Words in a Song
    * Minimum number of words in a Song
    * Modal Words in a Song
    * Standrad deviation 
* Histogram - This shows the count of words in lyrics in y axis and lyrics in xaxis
* Word Cloud - Data visualisation for representing text data in which the size of each word indicates its frequency or importance
* Sentiment Analysis - VADER Sentiment Analysis. VADER (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed on texts. It is used to provide the percentage of positive, negative and netural sentiments. 

## Application layout

    .
    ├── src                      # Source files
    ├────── config               # Config files (parameters used in application)
    ├────── data                 # Data files  (functions to fetch data such as artists, title, lyrics)
    ├────── helper               # Helper files (modular functions used in application)
    ├────── static               # Static files (images)
    ├────── templates            # Templates ( html files)
    ├────── views.py             # Views intantiates Flask application
    ├── test                   
    ├── environment.yml          # To create environment using conda
    ├── requirements.py          # To create environment using PIP
    └── README.md

## Architectural diagram 


## Future scope 

    * Dockerising the application
    * Error handling can be improved
    * Unit test can be added 
    * Git CI/CD pipeline 
    
## Screen shots 
![Page 1 ](/src/static/Choose.png)
![Page 2 ](/src/static/Songselection.png)
![Page 3 ](/src/static/Dashboard.png)


