# 🦋 Butterfly recognition 
Identifying a Polish butterfly species based on an image.

# 🌿 Motivation
There is a butterfly bush in my garden. 
During the vacations this plant attracts a lot of butterflies. 
Curiosity to identify what species of butterfly sits on this plant led me to build a model to identify them.
# 🖼️ Data
The data I have can be divided into two groups. 
The first group is unlicensed images from google, the second group consists of my private photos, which I haven't shared in the GitHub files. You can find this Dataset folder under this link: https://github.com/Czarstoon/Identifying_Butterflies_App/tree/main/Model_building/Dataset
# ⚙️ Project specifications
The project consists of two main parts. The first one is building the model, while the second is a desktop application that allows testing the model.
## 📚 Information about the model
### Butterfly Species
At this moment, the model identifies five butterfly species:

* **Aglais io**

![Aglais io](https://github.com/Czarstoon/Identifying_Butterflies_App/blob/main/Model_building/Dataset/Train/Aglais_io_1.jpg)
* **Argynnis paphia**   

![Argynnis paphia](https://github.com/Czarstoon/Identifying_Butterflies_App/blob/main/Model_building/Dataset/Train/Argynnis_paphia_1.jpg)
* **Nymphalis antiopa**

![Nymphalis antiopa](https://github.com/Czarstoon/Identifying_Butterflies_App/blob/main/Model_building/Dataset/Train/Nymphalis_antiopa_1.jpg)
* **Papilio machaon**

![Papilio machaon](https://github.com/Czarstoon/Identifying_Butterflies_App/blob/main/Model_building/Dataset/Train/Papilio_machaon_1.jpg)
* **Vanessa_atalanta**

![Vanessa_atalanta](https://github.com/Czarstoon/Identifying_Butterflies_App/blob/main/Model_building/Dataset/Train/Vanessa_atalanta_1.jpg)
### Model characteristics
The model is a convolutional neural network.
The model consists of five layers Filter(Convolution), 
RelU activation Function and Max-pooling then in a classical neural network scheme in the hidden 
layer there is SoftPlus activation function and in the output there is SoftMax function.
For more details on the model diagram, see the file CNN.ipynb.
### Evaluation Method
I used two strategies in evaluating the model. 
The first is to evaluate the training set, the validation set, 
the test set and the set based on private images using accuracy, 
loss and Area under curve. The second strategy was to determine 
the Confusion Matrix, and based on it Recall/Sensitivity, 
Precision, Specifity, F1-score.
For more details on the model diagram, see the file CNN.ipynb.
### Tech stack for model building
**Programming Language:** Python

**Platform:** Jupyter Notebook

**Used modules:** Numpy, Pandas, Matplotlib, Tensorflow/Keras, OpenCV
### Key links and files
You can find more details about the construction and evaluation of the model using these links:
* **HTML file**:
https://czarstoon.github.io/ 
* **PDF file**:
https://github.com/Czarstoon/Identifying_Butterflies_App/blob/main/Model_building/Identifying_Butterflies_Model_CNN.pdf

All model files can be found in the Model_building folder:
https://github.com/Czarstoon/Identifying_Butterflies_App/tree/main/Model_building 
### Running the notebook
* build virtual environment
* install requirements from model_requirements.txt file

## 🖥️ GUI application

### Used design pattern

I've used Model–view–viewmodel (MVVM) pattern.
* Model: Data (buttefly spieces as ENUM) and Model (Convolutional neural network model) **model.py** in GUI_APP folder  
* View: Graphical interface **butterfly_application_ui.py** in GUI_APP folder  
* ViewModel: passing data and actions between View and Model and managing the application logic **modelview.py** also inside GUI_APP folder 

path to GUI_APP folder: https://github.com/Czarstoon/Identifying_Butterflies_App/tree/main/GUI_APP
### Tech stack for gui app
**Programming Language:** Python

**Used modules:** PyQt5, Pyinstaller
### Key files
All gui app files can be found in the GUI_APP folder:
https://github.com/Czarstoon/Identifying_Butterflies_App/tree/main/GUI_APP
### Screens from the app

* Model page (before the identification procedure) 
![screen_1](https://github.com/Czarstoon/Identifying_Butterflies_App/blob/main/GUI_APP/screens/screen_1.PNG)

* Model page (after the identification procedure) 
![screen_2](https://github.com/Czarstoon/Identifying_Butterflies_App/blob/main/GUI_APP/screens/screen_2.PNG)
* Specification page (with CNN visualisation)
![screen_3](https://github.com/Czarstoon/Identifying_Butterflies_App/blob/main/GUI_APP/screens/screen_3.PNG)
* Navigation page (app structure)
![screen_4](https://github.com/Czarstoon/Identifying_Butterflies_App/blob/main/GUI_APP/screens/screen_4.PNG)
### Running the gui application
There is two possible way to run the app:
* build virtual evnironment and install requirements.txt file with essential packages   

    * CMD command:

        * python -m venv env_name

        * pip install -r requirements.txt

        * py main.py 

    * install setup file from this link (only for Windows):
        https://drive.google.com/file/d/1He4dTMBqwRgRF31qELbeu5QuyDtt0WYD/view?usp=sharing

