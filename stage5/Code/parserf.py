import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--classifier', type=str, help='Classifier name')
#parser.add_argument('--dataset', type=str, help='dataset name')
#parser.add_argument('--sci', type=str, help='Whether dataset is in Scikit or not')
parser.add_argument('--range1', type=int, help='range1')
parser.add_argument('--range2', type=int, help='range2')
parser.add_argument('--label_byte', type=int, help='what label to train')
# parser.add_argument('--byte_h', type=int, help='byte_1')
# parser.add_argument('--byte_l', type=int, help='byte_0')
parser.add_argument('--epoch', type=int, help='epoch number')
parser.add_argument('--byte_num', type=str, help='byte num save')
#parser.add_argument('--eps', type=float, help='epsilon')
parser.add_argument('--batch', type=int, help='batch size')
#parser.add_argument('--cri', type=str, help='Criterion')
#parser.add_argument('--D', type=int, help='Max Depth')
#parser.add_argument('--dim', type=str, help='PCA,LDA,K-PCA')
#parser.add_argument('--dimn', type=int, help='PCA dimensions')
#parser.add_argument('--n', type=int, help='neighbors')
#parser.add_argument('--e', type=float, help='Etha')

parser.add_argument('--start', type=int, help='start test')
parser.add_argument('--finish', type=int, help='finish test')



args = parser.parse_args()

start=args.start
finish=args.finish
range1=args.range1
range2=args.range2
label_byte=args.label_byte
# byte_l=args.byte_l
# byte_h=args.byte_h
batch_num=args.batch
byte_num=args.byte_num
classifier=args.classifier
epoch_num=args.epoch
#existing_dataset=args.sci
#n_est=args.est
#jobs=args.j
#knum=args.knum
#cluster=args.cluster
#cri=args.cri
#TD=args.D
#dimension_reduction_strategy=args.dim
#dim_num=args.dimn
##et=args.e
#kernel_kpca=args.kernel
