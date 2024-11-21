import java.util.ArrayList;

public class Network {
    ArrayList<Layer> layers = new ArrayList<>();
    int size;
    int outputSize;

    /*
    How to read this array:
    weights[l][i][j] represents the weight from layer l neuron i, to layer l+1 neuron j. 
    For example, weights[0][0][0] means the connection from the first neuron in the input to the first neuron in the first hidden layer.
    */
    Double[][][] weights;
    /*
    How to read this array:
    biases[l][i] represents the bias for the ith neuron in the lth layer.
    */
    Double[][] biases;

    //Constructor
    public Network(int[] sizes) {
        size = sizes.length;
        outputSize = sizes[size - 1];

        int maxNeuronsInLayer = sizes[0];

        //input layer
        layers.add(new Layer(sizes[0], true, false));

        //hidden layers
        for (int i = 1; i < size - 1; i++) {

            if (sizes[i] > maxNeuronsInLayer) {
                maxNeuronsInLayer = sizes[i];
            }

            layers.add(new Layer(sizes[i], false, false));
        }

        //output layer
        if (sizes[size - 1] > maxNeuronsInLayer) {
            maxNeuronsInLayer = sizes[size - 1];
        }
        layers.add(new Layer(sizes[size - 1], false, true));

        weights = new Double[size][maxNeuronsInLayer][maxNeuronsInLayer];
        biases = new Double[size][maxNeuronsInLayer];
    }

    //Actually create weights and connections between layers
    public void connectNeurons() {
        //In the layer i-1,
        for (int i = 1; i < size; i++) {
            //From jth neuron,
            for (int j = 0; j < layers.get(i - 1).getSize(); j++) {
                Neuron inputNeuron = layers.get(i-1).asNeuronList().get(j);
                //To kth neuron in layer i,
                for (int k = 0; k < layers.get(i).getSize(); k++) {
                    Neuron destinationNeuron = layers.get(i).asNeuronList().get(k);
                    Double addedWeight = destinationNeuron.addInput(inputNeuron);
                    // System.out.println("Connecting " + (i-1) + "." + j + " to " + i + "." + k);

                    //Adding this weight to the weights array
                    weights[i - 1][j][k] = addedWeight;
                }
            }
        }

        //creating biases array
        for (int l = 0; l < size; l++) {
            for (int i = 0; i < layers.get(l).getSize(); i++) {
                Neuron thisNeuron = layers.get(l).asNeuronList().get(i);
                Double bias = thisNeuron.getBias();
                biases[l][i] = bias;
            }
        }
    }

    //infamous compute (forward feeding inputs)
    public void compute(ArrayList<Double> input) {
        layers.get(0).set(input);
        for (int i = 1; i < size; i++) {
            layers.get(i).compute();
        }
    }

    //return the result of the cost function based on an expected result (assumes already computed)
    public Double computeCost(ArrayList<Double> expectedResult) {
        ArrayList<Double> networkAnswer = getValue();
        Double cost = 0.0;
        for (int i = 0; i < outputSize; i++) {
            cost += Math.pow(Math.abs(networkAnswer.get(i) - expectedResult.get(i)), 2);
        }
        return cost;
    }

    //outputs last layer of the network as an array
    public ArrayList<Double> getValue() {
        return layers.get(size - 1).asArray();
    }

}