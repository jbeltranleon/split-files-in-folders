train_ATELECTASIS = !find ../input/xrays-chest-224-small-aug-less-values-selected/input_224_small_aug_less_values_selected/224_small_aug_less_values_selected/train/atelectasis/ -type f  -exec file {} \+ | grep -c -i 'image'
train_EFFUSION = !find ../input/xrays-chest-224-small-aug-less-values-selected/input_224_small_aug_less_values_selected/224_small_aug_less_values_selected/train/effusion/ -type f  -exec file {} \+ | grep -c -i 'image'
train_INFILTRATION = !find ../input/xrays-chest-224-small-aug-less-values-selected/input_224_small_aug_less_values_selected/224_small_aug_less_values_selected/train/infiltration/ -type f  -exec file {} \+ | grep -c -i 'image'
train_NO_FINDING = !find ../input/xrays-chest-224-small-aug-less-values-selected/input_224_small_aug_less_values_selected/224_small_aug_less_values_selected/train/no_finding/ -type f  -exec file {} \+ | grep -c -i 'image'

val_ATELECTASIS = !find ../input/xrays-chest-224-small-aug-less-values-selected/input_224_small_aug_less_values_selected/224_small_aug_less_values_selected/val/atelectasis/ -type f  -exec file {} \+ | grep -c -i 'image'
val_EFFUSION = !find ../input/xrays-chest-224-small-aug-less-values-selected/input_224_small_aug_less_values_selected/224_small_aug_less_values_selected/val/effusion/ -type f  -exec file {} \+ | grep -c -i 'image'
val_INFILTRATION = !find ../input/xrays-chest-224-small-aug-less-values-selected/input_224_small_aug_less_values_selected/224_small_aug_less_values_selected/val/infiltration/ -type f  -exec file {} \+ | grep -c -i 'image'
val_NO_FINDING = !find ../input/xrays-chest-224-small-aug-less-values-selected/input_224_small_aug_less_values_selected/224_small_aug_less_values_selected/val/no_finding/ -type f  -exec file {} \+ | grep -c -i 'image'

test_ATELECTASIS = !find ../input/xrays-chest-224-small-aug-less-values-selected/input_224_small_aug_less_values_selected/224_small_aug_less_values_selected/test/atelectasis/ -type f  -exec file {} \+ | grep -c -i 'image'
test_EFFUSION = !find ../input/xrays-chest-224-small-aug-less-values-selected/input_224_small_aug_less_values_selected/224_small_aug_less_values_selected/test/effusion/ -type f  -exec file {} \+ | grep -c -i 'image'
test_INFILTRATION = !find ../input/xrays-chest-224-small-aug-less-values-selected/input_224_small_aug_less_values_selected/224_small_aug_less_values_selected/test/infiltration/ -type f  -exec file {} \+ | grep -c -i 'image'
test_NO_FINDING = !find ../input/xrays-chest-224-small-aug-less-values-selected/input_224_small_aug_less_values_selected/224_small_aug_less_values_selected/test/no_finding/ -type f  -exec file {} \+ | grep -c -i 'image'

output_classes = 4
learning_rate = 0.0001
img_width, img_height,channel = 224, 224, 3
training_examples = train_total 
batch_size = 20 
epochs = 5
resume_model = False
training_data_dir = '../input/xrays-chest-224-small-aug-less-values-selected/input_224_small_aug_less_values_selected/224_small_aug_less_values_selected/train'
val_data_dir = '../input/xrays-chest-224-small-aug-less-values-selected/input_224_small_aug_less_values_selected/224_small_aug_less_values_selected/val'
test_data_dir = '../input/xrays-chest-224-small-aug-less-values-selected/input_224_small_aug_less_values_selected/224_small_aug_less_values_selected/test'
trained_model_dir = '../input/inceptionv3/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5'