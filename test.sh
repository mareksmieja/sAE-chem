#!/usr/bin/env bash

dir_root=/mnt/users/smieja/local/train

model_files=(D2_Ki Delta_Ki Kappa_Ki Mi_Ki D2_EC50 Delta_EC50 Kappa_EC50 Mi_EC50)

act_file=${dir_root}/skrining_data

echo ${act_file}

for (( i = 0; i < ${#model_files[@]}; ++i )); do
    ae_files[i]=${dir_root}/save/ae_model-${model_files[i]}.pth
    cl_files[i]=${dir_root}/save/classifier_model-${model_files[i]}.pth
	nice -9 python supervised_ae.py --data_act ${act_file} --pretrain_epochs 75 --epochs 100 --dims_layers_ae 7000 4000 500 1000 100 --dims_layers_classifier 100 --batch_size 50 --lr 0.0001 --dir_save ${dir_root}/save --use_dropout --procedure pre-training_ae training_all --scale_loss 1 --ae ${ae_files[i]} --classifier ${cl_files[i]} --test
done



