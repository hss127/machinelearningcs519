
The file for training/testing is trace.npy
Get the data for training and testing at the link below:
https://drive.google.com/drive/folders/1dBiQR1se8hd3CB2rbMoLEAWdiTmXVPZ7


For training CNN:
python train.py --range1 0 --range2 200 --byte_num BYTE0_CNN.h5 --label_byte 0 --epoch 150 --batch 100 --classifier CNN
python train.py --range1 270 --range2 400 --byte_num BYTE1_CNN.h5 --label_byte 1 --epoch 400 --batch 100 --classifier CNN
python train.py --range1 520 --range2 670 --byte_num BYTE2_CNN.h5 --label_byte 2 --epoch 400--batch 100 --classifier CNN
python train.py --range1 770 --range2 930 --byte_num BYTE3_CNN.h5 --label_byte 3 --epoch 400 --batch 100 --classifier CNN

For testing CNN:

python test.py --start 0 --finish 43500 --classifier CNN --byte_num BYTE0_CNN.h5 --range1 0 --range2 200 --label_byte 0
python test.py --start 0 --finish 43500 --classifier CNN --byte_num BYTE1_CNN.h5 --range1 270 --range2 400 --label_byte 1
python test.py --start 0 --finish 43500 --classifier CNN --byte_num BYTE2_CNN.h5 --range1 520 --range2 670 --label_byte 2
python test.py --start 0 --finish 43500 --classifier CNN --byte_num BYTE3_CNN.h5 --range1 770 --range2 930 --label_byte 3


For training MLP
python train.py --start 0 --finish 43500 --classifier MLP --byte_num BYTE0_MLP.h5  --label_byte 0 --range1 5 --range2 205
python train.py --start 0 --finish 43500 --classifier MLP --byte_num BYTE1_MLP.h5  --label_byte 1 --range1 255 --range2 455
python train.py --start 0 --finish 43500 --classifier MLP --byte_num BYTE2_MLP.h5  --label_byte 2 --range1 505 --range2 705
python train.py --start 0 --finish 43500 --classifier MLP --byte_num BYTE3_MLP.h5  --label_byte 3 --range1 755 --range2 955


for testing MLP:
python test.py --start 0 --finish 43500 --classifier MLP --byte_num BYTE0_MLP.h5  --label_byte 0 --range1 5 --range2 205
python test.py --start 0 --finish 43500 --classifier MLP --byte_num BYTE1_MLP.h5  --label_byte 1 --range1 255 --range2 455
python test.py --start 0 --finish 43500 --classifier MLP --byte_num BYTE2_MLP.h5  --label_byte 2 --range1 505 --range2 705
python test.py --start 0 --finish 43500 --classifier MLP --byte_num BYTE3_MLP.h5  --label_byte 3 --range1 755 --range2 955

