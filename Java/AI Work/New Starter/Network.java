import java.util.ArrayList;

public class Network {
    private int[] layerSizes;

    private ArrayList<Layer> layers;

    public Network(int[] layerSizes) {
        this.layerSizes = layerSizes;

        Layer inputLayer = new Layer(layerSizes[0], true, false);

        layers.add(inputLayer);

        for (int i = 1; i < layerSizes.length - 1; i++) {
            Layer hiddenLayer = new Layer(layerSizes[i], layerSizes[i - 1], false, false);
            layers.add(hiddenLayer);
        }

        Layer outputLayer = new Layer(layerSizes[layerSizes.length], layerSizes[layerSizes.length - 1], false, true);
        layers.add(outputLayer);
    }
}
