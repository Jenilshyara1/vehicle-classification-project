import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import  image

class PredictPipeline:
    def __init__(self,filename) :
        self.filename = filename

    def predict(self):
        model = load_model("artifacts\\training\\model.h5")
        test_image = image.load_img(self.filename,target_size = (224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image,axis=0)
        index = np.argmax(model.predict(test_image),axis=1)
        class_name = ["bus","car","motorcycle","train","truck"]
        result = class_name[index[0]]
        return [{"image": result}]

