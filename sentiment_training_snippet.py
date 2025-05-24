df = pd.concat([df, df_2 ,train2,df5,df6], ignore_index=True)
df=df.dropna()
df=df.drop_duplicates()
print(df.head())
print(df.shape)



def clean_tweet(tweet):
    if not isinstance(tweet, str):
        return tweet
    tweet = tweet.lower()

    tweet = re.sub(r"n't", " _NEG_", tweet)
    tweet = re.sub(r"\bnot\b", " _NEG_", tweet)

    tweet = re.sub(r'http\S+|www\S+|https\S+', '', tweet, flags=re.MULTILINE)
    ###################################
    ####################################
   ######################################

    ##stop_words = s############
    words = tweet.split()
    #words = [word f#####################]

    ps = PorterStemmer()
    #words = [ps#########################]
    #tweet = ' '.join(#####s)

    return tweet

df['Cleaned_Tweet'] = df['text'].astype(str).apply(clean_tweet)


df_balanced = pd.concat([df['Cleaned_Tweet'], df['sentiment']], axis=1)


######### LSTM Model Architecture Snippet 

import tensorflow as tf
from tensorflow.keras.layers import Layer
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Bidirectional, LSTM, Dense, Dropout

class Attention(Layer):
    #def __init__(###################):
        #######################

    #def ###############:
        #self.W = self.#################################,
                                 ##############################
        ##########################################,
                                 ###############################
        ##super(Attention, self).build(input_shape)

    ###################################
########################################

from tensorflow.keras.regularizers import l2

vocab_size = ##########
embedding_dim = ##
hidden_dim = ###
output_dim = 3

model1 = Sequential([
    Embedding(input_dim=vocab_size, output_dim=embedding_dim),
    Bidirectional(LSTM(hidden_dim, return_sequences=True)),
    Attention(),
    Dropout(####),
    Dense(#####, activation='relu', ###############),
    Dropout(########),
    Dense(##, activation='relu', kernel_regularizer=#########),
    Dropout(####),
    Dense(output_dim, activation='softmax')
])

model1.compile(
    optimizer=tf.keras.optimizers.#################,
    loss='############',
    metrics=['accuracy']
)



history = model1.fit(
    X_train_pad, y_train,
    validation_data=(X_val_pad, y_val),
    epochs=50,
    batch_size=64,
    class_weight=class_weights_dict,
    callbacks=[early_stopping, lr_schedule]
)
