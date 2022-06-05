# EfficientNet Model – Machine Learning Notebook

EfficientNet Model is a deep learning model for classifying Indonesian food. This model is made using transfer learning method with EfficientNetB0 architecture. The following is the methodology for making the EfficientNet Model.
### 1. Data Gathering
- The method of collecting datasets uses the data scraping method.
- The dataset is a food image data.
- Consists of 10 categories/classes, namely ayam bakar, bakso, bandeng presto, gado gado, gudeg, lumpia semarang, nasi pindang, rendang, sate, dan telur asin.
- The total image data is … . Means that each category has the amount of data as much as …
- Dataset link here

### 2. Preprocessing
- After the data is collected, the next step is data cleaning, for example deleting image data that does not represent a certain category.
- The dataset is divided into 3 folders, namely train (80%), validation (10%), and test (10%).
- Resize the image to ```224x224``` pixels
- Change all image color to rgb
- In the data train, the data augmentation method is applied to add diversity to the dataset with the following details
  ```
  horizontal_flip = True
  rotation_range = 0.2
  zoom_range = 0.2
  width_shift_range = 0.2
  height_shift_range = 0.2
  ```
  
### 3. Training
- Training using transfer learning method. Transfer learning is the reuse of knowledge from previously trained models to perform new tasks. The transfer learning model (pre-trained model) used is image feature extraction with EfficientNetB0 architecture that has been trained on ImageNet.
- The choice of this method because it has a relatively short training time but has a fairly high accuracy.
- Perform freeze layer technique on all layers on EfficientNetB0. Then the transfer learning model is added with several layers to make the model accuracy more better
   * Added ```Flatten()``` layer
   * Added ```Dense(units=64, activation='relu')``` layer
   * Added ```Dense(units=128, activation='relu')``` layer
   * Added ```Dense(units=256, activation='relu')``` layer
   * Added ```Dropout(units=0.2)``` layer
   * Added output layer ```Dense(units=10, activation='softmax')```
- The training process uses Adam's optimizer with ```learning_rate = 0.0001```
- Training in setting with 20 epochs
- Set the callbacks ```EarlyStopping``` to stop training when ```val_loss``` doesn't improve

### 4. Training Results
### 5. Model Evaluation
### 6. Export Model
