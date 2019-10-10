import lastfm


top_50_artist = lastfm.get_top_artist()
print(len(top_50_artist['artists']['artist']))