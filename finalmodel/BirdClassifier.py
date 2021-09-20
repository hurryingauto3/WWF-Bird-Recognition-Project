import dependencies

dataset, labels = load_dataset()
dataset = read_images(dataset)
X_train, X_test, y_train, y_test = trainer(dataset, labels, 0.3, 42)

#cnn models
cnn_1.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

cnn_1.summary()
# cnn_2.compile(optimizer='sgd',
#               loss='categorical_crossentropy',
#               metrics=['accuracy'])
#
# cnn_2.summary()

#CNN training
cnn1_history = cnn_1.fit(X_train, y_train, epochs=30, batch_size=32, validation_data=(X_test, y_test))
# cnn2_history = cnn_2.fit(X_train, y_train, epochs=30, batch_size=32, validation_data=(X_test, y_test))

#CNN Results
loss_plot(cnn1_history)
accuracy_plot(cnn1_history)
# loss_plot(cnn2_history)
# accuracy_plot(cnn2_history)

"""# ResNet"""
resnet.compile(optimizer = optimizers.Adam(0.001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

resnet.summary()

resnet_history = resnet.fit(X_train, y_train, epochs=10, batch_size=64, validation_data=(X_test, y_test))

#ResNet Results

loss_plot(resnet_history)
accuracy_plot(resnet_history)

# predictions = resnet.predict(X_test)
#
# predictions.shape
#
# predictions[0]
