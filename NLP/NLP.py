import nltk
from geotext import Geotext
import matplotlib
from nltk.tokenize import sent_tokenize, word_tokenize , PunktSentenceTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer , WordNetLemmatizer
from nltk.corpus import state_union
#example_text="hello my name is victor and i'm 24 ,it's snowing and it's cold"
#
#print(sent_tokenize(example_text))

#for i in word_tokenize(example_text) :
 #   print(i)
#words = word_tokenize(example_text)  
#stop_words=set(stopwords.words("english"))
#
#filtered_text = []
#stop_words_list = []
#for j in words:
#    if j not in stop_words :
#        filtered_text.append(j)
#    elif j in stop_words :
#        stop_words_list.append(j)
#print("stopwords:" ,stop_words_list)
#
#ps = PorterStemmer()
# 
#
#for k in filtered_text :
#    print(k,ps.stem(k))
    

train_text = state_union.raw("2005-GWBush.txt")
sample_text =  ("Barack Obama went to China yesterday. He lives in Grand Hyatt Beijing. This is a superb hotel.") #my_text.raw("txt.txt")
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized :
            words = nltk.word_tokenize(i)
            
            tagged = nltk.pos_tag(words)
            
            
            #RECOGNITION
            namedEnt = nltk.ne_chunk(tagged)
#            lemmatizer = WordNetLemmatizer()
#            print(lemmatizer.lemmatize(i))
#            CHUNKING
#            chunkGram = r"""Chunk:{<RB.?>*<VB.?>*<NNP>+<NN>?}"""
#            chunkParser = nltk.RegexpParser(chunkGram)
#            chunked = chunkParser.parse(tagged)
#            
            namedEnt.draw()
#            print (chunked)
            print("TAGGING","\n",tagged,"\n","RECOGNITION","\n",namedEnt)
            print()
    except Exception as e :
            print(str(e))
            
process_content()


