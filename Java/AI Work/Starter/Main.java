import java.util.ArrayList;
// import java.lang.Math;

public class Main {
    public static void main(String[] args) {
        //Timing
        long startTime = System.nanoTime();
        
        //Program start
        int[] networkSpecifications = {2, 10, 15, 100, 100, 2};
        Network neuralNetwork = new Network(networkSpecifications);
        neuralNetwork.connectNeurons();

        int epochs = 1000; //generations
        int miniBatchSize = 20; //num of test cases per epoch

        for (int i = 0; i < epochs; i++) {
            Double totalCost = 0.0;

            for (int j = 0; j < miniBatchSize; j++) {
                ArrayList<Double> networkInput = new ArrayList<>();

                networkInput.add(Math.random() * 16); //temp inputs
                networkInput.add(Math.random() * 10); //temp inputs
        
                neuralNetwork.compute(networkInput);

                ArrayList<Double> expectedOutput = new ArrayList<>();

                if (evaluate(networkInput.get(0), networkInput.get(1))) {
                    expectedOutput.add(1.0);
                    expectedOutput.add(0.0);
                }
                else {
                    expectedOutput.add(0.0);
                    expectedOutput.add(1.0);
                }

                totalCost += neuralNetwork.computeCost(expectedOutput);

            }

            totalCost = totalCost / 20;
            System.out.println("average cost: " + totalCost);
        }

        //Timing
        long endTime = System.nanoTime();
        long duration = (endTime - startTime);
        duration /= 1000000;

        System.out.println("" + duration + " miliseconds.");

    }

    public static boolean evaluate(Double x, Double y) {
        return((Math.pow(x-5, 2) + Math.pow(y-3, 2) < 10) || (Math.pow(x-8, 2) + 5 * Math.pow(y-3, 2) < 10) || (y > 50/x));
    }

}