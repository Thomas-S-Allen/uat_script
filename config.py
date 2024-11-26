
API_URL = "https://devapi.adsabs.harvard.edu/v1" # ADS API URL
API_TOKEN = ""

UAT_JSON_PATH = ''

# CLASSIFICATION_PRETRAINED_MODEL = "adsabs/ASTROBERT"
# CLASSIFICATION_PRETRAINED_MODEL_REVISION = "SciX-Categorizer"
# CLASSIFICATION_PRETRAINED_MODEL_TOKENIZER = "adsabs/ASTROBERT"
CLASSIFICATION_PRETRAINED_MODEL = "adsabs/nasa-smd-ibm-v0.1_UAT_Labeler"
CLASSIFICATION_PRETRAINED_MODEL_REVISION = None
CLASSIFICATION_PRETRAINED_MODEL_TOKENIZER = None

CLASSIFICATION_THRESHOLDS = [0.06, 0.03, 0.04, 0.02, 0.99, 0.02, 0.02, 0.99]
ADDITIONAL_EARTH_SCIENCE_PROCESSING = False
ADDITIONAL_EARTH_SCIENCE_PROCESSING_THRESHOLD = 0.015
