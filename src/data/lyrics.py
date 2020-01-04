import src.helper.request as r
import re

def get_lyrics_by_artist(artist, song):	
	"""
      Gets the lyrics for the artist and song 
    Parameters: 
		artist: name of the artist
		song : name of th song
    Returns: 
        string[] : lyrics , preprocessed and split by space  """

	#Preprocessing
	artist =  re.sub(r'\s+', "%20", artist)
	song = re.sub(r'\s+', "%20", song)
	song = song.replace('?', '%3F')
	
	link = 'https://api.lyrics.ovh/v1/{0}/{1}'
	link_url=link.format(artist,song)

	data,status_code = r.get_request(link = link_url)    
	
	if status_code == 200:
		lyrics = data['lyrics']
		lyrics = lyrics.replace('\n\n', ' ')
		lyrics = lyrics.replace('\n', ' ')
		return lyrics.split(' ')
	else:
		return None

  
