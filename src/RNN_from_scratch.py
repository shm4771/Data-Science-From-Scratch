##Idea here is that given the sequence of word, we want to another sequence 
# for this, we need data. so we will use sequence of numbers to make this easier
# the output will be square of the number
import numpy as np 
from numpy.random import randn

class RNN:
    def __init__(self, input_size, output_size, hidden_size=64):      
        #Network architecture
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size      
        #Weight matrices
        normalizer_factor = (self.input_size * self.hidden_size)
        self.Wxh = randn(self.hidden_size, self.input_size) / normalizer_factor
        self.Whh = randn(self.hidden_size, self.hidden_size) / normalizer_factor
        self.Why = randn(self.output_size, self.hidden_size) / normalizer_factor     
        #Biases
        self.bh = np.zeros((hidden_size, 1))
        self.by = np.zeros((output_size, 1))      
        
    def forward(self, inputs):
        """ input is the sequence of integer inputs mapped with words """
        """ for example inputs = [[2, 1, 0], [0, 1]]"""
        """ This function returns the dictonary of all hidden states and outputs for input sequence of vectors"""
        xs, hs, zs, y = {}, {}, {}, {}
        hs[-1] = np.zeros((self.hidden_size, 1)) #initial entry for hidden state at t = 0
        for t, input_val in enumerate(inputs):
            xs[t] = np.zeros((self.input_size, 1), dtype=int)
            xs[t][input_val] = 1
            hs[t] = np.tanh(self.Wxh @ xs[t] + self.Whh @ hs[t-1] + self.bh)
            zs[t] = self.Why @ hs[t] + self.by
            y[t] = self.softmax(zs[t])
        return xs, hs, y
        
    
    def backprop(self, xs, hs, ypred, targets):
        """This function updates the values of weights and biases using BPTT"""
        """ dL_dy is the dictionary of derivative of cross entropy loss with respect to output"""
        DWxh, DWhh, DWhy = np.zeros_like(self.Wxh),np.zeros_like(self.Whh), np.zeros_like(self.Why)
        Dbh, Dby = np.zeros_like(self.bh), np.zeros_like(self.by)
        dh_next = np.zeros((self.hidden_size, 1))
        #dh_next contains previously computed derivative terms
        for t in reversed(range(len(xs))):
            dL_dy = np.copy(ypred[t])
            dL_dy[targets[t]] -= 1
            Dby += dL_dy
            DWhy += dL_dy @ hs[t].T
            
            #dh has two components 
            dh = self.Why.T @ dL_dy + dh_next
            dh_rec = (1- hs[t] * hs[t]) * dh
            
            #Update the weight and bias terms
            Dbh += dh_rec
            DWxh +=  dh_rec @ xs[t].T
            DWhh +=  hs[t-1].T @dh_rec
            dh_next = self.Whh @ dh_rec
            
        for dparam in [DWxh, DWhh, DWhy, Dbh, Dby]:
            np.clip(dparam, -5, 5, out=dparam) 

        return DWxh, DWhh, DWhy, Dbh, Dby
            
    def softmax(self, z):
        return np.exp(z) / sum(np.exp(z))
    
    def update_model(self, DWxh, DWhh, DWhy, Dbh, Dby, alpha=0.01):
        self.Wxh -= alpha * DWxh
        self.Whh -= alpha * DWhh
        self.Why -= alpha * DWhy
        self.bh -= alpha * Dbh
        self.by -= alpha * Dby
    
    def cross_entropy(self, y_pred, y_actual):
        return sum(-np.log(y_pred[t][index]) for t, index in enumerate(y_actual))
    

    def train_model(self, x_data, y_data, epochs=200):
        for epoch in range(epochs):
            loss = 0
            for x_seq, y_seq in zip(x_data, y_data):
                xs, hs, y_pred = self.forward(x_seq)
                loss += self.cross_entropy(y_pred, y_seq)
                DWxh, DWhh, DWhy, Dbh, Dby = self.backprop(xs, hs, y_pred, y_seq)
                self.update_model(DWxh, DWhh, DWhy, Dbh, Dby)
            print("loss:", loss)

            
    def predict(self, x_data):
        y_data = np.zeros_like(x_data)
        for i, x_seq in enumerate(x_data):
            xs, hs, y_pred = self.forward(x_seq)
            for key, arr in y_pred.items():
                predicted_value = int(np.where(arr == np.amax(arr))[0])
                y_data[i][key] = predicted_value
        return y_data


    def one_to_many_predict(self, x_data):
        y_data = []
        for i, x_seq in enumerate(x_data):
            x_0 = np.copy(x_seq)
            for count in range(7):
                xs, hs, y_pred = self.forward(x_seq)
                print("x_seq:", x_seq)
                for key, arr in y_pred.items():
                    predicted_value = int(np.where(arr == np.amax(arr))[0]) + 1
                x_seq = x_seq + [predicted_value]
                #print(x_seq, predicted_value)
            y_data.append(x_seq)
        return y_data

    def test_model(self, x_data, y_data):
        loss = 0
        for x_seq, y_seq in zip(x_data, y_data):
            xs, hs, y_pred = self.forward(x_seq)
            loss = self.cross_entropy(y_pred, y_seq)

        #print("loss:", loss)

def main():
    #creating data for the program 
    data_x = [[0]]
    data_y = [[0]]
    for seq_len in range(2, 5):
        data_x += [[i+j for i in range(seq_len)] for j in range(10)]
        data_y += [[i+j for i in range(seq_len)] for j in range(10)]

    data_x = data_x * 3
    data_y = data_y * 3
    #creating the model
    rnn = RNN(22, 22)
    rnn.train_model(data_x, data_y)

    #Test the model
    print("testing model")
    x_test = [[2], [5]]
    y_data = [[3, 4], [6, 9]]
    #rnn.test_model(x_test, y_data)
    print(rnn.one_to_many_predict(x_test))
    #print(rnn.Wxh)



if __name__ == '__main__':
    main()