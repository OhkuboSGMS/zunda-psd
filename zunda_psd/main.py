from typing import List, Dict, Union, Optional, Iterator
from psd_tools import PSDImage
from psd_tools.api.layers import Layer
from PIL import Image


def _get_parent_layer_name(layer: Union[Layer, PSDImage]) -> Optional[str]:
    """
    引数のレイヤの親のレイヤを取得．最親はPSDImageが返却されるので，
    PSDImageの場合はNoneを返却
    :param layer:
    :return:
    """
    return layer.parent if not isinstance(layer.parent, PSDImage) else None


def parent_layer_iterator(layer: Layer) -> Iterator[Layer]:
    """
    渡した引数を含む，親のレイヤを順に返却する
    :param layer:
    :return:
    """
    while layer:
        yield layer
        layer = _get_parent_layer_name(layer)


def get_layer_path(layer: Layer) -> str:
    return '/'.join(map(lambda l: l.name, reversed(list(parent_layer_iterator(layer)))))


def layer_path_dict(psd: PSDImage) -> Dict[str, Layer]:
    return {get_layer_path(layer): layer for layer in psd.descendants()}


def psd_to_image(enable_layers: List[str], psd: PSDImage) -> Image:
    """
    指定されたレイヤ(enable_layers)をvisibleにして画像を生成.
    :param enable_layers:
    :param psd:
    :return: Image
    """
    path_dict = layer_path_dict(psd)

    for layer in psd.descendants():
        if layer.is_group():
            layer.visible = True
        else:
            layer.visible = False

    for path in enable_layers:
        if path in path_dict:
            path_dict[path].visible = True
        else:
            print(f'warning not found :{path}')
    print('~~~~~')
    for l in psd.descendants():
        print(get_layer_path(l))
    # forceによって反映される
    return psd.composite(force=True)


if __name__ == '__main__':
    """
    指定されたPixelLayerのみをOnにする
    それ以外はOff
    GroupLayerはOnにする
    指定事項から
    """
    psd = PSDImage.open('ずんだもん立ち絵素材2.3/ずんだもん立ち絵素材2.3.psd')
    # layer set
    layers = [
        '!枝豆/*枝豆萎え',
        '!眉/*困り眉1',
        '!目/*目セット/!黒目/*普通目',
        '!目/*目セット/*普通白目',
        '*服装1/*いつもの服',
        '*服装1/!右腕/*基本',
        '*服装1/!左腕/*基本',
        '!口/*むー',
        '尻尾的なアレ'

    ]
    image = psd_to_image(layers, psd)
    # image.show()
    image.save('1.png')
