with open("story.txt","r") as f:
  story = f.read()
words = set()
starter_index = -1;
for i,char in enumerate(story):
  if(char.startswith("<")):
    starter_index = i
  if( starter_index!=-1 and char.endswith(">")):
    words.add(story[starter_index:i+1])
    starter_index = -1
# print(words)

for word in words:
  answer = input(f"Enter a word for {word}: ")
  story = story.replace(word,answer)

print(story)
