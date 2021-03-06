import torch
import torch.utils.data as data
import random
from PIL import Image


class ImageFolder(data.Dataset):
    def __init__(
        self,
        root,
        transform=None,
        target_transform=None,
        loader=None,
        is_valid_file=None,
    ):
        super(ImageFolder, self).__init__()
        self.root = root
        self.transform = transform
        self.target_transform = target_transform

        self.len = 100

    def __getitem__(self, index):
        # TODO: image size range and target range settings in pyteaconfig.json

        img = Image.Image()
        height = random.randint(256, 1280)
        width = random.randint(256, 1280)
        img._setSize(1, height, width)
        target = random.randint(0, 9)

        if self.transform is not None:
            img = self.transform(img)
        if self.target_transform is not None:
            target = self.target_transform(target)

        return img, target

    def __len__(self):
        return self.len
