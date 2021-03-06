import torch
import torch.utils.data as data
import random
from PIL import Image


class CIFAR10(data.Dataset):
    def __init__(
        self, root, train=True, transform=None, target_transform=None, download=False,
    ):
        super(CIFAR10, self).__init__()
        self.root = root
        self.transform = transform
        self.target_transform = target_transform

        # TODO: symbolic?
        if train:
            self.len = 500
        else:
            self.len = 100

    def __getitem__(self, index):
        img = Image.Image()
        img._setSize(3, 28, 28)
        target = random.randint(0, 9)

        if self.transform is not None:
            img = self.transform(img)
        if self.target_transform is not None:
            target = self.target_transform(target)

        return img, target

    def __len__(self):
        return self.len


class CIFAR100(data.Dataset):
    def __init__(
        self, root, train=True, transform=None, target_transform=None, download=False,
    ):
        super(CIFAR100, self).__init__()
        self.root = root
        self.transform = transform
        self.target_transform = target_transform

        # TODO: symbolic?
        if train:
            self.len = 500
        else:
            self.len = 100

    def __getitem__(self, index):
        img = Image.Image()
        img._setSize(3, 28, 28)
        target = random.randint(0, 99)

        if self.transform is not None:
            img = self.transform(img)
        if self.target_transform is not None:
            target = self.target_transform(target)

        return img, target

    def __len__(self):
        return self.len
