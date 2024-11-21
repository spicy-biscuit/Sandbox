import java.util.ArrayList;
// import java.lang.Math;

public class Layer {

    //FIXME: Add support for inputting expected output of a neuron into said neuron

    ArrayList<Neuron> neurons = new ArrayList<>();
    int size;
    boolean isInput = false;
    boolean isOutput = false;

    //Constructor
    public Layer(int numNeurons, boolean input, boolean output) {
        for (int i = 0; i < numNeurons; i++) {
            neurons.add(new Neuron(input, output));
        }
        size = numNeurons;
    }

    public void compute() {
        for (int i = 0; i < size; i++) {
            neurons.get(i).compute();
        }
    }

    //setting the layer to a set of values - usually for input layer
    public void set(ArrayList<Double> newValues) {
        for (int i = 0; i < size; i++) {
            neurons.get(i).setValue(newValues.get(i));
        }
    }

    //Accessing
    public ArrayList<Double> asArray() {
        ArrayList<Double> returnThis = new ArrayList<>();

        for (int i = 0; i < size; i++) {
            returnThis.add(neurons.get(i).getValue());
        }

        return returnThis;
    }

    public ArrayList<Neuron> asNeuronList() {
        return neurons;
    }

    public int getSize() {
        return size;
    }
}