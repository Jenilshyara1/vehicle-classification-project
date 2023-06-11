from vehicleclassifier.pipeline.predict import PredictPipeline

# predict_pipeline = PredictPipeline("test.jpg")
predict_pipeline = PredictPipeline("dataset\\test\\bus\\bus0.png")

out = predict_pipeline.predict()
print(out)