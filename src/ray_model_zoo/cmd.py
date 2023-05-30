import argparse

from models import models, model_params


def list_model(args):
    """列出model信息"""
    var_models = ()
    if args.models:
        var_models = set(args.models.upper().split(','))
    if args.all_models:
        var_models = models

    for m in var_models:
        print(f"{m}")
        if args.param:
            print(f"\t{model_params(args.param)}")


"""
  zoo [model|serve] [list|get|pull|delete] [OPTIONS] 
"""
parser = argparse.ArgumentParser(description="Ray model zoo manipulate tools.")
model_parser = parser.add_subparsers(title='model tools',
                                     description='models\' manipulate tools',
                                     dest='model')
list_parser = model_parser.add_parser('list', help='list model(s) with supported param choice')

list_parser.add_argument('--all', default=True, dest='all_models', action='store_true', help='list all model names')
list_parser.add_argument('models', type=str, help='models\' name list')
list_parser.add_argument('--param', dest='param', help='param type choice')
list_parser.set_defaults(func=list_model)

args = parser.parse_args()
args.func(args)
