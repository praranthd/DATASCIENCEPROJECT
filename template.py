import logging
import os
from pathlib import Path
from logging.handlers import RotatingFileHandler

PROJECT_NAME = "src"

# --------------------------------------------------
# 1. Configure logging
# --------------------------------------------------

log_dir = Path("logs")
log_dir.mkdir(parents=True, exist_ok=True)

logger = logging.getLogger("student_performance_project")
logger.setLevel(logging.INFO)
logger.propagate = False

if not logger.handlers:
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | "
        "%(name)s | %(message)s"
    )

    # Display logs in terminal
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Save logs in a rotating file
    file_handler = RotatingFileHandler(
        log_dir / "project.log",
        maxBytes=5 * 1024 * 1024,
        backupCount=3,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)


# --------------------------------------------------
# 2. Define project files
# --------------------------------------------------

list_of_files = [
    f"{PROJECT_NAME}/__init__.py",

    # ML components
    f"{PROJECT_NAME}/components/__init__.py",
    f"{PROJECT_NAME}/components/data_ingestion.py",
    f"{PROJECT_NAME}/components/data_validation.py",
    f"{PROJECT_NAME}/components/data_transformation.py",
    f"{PROJECT_NAME}/components/model_trainer.py",
    f"{PROJECT_NAME}/components/model_evaluation.py",

    # Configuration
    f"{PROJECT_NAME}/configuration/__init__.py",

    # Data access
    f"{PROJECT_NAME}/data_access/__init__.py",
    f"{PROJECT_NAME}/data_access/student_performance_data.py",

    # Cloud storage
    f"{PROJECT_NAME}/cloud_storage/__init__.py",
    f"{PROJECT_NAME}/cloud_storage/aws_storage.py",

    # Entities
    f"{PROJECT_NAME}/entity/__init__.py",
    f"{PROJECT_NAME}/entity/config_entity.py",
    f"{PROJECT_NAME}/entity/artifact_entity.py",

    # Constants
    f"{PROJECT_NAME}/constants/__init__.py",

    # Logging and utilities
    f"{PROJECT_NAME}/utils/__init__.py",
    f"{PROJECT_NAME}/utils/logger.py",
    f"{PROJECT_NAME}/utils/main_utils.py",

    # Pipelines
    f"{PROJECT_NAME}/pipeline/__init__.py",
    f"{PROJECT_NAME}/pipeline/training_pipeline.py",
    f"{PROJECT_NAME}/pipeline/prediction_pipeline.py",

    # API
    f"{PROJECT_NAME}/api/__init__.py",
    f"{PROJECT_NAME}/api/main.py",
    "app.py",

    # Configuration files
    "config/model.yaml",
    "config/schema.yaml",

    # Tests
    "tests/__init__.py",
    "tests/test_data_ingestion.py",
    "tests/test_model.py",
    "tests/test_api.py",

    # Root files
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    ".gitignore",
    "README.md",
    "pyproject.toml",
    "dvc.yaml",
    "params.yaml",
]

list_of_directories = [
    "data/raw",
    "data/interim",
    "data/processed",
    "artifacts/models",
    "artifacts/metrics",
    "logs",
    "notebooks",
]


# --------------------------------------------------
# 3. Create directories
# --------------------------------------------------

try:
    logger.info("Starting project structure creation")

    for directory in list_of_directories:
        directory_path = Path(directory)

        if not directory_path.exists():
            directory_path.mkdir(parents=True, exist_ok=True)
            logger.info("Created directory: %s", directory_path)
        else:
            logger.info("Directory already exists: %s", directory_path)

    # --------------------------------------------------
    # 4. Create files
    # --------------------------------------------------

    for filepath in list_of_files:
        filepath = Path(filepath)

        # Create parent directories when necessary
        filepath.parent.mkdir(parents=True, exist_ok=True)

        if not filepath.exists():
            filepath.touch()
            logger.info("Created file: %s", filepath)

        elif filepath.stat().st_size == 0:
            logger.warning("File exists but is empty: %s", filepath)

        else:
            logger.info("File already contains data: %s", filepath)

    logger.info("Project structure creation completed successfully")

except OSError:
    logger.exception("Failed to create project structure")
    raise

except Exception:
    logger.exception("Unexpected error during project setup")
    raise
