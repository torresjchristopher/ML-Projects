from pydantic import BaseModel

class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

def predict_class(model, features: IrisFeatures):
    input_data = [[
        features.sepal_length,
        features.sepal_width,
        features.petal_length,
        features.petal_width
    ]]
    prediction = model.predict(input_data)[0]
    return int(prediction)
