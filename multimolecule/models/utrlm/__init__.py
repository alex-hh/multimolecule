# MultiMolecule
# Copyright (C) 2024-Present  MultiMolecule

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from transformers import (
    AutoBackbone,
    AutoConfig,
    AutoModel,
    AutoModelForMaskedLM,
    AutoModelForPreTraining,
    AutoModelForSequenceClassification,
    AutoModelForTokenClassification,
    AutoTokenizer,
)

from multimolecule.tokenisers.rna import RnaTokenizer

from ..modeling_auto import (
    AutoModelForNucleotidePrediction,
    AutoModelForSequencePrediction,
    AutoModelForTokenPrediction,
)
from .configuration_utrlm import UtrLmConfig
from .modeling_utrlm import (
    UtrLmForMaskedLM,
    UtrLmForNucleotidePrediction,
    UtrLmForPreTraining,
    UtrLmForSequencePrediction,
    UtrLmForTokenPrediction,
    UtrLmModel,
    UtrLmPreTrainedModel,
)

__all__ = [
    "RnaTokenizer",
    "UtrLmConfig",
    "UtrLmModel",
    "UtrLmPreTrainedModel",
    "RnaTokenizer",
    "UtrLmForMaskedLM",
    "UtrLmForNucleotidePrediction",
    "UtrLmForSequencePrediction",
    "UtrLmForTokenPrediction",
]

AutoConfig.register("utrlm", UtrLmConfig)
AutoBackbone.register(UtrLmConfig, UtrLmModel)
AutoModel.register(UtrLmConfig, UtrLmModel)
AutoModelForMaskedLM.register(UtrLmConfig, UtrLmForMaskedLM)
AutoModelForPreTraining.register(UtrLmConfig, UtrLmForPreTraining)
AutoModelForNucleotidePrediction.register(UtrLmConfig, UtrLmForNucleotidePrediction)
AutoModelForSequencePrediction.register(UtrLmConfig, UtrLmForSequencePrediction)
AutoModelForSequenceClassification.register(UtrLmConfig, UtrLmForSequencePrediction)
AutoModelForTokenPrediction.register(UtrLmConfig, UtrLmForTokenPrediction)
AutoModelForTokenClassification.register(UtrLmConfig, UtrLmForTokenPrediction)
AutoTokenizer.register(UtrLmConfig, RnaTokenizer)
