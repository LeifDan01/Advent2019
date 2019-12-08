

file = open("input.txt", "r").read()
# file = '123456789012'
opcodesOG = file.split(",")

wide = 25
tall = 6
numLayers = int(len(file) / (wide * tall))
layers = {}

for layerNum in range(0, numLayers):
    start = layerNum * wide * tall
    end = (layerNum + 1) * wide * tall
    layers[layerNum] = file[start:end]

bestLayer = ''
bestZeros = 10000

for layer in layers.values():
    zeros = layer.count('0')
    if zeros < bestZeros:
        bestZeros = zeros
        bestLayer = layer

print(bestLayer.count('1'))
print(bestLayer.count('2'))
print(bestLayer.count('2') * bestLayer.count('1'))
#2268 high
