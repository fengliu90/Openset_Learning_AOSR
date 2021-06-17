import numpy as np

splits_2020 = {
    'mnist': [
        [2, 4, 5, 9, 8, 3],
        [3, 2, 6, 9, 4, 0],
        [5, 8, 3, 2, 4, 6],
        [3, 7, 8, 4, 0, 5],
        [6, 3, 4, 9, 8, 2]
    ],
    'svhn': [
        [5, 3, 7, 2, 8, 6],
        [3, 8, 7, 6, 2, 5],
        [8, 9, 4, 7, 2, 1],
        [3, 8, 2, 5, 0, 6],
        [4, 9, 2, 7, 1, 0]
    ],
    'cifar10': [
        [0, 6, 4, 9, 1, 7],
        [7, 6, 4, 9, 0, 1],
        [1, 5, 7, 3, 9, 4],
        [8, 6, 1, 9, 0, 7],
        [2, 4, 1, 7, 9, 6]
    ],
    'cifar100': [
        [4, 7, 9, 1],
        [6, 7, 1, 9],
        [9, 6, 1, 7],
        [6, 4, 9, 1],
        [1, 0, 9, 8]
    ],
    'cifar100-10': [
        [30, 25, 1, 9, 8, 0, 46, 52, 49, 71],
        [41, 9, 49, 40, 73, 60, 48, 30, 95, 71],
        [8, 9, 49, 40, 73, 60, 48, 95, 30, 71],
        [95, 60, 30, 73, 46, 49, 68, 99, 8, 71],
        [33, 2, 3, 97, 46, 21, 64, 63, 88, 43]
    ],
    'cifar100-50': [
        [27, 94, 29, 77, 88, 26, 69, 48, 75, 5, 59, 93, 39, 57, 45, 40, 78, 20, 98, 47, 66, 70, 91, 76, 41, 83, 99, 32, 53, 72, 2, 95, 21, 73, 84, 68, 35, 11, 55, 60, 30, 25, 1, 9, 8, 0, 46, 52, 49, 71],
        [65, 97, 86, 24, 45, 67, 2, 3, 91, 98, 79, 29, 62, 82, 33, 76, 0, 35, 5, 16, 54, 11, 99, 52, 85, 1, 25, 66, 28, 84, 23, 56, 75, 46, 21, 72, 55, 68, 8, 69, 41, 9, 49, 40, 73, 60, 48, 30, 95, 71],
        [20, 83, 65, 97, 94, 2, 93, 16, 67, 29, 62, 33, 24, 98, 5, 86, 35, 54, 0, 91, 52, 66, 85, 84, 56, 11, 1, 76, 25, 55, 21, 99, 72, 41, 23, 75, 28, 68, 69, 46, 8, 9, 49, 40, 73, 60, 48, 95, 30, 71],
        [92, 82, 77, 64, 5, 33, 62, 56, 70, 0, 20, 28, 67, 14, 84, 53, 91, 29, 85, 2, 52, 83, 75, 35, 11, 21, 72, 98, 55, 1, 41, 76, 25, 66, 69, 9, 48, 54, 40, 23, 95, 60, 30, 73, 46, 49, 68, 99, 8, 71],
        [47, 6, 19, 0, 62, 93, 59, 65, 54, 70, 34, 55, 23, 38, 72, 76, 53, 31, 78, 96, 77, 27, 92, 18, 82, 50, 98, 32, 1, 75, 83, 4, 51, 35, 80, 11, 74, 66, 36, 42, 33, 2, 3, 97, 46, 21, 64, 63, 88, 43]
    ],
    'tiny_imagenet': [
        [108, 147, 17, 58, 193, 123, 72, 144, 75, 167, 134, 14, 81, 171, 44, 197, 152, 66, 1, 133],
        [198, 161, 91, 59, 57, 134, 61, 184, 90, 35, 29, 23, 199, 38, 133, 19, 186, 18, 85, 67],
        [177, 0, 119, 26, 78, 80, 191, 46, 134, 92, 31, 152, 27, 60, 114, 50, 51, 133, 162, 93],
        [98, 36, 158, 177, 189, 157, 170, 191, 82, 196, 138, 166, 43, 13, 152, 11, 75, 174, 193, 190],
        [95, 6, 145, 153, 0, 143, 31, 23, 189, 81, 20, 21, 89, 26, 36, 170, 102, 177, 108, 169]
    ]
}

def split_know_unkn_mnist_svhn_cifar10(trX,
                                       trY,
                                       teX,
                                       teY,
                                       num_shuffle=5,
                                       know_class_list=None,
                                       unkn_class_list=None,
                                       r_seed=0):
    np.random.seed(r_seed)

    know_trX_list = []
    know_trY_list = []
    know_teX_list = []
    know_teY_list = []
    unkn_teX_list = []
    unkn_teY_list = []

    if know_class_list is None:
        know_class_list = []
        unkn_class_list = []
        for i in range(num_shuffle):
            permut_label = np.random.permutation(10)
            know_class_list.append(permut_label[:6])
            unkn_class_list.append(permut_label[6:])

    print(f'numpy random seed {r_seed}')

    for i in range(num_shuffle):

        know_trX_list_temp = []
        know_trY_list_temp = []
        know_teX_list_temp = []
        know_teY_list_temp = []
        unkn_teX_list_temp = []
        unkn_teY_list_temp = []

        print(f'Ranodm set {i}')
        print(f'    know classes {know_class_list[i]}')
        print(f'    unkn classes {unkn_class_list[i]}')

        for c_label in know_class_list[i]:

            trID = np.where(trY == c_label)
            teID = np.where(teY == c_label)
            trX_new = trX[trID]
            trY_new = trY[trID]
            teX_new = teX[teID]
            teY_new = teY[teID]
            know_trX_list_temp.append(trX_new)
            know_trY_list_temp.append(trY_new)
            know_teX_list_temp.append(teX_new)
            know_teY_list_temp.append(teY_new)

        for c_label in unkn_class_list[i]:
            teID = np.where(teY == c_label)
            teX_new = teX[teID]
            teY_new = teY[teID]
            unkn_teX_list_temp.append(teX_new)
            unkn_teY_list_temp.append(teY_new)

        know_trX_list.append(np.concatenate(know_trX_list_temp, axis=0))
        know_trY_list.append(np.concatenate(know_trY_list_temp, axis=0))
        know_teX_list.append(np.concatenate(know_teX_list_temp, axis=0))
        know_teY_list.append(np.concatenate(know_teY_list_temp, axis=0))
        unkn_teX_list.append(np.concatenate(unkn_teX_list_temp, axis=0))
        unkn_teY_list.append(np.concatenate(unkn_teY_list_temp, axis=0))

    dataset_X_dict = {
        'kn_tr': know_trX_list,
        'kn_te': know_teX_list,
        'uk_te': unkn_teX_list
    }
    dataset_Y_dict = {
        'kn_tr': know_trY_list,
        'kn_te': know_teY_list,
        'uk_te': unkn_teY_list
    }

    return dataset_X_dict, dataset_Y_dict