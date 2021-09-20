import dependencies

dataset, labels = load_dataset()
dataset = read_images(dataset)

print(labels.count(0), labels.count(1), labels.count(2))

X_train, X_test, y_train, y_test = trainer(dataset, labels, 0.3, 42)

cnn_1.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

cnn_1.summary()

# cnn_2.compile(optimizer='sgd',
#               loss='categorical_crossentropy',
#               metrics=['accuracy'])
#
# cnn_2.summary()

"""# Training"""

cnn1_history = cnn_1.fit(X_train, y_train, epochs=30, batch_size=32, validation_data=(X_test, y_test))
# cnn2_history = cnn_2.fit(X_train, y_train, epochs=30, batch_size=32, validation_data=(X_test, y_test))

"""# Results"""

#plotting loss graph
plt.figure()
plt.title('Loss')
plt.plot(cnn_history.history['loss'])
plt.plot(cnn_history.history['val_loss'])
plt.legend(['train', 'test'])
plt.ylim([0, 18])
plt.show()

#plotting accuracy graph
plt.figure()
plt.title('Accuracy')
plt.plot(cnn_history.history['accuracy'])
plt.plot(cnn_history.history['val_accuracy'])
plt.legend(['train', 'test'])
plt.ylim([0, 1])
plt.show()

"""# ResNet"""

image_input = layers.Input(shape=(224, 224, 3))

# model = ResNet50(input_tensor=image_input, include_top=True,weights='imagenet')

res = applications.ResNet50(
    include_top=True,
    weights=None,
    input_tensor=image_input,
    input_shape=(224,224,3),
    pooling=None,
    classifier_activation="softmax",
)

last_layer = res.get_layer('avg_pool').output
x = layers.Flatten(name='flatten1')(last_layer)
d1 = layers.Dropout(0.5, name='dropout1')(x)

y = layers.Dense(512, activation='relu', name='flatten2')(d1)
d2 = layers.Dropout(0.5, name='dropout2')(y)

z = layers.Dense(256, activation='relu', name='flatten3')(d2)
d3 = layers.Dropout(0.5, name='dropout3')(z)

out = layers.Dense(3, activation='softmax', name='output_layer')(d3)
resnet = models.Model(inputs=image_input,outputs= out)

resnet.compile(optimizer = optimizers.Adam(0.001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

resnet.summary()

resnet_history = resnet.fit(X_train, y_train, epochs=10, batch_size=64, validation_data=(X_test, y_test))

#plotting accuracy graph
plt.figure()
plt.title('Accuracy')
plt.plot(resnet_history.history['accuracy'])
plt.plot(resnet_history.history['val_accuracy'])
plt.legend(['train', 'test'])
plt.ylim([0, 1])
plt.show()

predictions = resnet.predict(X_test)

predictions.shape

predictions[0]
