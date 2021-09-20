def trainer(dataset, labels, test_s, random_s):
    X_train, X_test, y_train, y_test = train_test_split(dataset, labels, test_size=test_s, random_state=random_s)

    X_train = np.array(X_train) / 255.0
    X_test = np.array(X_test) / 255.0
    y_train = np.array(y_train)
    y_test = np.array(y_test)
    y_train, y_test = np_utils.to_categorical(y_train), np_utils.to_categorical(y_test)

    return X_train, X_test, y_train, y_test
    # len(y_train) - np.count_nonzero(y_train) # 397, 27.6%
    # np.count_nonzero(y_train==1) # 365, 30%
    # np.count_nonzero(y_train==2) # 334, 32.8%
