import java.util.ArrayList;

public class Network {
    private int[] layerSizes;
    private int numLayers; //how many layers
    private int outputSize;

    private ArrayList<Layer> layers = new ArrayList<>();

    //Constructor
    public Network(int[] layerSizes) {
        this.layerSizes = layerSizes;
        this.numLayers = layerSizes.length;

        Layer inputLayer = new Layer(layerSizes[0], true, false);

        layers.add(inputLayer);

        for (int i = 1; i < numLayers - 1; i++) {
            Layer hiddenLayer = new Layer(layerSizes[i], layerSizes[i - 1], false, false);
            layers.add(hiddenLayer);
        }

        Layer outputLayer = new Layer(layerSizes[numLayers - 1], layerSizes[numLayers - 2], false, true);
        layers.add(outputLayer);
        outputSize = layerSizes[numLayers - 1];

        //Connecting layers
        for (int i = 1; i < numLayers; i++) {
            layers.get(i).setPreviousLayer(layers.get(i-1));
        }
    }

    //compute
    public ArrayList<Double> compute(ArrayList<Double> input) {
        layers.get(0).setValues(input);
        for (int i = 1; i < numLayers; i++) {
            layers.get(i).compute();
        }
        return(layers.get(numLayers - 1).getOutput());
    }

    //compute cost
    public Double computeCost(ArrayList<Double> input, ArrayList<Double> expectedResult) {
        ArrayList<Double> networkOutput = compute(input);
        Double costOutput = 0.0;

        for (int i = 0; i < outputSize; i++) {
            costOutput += Math.pow((expectedResult.get(i) - networkOutput.get(i)), 2) / 2.0;
        } 

        return costOutput;
    }
    public Double computeCostAll(ArrayList<ArrayList<ArrayList<Double>>> batch) {
        int batchSize = batch.size();
        Double totalCost = 0.0;
        for (int i = 0; i < batchSize; i++) {
            ArrayList<ArrayList<Double>> thisData = batch.get(i);
            totalCost += computeCost(thisData.get(0), thisData.get(1));
        }
        totalCost /= batchSize;
        return totalCost;
    }

    //train
    public void train(ArrayList<ArrayList<ArrayList<Double>>> trainingData, Double learningRate) {
        int dataSize = trainingData.size();

        Double originalCost = computeCostAll(trainingData);
        remember();
        mutate(learningRate);
        Double newCost = computeCostAll(trainingData);
        if (newCost > originalCost) {
            rollBack();
        }
        else {
            System.out.println("Cost: " + originalCost);
        }
    }

    public Double examine(ArrayList<ArrayList<ArrayList<Double>>> trainingData) {
        int dataSize = trainingData.size();
        Double correct = 0.0;
        Double wrong = 0.0;
        for (int i = 0; i < dataSize; i++) {
            ArrayList<ArrayList<Double>> thisData = trainingData.get(i);
            ArrayList<Double> networkOutput = compute(thisData.get(0));
            ArrayList<Double> expectedResult = thisData.get(1);
            if (networkOutput.get(0) > networkOutput.get(1)) {
                if (expectedResult.get(0) > expectedResult.get(1)) {
                    correct += 1.0;
                }
                else {
                    wrong += 1.0;
                }
            }
            else {
                if (expectedResult.get(1) > expectedResult.get(0)) {
                    correct += 1.0;
                }
                else {
                    wrong += 1.0;
                }
            }
        }
        System.out.println("" + correct + " " + wrong);
        return(100 * correct / (correct + wrong));
    }

    //get output
    public ArrayList<Double> getOutput() {
        return(layers.get(numLayers - 1).getOutput());
    }

    /*
     * Getting better at results
     * To do:
     * random mutations
     *    mutate
     *    remember
     * backpropogation
     *    i dont even know what the freak
     */
    //RANDOM MUTATIONS
    public void remember() {
        for (int i = 1; i < numLayers; i++) {
            layers.get(i).remember();
        }
    }

    public void rollBack() {
        for (int i = 1; i < numLayers; i++) {
            layers.get(i).rollBack();
        }
    }

    public void mutate(Double learningRate) {
        for (int i = 1; i < numLayers; i++) {
            layers.get(i).mutate(learningRate);
        }
    }


    //BACKPROPOGATION
}