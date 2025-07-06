import torch
import torch.nn as nn

class Generator(nn.Module):
    def __init__(self, noise_dim: int = 100, output_dim: int = 256):
        super(Generator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(noise_dim, 128),
            nn.LeakyReLU(0.2),
            nn.Linear(128, 256),
            nn.LeakyReLU(0.2),
            nn.Linear(256, output_dim),
            nn.Tanh()  
        )

    def forward(self, z: torch.Tensor) -> torch.Tensor:
        return self.model(z)
