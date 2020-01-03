import io
import pandas as pd

from flask import Flask,request,render_template
from src.data import artist as artist
from src.data import lyrics as lyrics
from src.helper import plots as plot
from src.helper.sentiment import SentimentAnalyzer

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')


@app.route('/search_artist', methods=['POST'])
def search_artist():  
   """ 
      Searches and returns list of artist
  
    Parameters: 
      txt_artist: name of the artist to search
      txt_limit: number of artist to return ( limit currently is 10)
  
    Returns: 
    List: list of artists  """

   txt_artist = request.form['txt_artist']
   limit = request.form['txt_limit']
   result=artist.search_artist_by_name(txt_artist,int(limit))   
   msg=''
   if not result:
      msg='That artist has not been found, have you spelled it correctly?'
		
   return render_template("index.html", result=result, errormsg=msg)

@app.route('/song_list', methods=['POST'])
def song_list():
   
   """ 
     Gets titles for selected author and returns lyrics for analysis
  
    Parameters: 
      rb_artist: selected artist
      limit of title: default hardcoded 20
  
    Returns: 
    dashboarh of plots. """

   msg=[]
   results={}
   files=[]
   
   #Artist
   rb_artist=request.form['rb_artist'].split('/')
   artist_id =rb_artist[0]
   artist_name=rb_artist[1]  

   songs = pd.DataFrame()
   songs = songs.drop_duplicates(keep='first')
   
   #Title
   title_list=artist.get_title_by_artist(artist_id,20) 
   songs['Title']=title_list 

   #LyricsList
   LyricsList=list(map(lambda i : lyrics.get_lyrics_by_artist(artist_name,i),title_list))
   songs['LyricsList']=LyricsList 

   #LyricsCount
   songs = songs.dropna()
   songs['LyricCount'] = songs['LyricsList'].apply(lambda lyrics: len(lyrics))
   songs = songs[songs['LyricCount'] > 1]

   #Statistics
   res_df=pd.DataFrame()
   stats = songs['LyricCount'].describe()
   if stats.any():
      results[artist_name] = {
         'Mean' : stats.loc['mean'],
         'Standard Deviation': stats.loc['std'],
         'Minimum number of words in a Song': stats.loc['min'],
         'Maximum number of words in a Song': stats.loc['max'],
         'Median Words in a Song': stats.loc['50%'],
         'Modal Words in a Song': songs['LyricCount'].mode().loc[0]
      }

      res_df= pd.DataFrame(results) 
      
      #Create plots
      plot.delete_all_files_in_image()
     
      sentiment_analyzer = SentimentAnalyzer()
      sent_image=sentiment_analyzer.generate_sentiment_graph(songs, "sentiment")
      
      stats_image=plot.generate_barplot(res_df,"stats","Stats Information",artist_name,rot_val=0)  
      hist_image=plot.generate_histplot(songs,"hist","Lyrics","LyricsCount","Title","LyricCount") 
      word_image=plot.generate_word_cloud(songs,"wordcloud")

      files.append(sent_image)
      files.append(hist_image)
      files.append(word_image)
      files.append(stats_image)  
   
  
   return render_template("songlist.html", result=res_df,errormsg=msg,files=files)