from .base import GenerationResult, ImageProvider, ProviderError, TransientProviderError
from .higgsfield import HiggsfieldProvider
from .krea import KreaProvider

PROVIDERS = {
    "krea": KreaProvider,
    "higgsfield": HiggsfieldProvider,
}

__all__ = [
    "GenerationResult",
    "ImageProvider",
    "ProviderError",
    "TransientProviderError",
    "KreaProvider",
    "HiggsfieldProvider",
    "PROVIDERS",
]
