# 8-7. Album: Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the
# album information correctly.
# Add an optional parameter to make_album() that allows you to store the
# number of tracks on an album. If the calling line includes a value for the num-
# ber of tracks, add that value to the album’s dictionary. Make at least one new
# function call that includes the number of tracks on an album.

def make_album(artist, album, tracks=0):
    info = {'artist name': artist, 'album name': album}
    if tracks:
        info['Tracks'] = tracks
    return info

masterpiece = make_album('Metallica', 'Black album')
print(masterpiece)

masterpiece = make_album('Iron Maiden', 'Killers')
print(masterpiece)

masterpiece = make_album('The Meteors', 'Psychobilly')
print(masterpiece)

masterpiece = make_album('Running Wild', 'Gates to Purgatory', tracks=10)
print(masterpiece)