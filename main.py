from vehicleclassifier import logger
from vehicleclassifier.pipeline.stage_01_prepare_base_model import PrepareBaseModelTrainingPipeline
from vehicleclassifier.pipeline.stage_02_training import ModelTrainingPipeline
from vehicleclassifier.pipeline.stage_03_evaluation_pipeline import EvaluationPipeline
STAGE_NAME="prepare base model"

try:
    logger.info(f"****************")
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed<<<<<<")
except Exception as e:
    logger.exception(e)
    raise 


STAGE_NAME = "Training"

try:
    logger.info(f">>>>>>stage {STAGE_NAME} started <<<<<<<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)

STAGE_NAME = "Evaluation"

try:
    logger.info(f">>>>>>stage {STAGE_NAME} started <<<<<<<<<<<")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f">>>>>>stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)