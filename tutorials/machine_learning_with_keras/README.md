# tfkeras_tutorial
Valleau lab tensorflow keras tutorial. Basics of machine learning and making neural networks.

<span style="color:orange">__Status__</span>: Part 1 complete, Part 2 ppt done,
need to finish jupyter demonstration.

## Getting it working
Create and install the conda environment, then activate it with the commands below:

><code>conda env create -f environment.yml</code>

><code>conda activate kerastutorial</code>

## Tutorial contents:
The tutorial covers keras tensorflow. A basic DNN implimentation, as well as 
hyperparameters and hyperparameter optimization. It then covers a keras model
class definition (the "proper" way) allow us to build much more complex and
intertwined models.

<span style="color:orange">__Part 1a__</span>:

- Basic Keras objects
- Function to create a Dense NN
- Using our model on the diabetes data, training and predicting

    
<span style="color:orange">__Part 1b__</span>:

- Additional Keras objects and parameters eg. hyperparameter specification
- Simple grid optimization of a single hyperparameter

<span style="color:orange">__Part 2__</span>:

- Keras functional API and class definitions
- Example of a much more complex model

## Rep Contents

- tutorial.pptx: powerpoint tutorial covering machine learning and neural network basics
- tutorial.ipynb: tutotial implimentation in python
- environment.yml: conda environment specifications
- utils.py: module to use during tutorial
