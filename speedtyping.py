import random

def word_drill():
    # List of words to use for the drill
    words = ['rhythm', 'jazz', 'quilt', 'empathy', 'galaxy']
    
    # Shuffle the words to create a random order
    random.shuffle(words)
    
    # Keep track of how many words have been typed correctly
    correct_words = 0
    
    # Display the shuffled words one at a time and prompt the user to type them
    for word in words:
        # Display the current word with a ">" character next to it
        print("> {}".format(word))
        
        # Get the user's input and compare it to the correct word
        user_input = input()
        if user_input == word:
            correct_words += 1
    
    # Calculate the user's typing speed in words per minute
    num_words = len(words)
    typing_speed = (correct_words / num_words) * 60
    
    # Display the user's results
    print("You typed {} words correctly out of {}. Your typing speed was {:.2f} words per minute.".format(correct_words, num_words, typing_speed))


def sentence_drill():
    # List of sentences to use for the drill
    sentences = [
        "Sheena leads, Sheila needs",
        "A big black bug bit a big black bear.",
        "I slit the sheet, the sheet I slit, and on the slitted sheet I sit"
    ]
    
    # Shuffle the sentences to create a random order
    random.shuffle(sentences)
    
    # Keep track of how many sentences have been typed correctly
    correct_sentences = 0
    
    # Display the shuffled sentences one at a time and prompt the user to type them
    for sentence in sentences:
        # Display the current sentence with a ">" character next to it
        print("> {}".format(sentence))
        
        # Get the user's input and compare it to the correct sentence
        user_input = input()
        if user_input == sentence:
            correct_sentences += 1
    
    # Calculate the user's typing speed in sentences per minute
    num_sentences = len(sentences)
    typing_speed = (correct_sentences / num_sentences) * 60
    
    # Display the user's results
    print("You typed {} sentences correctly out of {}. Your typing speed was {:.2f} sentences per minute.".format(correct_sentences, num_sentences, typing_speed))


# Main program loop
while True:
    # Display the available drills
    print("Choose a game:")
    print("1. Word drill")
    print("2. Sentence drill")
    print("3. Quit")
    
    # Get the user's choice of drill
    choice = input()
    
    # Play the selected drill or quit the program
    if choice == "1":
        word_drill()
    elif choice == "2":
        sentence_drill()
    elif choice == "3":
        print("Thanks for using Speed Typing Test. Hope you enjoyed the test.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
    
    # Ask the user whether to continue playing the remaining drills
    print("Do you want to play another game? (y/n)")
    play_again = input()
    if play_again.lower() != "y":
        print("Thanks for using Speed Typing Test. Hope you enjoyed the test.")
        break