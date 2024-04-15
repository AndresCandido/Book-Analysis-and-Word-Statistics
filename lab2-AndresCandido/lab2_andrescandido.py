## Lab 2 by Andres Candido
import reader
 
def Book_Summary(book,story):
  sentences = story.split(".")

  ## Part 1: Get the average sentence length
  words = []
  sum_of_sentence_length = 0
  for i in range(0, len(sentences)): 
    sum_of_sentence_length = sum_of_sentence_length + len(sentences[i])
    words = words + sentences[i].split()

  avg_sentence_length = sum_of_sentence_length / len(sentences)
  ## Parts 2&3: Get the average word length AND count words of each size
  sum_of_word_length = 0
  word_size = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  word_dictionary = {}
  for i in range(0, len(words)):   
    sum_of_word_length = sum_of_word_length + len(words[i])
    if len(words[i]) < 21:
      word_size[len(words[i])] += 1
    word_dictionary[words[i]]=0
  ## Part 4 Get 100 most common words
  for i in range(0, len(words)): 
    word_dictionary[words[i]]=word_dictionary[words[i]]+1

  avg_word_length = sum_of_word_length / len(words)

  print("Summary of:",book,'\n') 
  print("Average sentence length (in characters):",avg_sentence_length)
  print("Average word length (in characters):",avg_word_length)
  print("Word count based on length (1 through 20 characters):\n",word_size[1:21])
  print("100 most common words in the book:\n",dict(sorted(word_dictionary.items(), key = lambda x: x[1], reverse = True)[:100]) )
  print("------------------------------------------------\n")

## ---------------------------- Function Calls -----------------------------
book1 = "The_War_of_the_Worlds.txt"
story1 = reader.readbook(book1,True)

book2 = "The_heart_of_Darkness.txt"
story2 = reader.readbook(book2,True)

book3 = "Beyond_Good_and_Evil.txt"
story3 = reader.readbook(book3,True)

Book_Summary(book1,story1)
Book_Summary(book2,story2)
Book_Summary(book3,story3)