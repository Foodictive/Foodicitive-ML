# Foodictive - Machine Learning Notebook
 
## Introduction
This repo contain's 2 model Foodictive Machine Learning

## How To Use
### Run in Google Colab
...
### Applied .tflite to Android
The model in this repository is designed to run on android applications. The following is a documentation guide for using the .tflite model in android studio (We use kotlin)
1. Lakukan instansiasi model kedalam variable model
   ```
   val model = YourModel.newInstance(this)
   ```
2. Mengambil gambar yang sudah dalam bentuk bitmap, kemudian dimasukkan ke variable image.
   ```
   val image = TensorImage.fromBitmap(bitmap)
   ```
3. Melakukan prediksi terhadap image, Nilai akurasi diurutkan dari terbesar dalam bentuk list. Hasil berupa list dimasukkan kedalam variable outputs
   ```
   val outputs = model.process(image).probabilityAsCategoryList.apply {
      sortByDescending { it.score }
   }
   ```
4. Akses nilai list pertama dengan outputs[0] untuk mendapatkan kategori hasil prediksi dengan nilai akurasi terbesar. Masukkan outputs[0] kedalam variable probability
```
val probability = outputs[0]
```
   
Here is the full code
```
val model = YourModel.newInstance(this)
val image = TensorImage.fromBitmap(bitmap)

val outputs = model.process(image).probabilityAsCategoryList.apply {
    sortByDescending { it.score }
}
val probability = outputs[0]
```
        
## Contributing
We are open and grateful to anyone who wants to contribute to the development of this machine learning model in order to get better results. Here are the steps you can take
1. Fork this repository.
2. Clone the forked repository to your machine.
3. Commit changes to your own branch.
4. Push your work back up to your fork.
5. Submit a Pull request for review.
6. Wait until we review your change.

## References
