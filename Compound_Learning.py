import tkinter as tk
from tkinter import font
import random


# ── Compound word data ──────────────────────────────────────────────
COMPOUND_WORDS = [
{
"word": "SUNSHINE",
"part1": "SUN",
"part2": "SHINE",
"meaning": "The light and warmth that comes from the sun.",
"emoji": "☀️",
"sentence": "We played outside in the warm sunshine.",
"color": "#FF6B35",
},
{
"word": "RAINBOW",
"part1": "RAIN",
"part2": "BOW",
"meaning": "A colorful arc in the sky made of light and water drops.",
"emoji": "🌈",
"sentence": "After the storm, a beautiful rainbow appeared.",
"color": "#A855F7",
},
{
"word": "BUTTERFLY",
"part1": "BUTTER",
"part2": "FLY",
"meaning": "A pretty insect with colorful wings.",
"emoji": "🦋",
"sentence": "A blue butterfly landed on the flower.",
"color": "#3B82F6",
},
{
"word": "SNOWFLAKE",
"part1": "SNOW",
"part2": "FLAKE",
"meaning": "A tiny piece of snow with a unique crystal shape.",
"emoji": "❄️",
"sentence": "Every snowflake is different from every other one.",
"color": "#06B6D4",
},
{
"word": "FOOTBALL",
"part1": "FOOT",
"part2": "BALL",
"meaning": "A sport played by kicking a ball with your feet.",
"emoji": "⚽",
"sentence": "We played football at recess today.",
"color": "#22C55E",
},
{
"word": "BEDROOM",
"part1": "BED",
"part2": "ROOM",
"meaning": "A room in a house where you sleep.",
"emoji": "🛏️",
"sentence": "She painted her bedroom bright yellow.",
"color": "#F59E0B",
},
{
"word": "BOOKWORM",
"part1": "BOOK",
"part2": "WORM",
"meaning": "Someone who loves to read books all the time.",
"emoji": "📚",
"sentence": "My little brother is such a bookworm!",
"color": "#EF4444",
},
{
"word": "CUPCAKE",
"part1": "CUP",
"part2": "CAKE",
"meaning": "A small cake baked in a cup-shaped mold.",
"emoji": "🧁",
"sentence": "Mom made cupcakes for my birthday party.",
"color": "#EC4899",
},
{
"word": "STARFISH",
"part1": "STAR",
"part2": "FISH",
"meaning": "A sea animal shaped like a star with five arms.",
"emoji": "⭐",
"sentence": "We found a starfish at the beach.",
"color": "#F97316",
},
{
"word": "AIRPLANE",
"part1": "AIR",
"part2": "PLANE",
"meaning": "A flying vehicle that travels through the air.",
"emoji": "✈️",
"sentence": "The airplane flew above the clouds.",
"color": "#6366F1",
},
{
"word": "FIREFLY",
"part1": "FIRE",
"part2": "FLY",
"meaning": "A small bug that glows in the dark at night.",
"emoji": "✨",
"sentence": "Fireflies lit up the garden at night.",
"color": "#EAB308",
},
{
"word": "WATERFALL",
"part1": "WATER",
"part2": "FALL",
"meaning": "Water that falls down from a high place like a cliff.",
"emoji": "💧",
"sentence": "We hiked to see the tall waterfall.",
"color": "#0EA5E9",
},
{
"word": "SUNFLOWER",
"part1": "SUN",
"part2": "FLOWER",
"meaning": "A tall plant with a big yellow flower that faces the sun.",
"emoji": "🌻",
"sentence": "We grew a sunflower taller than the fence.",
"color": "#FBBF24",
},
{
"word": "POPCORN",
"part1": "POP",
"part2": "CORN",
"meaning": "Corn kernels that puff up when heated with air or oil.",
"emoji": "🍿",
"sentence": "We made popcorn for movie night.",
"color": "#F59E0B",
},
{
"word": "DRAGONFLY",
"part1": "DRAGON",
"part2": "FLY",
"meaning": "A flying insect with long wings that hovers over water.",
"emoji": "🐉",
"sentence": "A dragonfly skimmed across the pond.",
"color": "#10B981",
},
{
"word": "TREEHOUSE",
"part1": "TREE",
"part2": "HOUSE",
"meaning": "A small house or clubhouse built up in a tree.",
"emoji": "🌳",
"sentence": "Dad helped us build a treehouse in the backyard.",
"color": "#16A34A",
},
{
"word": "SEASHELL",
"part1": "SEA",
"part2": "SHELL",
"meaning": "A hard shell from a sea animal found on the beach.",
"emoji": "🐚",
"sentence": "She collected a seashell for every beach she visited.",
"color": "#F97316",
},
{
"word": "BACKPACK",
"part1": "BACK",
"part2": "PACK",
"meaning": "A bag you carry on your back, usually for school.",
"emoji": "🎒",
"sentence": "Don't forget your backpack before the bus comes!",
"color": "#8B5CF6",
},
{
"word": "BIRTHDAY",
"part1": "BIRTH",
"part2": "DAY",
"meaning": "The day each year that celebrates when you were born.",
"emoji": "🎂",
"sentence": "Everyone sang happy birthday to Marcus.",
"color": "#EC4899",
},
{
"word": "BLUEBIRD",
"part1": "BLUE",
"part2": "BIRD",
"meaning": "A small bird with bright blue feathers.",
"emoji": "🐦",
"sentence": "A bluebird sat singing on the fence post.",
"color": "#3B82F6",
},
{
"word": "CAMPFIRE",
"part1": "CAMP",
"part2": "FIRE",
"meaning": "A fire you build outdoors when camping.",
"emoji": "🔥",
"sentence": "We roasted marshmallows over the campfire.",
"color": "#EF4444",
},
{
"word": "CLASSROOM",
"part1": "CLASS",
"part2": "ROOM",
"meaning": "The room in a school where students learn.",
"emoji": "🏫",
"sentence": "Our classroom has a fish tank by the window.",
"color": "#06B6D4",
},
{
"word": "CORNFIELD",
"part1": "CORN",
"part2": "FIELD",
"meaning": "A large field where corn plants are grown.",
"emoji": "🌽",
"sentence": "The scarecrow stood tall in the cornfield.",
"color": "#84CC16",
},
{
"word": "DAYLIGHT",
"part1": "DAY",
"part2": "LIGHT",
"meaning": "The natural light that comes during the day from the sun.",
"emoji": "🌤️",
"sentence": "We had plenty of daylight left to finish the game.",
"color": "#FCD34D",
},
{
"word": "DOORBELL",
"part1": "DOOR",
"part2": "BELL",
"meaning": "A button by a door that makes a ringing sound inside.",
"emoji": "🔔",
"sentence": "The doorbell rang just as we sat down to eat.",
"color": "#A78BFA",
},
{
"word": "DUGOUT",
"part1": "DUG",
"part2": "OUT",
"meaning": "A shelter where baseball players sit during a game.",
"emoji": "⚾",
"sentence": "The team cheered from the dugout.",
"color": "#92400E",
},
{
"word": "EARDRUM",
"part1": "EAR",
"part2": "DRUM",
"meaning": "A thin skin inside your ear that vibrates when it hears sound.",
"emoji": "👂",
"sentence": "Loud music can hurt your eardrum.",
"color": "#F472B6",
},
{
"word": "EYELID",
"part1": "EYE",
"part2": "LID",
"meaning": "The flap of skin that covers and protects your eye.",
"emoji": "👁️",
"sentence": "She could barely keep her eyelid open at bedtime.",
"color": "#64748B",
},
{
"word": "FISHPOND",
"part1": "FISH",
"part2": "POND",
"meaning": "A small body of water where fish live.",
"emoji": "🐟",
"sentence": "Grandpa has a fishpond in his garden.",
"color": "#0284C7",
},
{
"word": "FLAGPOLE",
"part1": "FLAG",
"part2": "POLE",
"meaning": "A tall pole used to raise and display a flag.",
"emoji": "🚩",
"sentence": "The flag waved at the top of the flagpole.",
"color": "#DC2626",
},
{
"word": "GRASSHOPPER",
"part1": "GRASS",
"part2": "HOPPER",
"meaning": "A jumping insect that lives in fields and grass.",
"emoji": "🦗",
"sentence": "A grasshopper leaped out from the tall grass.",
"color": "#4ADE80",
},
{
"word": "HANDBALL",
"part1": "HAND",
"part2": "BALL",
"meaning": "A game where you hit a ball against a wall with your hand.",
"emoji": "🤾",
"sentence": "We played handball against the gym wall at recess.",
"color": "#F97316",
},
{
"word": "HAYSTACK",
"part1": "HAY",
"part2": "STACK",
"meaning": "A big pile of dry grass stacked together on a farm.",
"emoji": "🌾",
"sentence": "The kitten hid behind the haystack.",
"color": "#CA8A04",
},
{
"word": "HONEYBEE",
"part1": "HONEY",
"part2": "BEE",
"meaning": "A bee that makes honey and lives in a hive.",
"emoji": "🐝",
"sentence": "A honeybee buzzed from flower to flower.",
"color": "#EAB308",
},
{
"word": "HORSEBACK",
"part1": "HORSE",
"part2": "BACK",
"meaning": "Riding on top of a horse.",
"emoji": "🐴",
"sentence": "They explored the trail on horseback.",
"color": "#A16207",
},
{
"word": "JELLYFISH",
"part1": "JELLY",
"part2": "FISH",
"meaning": "A soft sea creature shaped like a blob that can sting.",
"emoji": "🪼",
"sentence": "We spotted a jellyfish floating near the shore.",
"color": "#C084FC",
},
{
"word": "LUNCHBOX",
"part1": "LUNCH",
"part2": "BOX",
"meaning": "A container used to carry your lunch to school.",
"emoji": "🥪",
"sentence": "He packed a sandwich and an apple in his lunchbox.",
"color": "#FB923C",
},
{
"word": "MOONLIGHT",
"part1": "MOON",
"part2": "LIGHT",
"meaning": "The soft light that comes from the moon at night.",
"emoji": "🌙",
"sentence": "The garden looked magical in the moonlight.",
"color": "#818CF8",
},
{
"word": "NOTEBOOK",
"part1": "NOTE",
"part2": "BOOK",
"meaning": "A book with blank pages used for writing notes.",
"emoji": "📓",
"sentence": "She wrote her story ideas in a notebook.",
"color": "#34D399",
},
{
"word": "OUTDOOR",
"part1": "OUT",
"part2": "DOOR",
"meaning": "Something that happens or exists outside.",
"emoji": "🌿",
"sentence": "Outdoor recess is the best part of the day.",
"color": "#22C55E",
},
{
"word": "PANCAKE",
"part1": "PAN",
"part2": "CAKE",
"meaning": "A flat, round cake cooked in a pan, often eaten for breakfast.",
"emoji": "🥞",
"sentence": "Dad made a stack of pancakes on Saturday morning.",
"color": "#D97706",
},
{
"word": "PEANUT",
"part1": "PEA",
"part2": "NUT",
"meaning": "A small nut that grows underground and is used to make peanut butter.",
"emoji": "🥜",
"sentence": "The elephant reached for a peanut with its trunk.",
"color": "#A3622A",
},
{
"word": "PLAYGROUND",
"part1": "PLAY",
"part2": "GROUND",
"meaning": "An outdoor area with swings and slides for kids to play.",
"emoji": "🛝",
"sentence": "The new playground has a really tall slide.",
"color": "#F43F5E",
},
{
"word": "RAINDROP",
"part1": "RAIN",
"part2": "DROP",
"meaning": "A single drop of water that falls from a rain cloud.",
"emoji": "🌧️",
"sentence": "A raindrop landed right on the tip of her nose.",
"color": "#60A5FA",
},
{
"word": "SAILBOAT",
"part1": "SAIL",
"part2": "BOAT",
"meaning": "A boat that moves using wind caught in a sail.",
"emoji": "⛵",
"sentence": "A tiny sailboat crossed the lake.",
"color": "#0EA5E9",
},
{
"word": "SANDBOX",
"part1": "SAND",
"part2": "BOX",
"meaning": "A box filled with sand for kids to play in.",
"emoji": "🏖️",
"sentence": "The toddler dug tunnels in the sandbox.",
"color": "#BD9807",
},
{
"word": "SCARECROW",
"part1": "SCARE",
"part2": "CROW",
"meaning": "A figure put in a field to frighten birds away from crops.",
"emoji": "🎃",
"sentence": "The scarecrow wore an old hat and a patchy coat.",
"color": "#F59E0B",
},
{
"word": "SKATEBOARD",
"part1": "SKATE",
"part2": "BOARD",
"meaning": "A flat board with wheels that you ride by pushing with your foot.",
"emoji": "🛹",
"sentence": "He learned to do tricks on his skateboard.",
"color": "#7C3AED",
},
{
"word": "SUNBURN",
"part1": "SUN",
"part2": "BURN",
"meaning": "Red, sore skin caused by staying in the sun too long.",
"emoji": "🌞",
"sentence": "Always wear sunscreen so you don't get a sunburn.",
"color": "#EF4444",
},
{
"word": "THUNDERSTORM",
"part1": "THUNDER",
"part2": "STORM",
"meaning": "A storm with heavy rain, lightning, and loud thunder.",
"emoji": "⛈️",
"sentence": "The thunderstorm knocked out the power for an hour.",
"color": "#475569",
},
{
"word": "TOOTHBRUSH",
"part1": "TOOTH",
"part2": "BRUSH",
"meaning": "A small brush used to clean your teeth.",
"emoji": "🪥",
"sentence": "Brush with your toothbrush for two whole minutes.",
"color": "#2DD4BF",
}]




# ── Main App ─────────────────────────────────────────────────────────
class CompoundWordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🌟 Compound Word Adventure!")
        self.root.geometry("700x580")
        self.root.resizable(False, False)
        self.root.configure(bg="#FFF8F0")

        self.words = COMPOUND_WORDS.copy()
        random.shuffle(self.words)
        self.index = 0
        self.score = 0
        self.showing_answer = False

        # Fonts
        self.font_big = font.Font(family="Helvetica", size=52, weight="bold")
        self.font_med = font.Font(family="Helvetica", size=22, weight="bold")
        self.font_small = font.Font(family="Helvetica", size=14)
        self.font_body = font.Font(family="Helvetica", size=13)
        self.font_btn = font.Font(family="Helvetica", size=15, weight="bold")

        self._build_ui()
        self._load_card()

    # ── Build widgets (once) ─────────────────────────────────────────
    def _build_ui(self):
        # Top bar
        top = tk.Frame(self.root, bg="#FFF8F0")
        top.pack(fill="x", padx=24, pady=(18, 0))

        tk.Label(top, text="🌟 Compound Word Adventure!",
                 font=self.font_med, bg="#FFF8F0", fg="#1E293B").pack(side="left")

        self.score_lbl = tk.Label(top, text="Card 1 of 51",
                                  font=self.font_small, bg="#FFF8F0", fg="#64748B")
        self.score_lbl.pack(side="right")

        # Card frame
        self.card = tk.Frame(self.root, bg="white", bd=0,
                             highlightthickness=3, highlightbackground="#E2E8F0",
                             relief="flat")
        self.card.pack(padx=30, pady=16, fill="both", expand=True)

        # Emoji
        self.emoji_lbl = tk.Label(self.card, text="", font=font.Font(size=52),
                                  bg="white")
        self.emoji_lbl.pack(pady=(28, 4))

        # Parts row (WORD1 + WORD2)
        self.parts_frame = tk.Frame(self.card, bg="white")
        self.parts_frame.pack()

        self.part1_lbl = tk.Label(self.parts_frame, text="", width=7,
                                  font=self.font_med, bg="#DBEAFE", fg="#1E40AF",
                                  pady=8, relief="flat")
        self.part1_lbl.pack(side="left", padx=6, ipadx=6)

        tk.Label(self.parts_frame, text="+", font=self.font_med,
                 bg="white", fg="#94A3B8").pack(side="left")

        self.part2_lbl = tk.Label(self.parts_frame, text="", width=7,
                                  font=self.font_med, bg="#DCF5DC", fg="#166534",
                                  pady=8, relief="flat")
        self.part2_lbl.pack(side="left", padx=6, ipadx=6)

        tk.Label(self.parts_frame, text="=", font=self.font_med,
                 bg="white", fg="#94A3B8").pack(side="left")

        self.word_lbl = tk.Label(self.parts_frame, text="?????",
                                 font=self.font_med, bg="#F1F5F9", fg="#334155",
                                 pady=8, width=15, relief="flat")
        self.word_lbl.pack(side="left", padx=6, ipadx=6)

        # Meaning (hidden until reveal)
        self.meaning_frame = tk.Frame(self.card, bg="white")
        self.meaning_frame.pack(fill="x", padx=40, pady=(18, 0))

        self.meaning_title = tk.Label(self.meaning_frame, text="📖 What it means:",
                                      font=self.font_small, bg="white", fg="#64748B")
        self.meaning_title.pack(anchor="w")

        self.meaning_lbl = tk.Label(self.meaning_frame, text="",
                                    font=self.font_body, bg="white", fg="#1E293B",
                                    wraplength=560, justify="left")
        self.meaning_lbl.pack(anchor="w", pady=(2, 0))

        self.sentence_lbl = tk.Label(self.meaning_frame, text="",
                                     font=font.Font(family="Helvetica", size=12,
                                                    slant="italic"),
                                     bg="white", fg="#6366F1", wraplength=560,
                                     justify="left")
        self.sentence_lbl.pack(anchor="w", pady=(4, 0))

        # Buttons
        btn_row = tk.Frame(self.root, bg="#FFF8F0")
        btn_row.pack(pady=14)

        self.reveal_btn = tk.Button(btn_row, text="✨ Reveal Answer",
                                    font=self.font_btn, bg="#6366F1", fg="white",
                                    activebackground="#4F46E5", activeforeground="white",
                                    bd=0, padx=22, pady=10, cursor="hand2",
                                    command=self._reveal)
        self.reveal_btn.pack(side="left", padx=10)

        self.next_btn = tk.Button(btn_row, text="Next Word →",
                                  font=self.font_btn, bg="#22C55E", fg="white",
                                  activebackground="#16A34A", activeforeground="white",
                                  bd=0, padx=22, pady=10, cursor="hand2",
                                  state="disabled", command=self._next)
        self.next_btn.pack(side="left", padx=10)

    # ── Load current card data ───────────────────────────────────────
    def _load_card(self):
        w = self.words[self.index]
        self.showing_answer = False

        # Update score bar
        self.score_lbl.config(text=f"Card {self.index + 1} of {len(self.words)}")

        # Update card highlight color
        self.card.config(highlightbackground=w["color"])

        # Emoji + parts
        self.emoji_lbl.config(text=w["emoji"])
        self.part1_lbl.config(text=w["part1"])
        self.part2_lbl.config(text=w["part2"])

        # Hide the answer word
        self.word_lbl.config(text="?????", bg="#F1F5F9", fg="#334155")

        # Hide meaning
        self.meaning_title.config(text="")
        self.meaning_lbl.config(text="")
        self.sentence_lbl.config(text="")

        # Reset buttons
        self.reveal_btn.config(state="normal", bg="#6366F1", text="✨ Reveal Answer")
        last = (self.index == len(self.words) - 1)
        self.next_btn.config(state="disabled",
                             text="🎉 Play Again!" if last else "Next Word →")

    def _reveal(self):
        if self.showing_answer:
            return
        self.showing_answer = True
        w = self.words[self.index]

        self.word_lbl.config(text=w["word"], bg=w["color"], fg="white")
        self.meaning_title.config(text="📖 What it means:")
        self.meaning_lbl.config(text=w["meaning"])
        self.sentence_lbl.config(text=f'"{w["sentence"]}"')

        self.reveal_btn.config(state="disabled", bg="#CBD5E1", text="✅ Revealed!")
        self.next_btn.config(state="normal")



    def _next(self):
        self.index += 1
        if self.index >= len(self.words):
            # Restart
            random.shuffle(self.words)
            self.index = 0
        self._load_card()


# ── Run ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app = CompoundWordApp(root)
    root.mainloop()