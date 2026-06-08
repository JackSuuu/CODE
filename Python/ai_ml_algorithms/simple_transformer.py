import torch
import torch.nn as nn


class Transformer(nn.Module):
    def __init__(self, input_dim, hidden_dim, num_layers, num_heads):
        super(Transformer, self).__init__()

        self.embedding = nn.Embedding(input_dim, hidden_dim)
        self.encoder = nn.TransformerEncoder(
            nn.TransformerEncoderLayer(hidden_dim, num_heads),
            num_layers
        )
        self.fc = nn.Linear(hidden_dim, input_dim)

    def forward(self, x):
        embedded = self.embedding(x)
        encoded = self.encoder(embedded)
        output = self.fc(encoded)
        return output


# Example usage:
input_dim = 1000
hidden_dim = 256
num_layers = 4
num_heads = 8

model = Transformer(input_dim, hidden_dim, num_layers, num_heads)

# Initialize input tensor
input_tensor = torch.tensor([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# Forward pass
output = model(input_tensor)
print(output)
