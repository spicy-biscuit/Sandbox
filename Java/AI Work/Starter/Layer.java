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
 * - Add random mutation stuff
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

    //get the output
    public ArrayList<Double> getOutput() {
        return values;
    }

    //set Value
    public void setValues(ArrayList<Double> input) {
        values = input;
    }

    //gets num of neurons
    public int getNumValues() {
        return numValues;
    }

    //infamous compute
    public void compute() {
        values = ArrayFunctions.arrayMultiplication(weights, previousLayer.getOutput());
        values = ArrayFunctions.componentAdd(values, biases);
        values = ArrayFunctions.sigmoid(values);
    }

    /*
     * Getting better at results
     */
    //RANDOM MUTATIONS
    int numValuesCopy = numValues;

    ArrayList<Double> valuesCopy;
    ArrayList<Double> biasesCopy;
    ArrayList<ArrayList<Double>> weightsCopy = new ArrayList<>();

    // Layer previousLayerCopy = previousLayer;

    boolean isInputCopy = isInput;
    boolean isOutputCopy = isOutput;

    @SuppressWarnings("unchecked")
    public void remember() { //sets "copy" values to be the originals, in case we need to go back to them
        numValuesCopy = numValues;

        valuesCopy = (ArrayList<Double>) values.clone();
        biasesCopy = (ArrayList<Double>) biases.clone();
        weightsCopy = new ArrayList<>();

        for (int i = 0; i < numValues; i++) {
            ArrayList<Double> thisRow = (ArrayList<Double>) weights.get(i).clone();
            weightsCopy.add(thisRow);
        }

        // Layer previousLayerCopy = previousLayer;

        boolean isInputCopy = isInput;
        boolean isOutputCopy = isOutput;
    }

    public void rollBack() { //sets the originals to be the "copy" values
        numValues = numValuesCopy;

        values = valuesCopy;
        biases = biasesCopy;

        weights = weightsCopy;

        // previousLayer = previousLayerCopy;

        isInput = isInputCopy;
        isOutput = isOutputCopy;
    }

    public void mutate(Double learningRate) { //randomly changes every weight and bias by a random value multiplied by the learningRate
        remember();
        //weights
        for (int i = 0; i < numValues; i++) {
            for (int j = 0; j < previousLayer.getNumValues(); j++) {
                Double newValue = weights.get(i).get(j) + (Math.random() * learningRate);
                weights.get(i).set(j, newValue);
            }
        }
        //biases
        for (int i = 0; i <numValues; i++) {
            Double newValue = biases.get(i) + (Math.random() * learningRate);
            biases.set(i, newValue);
        }
    }



    //BACKPROPOGATION
}
