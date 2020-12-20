import json
from tkinter import *
from os import path
from random import choice


def create_playlist():
    output = dict()
    output["playlistName"] = values["playlistName"].get()
    output["scenarioList"] = random_scenario_list()
    output["isFavorite"] = False
    with open(path.join(config["playlists_path"], values["playlistName"].get()) + ".json", 'w') as outfile:
        json.dump(output, outfile)
        global message
    message.set("Playlist {} created".format(output["playlistName"]))


def random_scenario_list():
    scenarioList = []
    for playlistname in config["playlist_names"]:
        for amount in values["entryfields"]:
            i = 0
            while i < int(amount.get()):
                playlist = json.load(open(path.join(config["playlists_path"], playlistname) + ".json", "r"))
                scenarioList.append(choice(playlist["scenarioList"]))
                i += 1
    return scenarioList


config = json.load(open('config.json', 'r'))
window = Tk()
window.title("Playlist Randomizer")
header = Frame(window)
body = Frame(window)
bottom = Frame(window)
message = StringVar()
message_label = Label(bottom, textvariable = message)
message_label.grid(row=0, column=0, columnspan=2)
playlist_name_var = StringVar()
playlist_name_var.set("Name of Playlist")
playlist_name_entry = Entry(header, textvariable=playlist_name_var)
playlist_name_entry.setvar("Name of Playlist")
playlist_name_entry.pack()
label_list = []
entry_list = []
i = 0
for e in config["playlist_names"]:
    label_list.append(Label(body, text=e))
    entry_list.append(Entry(body, width=3))
    entry_list[-1].insert(0, "0")
    label_list[i].grid(row=i, column=0, sticky="w")
    entry_list[i].grid(row=i, column=1, sticky="e")
    i += 1
values = dict()
values["entryfields"] = entry_list
values["playlistName"] = playlist_name_var
randomize_button = Button(bottom, text="Create Playlist", command=create_playlist)
randomize_button.grid(row=1, column=0, columnspan=2)
header.grid(row=0, column=0, columnspan=2)
body.grid(row=1, column=0, columnspan=2)
bottom.grid(row=2, column=0, columnspan=2)
window.mainloop()


