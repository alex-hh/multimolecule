from __future__ import annotations

from typing import Tuple

import torch
from torch import Tensor, nn
from torch.nn import functional as F
from transformers.activations import ACT2FN
from transformers.modeling_outputs import ModelOutput

from multimolecule.models.configuration_utils import PretrainedConfig

from .output import HeadOutput
from .transform import HeadTransforms


class MaskedLMHead(nn.Module):
    """Head for masked language modeling."""

    def __init__(self, config: PretrainedConfig, weight: Tensor | None = None):
        super().__init__()
        self.config = config.lm_head if hasattr(config, "lm_head") else config.head
        if self.config.hidden_size is None:
            self.config.hidden_size = config.hidden_size
        self.num_labels = config.vocab_size
        self.dropout = nn.Dropout(self.config.dropout)
        self.transform = HeadTransforms.build(self.config)
        self.decoder = nn.Linear(self.config.hidden_size, self.num_labels, bias=False)
        if weight is not None:
            self.decoder.weight = weight
        if self.config.bias:
            self.bias = nn.Parameter(torch.zeros(self.num_labels))
            self.decoder.bias = self.bias
        self.activation = ACT2FN[self.config.act] if self.config.act is not None else None

    def forward(self, outputs: ModelOutput | Tuple[Tensor, ...], labels: Tensor | None = None) -> HeadOutput:
        sequence_output = outputs[0]
        output = self.dropout(sequence_output)
        output = self.transform(output)
        output = self.decoder(output)
        if self.activation is not None:
            output = self.activation(output)
        if labels is not None:
            return HeadOutput(output, F.cross_entropy(output.view(-1, self.config.vocab_size), labels.view(-1)))
        return HeadOutput(output)