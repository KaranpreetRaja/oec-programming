
import random

shapes = ["circle", "square", "triangle", "rectangle"]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "m", "n", "o", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F","G", "H", "I", "J", "K", "M", "N", "O", "P", "Q", "R", "S", "T", "V", "W", "X","Y", "Z"]
words = ["apple", "banana", "cat", "dog", "elephant", "fish", "giraffe", "horse", "iguana", "jellyfish", "kangaroo", "lion", "monkey", "nose", "octopus", "penguin", "quail", "rabbit", "snake", "tiger", "umbrella", "vulture", "whale", "xylophone", "yak", "zebra", "run", "cooking", "jump", "swim", "walk", "sleep", "eat", "drink", "play", "read", "write", "dance", "sing", "draw", "paint", "talk", "listen", "watch", "clean", "cook", "laugh", "cry", "smile", "frown", "yell", "whisper", "think", "imagine", "dream", "hug", "kiss", "love", "hate", "like", "dislike", "want", "need", "have", "give", "take", "make", "break", "fix", "open", "close", "lock", "unlock", "enter", "exit", "start", "stop", "end", "begin", "finish", "win", "lose", "succeed", "fail", "try", "help", "hurt", "heal", "teach", "learn", "understand", "know", "forget", "remember", "remember", "forget", "believe", "doubt", "trust", "suspect", "hope", "wish", "want", "need", "have", "give", "take", "make", "break", "fix", "open", "close", "lock", "unlock", "enter", "exit", "start", "stop", "end", "begin", "finish", "win", "lose", "succeed", "fail", "try", "help", "hurt", "heal", "teach", "learn", "understand", "know", "forget", "remember", "remember", "forget", "believe", "doubt", "trust", "suspect", "hope", "wish", "faster", "amplify"]
sentences = ["Hello my name is alex", "I want to be a cowboy when I grow up", "I have no reason to quit school", "I am tall", "The sun is shining brightly", "I enjoy playing video games", "My favorite color is blue", "Pizza is my go-to comfort food", "I like to take long walks in the park", "Learning new things is always exciting", "I have a pet cat named Whiskers", "Basketball is a fun sport to play", "I love watching movies on weekends", "I'm learning to play the guitar", "Coffee helps me stay awake during exams", "I dream of traveling the world", "Ice cream is a delicious treat", "I often listen to music while working", "The mountains are a beautiful sight", "I believe in the power of kindness", "Cats and dogs make great companions", "I enjoy solving puzzles", "Rainy days are perfect for reading", "I value honesty in relationships", "Mangoes are my favorite fruit", "I prefer tea over coffee", "I have a collection of vintage stamps", "Dancing is a great way to express oneself", "I like to start my day with a good breakfast", "The ocean waves are calming", "I look forward to the weekend", "I believe in continuous self-improvement", "Chocolate chip cookies are irresistible", "I enjoy attending live concerts", "Winter is my favorite season", "I find joy in helping others", "I'm fascinated by outer space", "I like to write in my journal", "Sunsets are a beautiful way to end the day", "I appreciate a good sense of humor", "I try to stay positive in challenging times", "I believe in the importance of education", "Learning a new language is on my bucket list"]
hard_sentances = ["After the rain, a rainbow painted the sky with vibrant colors.", "In the quiet library, students diligently studied for their exams.", "The mysterious old book contained ancient secrets and hidden knowledge.", "Surrounded by nature, the tranquil lake reflected the beauty of the mountains.", "Despite the challenges, she persevered and achieved her long-awaited success.", "The intricate dance of fireflies illuminated the dark night with enchanting light.", "The curious cat explored the unfamiliar territory with cautious steps.", "The melody of the piano echoed through the empty concert hall, captivating the audience.", "Under the starry night sky, the campfire flickered, casting shadows on the faces of friends.", "In the bustling city, a street performer captivated passersby with mesmerizing music.", "The worn-out map led the adventurous travelers to a hidden oasis in the desert.", "The antique clock chimed, marking the passage of time in the quiet room.", "The aroma of freshly brewed coffee wafted through the cozy cafe, inviting customers inside.", "The resilient oak tree stood tall, weathering countless storms over the years.", "With a sense of accomplishment, she completed the challenging crossword puzzle.", "In the vast universe, distant galaxies twirled in a cosmic ballet of celestial beauty.", "The eloquent speaker delivered a thought-provoking speech that resonated with the audience.", "The vintage camera captured moments frozen in time, preserving memories for generations.", "The diligent scientist conducted experiments, unraveling the mysteries of the natural world.", "A gentle breeze rustled the leaves, creating a soothing symphony in the peaceful garden.", "Navigating through the labyrinth of city streets, he discovered hidden gems and quaint shops.", "The historic castle, with its towering spires, told tales of a bygone era.", "With a steady hand, the artist meticulously painted a masterpiece on the canvas.", "The aromatic spices infused the kitchen, creating a culinary masterpiece on the stove.", "The intricate tapestry depicted scenes from ancient mythology, telling a captivating story.", "Amidst the chaos, a serene garden provided a sanctuary for those seeking peace and quiet.", "The charismatic leader inspired the team with a vision for a brighter and collaborative future.", "As the sun set, the city skyline transformed into a breathtaking panorama of lights.", "The resilient daisy bloomed in the harshest conditions, symbolizing hope and perseverance.", "The rhythmic sound of waves crashing on the shore lulled beachgoers into a state of relaxation.", "The diligent student delved into the complex theories, eager to expand their understanding.", "The ancient ruins whispered tales of a civilization long forgotten in the passage of time.", "With a gentle touch, the sculptor shaped the clay into a sculpture that told a unique story."]


def create_session(level, amount):
    # Create a session given level and amount of prompts
    # Returns a session_id and a list of prompts
    selections = []
    for i in range(amount):
        if level == 1:
            # select random shape from shapes
            selections.append(random.choice(shapes))

        elif level == 2:
            # select random letter
            selections.append(random.choice(letters))
            
        elif level == 3:
            # select random word
            selections.append(random.choice(words))

        elif level == 4:
            # select random sentence
            selections.append(random.choice(sentences))

        elif level == 5:
            # select random hard sentence
            selections.append(random.choice(hard_sentances))

        else:
            # select random sentence
            selections.append(random.choice(sentences))

    return selections

