import torch

@torch.jit.script
def test_func(input):
    rv = 10.0
    for i in range(5):
        rv = rv + input
        rv = rv/2
    return rv

print(test_func.graph)

