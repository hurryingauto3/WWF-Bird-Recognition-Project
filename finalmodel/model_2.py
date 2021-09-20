#creating the network architecture
cnn_2 = models.Sequential([
    layers.Conv2D(filters=512, kernel_size=(3, 3), activation='relu', padding='same', input_shape=(100, 100, 3)),
    layers.Conv2D(filters=512, kernel_size=(3, 3), activation='relu', padding='same'),
    layers.MaxPooling2D((3, 3)),

    layers.Dropout(0.6),

    layers.Conv2D(filters=256, kernel_size=(3, 3), activation='relu', padding='same'),
    layers.Conv2D(filters=256, kernel_size=(3, 3), activation='relu', padding='same'),
    layers.MaxPooling2D((2, 2)),

    layers.Dropout(0.5),

    layers.Flatten(),
    layers.Dense(512, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(256, activation='relu'),
    layers.Dense(3, activation='softmax')
])
