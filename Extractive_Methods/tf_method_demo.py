import ./TF-Method/FreqSummarize

text = """
Maria Sharapova has basically no friends as tennis players on the WTA Tour. The Russian player has no problems in openly speaking about it and in a recent interview she said: ‘I don’t really hide any feelings too much.
I think everyone knows this is my job here. When I’m on the courts or when I’m on the court playing, I’m a competitor and I want to beat every single person whether they’re in the locker room or across the net.
So I’m not the one to strike up a conversation about the weather and know that in the next few minutes I have to go and try to win a tennis match.
I’m a pretty competitive girl. I say my hellos, but I’m not sending any players flowers as well. Uhm, I’m not really friendly or close to many players.
I have not a lot of friends away from the courts.’ When she said she is not really close to a lot of players, is that something strategic that she is doing? Is it different on the men’s tour than the women’s tour? ‘No, not at all.
I think just because you’re in the same sport doesn’t mean that you have to be friends with everyone just because you’re categorized, you’re a tennis player, so you’re going to get along with tennis players.
I think every person has different interests. I have friends that have completely different jobs and interests, and I’ve met them in very different parts of my life.
I think everyone just thinks because we’re tennis players we should be the greatest of friends. But ultimately tennis is just a very small part of what we do.
There are so many other things that we’re interested in, that we do.
"""

summary_doc1 = FreqSummarize(
    text=text,
    retain_percentage=0.3,
    nlp_loader=spacy.load("en_core_web_sm"),
    stopwords= STOP_WORDS,
    punctuation=punctuation,
    selection_metric=nlargest,
    intialize=True
)

print(summary_doc1.final_summary)
