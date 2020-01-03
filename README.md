# Steps to install 

## Conda installation 

### create environment  
`conda env create -f environment.yml`

### update environment 
`conda env create -f environment.yml`

### activate (air_env) environment
`conda activate air_env`

### PIP installation

`virtualenv air_env`
`source air_env/bin/activate`
`pip install -r requirements.txt`

## Start application

`python run.py`

## Notes

* Need internet connection the application to work. css and api calls uses  calls to web
* css is extracted from www.w3schools.com/w3css/ and used in this sample 
* Generated plots are saved as images and displayed in dashboard
* Functions are made generic as possible and modularised 

## Types of plots in dashboard 
* Statics
* Histogram
* Word Cloud
* Sentiment Analysis 

## Applcation layout

    .
    ├── src                   # Source files
    ├────── config               # Config files (parameters used in application)
    ├────── data                 # Data files  (functions to fetch data such as artists, title, lyrics)
    ├────── helper               # Helper files (modular functions used in application)
    ├────── static               # Static files (images)
    ├────── templates            # Templates ( html files)
    ├────── views.py             # Views intantiates Flask application
    ├── test                   
    ├── environment.yml          # To create environment using conda
    ├── requirements.py          # To create environment using PIP
    └── README.m
