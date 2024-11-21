import java.util.ArrayList;

public class ArrayFunctions {
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

    public static ArrayList<Double> arrayMultiplication(ArrayList<ArrayList<Double>> array, ArrayList<Double> vector) {
        ArrayList<Double> output = new ArrayList<>();

        int size = vector.size();

        for (int i = 0; i < size; i++) {
            Double thisValue = 0.0;
            for (int j = 0; i < size; j++) {
                thisValue += array.get(i).get(j);
            }
            thisValue *= vector.get(i);
            output.add(thisValue);
        }
        return(output);
    }

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
}
