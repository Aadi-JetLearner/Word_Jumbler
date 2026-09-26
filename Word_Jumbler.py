from tkinter import *
import random
from tkinter import messagebox
Score = 0 
wd = Tk()
wd.geometry("600x600")

wd.config(background="black")
wd.title("Word_Jumbler")
List = ["apple", "banana", "cloud", "river", "mountain", "pencil", "window", "garden", "tiger", "ocean", "cookie", "planet", "forest", "mirror", "castle", "rabbit", "button", "camera", "bottle", "island", "sunshine", "pillow", "rocket", "bridge", "diamond", "thunder", "rainbow", "dragon", "candle", "blanket", "keyboard", "guitar", "volcano", "mushroom", "penguin", "whistle", "carpet", "lantern", "bicycle", "puzzle", "coconut", "avocado", "strawberry", "watermelon", "pineapple", "lemon", "peach", "cherry", "grape", "orange", "potato", "carrot", "broccoli", "pepper", "onion", "garlic", "cheese", "bread", "butter", "honey", "coffee", "cereal", "sandwich", "pancake", "waffle", "biscuit", "noodle", "popcorn", "marshmallow", "chocolate", "vanilla", "cinnamon", "ginger", "bubble", "feather", "shadow", "echo", "whisper", "silence", "thunder", "breeze", "storm", "snowflake", "raindrop", "sunset", "sunrise", "moonlight", "starlight", "galaxy", "nebula", "comet", "asteroid", "meteor", "planet", "satellite", "telescope", "spaceship", "universe", "cosmos", "gravity", "orbit", "rocket", "astronaut", "alien", "robot", "machine", "computer", "keyboard", "monitor", "printer", "speaker", "camera", "battery", "cable", "button", "screen", "window", "door", "table", "chair", "shelf", "drawer", "carpet", "curtain", "lamp", "clock", "mirror", "picture", "poster", "book", "notebook", "paper", "eraser", "ruler", "scissors", "stapler", "marker", "crayon", "paintbrush", "puzzle", "toy", "doll", "balloon", "kite", "yo-yo", "teddy", "train", "airplane", "helicopter", "bicycle", "scooter", "skateboard", "bus", "taxi", "tractor", "truck", "motorcycle", "submarine", "boat", "canoe", "bridge", "tunnel", "road", "highway", "station", "airport", "harbor", "village", "city", "castle", "palace", "tower", "cottage", "house", "school", "library", "museum", "theater", "hospital", "market", "bakery", "restaurant", "garden", "park", "playground", "forest", "jungle", "desert", "island", "beach", "river", "lake", "waterfall", "mountain", "valley", "canyon", "cave", "volcano", "meadow", "field", "flower", "tree", "bush", "grass", "moss", "fern", "rose", "tulip", "daisy", "sunflower", "lavender", "oak", "pine", "willow", "bamboo", "cactus", "mushroom", "butterfly", "bee", "ant", "spider", "beetle", "dragonfly", "ladybird", "grasshopper", "snail", "rabbit", "squirrel", "fox", "wolf", "bear", "deer", "tiger", "lion", "elephant", "giraffe", "zebra", "monkey", "gorilla", "panda", "koala", "kangaroo", "penguin", "dolphin", "whale", "shark", "octopus", "jellyfish", "turtle", "crocodile", "alligator", "parrot", "eagle", "owl", "falcon", "sparrow", "pigeon", "peacock", "flamingo", "swan", "duck", "chicken", "rooster", "horse", "cow", "sheep", "goat", "pig", "dog", "cat", "hamster", "mouse", "rain", "snow", "wind", "fog", "mist", "cloud", "storm", "lightning", "sunshine", "daylight", "twilight", "dawn", "dusk", "night", "morning", "evening", "winter", "spring", "summer", "autumn", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "music", "melody", "rhythm", "song", "guitar", "piano", "violin", "drum", "trumpet", "flute", "concert", "dance", "painting", "drawing", "sculpture", "poetry", "story", "adventure", "mystery", "journey", "treasure", "pirate", "wizard", "witch", "knight", "princess", "king", "queen", "dragon", "giant", "monster", "ghost", "fairy", "unicorn", "magic", "spell", "potion", "wand", "crown", "sword", "shield", "helmet", "armor", "map", "compass", "island", "treasure", "gold", "silver", "emerald", "ruby", "sapphire", "crystal", "quartz", "marble", "velvet", "silk", "cotton", "leather", "wood", "metal", "glass", "plastic", "paper", "stone", "brick", "sand", "clay", "water", "fire", "earth", "air", "energy", "light", "shadow", "sound", "color", "shape", "circle", "square", "triangle", "spiral", "star", "heart", "arrow", "diamond", "puzzle", "question", "answer", "idea", "dream", "memory", "thought", "secret", "message", "letter", "number", "word", "language", "alphabet", "sentence", "paragraph", "chapter", "story", "book", "magazine", "newspaper", "calendar", "holiday", "birthday", "party", "gift", "present", "surprise", "friend", "family", "smile", "laugh", "joke", "game", "sport", "football", "basketball", "tennis", "cricket", "swimming", "running", "cycling", "skating", "climbing", "camping", "fishing", "hiking", "exploring", "travel", "adventure", "discovery", "science", "history", "math", "music", "art", "biology", "chemistry", "physics", "computer", "program", "code", "python", "function", "variable", "string", "number", "list", "dictionary", "loop", "random", "future", "present", "yesterday", "tomorrow", "always", "never", "sometimes", "maybe", "quickly", "slowly", "quietly", "loudly", "brightly", "carefully", "happily", "strangely", "beautiful", "ancient", "modern", "tiny", "giant", "smooth", "rough", "soft", "hard", "warm", "cold", "bright", "dark", "fast", "slow", "young", "old", "new", "old", "happy", "curious", "clever", "brave", "kind", "funny", "mysterious", "magical", "ordinary", "strange", "wonderful", "random"]

def Play_Game():
    global RW

    RW = random.choice(List)

    JW = list(RW)
    random.shuffle(JW)

    FW = "".join(JW)

    ETRY1.delete(0, END)
    ETRY1.insert(0, FW)
    
def Check_Win():
    global Score
    if ETRY2.get().strip().lower() == RW.lower():
        Score =+ 1
        messagebox.showwarning("showinfo", "Congrats!, Right Answer!")
        ETRY1.delete(0,END)
        ETRY2.delete(0,END)
    else:
        messagebox.showwarning("showinfo", "Wrong:(")
        ETRY1.delete(0,END)
        ETRY1.delete(0,END)
LbT = Label(wd, text = "JUMBLED WORD GAME:",fg = "white", width = 45, height = 6,bg = "black", font = ("Times New Roman", 15, "bold"))
LbT.place(x = 25, y = 15)
ETRY1 = Entry(wd, bg = "white", font = ("Arial", 24), width = 10)
ETRY1.place(x = 205, y = 200)
ETRY2 = Entry(wd, bg = "white", width = 20, font = ("Arial", 30))
ETRY2.place(x = 80, y = 260)
BT1 = Button(wd, bg = "grey", width = 40, height = 4,fg = "white", text = "SUBMIT", command =  Check_Win)
BT1.place(x = 145, y = 330)
BT2 = Button(wd, bg = "grey", width = 40, height = 4, text = "RESET",fg = "yellow", command =  Play_Game)
BT2.place(x = 145, y = 400)

Play_Game()





    
























wd.mainloop()