# Work in Progress

import os
import h5py
from keras import backend as K

weights_path = 'mnist_model_weights.h5'

assert os.path.exists(weights_path), 'Model weights not found (see "weights_path" variable in script).'
f = h5py.File(weights_path)
layer_names = [n.decode('utf8') for n in f.attrs['layer_names']]
print(layer_names)
weight_value_tuples = []
for k, name in enumerate(layer_names):
    # if k >= len(model.layers):
    #     # 全結合層の重みは読み込まない
    #     break
    g = f[name]
    weight_names = [n.decode('utf8') for n in g.attrs['weight_names']]
    print(weight_names)
    if len(weight_names):
        weight_values = [g[weight_name] for weight_name in weight_names]
        print(weight_values)
        print(len(weight_values[0]))
        print(weight_values[0][0])
        # layer = model.layers[k]
        # symbolic_weights = layer.trainable_weights + layer.non_trainable_weights
#         if len(weight_values) != len(symbolic_weights):
#             raise Exception('Layer #' + str(k) +
#                             ' (named "' + layer.name +
#                             '" in the current model) was found to '
#                             'correspond to layer ' + name +
#                             ' in the save file. '
#                             'However the new layer ' + layer.name +
#                             ' expects ' + str(len(symbolic_weights)) +
#                             ' weights, but the saved weights have ' +
#                             str(len(weight_values)) +
#                             ' elements.')
#         weight_value_tuples += zip(symbolic_weights, weight_values)
# K.batch_set_value(weight_value_tuples)
f.close()
print('Model loaded.')
