# **Summary of Findings:**


**Main Observations:**

My analysis is very general because of the actual results I was able to retrieve using TF-IDF weighting in the time given for this task.

Firstly, it looks like Shoshana Zuboff is particularly important (as an author / source maybe?) - as the terms "zuboff points" and "zuboff" have the highest scores - 10712 and 10711.

From scanning the rest of the terms and scores I see that the second most important concept in the articles is 'zoning' / 'zones', appearing 4 times after Zuboff. This may be to do with various geographical and political zones and the data about them.

Thirdly, there is a particular focus on young girls, with the phrases 'young' and 'young people / girls /girls' listed, and scores of 10702 to 10699. So I'd assume that the articles have information specifically surrounding various observations on that group of people.

The next notable term is 'years' - this appears in 8 of the top 30 highest weighted bigrams, so it's likely that the articles in the corpus highlight the long term implications of some policies, as well as acknowledging research and considerations from the past.

Interestingly, the dictionary returned after creating a Tf-idf Vectorizer correctly sorts simultaneously in  alphabetical and numerical order by both keys and values .


**Potential Improvements:**

Cleaner / more accurate results may have been obtained by updating the default stopwords with some custom additions e.g. 'yet' which also had a high score but doesn’t necessarily add valuable insight to this text analysis.

Keeping in some more information initially  from the JSON objects (rather than just looking at "content") is likely to have given a better idea of the general topic of each article and allowed for further comparison between articles.

Exploring TF-IDF in more detail may have allowed me to group similar articles in the corpus together and find key concepts in each one rather than seeing just an overall trend.

Also with a longer time constraint I could have figured out how to use NLTKWordTokenizer to identify the frequency of key words across articles.

**Evaluation / Other Considerations:**

Although a consideration has been made for 429 status code responses from the API calls, I am generally unsure of the time complexity implications of scaling the scraping solution up to 100's of URL's - and this code could definitely be optimized for space / memory usage (again - time permitting)

