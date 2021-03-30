import tensorflow.keras as ks
from numpy.random import seed
seed(1)

def build_dnn(neurons=(3, 4, 5),
              loss='MSE',
              activation='relu',
              do_rate=.2,
              l2=.01,
              lr=.001,
              beta_1=.9,
              beta_2=.999
              ):
    """Create Dense Neural network with dropout, and l2 capabilites using the 
    Adam optimizer.
    
    Args:
        neurons - neuron counts in hidden layers. Dense NN will have len(neurons) hidden layers
            type == tuple of int
            d (3, 4, 5)
            
        loss - loss function to use. a default keras loss OR you can define your own
            type == str or ks.losses class
            
        activation - activation function to use in hidden layers
            type == str
            d 'relu'
            
        do_rate - dropout rate to use on hidden layers
            type == float
            d .2
            
        l2 - l2 regularization rate to use on hidden layer weights
            type == float
            d 0.01
            
        lr - Adam learning rate to use
            type == float
            d .001
            
        beta_1 - Adam first momentum parameter
            type == float
            d = .9
            
        beta_2 - Adam second momentum parameter
            type == float
            d = .999
            
    Returns:
        model - keras sequential model, built and compiled
            type == ks.engine.sequential.Sequential
    """
    ## prepare the optimizer
    opt = ks.optimizers.Adam(learning_rate=lr, beta_1=beta_1, beta_2=beta_2)
    
    ## prepare the regularizer for hidden layers with specified l2 rate
    reg = ks.regularizers.l2(l2)
    
    ## initialize the model object
    model = ks.Sequential()
    
    ## build each of the hidden layers
    for neuron_count in neurons:
        
        #. add the dense layer
        model.add(
            ks.layers.Dense(
                neuron_count, # specified number of neurons
                kernel_regularizer = reg,
                activation = activation #specified activation. Note you can define your own like I did regularizers
                )
        )
        
        #. add the dropout layer with the specified dropout rate
        model.add(ks.layers.Dropout(do_rate))
        
        
    ## after hidden layers, build output layer - default linear activation
    model.add(ks.layers.Dense(1))
    
    ## compile it
    model.compile(
        optimizer = opt, # with our optimizer
        loss = loss # and specified loss function. Note you can creat your own loss function instead of using one of the defaults
    )
   
    return model

## first create a wrapper function to return the metric that we care about
#. that would be the loss ON SOME VALIDATION DATA
def dnn_point_evaluation(no_neurons, train_data):
    '''
    Build, train, and evaluate (validation) a DNN for the number of neurons in the first
    hidden layer as a grid point.
    
    Arguments:
        no_neurons - number of neurons in the first hidden layer
            type == int
            
        train_data - tuple of training x, training y
            type == tuple
    '''
    
    ## create the model that we want, no dropout rate and specified first HL count
    model = build_dnn(neurons = (no_neurons, 5, 5),
                      do_rate = 0.0)
    
    ## train the model on the training data, evaluating on validation
    history = model.fit(train_data[0], train_data[1], 
                   epochs = 100, batch_size = 32, verbose = 2,
                   validation_split = 0.2, ) # this time we specify 20% of the training data for val
    
    ## get the metric that we care about, the final validation loss
    val_loss = history.history['val_loss'][-1]
    
    return val_loss