import pandas as pd
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import matplotlib.pyplot as plt

class AI:
    def __init__(self):
        # 2. Build Neural Network
        self.model = Sequential()
        self.model.add(Dense(12, input_dim=7, activation='relu'))  # 12 neurons, 7 inputs
        self.model.add(Dense(8, activation='relu'))  # 8 neurons 12 inputs
        self.model.add(Dense(1, activation='sigmoid'))  # Sigmoid for binary classification # 1 neuron, 8 inputs

    def main_pipeline(self):
        # 1. Load and Prepare Data
        df = pd.read_csv("factorized_credit_card.csv")  # Replace with your dataset path

        # Assuming DEFAULT is your target variable
        nX = df.drop('DEFAULT', axis=1)
        ny = df['DEFAULT']

        X = nX.to_numpy()
        y = ny.to_numpy()

        # 3. Compile and Train
        self.model.compile(loss='binary_crossentropy',
                           optimizer=keras.optimizers.Adam(learning_rate=0.001, gradient_accumulation_steps=None),
                           metrics=['accuracy'])
        # Gradient descent (with momentum) optimizer.
        # self.model.compile(loss='binary_crossentropy',
        #                    optimizer=keras.optimizers.SGD(learning_rate=0.01, gradient_accumulation_steps=None),
        #                    metrics=['accuracy'])
        history = self.model.fit(X, y, epochs=250, batch_size=32, validation_split=0.2)  # Tune hyperparameters

        # 4. Evaluate and Predict (Optional)
        accuracy = self.model.evaluate(X, y)
        acc = history.history['accuracy']
        val_acc = history.history['val_accuracy']
        loss = history.history['loss']
        val_loss = history.history['val_loss']
        epochs_range = range(250)
        plt.figure(figsize=(8, 8))
        plt.subplot(1, 2, 1)
        plt.plot(epochs_range, acc, label='Training Accuracy')
        plt.plot(epochs_range, val_acc, label='Validation Accuracy')
        plt.legend(loc='lower right')
        plt.title('Training and Validation Accuracy')
        plt.subplot(1, 2, 2)
        plt.plot(epochs_range, loss, label='Training Loss')
        plt.plot(epochs_range, val_loss, label='Validation Loss')
        plt.legend(loc='upper right')
        plt.title('Training and Validation Loss')
        plt.show()

    def predict(self, px):
        new_data = pd.DataFrame(px)  # Replace with your new data
        predictions = self.model.predict(new_data)
        return predictions

    def save_model(self):
        self.model.save('model.keras')

    def load_model(self):
        self.model = keras.models.load_model('model.keras')


class NewDataType:
    def __init__(self):
        # Read the CSV file into a DataFrame
        self.df = pd.read_csv('credit_card.csv')

    def execute_factor(self):
        # Convert `CHECKING_ACCOUNT`, `EDUCATION`, and `MARRIAGE` to numerical representations
        for column_name in ['CHECKING_ACCOUNT', 'EDUCATION', 'MARRIAGE']:
            self.df[column_name] = pd.factorize(self.df[column_name])[0]

        # Print the updated dataframe
        print(self.df.head())
        self.df.to_csv('factorized_credit_card.csv', index=False)


def train():
    ai_0 = AI()
    ai_0.main_pipeline()
    ai_0.save_model()
    my_predictions = ai_0.predict([[6022, 0, 0, 0, 24, 934.0122, 0.0]])  # need 1
    print('inference = ' + str(my_predictions) + 'and i need 1')
    my_predictions = ai_0.predict([[27099, 0, 0, 1, 34, 4223.5297, 457.0698]])  #  need 0
    print('inference = ' + str(my_predictions) + 'and i need 0')


def from_pretrained():
    ai_1 = AI()
    ai_1.load_model()
    my_predictions = ai_1.predict([[6022, 1, 2, 1, 44, 2500.0333, 0.0]])  # need 1
    print('inference = ' + str(my_predictions) + 'and i need 1')
    my_predictions = ai_1.predict([[15055, 0, 0, 0, 37, 14522.9563, 602.2]])  # need 0
    print('inference = ' + str(my_predictions) + 'and i need 0')


if __name__ == '__main__':
    train()
    from_pretrained()
