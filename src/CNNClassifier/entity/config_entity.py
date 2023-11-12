from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_file_path: Path
    unzip_dir : Path


@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    param_image_size: list
    params_learning_rate: float
    param_include_top: bool
    param_weight: str
    param_class: int

@dataclass(frozen=True)
class TrainingModelConfig:
    root_dir : Path
    trained_model_path : Path
    updated_base_model_path : Path
    training_data : Path
    params_epochs : int
    params_batch_size : int
    params_is_augmentation : bool
    params_image_size : list

