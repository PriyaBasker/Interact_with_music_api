import src.helper.request as r
import re

def get_lyrics_by_artist(artist, song):	
	# print(song)
	artist =  re.sub(r'\s+', "%20", artist)
	song = re.sub(r'\s+', "%20", song)
	song = song.replace('?', '%3F')
	# print(song)
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

  
