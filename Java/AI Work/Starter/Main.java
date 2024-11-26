import java.util.ArrayList;
import java.util.Collections;

public class Main {
    public static void main(String[] args) {
        int[] networkSpecifications = {3, 5, 5, 2};

        Network neuralNetwork = new Network(networkSpecifications);
        
        ArrayList<Double> input = new ArrayList<>();
        input.add(0.483);
        input.add(0.5483929);
        
        ArrayList<Double> expected = new ArrayList<>();
        expected.add(0.0);
        expected.add(1.0);

        System.out.println(neuralNetwork.computeCost(input, expected));
        
        //create training batch
        ArrayList<ArrayList<ArrayList<Double>>> trainingBatch = new ArrayList<>();
        for (int i = 0; i < 100000; i++) {
            ArrayList<ArrayList<Double>> thisData = new ArrayList<>();
            ArrayList<Double> inputData = new ArrayList<>();
            Double x = Math.random();
            Double y = Math.random();
            Double z = Math.random();
            inputData.add(x);
            inputData.add(y);
            inputData.add(z);
            ArrayList<Double> outputData = getCorrectOutput(x, y, z);
            thisData.add(inputData);
            thisData.add(outputData);
            trainingBatch.add(thisData);
        }
        //create testing batch
        ArrayList<ArrayList<ArrayList<Double>>> testingBatch = new ArrayList<>();
        for (int i = 0; i < 10000; i++) {
            ArrayList<ArrayList<Double>> thisData = new ArrayList<>();
            ArrayList<Double> inputData = new ArrayList<>();
            Double x = Math.random();
            Double y = Math.random();
            Double z = Math.random();
            inputData.add(x);
            inputData.add(y);
            inputData.add(z);
            ArrayList<Double> outputData = getCorrectOutput(x, y, z);
            thisData.add(inputData);
            thisData.add(outputData);
            testingBatch.add(thisData);
        }

        while (true) {
            
            for (int i = 0; i < 100; i++) {
                Collections.shuffle(trainingBatch);
                ArrayList<ArrayList<ArrayList<Double>>> miniBatch = new ArrayList<>(trainingBatch.subList(0, 1000));
                neuralNetwork.train(miniBatch, 0.01);
            }
            
            System.out.println("Percent correct: " + neuralNetwork.examine(testingBatch));
        }

    }

    public static ArrayList<Double> getCorrectOutput(Double x, Double y, Double z) {
        boolean a = false;
        if (x * y - z >= 0.58) {
            a = true;
        }
        if (x + y - z < -1.0) {
            a = true;
        } 

        ArrayList<Double> b = new ArrayList<>();
        if (a) {
            b.add(1.0);
            b.add(0.0);
            return b;
        }
        b.add(0.0);
        b.add(1.0);
        return b;
    }
}
