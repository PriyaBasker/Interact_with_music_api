import src.helper.request as r
header = {'User-Agent': 'AverageLengthofSongs/0.0.1 (priya.basker@gmail.com)'}


def search_artist_by_name(artist,limit=10):	
   
	link = "https://musicbrainz.org/ws/2/artist?"	  
	params = {'query':artist,'limit':limit,'offset':0,'fmt':'json'} 

	data,status_code= r.get_request(link = link,params = params,header=header) 	
	
	artists_dict = {}

	if status_code == 200:		
		for i, artist in enumerate(data['artists']):
			artists_dict[i + 1] = [artist['name'], artist['id']]

	return artists_dict

	#Should i remove duplicated of artist name ?
def get_title_by_artist(id_tag,limit=10):
	
	link = "https://musicbrainz.org/ws/2/work?"	  
	params = {'artist':id_tag,'limit':limit,'offset':0,'fmt':'json'} 
    
	data,status_code = r.get_request(link = link,params = params,header=header) 	
	
	song_list=[]

	if status_code == 200:	       
		for i, release in enumerate(data['works']):
			song_list.append(release['title'])

	return song_list





