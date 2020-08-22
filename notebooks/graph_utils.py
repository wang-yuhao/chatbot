import matplotlib.pyplot as plt

def plot_metrics(metrics_name, train_data, dev_data, epochs):
    epochs = [i for i in range(1,epochs+1)]
    label1 = 'train_' + metrics_name
    label2 = 'dev_' + metrics_name
    plt.plot(epochs, train_data, label=label1)
    plt.plot(epochs, dev_data, label=label2)
    plt.xlabel('Epochs')
    plt.ylabel(metrics_name)

    plt.title('Metrics - ' + metrics_name)
    plt.legend()
    plt.savefig('Metrics_' + metrics_name + '.png', dpi=600)
    plt.show()
    
def plot_loss(train_data, epochs):
    epochs = [i for i in range(1,epochs+1)]
    plt.plot(epochs, train_data, label='loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')

    plt.title('Train - Loss')
    plt.legend()
    plt.savefig('train_loss.png', dpi=600)
    plt.show()
