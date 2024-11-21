import java.util.ArrayList;

public class Neuron {
    Double value;
    ArrayList<Neuron> feederValues;
    ArrayList<Double> weights;
    Double bias;
    boolean isInput = false;
    boolean isOutput = false;

    int numWeights;

    //Backpropogation variables
    Double expectedOutput; //Only for output Layer neurons
    Double derivative; //derivative of cost with resepct to value of THIS neuron
    ArrayList<Double> weightDerivatives; //derivative of cost with respect to value of ITH neuron
    Double biasDerivative; //derivative of cost with respect to bias of THIS neuron

    //Constructors
    public Neuron(ArrayList<Neuron> inFeederValues, ArrayList<Double> inWeights, Double inBias, boolean input, boolean output) {
        feederValues = inFeederValues;
        weights = inWeights;
        bias = inBias;
        isInput = input;
        isOutput = output;
        numWeights = weights.size();
    }

    public Neuron(boolean input, boolean output) {
        value = Math.random() * 2 - 1;
        feederValues = new ArrayList<>();
        weights = new ArrayList<>();
        bias = Math.random() * 2 - 1;

        numWeights = 0;

        isInput = input;
        isOutput = output;
    }

    //Computation (takes inputs and sets the value)
    public void compute() {
        Double output = 0.0;
        for (int i = 0; i < numWeights; i++) {
            output += feederValues.get(i).getValue() * weights.get(i);
        }
        output += bias;
        output = 1 / (1 + Math.pow(Math.E, (-1 * output)));
        value = output;
    }

    public void calculateDerivatives() {
        if (isOutput) {
            weightDerivatives = new ArrayList<>();

            Double baseline;
            baseline = Math.pow(value - expectedOutput, 2);
            baseline /= value * (1 - value);
            for (int i = 0; i < numWeights; i++) {
                Double thisDerivative = baseline / feederValues.get(i).getValue();
                weightDerivatives.add(thisDerivative);
            }

            biasDerivative = baseline;
        }

        else if (isInput) {
            ; //do nothing
        }

        else {
            weightDerivatives = new ArrayList<>();

            Double baseline;
            baseline = derivative;
            baseline /= value * (1 - value);
            for (int i = 0; i < numWeights; i++) {
                Double thisDerivative = baseline / feederValues.get(i).getValue();
                weightDerivatives.add(thisDerivative);
            }

            biasDerivative = baseline;
        }
    }

    //Used in Network.connectNeurons, this adds an input neuron to a neuron
    public Double addInput(Neuron newInput) {
        feederValues.add(newInput);
        Double addedWeight = Math.random() * 2 - 1;
        weights.add(addedWeight);
        numWeights += 1;
        return addedWeight;
    }

    //sets the value, used in Layer.set, usually used with input layer
    public void setValue(Double newValue) {
        value = newValue;
    }

    public void resetDerivatives() {
        expectedOutput = 0.0;
        derivative = 0.0;
        weightDerivatives = new ArrayList<>();
        biasDerivative = 0.0;
    }

    //returns value, used in computations for other Neurons
    public Double getValue() {
        return value;
    }

    //returns bias, used to assemble all biases in the network class
    public Double getBias() {
        return bias;
    }
}