import click

from zoo.model import models

"""
click 库：https://click.palletsprojects.com/en/8.1.x/quickstart/#screencast-and-examples
"""


@click.group()
def cli():
    pass


@click.command(name='list')
@click.argument('model_names', nargs=-1)  # 接受多个位置参数
@click.option('-t', '--model-type', default=False, is_flag=True, show_default=True,
              help="list all model parameter choices")
def list_model(model_names, model_type):
    """列出model信息"""
    var_models = {}
    if model_names is None or len(model_names) == 0:
        var_models = models
    else:
        for m in set(model_names):
            var_models[m] = models[m] if m in models else {}

    print("🍺 supported models:")
    for m, param_choices in var_models.items():
        print(f"📦 {m}")
        if model_type:
            for k, _ in param_choices.items():
                print(f"\t- {k}")


"""
  zoo [model|serve] [list|get|pull|delete] [OPTIONS] 
"""
if __name__ == '__main__':
    cli.add_command(list_model)
    cli()
