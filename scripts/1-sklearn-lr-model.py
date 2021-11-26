from models.sklearn_lr import SklearnLR
from shared.eval import test_model_implementation

class_params = {
            "n_samples": 10000,
            "n_features": 20,
            "n_classes": 2,
            "class_sep": 4,
            "random_state": 88
}

test_model_implementation(SklearnLR(), **class_params)

