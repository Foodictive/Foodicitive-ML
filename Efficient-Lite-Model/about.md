# Efficient-Lite Model – Machine Learning Notebook

EfficientNet-Lite Model is a deep learning model for classifying Indonesian food. This model is made using transfer learning method with EfficientNet-Lite0 architecture. The following is the methodology for making the EfficientNet Model.
### 1. Data Gathering
- The method of collecting datasets uses the data scraping method.
- The dataset is a food image data.
- Consists of 10 categories/classes, namely ayam bakar, bakso, bandeng presto, gado gado, gudeg, lumpia semarang, nasi pindang, rendang, sate, dan telur asin.
- The total data is 3900 images.

### 2. Preprocessing
- Split dataset to train_data (80%) and test data (20%).
- Data augmentation for this model 
  ```
  layers.Rescaling(1./255),
  layers.RandomFlip("horizontal_and_vertical"),
  layers.RandomRotation(0.2),
  layers.RandomContrast(0.2),
  layers.RandomZoom(0.4)
  ```
  
### 3. Training
- Add spesification for model with efficientnet_lite0
- Set batch size 32
- Set taining with 15 epoch
- Set Learning rate 0.001
- Set drop rate 0,7

### 4. Training Results
- Training Accuracy   : 0.9736
- Validation Accuracy : 0.9246
- Training Loss       : 0.6694
- Validation Loss     : 0.7189

### 6. Export Model
- Configuration for post-training quantization
  * Use ```for_dynamic()``` for dynamic range quantization
  * Use ```for_float16()``` for float16 quantization 
  * Use ```for_int8``` for full integer quantization 

