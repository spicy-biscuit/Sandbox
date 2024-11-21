import java.util.ArrayList;

/*
 * LIST OF FUNCTIONS:
 * - Constructor for input layer
 * - Constructor for non-input layers
 * - setPreviousLayer
 * - 
 * 
 * 
 * TO DO:
 * - Add calculate
 * - Add backpropogation stuff (lots of work!!!)
 * 
 * 
 */

public class Layer {
    private int numValues;

    private ArrayList<Double> values;
    private ArrayList<Double> biases;
    //HOW TO READ:
    //weights.get(i).get(j) gives you the connection between neuron j (of layer l-1) to neuron i (of layer l)
    private ArrayList<ArrayList<Double>> weights; //previous layers connections to this layer

    private Layer previousLayer;

    private boolean isInput;
    private boolean isOutput;

    //Constructor for input layer
    public Layer(int numNeurons, boolean input, boolean output) { //for INPUT LAYER
        numValues = numNeurons;

        values = new ArrayList<>();
        biases = new ArrayList<>();

        isInput = input;
        isOutput = output;

        for (int i = 0; i < numNeurons; i++) {
            values.add(0.0);
        }
    }

    //Constructor for non-input layer
    public Layer(int numNeurons, int previousNeurons, boolean input, boolean output) { //for EVERYTHING ELSE (not input)
        numValues = numNeurons;

        values = new ArrayList<>();
        biases = new ArrayList<>();

        isInput = input;
        isOutput = output;

        weights = new ArrayList<>();

        for (int i = 0; i < numValues; i++) {
            values.add(Math.random() * 2 - 1);
            biases.add(Math.random() * 2 - 1);

            ArrayList<Double> rowOfWeights = new ArrayList<>();
            for (int j = 0; j < previousNeurons; j++) {
               rowOfWeights.add(Math.random() * 2 - 1); 
            }

            weights.add(rowOfWeights);
        }
    }

    //Used to hook up the network
    public void setPreviousLayer(Layer layer) {
        previousLayer = layer;
    }
}
