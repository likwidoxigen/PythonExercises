def display_message():
    print("We are learning about functions!")


display_message()


def favorite_book(title):
    print(f"One of my favorite books is {title.title()}")


favorite_book("Kiln People")


def make_album(name, title, numSongs=None):
    album = {'Artist_Name': name, 'Album_Title': title}
    if numSongs:
        album["Song_Count"] = numSongs
    return album


albums = []
albums.append(make_album('Marylin Manson', 'Mechanical Animals'))
albums.append(make_album('Less Than Jake', 'Borders and Boundaries', 10))
albums.append(make_album("N'Sync", 'No Strings Attached'))
print(albums)

#Start with your program from Exercise 8-7. Write a while loop that allows users
#to enter an album’s artist and title. Once you have that information, call
#make_album() with the user’s input and print the dictionary that’s created. Be
#sure to include a quit value in the while loop.

albumInput = []
albums2 = []
artist = ""
while (artist != "QUIT"):
    artist = input("(Type QUIT to exit)Input the artist: ")
    if (artist == "QUIT"):
        break
    title = input("Input the album name: ")
    albumInput.append({'Artist_Name': artist, 'Album_Title': title})

for al in albumInput:
    albums2.append(make_album(al['Artist_Name'], al['Album_Title']))

print(albums2)
