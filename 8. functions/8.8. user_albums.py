# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.

def make_album(artist, album, tracks=0):
    info = {'artist name': artist.title(), 'album name': album.title()}
    if tracks:
        info['Tracks'] = tracks
    return info

while True:
    print("'Please, enter an album's artist and title:")
    print("Enter 'q' to quit.")
    art = input('Artist name:')
    if art == 'q':
        break
    alb = input('Album name:')
    if alb == 'q':
        break

    formated = make_album(art, alb)
    print(formated)