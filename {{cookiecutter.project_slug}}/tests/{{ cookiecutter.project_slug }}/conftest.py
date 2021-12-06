"""conftest.py file for {{ cookiecutter.project_slug }}"""
import json
import logging
from importlib import resources
from pathlib import Path
from logging.handlers import RotatingFileHandler
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union


import pytest

APP_LOG_LEVEL = logging.INFO
TEST_LOG_LEVEL = logging.DEBUG


@dataclass
class FileResource:
    file_path: Path
    data: Any


@pytest.fixture(scope="session", name="logger")
def _logger(test_log_path):
    """A central logger that will log to file."""
    # log_file_name = f"{__name__}.log"
    log_dir_path: Path = test_log_path / Path("test-logs")

    logger = configure_file_logger(
        log_dir=log_dir_path, logger_name=__name__, log_level=TEST_LOG_LEVEL
    )

    return logger


def configure_file_logger(
    log_dir: str, logger_name: str, log_level: Union[str, int]
) -> logging.Logger:
    """Configure a logger with a RotatingFileHandler.

    Note: Calling this function more than once with the same logger_name
    will result in duplicated logs.
    """
    log_file_name = f"{logger_name}.log"
    logger_ = logging.getLogger(logger_name)
    log_dir_path: Path = Path(log_dir)
    log_dir_path.mkdir(parents=True, exist_ok=True)
    log_file_path = log_dir_path / Path(log_file_name)
    handler = log_file_handler(log_file_path, log_level=log_level)
    logger_.addHandler(handler)
    logger_.setLevel(log_level)
    ############################################################
    # NOTE add file handler to other library modules as needed #
    ############################################################
    # async_logger = logging.getLogger("eve_esi_jobs")
    # async_logger.addHandler(file_handler)
    # async_logger.setLevel(log_level)
    logger_.info("Rotating File Logger initializd at %s", log_file_path)
    return logger_


def log_file_handler(
    file_path: Path,
    log_level: int = logging.WARNING,
    format_string: Optional[str] = None,
):
    handler = RotatingFileHandler(file_path, maxBytes=102400, backupCount=10)
    if format_string is None:
        format_string = (
            "%(asctime)s %(levelname)s:%(funcName)s: "
            "%(message)s [in %(pathname)s:%(lineno)d]"
        )
    handler.setFormatter(logging.Formatter(format_string))
    handler.setLevel(log_level)
    return handler


@pytest.fixture(scope="session", name="test_log_path")
def test_log_path_(test_app_data_dir):
    """Make a test-log directory under the app data directory"""
    log_path = test_app_data_dir / Path("test-logs")
    print(f"Logging at: {log_path}")
    return log_path


@pytest.fixture(scope="session", name="test_app_data_dir")
def test_app_data_dir_(tmp_path_factory):
    """make a temp directory for app data."""
    test_app_data_dir = tmp_path_factory.mktemp("{{ cookiecutter.project_slug }}-")
    return test_app_data_dir


# @pytest.fixture(scope="session")
# def example_resource(logger: logging.Logger) -> dict:
#     """Load a resource file from a package directory.

#     An example of loading a single resource file.
#     """
#     try:
#         resource_path: str = "tests.{{ cookiecutter.project_slug }}.resources"
#         resource_name: str = "example.json"
#         with resources.open_text(resource_path, resource_name) as data_file:
#             data = json.load(data_file)
#             logger.info("Loaded resource file %s from %s", resource_name, resource_path)
#             return data
#     except Exception as ex:
#         logger.exception(
#             "Unable to load resource file %s from %s Error msg %s",
#             resource_name,
#             resource_path,
#             ex,
#         )
#         raise ex


@pytest.fixture(scope="session", name="json_resources")
def json_resources_example_(logger: logging.Logger) -> Dict[str, FileResource]:
    """
    Load all json resource files in a directory to a dict indexed by file name.

    Excludes __init__.py
    """
    json_resources = {}
    resource_path: str = "tests.{{ cookiecutter.project_slug }}.json_resources"
    resource_names = collect_resource_names(resource_path, [".json"])
    for name in resource_names:
        resource = load_json_resource(resource_path, name, logger)
        json_resources[name] = resource
    return json_resources


def load_json_resource(
    resource_path: str, resource_name: str, logger: logging.Logger
) -> FileResource:
    resource = load_file_resource(resource_path, resource_name, logger)
    resource.data = json.loads(resource.data)
    return resource


def load_file_resources(
    resource_path: str,
    resource_names: List[str],
    logger: logging.Logger,
    include_suffixes: Optional[List[str]] = None,
    path_only: bool = False,
    read_text: bool = True,
) -> Dict[str, FileResource]:
    """
    Load all the files found at a resource location.

    [extended_summary]

    Args:
        resource_path: package path to resource folder, eg. tests.resources.photos
        resource_names: A list of resources to load. An empty list means load all files found.
        logger: logger, usually passed in from a pytest.fixture
        exclude_suffixes: A list of string suffixes to exclude. eg. [".txt",".png"]. Defaults to None.
        path_only: Do not read the file. Defaults to False.
        read_text: Read file as text. Defaults to True.

    Returns:
        A dict of file resources
    """
    if not resource_names:
        file_names = collect_resource_names(resource_path, include_suffixes)
    else:
        file_name = resource_names
    file_resources = {}
    for file_name in file_names:
        file_resource = load_file_resource(
            resource_path, file_name, logger, path_only, read_text
        )
        file_resources[file_name] = file_resource
    return file_resources


def load_file_resource(
    resource_path: str,
    resource_name: str,
    logger: logging.Logger,
    path_only: bool = False,
    read_text: bool = True,
) -> FileResource:
    """
    Load a file resource.

    Load a string or bytes as a FileResource. Can optionaly return only a path to a
    file, with None as data.

    Args:
        resource_path: package path to resource folder, eg. tests.resources.photos
        resource_name: file name of resource, eg. beach.jpeg
        logger: logger, usually passed in from a pytest.fixture
        path_only: Do not read the file. Defaults to False.
        read_text: Read file as text. Defaults to True.

    Raises:
        ex: [description]

    Returns:
        FileResource: [description]
    """
    try:
        with resources.path(resource_path, resource_name) as data_path:
            data: Optional[Union[str, bytes]] = None
            if read_text:
                if not path_only:
                    data = data_path.read_text()
                    logger.debug(
                        "Loaded resource file %s from %s", resource_name, resource_path
                    )
                return FileResource(file_path=data_path, data=data)
            else:
                if not path_only:
                    data = data_path.read_bytes()
                    logger.debug(
                        "Loaded resource file %s from %s", resource_name, resource_path
                    )
                return FileResource(file_path=data_path, data=data)
    # TODO refine the exception handling for files, and resource loading.
    except Exception as ex:
        logger.exception(
            "Unable to load resource file %s from %s Error msg %s",
            resource_name,
            resource_path,
            ex,
        )
        raise ex


def collect_resource_names(
    resource_path: str,
    include_suffixes: Optional[List[str]] = None,
) -> List[Path]:
    """
    Returns a list of file names in a resource directory, excluding the __init__.py

    [extended_summary]

    Args:
        resource_path: package path to resource folder, eg. tests.resources.photos
        include_suffixes: A list of string suffixes to include. eg. [".txt",".png"]. Defaults to None.

    Returns:
        A list of file names in a resource directory.
    """

    if include_suffixes is None:
        include_suffixes = []
    result = []
    with resources.path(resource_path, "__init__.py") as data_path:
        for file in (x for x in data_path.parent.glob("*.*") if x.is_file()):
            if file.name != "__init__.py":
                if not include_suffixes or file.suffix in include_suffixes:
                    result.append(file.name)
    return result


# def make_file_resource(resource_path, resource_name, logger) -> FileResource:
#     try:
#         with resources.path(resource_path, resource_name) as data_path:
#             data = data_path.read_text()
#             logger.debug(
#                 "Loaded resource file %s from %s", resource_name, resource_path
#             )
#             return FileResource(file_path=data_path, data=data)
#     except Exception as ex:
#         logger.exception(
#             "Unable to load resource file %s from %s Error msg %s",
#             resource_name,
#             resource_path,
#             ex,
#         )
#         raise ex


@pytest.fixture(autouse=True)
def env_setup(monkeypatch, test_app_data_dir):
    """environment variables set for each test."""
    monkeypatch.setenv(
        "{{ cookiecutter.namespace_slug }}{{ cookiecutter.project_slug }}_TESTING",
        "True",
    )
    monkeypatch.setenv(
        "{{ cookiecutter.namespace_slug }}{{ cookiecutter.project_slug }}_LOG_LEVEL",
        str(APP_LOG_LEVEL),
    )
    monkeypatch.setenv(
        "{{ cookiecutter.namespace_slug }}{{ cookiecutter.project_slug }}_APP_DIR",
        str(test_app_data_dir),
    )
