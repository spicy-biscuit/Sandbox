import java.util.ArrayList;

public class ArrayFunctions {

    //componentwise combining arrays
    public static ArrayList<Double> componentMultiply(ArrayList<Double> array1, ArrayList<Double> array2) {
        ArrayList<Double> output = new ArrayList<>();

        for (int i = 0; i < array1.size(); i++) {
            output.add(array1.get(i) * array2.get(i));
        }

        return output;
    }
    
    public static ArrayList<Double> componentAdd(ArrayList<Double> array1, ArrayList<Double> array2) {
        ArrayList<Double> output = new ArrayList<>();

        for (int i = 0; i < array1.size(); i++) {
            output.add(array1.get(i) + array2.get(i));
        }

        return output;
    }
    
    public static ArrayList<Double> componentSubtract(ArrayList<Double> array1, ArrayList<Double> array2) {
        ArrayList<Double> output = new ArrayList<>();

        for (int i = 0; i < array1.size(); i++) {
            output.add(array1.get(i) - array2.get(i));
        }

        return output;
    }

    //Array multiplication by a vector
    public static ArrayList<Double> arrayMultiplication(ArrayList<ArrayList<Double>> array, ArrayList<Double> vector) {
        ArrayList<Double> output = new ArrayList<>();

        int size = vector.size();
        int arrayHeight = array.size();

        for (int i = 0; i < arrayHeight; i++) {
            Double thisValue = 0.0;
            ArrayList<Double> thisArray = array.get(i);
            for (int j = 0; j < size; j++) {
                thisValue += thisArray.get(j) * vector.get(j);
            }
            output.add(thisValue);
        }
        return(output);
    }

    //Transpose a 2d array
    //NOT FUNCTIONING, RECODE TO SOLVE W/ MEMORY ALLOCATION
    public static ArrayList<ArrayList<Double>> transpose(ArrayList<ArrayList<Double>> array) {
        int rows = array.size();
        int columns = array.get(0).size();

        rows += 1;
        columns += 1;

        rows /= 2;
        columns /= 2;

        for (int i = 0; i < rows; i++){
            for (int j = 0; j < columns; j++) {
                Double temp = array.get(i).get(j);
                array.get(i).set(j, array.get(j).get(i));
                array.get(j).set(i, temp);
            }
        }

        return array;
    }

    //sigmoid
    private static Double sigmoid(Double input) {
        return 1 / (1 + Math.exp(-input));
    }

    public static ArrayList<Double> sigmoid(ArrayList<Double> values) {
        for (int i = 0; i < values.size(); i++) {
            values.set(i, sigmoid(values.get(i)));
        }
        return values;
    }
}
