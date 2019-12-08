

file = open("input.txt", "r").read()
wide = 25
tall = 6
# file = '0222112222120000'
# wide = 2
# tall = 2

layerLength = wide * tall
numLayers = int(len(file) / (wide * tall))
layers = []

for layerNum in range(0, numLayers):
    start = layerNum * wide * tall
    end = (layerNum + 1) * wide * tall
    layers.append(file[start:end])

finalLayer = [None] * layerLength

for charPos in range(0, layerLength):
    for layer in layers:
        if layer[charPos] != '2':
            value = layer[charPos]
            if value == '1':
                finalLayer[charPos] = "*"
            else:
                finalLayer[charPos] = ' '
            break

finalString = ''.join(finalLayer)
for n in range(0, tall):
    start = n * wide
    end = (n + 1) * wide
    print(finalString[start:end])

# bestLayer = ''
# bestZeros = 10000
#
# for layer in layers.values():
#     zeros = layer.count('0')
#     if zeros < bestZeros:
#         bestZeros = zeros
#         bestLayer = layer
#
# print(bestLayer.count('1'))
# print(bestLayer.count('2'))
# print(bestLayer.count('2') * bestLayer.count('1'))
# #2268 high
