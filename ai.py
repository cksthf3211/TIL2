# conda env list
from pprint import pprint
# conda create -n [가상환경이름] python 3.9
# conda activate [가상환경이름]
# conda install pytorch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 pytorch-cuda=11.6 -c pytorch -c nvidia 

import torch
x = torch.rand(5, 3)
print(x)

import torch
# - GPU 사용 가능 -> True, GPU 사용 불가 -> False
torch.cuda.is_available() 

import torch 
print(torch.__version__)

# - GPU 이름 체크(cuda:0에 연결된 그래픽 카드 기준)
print(torch.cuda.get_device_name(), device = 0)
# - 'NVIDIA TITAN X (Pascal)' # 사용 가능 GPU 개수 체크
print(torch.cuda.device_count()) # 3

# pip install torchaudio

import torch
import torchaudio

# - 데이터에 접근
torchaudio.datasets.YESNO(
     root='./',
     url='http://www.openslr.org/resources/1/waves_yesno.tar.gz',
     folder_in_archive='waves_yesno',
     download=True)

yesno_data = torchaudio.datasets.YESNO('./', download=True)

n = 3
waveform, sample_rate, labels = yesno_data[n]
# - 튜플형태 - waveform: 파형, sample_rate: 샘플 속도, labels: 라벨
print("Waveform: {}\nSample rate: {}\nLabels: {}".format(waveform, sample_rate, labels))
# ('Waveform: tensor([[ 3.0518e-05,  6.1035e-05,  3.0518e-05,  ..., '
#  '-1.8311e-04,\n'
#  '          4.2725e-04,  6.7139e-04]])\n'
#  'Sample rate: 8000\n'
#  'Labels: [0, 0, 1, 0, 0, 0, 1, 0]')

# - 데이터셋을 torch.utils.data.DataLoader 로 넘겨줌
# - DataLoader 는 데이터셋을 sampler와 조합시켜 데이터셋을 순회할 수 있는 iterable을 만듬
data_loader = torch.utils.data.DataLoader(
    yesno_data,
    batch_size=1,
    shuffle=True
    )

for data in data_loader:
  print("Data: ", data)
  print("Waveform: {}\nSample rate: {}\nLabels: {}".format(data[0], data[1], data[2]))
  break
# Data:  [tensor([[[-3.0518e-05,  6.1035e-05,  3.0518e-05,  ...,  7.0190e-04,
#            1.5259e-04,  1.2207e-04]]]), tensor([8000]), [tensor([0]), tensor([0]), tensor([1]), tensor([1]), tensor([0]), tensor([1]), tensor([1]), tensor([0])]]
# Waveform: tensor([[[-3.0518e-05,  6.1035e-05,  3.0518e-05,  ...,  7.0190e-04,
#            1.5259e-04,  1.2207e-04]]])
# Sample rate: tensor([8000])
# Labels: [tensor([0]), tensor([0]), tensor([1]), tensor([1]), tensor([0]), tensor([1]), tensor([1]), tensor([0])]

# pip install matplotlib
# 데이터를 시각화 하기
import matplotlib.pyplot as plt
print(data[0][0].numpy())
# [[ 0.0007019   0.0007019   0.0005188  ... -0.00088501 -0.00253296   -0.00115967]]
plt.figure()
plt.plot(waveform.t().numpy())


# --------------------------------------


import torch
import torch.nn as nn
import torch.nn.functional as F

# 이미지를 인식하는 신경망을 정의
# 합성곱(convolution) 방법을 사용
# 커널이나 작은 행렬(matrix)를 통해 가중치를 부여한 이미지의 각 요소를 주변 값과 더함
# 이것은 입력된 이미지의 특징(모서리 감지, 선명함, 흐릿함 등과 같은)을 추출하는 데 도움
# 1개의 입력 이미지 채널을 가지고 목표인 0부터 9까지 숫자를 대표하는 10개의 라벨과 되응되 값을 출력하는 모델을 정의
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()

        # 첫번째 2D 합성곱 계층
        # 1개의 입력 채널(이미지)을 받아들이고, 사각 커널 사이즈가 3인 32개의 합성곱 특징들을 출력
        self.conv1 = nn.Conv2d(1, 32, 3, 1)
        # 두번째 2D 합성곱 계층
        # 32개의 입력 계층을 받아들이고, 사각 커널 사이즈가 3인 64개의 합성곱 특징을 출력
        self.conv2 = nn.Conv2d(32, 64, 3, 1)

        # 인접한 픽셀들은 입력 확률에 따라 모두 0 값을 가지거나 혹은 모두 유효한 값이 되도록 만듬
        self.dropout1 = nn.Dropout2d(0.25)
        self.dropout2 = nn.Dropout2d(0.5)

        # 첫번째 fully connected layer
        self.fc1 = nn.Linear(9216, 128)
        # 10개의 라벨을 출력하는 두번째 fully connected layer
        self.fc2 = nn.Linear(128, 10)

my_nn = Net()
print(my_nn)

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, 1)
        self.conv2 = nn.Conv2d(32, 64, 3, 1)
        self.dropout1 = nn.Dropout2d(0.25)
        self.dropout2 = nn.Dropout2d(0.5)
        self.fc1 = nn.Linear(9216, 128)
        self.fc2 = nn.Linear(128, 10)

    # x는 데이터를 나타냄
    def forward(self, x):
        # 데이터가 conv1을 지나감
        x = self.conv1(x)
        # x를 ReLU 활성함수(rectified-linear activation function)에 대입
        x = F.relu(x)

        x = self.conv2(x)
        x = F.relu(x)

        # x에 대해서 max pooling을 실행
        x = F.max_pool2d(x, 2)
        # 데이터가 dropout1을 지나감
        x = self.dropout1(x)
        # start_dim=1으로 x를 압축
        x = torch.flatten(x, 1)
        # 데이터가 fc1을 지나감
        x = self.fc1(x)
        x = F.relu(x)
        x = self.dropout2(x)
        x = self.fc2(x)

        # x에 softmax를 적용
        output = F.log_softmax(x, dim=1)
        return output
    

# 임의의 28x28 이미지로 맞춰줌
random_data = torch.rand((1, 1, 28, 28))

my_nn = Net()
result = my_nn(random_data)
print (result)

# ------
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, 1)
        self.conv2 = nn.Conv2d(32, 64, 3, 1)
        self.dropout1 = nn.Dropout2d(0.25)
        self.dropout2 = nn.Dropout2d(0.5)
        self.fc1 = nn.Linear(9216, 128)
        self.fc2 = nn.Linear(128, 10)
    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = self.conv2(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)
        x = self.dropout1(x)
        x = torch.flatten(x, 1)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.dropout2(x)
        x = self.fc2(x)
        output = F.log_softmax(x, dim=1)
        return output
    
random_data = torch.rand((1, 1, 28, 28))
my_nn = Net()
result = my_nn(random_data)
print (result)
# tensor([[-2.2461, -2.2776, -2.1615, -2.3338, -2.1912, -2.3508, -2.3556, -2.3509,
#          -2.5396, -2.2685]], grad_fn=<LogSoftmaxBackward>)