import json

class Character:
    def __init__(self, name, description, motivations):
        self.name = name
        self.description = description
        self.motivations = motivations

    def __str__(self):
        return f"Character: {self.name}\n  Description: {self.description}\n  Motivations: {', '.join(self.motivations)}"

class Location:
    def __init__(self, name, description, features):
        self.name = name
        self.description = description
        self.features = features

    def __str__(self):
        return f"Location: {self.name}\n  Description: {self.description}\n  Features: {', '.join(self.features)}"

class PlotPoint:
    def __init__(self, chapter, title, summary, characters_involved, locations_involved):
        self.chapter = chapter
        self.title = title
        self.summary = summary
        self.characters_involved = characters_involved
        self.locations_involved = locations_involved

    def __str__(self):
        return f"Chapter {self.chapter}: {self.title}\n  Summary: {self.summary}\n  Characters: {', '.join(self.characters_involved)}\n  Locations: {', '.join(self.locations_involved)}"

class NovelProject:
    def __init__(self, title):
        self.title = title
        self.characters = {}
        self.locations = {}
        self.plot = []

    def add_character(self, character):
        self.characters[character.name] = character

    def add_location(self, location):
        self.locations[location.name] = location

    def add_plot_point(self, plot_point):
        self.plot.append(plot_point)
        self.plot.sort(key=lambda pp: pp.chapter) # Keep plot ordered by chapter

    def get_character(self, name):
        return self.characters.get(name)

    def get_location(self, name):
        return self.locations.get(name)

    def compile_story(self):
        print(f"--- Compiling Novel: {self.title} ---")
        print("\n--- Characters ---")
        for char in self.characters.values():
            print(char)

        print("\n--- Locations ---")
        for loc in self.locations.values():
            print(loc)

        print("\n--- Plot ---")
        for pp in self.plot:
            print(pp)
        print("\n--- Compilation Complete ---")

# --- Example Usage: Building a 30-chapter novel structure ---

# Initialize the novel project
my_novel = NovelProject("The Chronos Chronicle")

# Define core elements (characters and locations)
hero = Character("Anya", "A young historian with a thirst for truth", ["Uncover the past", "Protect ancient artifacts"])
villain = Character("Silas", "A shadowy figure seeking to rewrite history", ["Control the timeline", "Gain ultimate power"])

ancient_library = Location("Library of Alexandria", "A vast repository of ancient knowledge", ["Hidden scrolls", "Secret passages"])
modern_city = Location("Neo-Veridia", "A bustling metropolis of the future", ["Advanced technology", "Underground resistance"])

my_novel.add_character(hero)
my_novel.add_character(villain)
my_novel.add_location(ancient_library)
my_novel.add_location(modern_city)

# Define plot points for each chapter (simplified for example)
# In a real scenario, this would be much more detailed.
for i in range(1, 31):
    title = f"Chapter {i} Event"
    summary = f"Something significant happens in chapter {i}."
    characters = [hero.name] if i % 2 == 0 else [hero.name, villain.name]
    locations = [ancient_library.name] if i % 3 == 0 else [modern_city.name]
    
    plot_point = PlotPoint(i, title, summary, characters, locations)
    my_novel.add_plot_point(plot_point)

# Compile and print the structured novel data
my_novel.compile_story()
