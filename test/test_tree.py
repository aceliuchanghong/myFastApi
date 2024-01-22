from tree_utils.struct_tree_out import print_tree

exclude_dirs_set = {'__init__.py', 'test', 'app', 'frontend', 'pages'}
print_tree('../../myFastApi', exclude_dirs=exclude_dirs_set)
