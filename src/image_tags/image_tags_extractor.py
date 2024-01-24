import torch

from PIL import Image
from ram.models import ram_plus
from ram import inference_ram as inference
from ram import get_transform

# Clone the repo and apply the setup process (install libraries in requirements.txt): https://github.com/xinyu1205/recognize-anything/
# Download the model weight: https://huggingface.co/xinyu1205/recognize-anything-plus-model/blob/main/ram_plus_swin_large_14m.pth


class ImageTagExtractor:
    def __init__(self, src_lang):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        self.transform = get_transform(image_size=384)

        # make sure that the downloaded model weight is accessible in the given path below, or point it to the right path.
        model = ram_plus(pretrained='ram_plus_swin_large_14m.pth',
                         image_size=384,
                         vit='swin_l')
        model.eval()
        self.model = model.to(device)

    def process(self, image_path:str):

        image = self.transform(Image.open(image_path)).unsqueeze(0).to(self.device)
        output = inference(image, model)

        # first item in the array is English (output[0]) and the second one is in Chinese (output[1])
        return output[0]