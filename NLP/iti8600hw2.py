import nltk
##from geotext import GeoText
from geopy.geocoders import Nominatim
import matplotlib
from nltk.tokenize import sent_tokenize, word_tokenize , PunktSentenceTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer , WordNetLemmatizer

sample_text =  ("Barack Obama went to China yesterday. He lives in Grand Hyatt Beijing. This is a superb hotel.")
tokenized = nltk.word_tokenize(sample_text)
all_words=[]
locations = []
for w in tokenized:

   words = nltk.word_tokenize(w)
   tag =nltk.pos_tag(words)
   if tag[0][1] == 'NNP':
       geolocator = Nominatim()
       place = geolocator.geocode(w)
       if place is not None :
           locations.append(place)
   else :   
        all_words.append(w)
        tagged = nltk.pos_tag(all_words)
        namedEnt = nltk.ne_chunk(tagged)
    
    
namedEnt.draw()
print(locations)
print("TAGGING/RDF:","\n",tagged)
