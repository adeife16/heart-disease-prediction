# Heart Disease Prediction

This project is a simple web application that uses a machine learning model to predict heart disease (Cardiomegaly) in X-ray images.

## How to use

1. Clone this repository
2. Download the model from [this link](https://drive.google.com/file/d/15C7tIQxLjbTl_JLJnVqm0DWWpRVAnRFA/view?usp=sharing)
3. Navigate to the client folder and run `npm install`
4. Move the model to the server folder
5. Navigate to the server folder and run `pip install -r requirements.txt` then start the server using `python app.py`

## Technology

The project uses the following technology:

* [Flask](https://flask.palletsprojects.com/) as the backend framework
* [TensorFlow](https://www.tensorflow.org/) as the machine learning library
* [Pillow](https://pillow.readthedocs.io/) as the image processing library
* [Vue.js](https://vuejs.org/) as the frontend framework

## Model

The model is a custom CNN architecture that uses convolutional and max-pooling layers to learn features from the input X-ray images. The model is trained on a dataset of X-ray images and corresponding labels. The model is able to predict the presence of cardiomegaly in the input images.

## License

The project is licensed under the [MIT license](LICENSE). See the [LICENSE](LICENSE) file for more information.

