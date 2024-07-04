import matplotlib.pyplot as plt
import torch

from data import PAD_TOKEN, padding_mask


def plot_linear_layer(
    layer,
):
    """
    Plots a heatmap of the weights for a linear layer.

    Parameters:
        layer (nn.Linear): The Linear layer for which the weights are to be visualized.
    """
    with torch.no_grad():
        weights = layer.weight
        plt.imshow(weights, cmap="bwr", aspect="auto", interpolation="none")
        plt.colorbar(label="Weight")
        plt.xlabel("Input")
        plt.ylabel("Output")
        plt.title("Linear Layer Weights")
        plt.show()
    return


def incorrect_predictions(model, dataloader):
    """
    Given a model and a dataloader, this function evaluates the model by predicting the labels for each input in the dataloader.
    It keeps track of incorrect predictions and returns a list of inputs that were incorrectly predicted for each label.

    Args:
        model (torch.nn.Module): The model used for prediction.
        dataloader (torch.utils.data.DataLoader): The dataloader containing the input data.

    Returns:
        List[List[List[int]]]: A list of incorrect predictions for each label. The list contains two sublists, one for each label.
            Each sublist contains a list of inputs that were incorrectly predicted for that label.
            Each input is represented as a list of integers.
    """
    model.eval()

    with torch.no_grad():
        incorrect_predictions = [[], []]
        for data in dataloader:
            inputs, labels = data
            output = model(inputs, mask=padding_mask(inputs))
            predictions = torch.argmax(torch.select(output, 1, 0), dim=1)
            for input, label, prediction in zip(inputs, labels, predictions):
                if label != prediction.item():
                    incorrect_predictions[label].append(input.tolist())
        return incorrect_predictions


def token_contributions(model, single_input):
    """
    Calculates the contributions of each token in the single_input sequence to each class in the model's
    predicted output. The contribution of a single token is calculated as the difference between the
    model output with the given input and the model output with the single token changed to the other
    parenthesis.

    Args:
        model (torch.nn.Module): The model used for prediction.
        single_input (torch.Tensor): The input sequence for which token contributions are calculated.

    Returns:
        List[float]: A list of contributions of each token to the model's output.
    """
    model.eval()
    output = model(single_input)

    result = []
    for i in range(single_input.shape[0]):
        t = single_input.clone()
        t[i] = 1 if t[i] == 0 else 0
        result.append((output - model(t)).abs().sum().item())
    return result

def activations(model, dataloader):
    """
    Returns the frequency of each hidden feature's activation in the feedforward layer of the model
    over all inputs in the dataloader.

    Args:
        model (torch.nn.Module): The model used for prediction.
        dataloader (torch.utils.data.DataLoader): The dataloader containing the input data.

    Returns:
        List[int]: A list of frequencies for each hidden feature in the feedforward layer of the model.
    """
    model.eval()
    activation_counts = {}

    for inputs, _ in dataloader:
        with torch.no_grad():
            outputs = model(inputs)

        activation = model.encoder.layers[0].activations
        for layer_activations in activation:
            for i, feature in enumerate(layer_activations):
                if i not in activation_counts:
                    activation_counts[i] = 0
                activation_counts[i] += feature

    return activation_counts.values()
