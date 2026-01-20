import torch
import torch.nn as nn

# Baseline model
class BaselineModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(100, 64),
            nn.ReLU(),
            nn.Linear(64, 4)
        )

    def forward(self, x):
        return self.model(x)


# Dendritic-inspired optimized model
class DendriticModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.dendritic = nn.Sequential(
            nn.Linear(100, 32),
            nn.ReLU(),
            nn.Linear(32, 16),
            nn.ReLU()
        )
        self.output = nn.Linear(16, 4)

    def forward(self, x):
        x = self.dendritic(x)
        return self.output(x)
