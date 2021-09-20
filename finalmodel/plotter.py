def loss_plot(cnn_history):
    #plotting loss graph
    plt.figure()
    plt.title('Loss')
    plt.plot(cnn_history.history['loss'])
    plt.plot(cnn_history.history['val_loss'])
    plt.legend(['train', 'test'])
    plt.ylim([0, 18])
    plt.show()

def accuracy_plot(cnn_history):
    #plotting accuracy graph
    plt.figure()
    plt.title('Accuracy')
    plt.plot(cnn_history.history['accuracy'])
    plt.plot(cnn_history.history['val_accuracy'])
    plt.legend(['train', 'test'])
    plt.ylim([0, 1])
    plt.show()
