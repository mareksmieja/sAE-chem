# sAE-chem (Pytorch)

Training mode (train.sh):

Set the following parameters:
1. dir_root - working directory
2. act_files - files containing pharmFPs of compounds acting on a sequence of targets
3. inact_files - as above but for inactive compounds (the order should be the same as above)

The script reads the above files located in dir_root. As the output, it saves trained models in ${dir_root}/save directory.

Testing mode (test.sh):

Once the models are created, they can be used to classify compounds into actives and inactives.

Set the following parameters:
1. dir_root - working directory
2. model_files - sequence of names indicating trained models
3. act_file - file with test data

The script outputs n files, where n is the number of models, in a directory ${dir_root}/save. The i-th row of j-th files indicates whether i-th compound from test file is active on j-th target.
