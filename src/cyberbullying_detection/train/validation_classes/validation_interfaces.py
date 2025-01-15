"""This module implements the AbstractValidation class. for several validation methods"""

from enum import Enum
from typing import Any, Dict, Union

import pandera
import pandera.polars
import pydantic
from hydra import compose
from omegaconf import OmegaConf

from src.cyberbullying_detection.train.abstractions.ABC_validations import (
    IConfigModel,
    IConfigurationLoader,
    IValidationModel,
)


class PanderaValidationModel(IValidationModel):
    """A wrapper for validating dataframes using Pandera."""

    def __init__(
        self,
        validation_model: type[
            Union[pandera.polars.DataFrameModel | pandera.DataFrameModel]
        ],
    ):
        """
        Initializes the PanderaValidationModel with a specified validation ModelsProduction.

        Args:
            validation_model (type): A Pandera DataFrameModel or Polars DataFrameModel type used for validation.
        """
        self.validation_model = validation_model

    def validate(self, dataframe: Any) -> Any:
        """
        Validates the schema of the provided dataframe using the Pandera validation ModelsProduction.

        Args:
            dataframe (Any): The dataframe to be validated.

        Returns:
            Any: The validated dataframe, or raises an error if validation fails.
        """
        return self.validation_model.validate(dataframe)


class PydanticConfigModel(IConfigModel):
    """A wrapper for validating configuration DataTrain using Pydantic."""

    def __init__(self, config_model: type[pydantic.BaseModel]):
        """
        Initializes the PydanticConfigModel with a specified Pydantic ModelsProduction.

        Args:
            config_model (type): A Pydantic BaseModel type used for configuration validation.
        """
        self.config_model = config_model

    def parse(self, config_data: Any) -> Any:
        """
        Validates and parses the given configuration DataTrain using the Pydantic ModelsProduction.

        Args:
            config_data (Any): The configuration DataTrain to be validated and parsed.

        Returns:
            Any: An instance of the Pydantic ModelsProduction populated with the validated configuration DataTrain.

        Raises:
            ValidationError: If the provided configuration DataTrain does not conform to the ModelsProduction.
        """
        return self.config_model(**config_data)


class HydraConfLoader(IConfigurationLoader):
    """A wrapper for loading configuration files using Hydra and OmegaConf."""

    def load(
        self, config_name: str
    ) -> Dict[str | bytes | int | Enum | float | bool, Any] | list | None | str:
        """
        Loads the configuration from a YAML file using Hydra.

        Args:
            config_name (str): The name of the configuration to be loaded.

        Returns:
            Dict: A dictionary representation of the loaded configuration.
        """
        hydra_config = compose(config_name=config_name)
        config_dict = OmegaConf.to_object(hydra_config)
        return config_dict
