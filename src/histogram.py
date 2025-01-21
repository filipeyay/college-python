import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from matplotlib_venn import venn2
from faker import Faker

fake = Faker()
num_people = 10
names = [fake.name() for _ in range(num_people)]
scores = np.random.randint(10, 50, size=num_people)

data = pd.DataFrame({"Name": names, "Scores": scores})
data.to_csv("data.txt", index=False, sep="\t")
data_recovered = pd.read_csv("data.txt", sep="\t")

plt.figure(figsize=(10, 6))
plt.hist(data_recovered["Scores"], bins=10, edgecolor="black")
plt.xlabel("Scores")
plt.ylabel("Probabilities")
plt.title("Histogram of Scores")
plt.grid(True)
plt.show()

text = " ".join(data_recovered["Name"])
wordcloud = WordCloud(width=800, height=400, background_color="black").generate(text)

plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Names")
plt.show()
