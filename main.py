import markovify
import json

with open('./tweets.json') as f:
  data = json.load(f)


result = list(map(lambda tweet: tweet['tweet']['full_text'], data))


deliminator = "\n\n"

text = deliminator.join(result) 

text_model = markovify.Text(text)

for i in range(30):
    print(text_model.make_short_sentence(280))
    print("\n")
