#  Copyright (c) ZenML GmbH 2021. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at:
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#  or implied. See the License for the specific language governing
#  permissions and limitations under the License.

from typing import Any, Dict, List, Tuple


class ConfigKeys:
    """Class to validate dictionary configurations."""

    @classmethod
    def get_keys(cls) -> Tuple[List[str], List[str]]:
        """Gets all the required and optional config keys for this class.

        Returns:
            A tuple (required, optional) which are lists of the
            required/optional keys for this class.
        """
        keys = {
            key: value
            for key, value in cls.__dict__.items()
            if not isinstance(value, classmethod)
            and not isinstance(value, staticmethod)
            and not callable(value)
            and not key.startswith("__")
        }

        required = [v for k, v in keys.items() if not k.endswith("_")]
        optional = [v for k, v in keys.items() if k.endswith("_")]

        return required, optional

    @classmethod
    def key_check(cls, config: Dict[str, Any]) -> None:
        """Checks whether a configuration dict contains all required keys
        and no unknown keys.

        Args:
            config: The configuration dict to verify.

        Raises:
            AssertionError: If the dictionary contains unknown keys or
                is missing any required key.
        """
        assert isinstance(config, dict), "Please specify a dict for {}".format(
            cls.__name__
        )

        # Required and optional keys for the config dict
        required, optional = cls.get_keys()

        # Check for missing keys
        missing_keys = [k for k in required if k not in config.keys()]
        assert len(missing_keys) == 0, "Missing key(s) {} in {}".format(
            missing_keys, cls.__name__
        )

        # Check for unknown keys
        unknown_keys = [
            k for k in config.keys() if k not in required and k not in optional
        ]
        assert (
            len(unknown_keys) == 0
        ), "Unknown key(s) {} in {}. Required keys : {} " "Optional Keys: {}".format(
            unknown_keys,
            cls.__name__,
            required,
            optional,
        )


class PipelineConfigurationKeys(ConfigKeys):
    """Keys for a pipeline configuration dict."""

    NAME = "name"
    STEPS = "steps"


class StepConfigurationKeys(ConfigKeys):
    """Keys for a step configuration dict."""

    SOURCE_ = "source"
    PARAMETERS_ = "parameters"
    MATERIALIZERS_ = "materializers"
