import mediapipe as mp
from mediapipe.model_maker import ModelMaker
from mediapipe.model_maker import DataLoader

# Step 1: Load your dataset
data = DataLoader.from_folder('./tic_tac_toe_api/app/src/frontend/src/ui/train')

# Step 2: Create a ModelMaker instance
model_maker = ModelMaker(data)

# Step 3: Train the model
model_maker.train()

# Step 4: Evaluate the model
model_maker.evaluate()

# Step 5: Export the model
model_maker.export('./tic_tac_toe_api/app/src/frontend/src/ui/CustomModel')