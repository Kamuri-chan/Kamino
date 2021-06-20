# Kamino

## Another bot? What's the purpose?
Yes, this is another bot, but unlike the others, this bot has a text processing feature. I'll explain more on the following lines:
- This bot uses some techniques called text preprocessing, TLDR: raw text, like any message, goes in, ready-for-processing text goes out. The explanation of the methods used on this work are bellow.
- This bot don't use ML, AI or any other fancy methods to retrieve and find the response, just uses text preprocessing and a keyword/precision metric.
- The keywords, as well the responses, are in a JSON file that can be updated by using an API with POST requests, making it much easier to add new features.

## The methods
When dealing with informal text and text that is not in standardized (or structured), usually it's a lot hardier to get some meaning out of it. That's when text preprocessing comes in.
The methods explored by this bot are:
- Tokenization:
  - This breakes down the message into several pieces, making it easier to work with.
- Removing stop-words:
  - This processing removes the uneeded words, that only makes the text longer and full of garbage:
    - "Stop  words  are  a  division  of  natural  language.  The motive  that  stop-words  should  be  removed  from  a text  is  that  they  make  the  text  look  heavier  and  less important for analysts. Removing stop words reduces the dimensionality of term  space. The  most common words  in  text  documents  are  articles,  prepositions, and pro-nouns, etc. that does not give the meaning of the   documents.   These   words   aretreated   as   stop words.  Example  for  stop  words:  the,  in,  a,  an,  with, etc.   Stop   words   are   removed   from   documents because those words are not measured as keywords in text mining applications" [[1]](#1).
- Also, I built a function to remove punctuation, as they are, most of the time, unecessary for the need of this project.
- Stemming and Lemmatization are not included yet, but I do have some plans to include some algorithms soon.
For now, that's it.

## The future
I don't know for certain the future of this project, I am doing it just for fun. But if you're interested, let me know, email me and let's drink a coffe ;D


## References
<a id="1">[1]</a> 
Dr.S.Vijayarani et al.
International Journal of Computer Science & Communication NetworksVol 5(1), 7-16.
ISSN:2249-5789
