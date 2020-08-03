#!/usr/bin/env bash

dir_root=/mnt/users/smieja/local/train

act_files=(D2_Ki_actives_onbits Delta_Ki_actives_onbits Kappa_Ki_actives_onbits Mi_Ki_actives_onbits D2_EC50_actives_onbits Delta_EC50_actives_onbits Kappa_EC50_actives_onbits Mi_EC50_actives_onbits)
inact_files=(D2_Ki_inactives_onbits Delta_Ki_inactives_onbits Kappa_Ki_inactives_onbits Mi_Ki_inactives_onbits D2_EC50_inactives_onbits Delta_EC50_inactives_onbits Kappa_EC50_inactives_onbits Mi_EC50_inactives_onbits)

for (( i = 0; i < ${#act_files[@]}; ++i )); do
    act_files[i]=${dir_root}/${act_files[i]}
    inact_files[i]=${dir_root}/${inact_files[i]}
	nice -9 python supervised_ae.py --data_act ${act_files[i]} --data_in ${inact_files[i]} --pretrain_epochs 75 --epochs 100 --dims_layers_ae 7000 4000 500 1000 100 --dims_layers_classifier 100 --batch_size 50 --lr 0.0001 --dir_save ${dir_root}/save --use_dropout --procedure pre-training_ae training_all --scale_loss 1
done



