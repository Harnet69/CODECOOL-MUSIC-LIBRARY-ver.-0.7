"""
The main program should use functions from music_reports and display modules
"""
import os
import music_reports
import display
import file_handling


def get_inputs(labels_list, message):
    inputs = []
    print(message) # prompt the user for info
    for item in labels_list:
        temp = input(f'{item} ')
        inputs.append(temp)

    return inputs


def menu_option_choose(albums):
    inputs = get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "0":
        display.print_albums_list(albums)
    elif option == "1":
        genre = get_inputs(['genre: '], 'What genre do you looking for?')
        albums_in_genre = music_reports.get_albums_by_genre(albums, genre[0])
        try:
            display.print_albums_list(albums_in_genre)
        except TypeError:
            print("Albums in such genre not found")
    elif option == "2":
        longest_album = music_reports.get_longest_album(albums)
        display.print_album_info(longest_album)
    elif option == "3":
        total_albums_length = music_reports.get_total_albums_length(albums)
        print(total_albums_length)


def main():
    """
    Calls all interaction between user and program, handles program menu
    and user inputs. It should repeat displaying menu and asking for
    input until that moment.

    You should create new functions and call them from main whenever it can
    make the code cleaner
    """
    os.system('clear')
    menu_options = ['Print albums list', 'Get_albums_by_genre',
                     'Get_longest_album', 'Get_total_albums_length']
    display.print_program_menu(menu_options)
    albums = file_handling.import_data()
    menu_option_choose(albums)


if __name__ == '__main__':
    main()
