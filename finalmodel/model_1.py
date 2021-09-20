cnn_1 = models.Sequential([
    layers.Conv2D(filters=1024, kernel_size=(3, 3), activation='relu', input_shape=(100, 100, 3)),
    layers.Conv2D(filters=1024, kernel_size=(3, 3), activation='relu'),

    # layers.BatchNormalization(),
    layers.MaxPooling2D((3, 3)),

    layers.Dropout(0.6),

    layers.Flatten(),
    layers.Dense(512, activation='relu', kernel_regularizer=regularizers.l2(0.04)),
    layers.Dropout(0.3),
    layers.Dense(256, activation='relu', kernel_regularizer=regularizers.l2(0.03)),
    layers.Dropout(0.3),
    layers.Dense(128, activation='relu', kernel_regularizer=regularizers.l2(0.02)),
    layers.Dropout(0.3),
    layers.Dense(3, activation='softmax')
])
