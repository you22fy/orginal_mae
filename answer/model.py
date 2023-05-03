from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import pandas as pd

model = AutoModelForSequenceClassification.from_pretrained("jarvisx17/japanese-sentiment-analysis")
tokenizer = AutoTokenizer.from_pretrained("jarvisx17/japanese-sentiment-analysis")

def predict_sentiment(text):
    nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
    result = nlp(text)

    return result

def find_closest_value(label, score):
    df = pd.read_csv("./static/csv/manga_np.csv", index_col=0, header=0)
    df_np = df.query("nega_posi == @label")
    difs = [abs(df_np.iloc[i,4]-score) for i in range(len(df_np))]

    sim_id = difs.index(min(difs))

    return df_np.iloc[sim_id]