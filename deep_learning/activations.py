import numpy as np
import pdb


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


def softmax(z):
    e = np.exp(z - np.max(z, axis=1, keepdims=True))
    return e / np.sum(e, axis=1, keepdims=True)


def linear(z):
    return z


def softplus(z):
    return np.log(1 + np.exp(z))


def softsign(z):
    return z / (1 + np.abs(z))


def tanh(z):
    return np.tanh(z)


def relu(z):
    return np.maximum(0, z)


def get_activation(name):
    try:
        return globals()[name]
    except:
        raise ValueError('无效的激活函数')


if __name__ == '__main__':
    activation = get_activation('softplus')
    z = activation(1)
    print(activation)
    print(z)