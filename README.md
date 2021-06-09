# WWF-Bird-Recognition-Project

## Description

To create an algorithm that distinguishes between 3 birds that will act as the first stage in developing a larger ML model for the WWF app for recognizing birds.


## Useful Links
- http://orientalbirdimages.org/birdimages.php
- http://www.vision.caltech.edu/visipedia/CUB-200.html
- https://www.kaggle.com/gpiosenka/100-bird-species

## Tentative Plan
- [ ] June Week 1: Images, Image Metadata, Relevance, Summary statistics, Scraped from Facebook, Instagram, Twitter, Datasets
- [ ] June Week 2: Labelled data for training and testing. [Data in the proper format, ready to be used for the model]
- [ ] July Week 2: Prototyped Machine Learning Model 
- [ ] July Week 3: Test run for the Model using training data
- [ ] July Week 4: Validation of Model 
- [ ] August Week 1: Final training of Reworked Model
- [ ] August Week 2: Final validation of Reworked Model
- [ ] September Week 2: Demonstration of the Model

### Subprocesses 
- [ ] Search for 800 - 1000 images for each class and label them - datasets/social media.
- [ ] Crop square images
- [ ] Make initial model - aim for 75% accuracy on data frrom dataset
- [ ] Build pipeline for incoming images - bounding box -> crop -> resize -> predict
- [ ] Deploy model (preferably on Heroku - can also try other platforms)
- [ ] Search for more images - Add non dataset images.
- [ ] Modify model for 85% accuracy on test data
- [ ] Data Augmentation
- [ ] Retrain model - aim for 90% accuracy on test data

## Deliverables 

1. Dataset on all 3 birds [Common Myna, Housecrow, Sparrow] in a proper format
2. Machine Learning Model 
3. Validation and Training of the Model
4. Demonstration of the Final Model 
