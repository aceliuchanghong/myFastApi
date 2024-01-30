from tree_utils.struct_tree_out import print_tree

exclude_dirs_set = {'__init__.py', 'backend', 'test', 'frontend', 'pages', 'main_sit.py', 'prompt2.md', 'prompt.md'}
exclude_dirs_set2 = {'__init__.py', 'test'}

print_tree('../../myFastApi', exclude_dirs=exclude_dirs_set)
