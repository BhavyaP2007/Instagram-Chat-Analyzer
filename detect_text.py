import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import detoxify
model = detoxify.Detoxify('original')
def checktext(text):

    results = model.predict(text)
    return results

