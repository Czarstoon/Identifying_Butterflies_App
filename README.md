# 🦋 Butterfly recognition 
Identifying a butterfly species from a photo.

# 🌿 Motivation
There is a butterfly bush in my garden. 
During the vacations this plant attracts a lot of butterflies. 
Curiosity to identify what species of butterfly sits on this plant led me to build a model to identify them.
The model is a Convolutional neural network.
# 🖼️ Data
The data I have can be divided into two groups. 
The first group is unlicensed images from google.The training set, 
which I augmented using ImageDataGenerator. 
Validation set and testing set. 
The second group is private photos from the garden.
The images are located in the Dataset folder.
# ⚙️ Project specifications
## Butterfly Species
In my garden I met 5 species of butterflies:

* **Aglais io**

![Aglais io](https://github.com/Czarstoon/Identifying-butterflies-/blob/main/Dataset/Train/Aglais_io_1.jpg)
* **Argynnis paphia**   

![Argynnis paphia](https://github.com/Czarstoon/Identifying-butterflies-/blob/main/Dataset/Train/Argynnis_paphia_1.jpg)
* **Nymphalis antiopa**

![Nymphalis antiopa](https://github.com/Czarstoon/Identifying-butterflies-/blob/main/Dataset/Train/Nymphalis_antiopa_1.jpg)
* **Papilio machaon**

![Papilio machaon](https://github.com/Czarstoon/Identifying-butterflies-/blob/main/Dataset/Train/Papilio_machaon_1.jpg)
* **Vanessa_atalanta**

![Vanessa_atalanta](https://github.com/Czarstoon/Identifying-butterflies-/blob/main/Dataset/Train/Vanessa_atalanta_1.jpg)
## Convolutional Neural network
The model consists of five layers Filter(Convolution), 
RelU activation Function and Max-pooling then in a classical neural network scheme in the hidden 
layer there is SoftPlus activation function and in the output there is SoftMax function.
For more details on the model diagram, see the file CNN.ipynb.
## Evaluation Method
I used two strategies in evaluating the model. 
The first is to evaluate the training set, the validation set, 
the test set and the set based on private images using accuracy, 
loss and Area under curve. The second strategy was to determine 
the Confusion Matrix, and based on it Recall/Sensitivity, 
Precision, Specifity, F1-score.
For more details on the model diagram, see the file CNN.ipynb.
## Tech stack
**Programming Language:** Python

**Used modules:** Numpy, Pandas, Matplotlib, Tensorflow/Keras, OpenCV
# Further development plans
I would like to implement the model for a Django web application.

