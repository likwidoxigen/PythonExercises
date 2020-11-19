def print_artist(album):
    print(album['Artist_Name'])

def change_list(list_from_user):
    list_from_user[2] = 5

def print_name(album):
    print(album["Album_Title"])

def make_album(name, title, numSongs=10):
    album = {'Artist_Name': name, 'Album_Title': title}
    if numSongs:
        album["Song_Count"] = numSongs
    return album

def main():
    albums = []
    bsb = make_album("Back Street Boys","I want it that way")
    print_artist(bsb)
    print_name(bsb)
    num_track = [1,3,6,7]
    print(num_track)
    change_list(num_track)
    print(num_track)
    # bsb = {
    #     Artist_Name: "Back Street Boys"
    #     Album_Title: "I want it that way"
    #     Song_count: 10
    # }
    artist1 = "Joe"
    title1 = "Buck"
    albums.append(make_album(artist1,title1))
    albums.append(make_album('Marylin Manson', 'Mechanical Animals'))
    albums.append(make_album('Less Than Jake', 'Borders and Boundaries', 12))
    albums.append(make_album("N'Sync", 'No Strings Attached'))
    print(albums)

main()