from torch.nn import Module, Conv2d, Linear, MaxPool2d, AdaptiveAvgPool2d
from torch.nn.functional import relu, dropout
from img_preprocess import *
class Network(Module):
    def __init__(self):
        super(Network,self).__init__()
        self.conv1 = Conv2d(in_channels=3, out_channels=64, kernel_size=5)
        self.conv2 = Conv2d(in_channels=64, out_channels=128, kernel_size=3)
        self.conv3 = Conv2d(in_channels=128, out_channels=256, kernel_size=5)

        self.maxPooling = MaxPool2d(kernel_size=4)
        self.adPooling = AdaptiveAvgPool2d(256)

        self.fc1 = Linear(in_features=256, out_features=128)
        self.fc1 = Linear(in_features=128, out_features=64)
        self.fc1 = Linear(in_features=64, out_features=2)

    def forward(self, x):
        x = self.conv1(x)
        x = self.maxPooling(x)
        x = relu(x)

        x = self.conv2(x)
        x = self.maxPooling(x)
        x = relu(x)
        
        x = self.conv3(x)
        x = self.maxPooling(x)
        x = relu(x)
        
        x = dropout(x)
        x = x.view(1, x.size()[0], -1)
        x = self.adPooling(x).squeez()

        x = self.fc1(x)
        x = relu(x)
        
        x = self.fc2(x)
        x = relu(x)

        return self.out(x)


imgldr = ImageLoader(trainData, transform)
dtaldr = DataLoader(imgldr, batch_size=10, shuffle=True)
data = iter(dtaldr)
images = next(data)

ntwrk = Network()
out = ntwrk(images[0])
print(out.size())