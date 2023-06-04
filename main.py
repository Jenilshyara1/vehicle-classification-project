from vehicleclassifier import logger

from vehicleclassifier.pipeline.stage_01_prepare_base_model import PrepareBaseModelTrainingPipeline

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