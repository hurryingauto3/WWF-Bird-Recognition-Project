# model = ResNet50(input_tensor=image_input, include_top=True,weights='imagenet')
image_input = layers.Input(shape=(224, 224, 3))
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
