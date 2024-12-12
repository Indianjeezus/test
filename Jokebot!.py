import random

# Database of Jokes
jokes_database = [
    "Why don't eggs tell jokes? They'd crack up.",
    "What do you call a fake noodle? An impasta.",
    "What did one wall say to the other wall? I'll meet you at the corner!",
    "Why was the math book sad? It had too many problems.",
    "What do you call cheese that isn't yours? Nacho cheese!",
    "Why don't scientists trust atoms? Because they might be up to something.",
    "What do you call a bear with no socks on? Barefoot!",
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "How do you organize a space party? You planet!",
    "What do you get when you cross a snowman with a vampire? Frostbite!"

]
new_jokes = [
    "What do you find in a pig’s nose? Hamboogers",
    "What do you call fake noodles? Impasta!",
    "What did the lumberjack say when he got in a car crash? It was an ax-cident",
    "Why do mother kangaroos hate the rain? Because the kids have to play inside all day",
    "What is an owl's favorite subject? Owlgebra",
    "In what month do people talk the least? February- it's the shortest month in the year",
    "Which runs faster, hot or cold? Hot. Everyone can catch a cold",
    "What does Christmas have to do with a cat in a desert? They both have sandy claws",
    "What did the hippy paper say to the hippy pen? Write-on",
    "Why did the matador trade his swords for a gun? He wanted to shoot the bull",
    "Do doctors make housecalls? Yes, but your house has to be really sick",
    "Why did the pig go into the kitchen? It felt like bacon",
    "What were Tarzan's last words? Who greased the vine?",
    "Why did the boy throw butter out his window? He wanted to see a butterfly",
    "What is a parasite? Something you see in Paris",
    "Why did the chicken cross the playground? To get to the other slide!",
    "Which garden has the most vegetables? Flash garden",
    "What is free & full of teeth? A smile",
    "What did the noodles say to the butter? Don't try and butter me up",
    "What shoe type can’t decide? Flip flops",
    "How many vampires does it take to put in a light bulb? None. Vampires like the dark",
    "What sport can also research? Surfing",
    "What is the best way to keep water from running? Don't pay the water bill",
    "What color screams hello? Yellow",
    "What do you call a cow with a twitch? Beef jerky",
    "What did John do when his dog ate his science book? He took the words right out of his mouth",
    "Why is it so hot in a stadium after a football game? All the fans have left",
    "Why is a lost Dalmatian easily found? Because he's always spotted",
    "What’s a top you can’t wear? A Laptop",
    "What kind of phone needs gas? Auto-mobile",
    "When is homework not homework? When it is turned into the teacher",
    "Why did the skeleton cross the road? To get to the body shop",
    "Why did the skier bring wipes? Because he didn’t want to wipe out",
    "What tunes do cows enjoy? Moo-sic",
    "When does it rain money? When there is a change in the weather",
    "Which are the stronger days of the week? Saturday and Sunday- the rest are weekdays",
    "What did Delaware? A brand New Jersey",
    "What do pigs give on Valentines day? Valenswines",
    "Why did the old woman tie skates on the rocking chair? Because she wanted to rock and roll",
    "What do you get when you send a cow to Alaska? Cold cream!",
    "How do potatoes resolve fights? They hash it out",
    "When can peanuts laugh? When you crack them up",
    "What do astronauts eat for dinner? Launch meat",
    "What is yellow and wears a mask? The lone lemon",
    "What does a cold stereo play? Cool music",
    "Why was the pencil’s joke bad? Because it had no point",
    "What does a bee sit on? His bee-hind (behind)",
    "Why did the skeleton go to the movies by himself? He had no body to go with him",
    "Why was the policeman in bed? Because he was an undercover cop",
    "Where do cows go to have fun? The moo-vies",
    "Why do bananas like gymnastics? They like to make splits",
    "How does a tree go home when ready? It leaves",
    "What starts with 'T', is full of 'T', and ends with 'T'? A teapot",
    "How does the beach greet you? With waves",
    "Teacher: Johnny, what is the definition of infinity? Tonight’s homework assignment",
    "What’s the best beach day? Sunday",
    "What did one window say to the other window? I am in 'pane'",
    "Why did the apple turnover? Because he got jealous of the jelly roll",
    "Why was the gift late to the party? It was all wrapped up",
    "What type of bow loves water? A rainbow",
    "What did the little boy tell the game warden? His dad was in the kitchen poaching eggs",
    "What do you call a chicken crossing the road? Poultry in motion",
    "What do you call a mean-tempered horse? A nightmare!",
    "Where do fish sleep? In a water bed!",
    "Why did the elephant decide not to move? Because he couldn't lift his trunk",
    "How do sheep get clean? They take a baa-aa-aa-th",
    "What did the judge say to the racket? We will send you to court",
    "What type of fly loves bread? Butterfly",
    "What kind of teeth can you buy with a dollar? Buck teeth",
    "What bow cannot be tied? A rainbow",
    "Why was the ocean arrested? Because it beat upon the shore",
    "What flies and helps people? A helidoctor",
    "What type of bug has good etiquette? A lady bug",
    "What do you call a lazy bull? A bulldozer",
    "What kind of plant do you put in a cake? Flower",
    "Why don’t ducks tell jokes while they are flying? Because they would quack up",
    "How do small children travel? In mini vans",
    "What has hands, but cannot clap? A clock",
    "What type of store do apes own? A monkey business",
    "How can hurricanes see? They have eyes",
    "What do you watch on TV in the morning? A breakfast serial (cereal)",
    "What type of check has no money? Spell-check",
    "Why did Billy take a ruler to bed with him? To see how long he slept",
    "What can you serve but not eat? A tennis ball",
    "How do you get the water into watermelon? Plant it in the spring",
    "Why was the boy covered in gift wrap? His mom told him to 'live in the present'",
    "When’s the best time to visit a dentist? Tooth-thirty",
    "How do camels blend in? Camel-flage"
]
jokes_database.extend(new_jokes)

def get_random_joke():
    return random.choice(jokes_database)

def chatbot():
    print("Welcome to the Joke Bot! Type 'joke' to hear a random joke or 'quit' to exit.")
    while True:
        user_input = input("> ").lower()
        if user_input in ['joke', 'tell me a joke', 'give me a laugh', 'make me laugh', 'i want a joke', 'tell a joke']:
            print(get_random_joke())
        elif user_input == 'quit':
            print("Thanks for using the Joke Bot! Goodbye!")
            break
        else:
            print("Sorry, I didn't understand that. Type 'joke' for a random joke or 'quit' to exit.")

if __name__ == "__main__":
    chatbot()



