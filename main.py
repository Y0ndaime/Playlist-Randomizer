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
    counter = 0
    amounts = values["entryfields"]
    repetitions = values["repetitions"]
    for playlistname in config["playlist_names"]:
        amount = amounts[counter]
        numbers = repetitions[counter].get().split(";")
        i = 0
        while i < int(amount.get()):
            playlist = json.load(open(path.join(config["playlists_path"], playlistname) + ".json", "r"))
            scen = choice(playlist["scenarioList"])
            scen["playCount"] = int(numbers[i])
            scenarioList.append(scen)
            i += 1
        counter += 1
    return scenarioList


config = json.load(open('config.json', 'r'))
window = Tk()
window.title("Playlist Randomizer")
header = Frame(window)
labels = Frame(window)
amount_label = Label(labels, text="Scens")
repetition_label = Label(labels, text="No. of plays             ")
name_label = Label(labels, text="Name")
name_label.pack(side="left")
repetition_label.pack(side="right")
amount_label.pack(side="right")

body = Frame(window)
bottom = Frame(window)
message = StringVar()
message_label = Label(bottom, textvariable = message)
message_label.pack(fill="x")
playlist_name_var = StringVar()
playlist_name_entry = Entry(header, textvariable=playlist_name_var)
playlist_name_entry.grid(row=0, column=1, sticky="e")
playlist_name_label = Label(header, text="Name of new Playlist:")
playlist_name_label.grid(row=0, column=0, sticky="e")
label_list = []
amount_entries_list = []
repetitions_entries_list = []

i = 0
for e in config["playlist_names"]:
    label_list.append(Label(body, text=e))
    amount_entries_list.append(Entry(body, width=6))
    amount_entries_list[-1].insert(0, "0")
    repetitions_entries_list.append(Entry(body, width=12))
    label_list[i].grid(row=i, column=0, sticky="w")
    amount_entries_list[i].grid(row=i, column=1, sticky="e")
    repetitions_entries_list[i].grid(row=i, column=2, sticky="e")
    i += 1
values = dict()
values["entryfields"] = amount_entries_list
values["playlistName"] = playlist_name_var
values["repetitions"] = repetitions_entries_list
randomize_button = Button(bottom, text="Create Playlist", command=create_playlist)
randomize_button.pack(fill="x")
header.pack(fill="x")
labels.pack(fill="x")
body.pack(fill="x")
bottom.pack(fill="x")
window.mainloop()


