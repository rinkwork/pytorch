import torch

if torch.cuda.is_available():
    print("PyTorch is using the GPU")
else:
    print("PyTorch is using the CPU")
