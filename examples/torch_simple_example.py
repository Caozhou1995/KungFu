#!/usr/bin/env python3

import kungfu.torch as kf
import torch

for d in dir(kf):
    print(d)

for d in dir(kf.ops):
    print(d)

f = kf.ops.collective.all_reduce
print(f)

x = torch.Tensor([2, 3])
print(x)

y = kf.ops.collective.all_reduce(x)
print(y)
