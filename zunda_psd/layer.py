from typing import List, Dict, Union

from psd_tools import PSDImage
from psd_tools.api.layers import Layer


def _layer_as_dict(layer: Layer) -> Dict[str, Union[Layer, Dict]]:
    if layer.is_group():
        return {layer.name: {layer.name: _layer_as_dict(child)} for child in layer}
    return {layer.name: layer}


# 同じ層で複数の選択肢を選んで組み合わせられるようにしたい
#
def layer_as_dict(psd: PSDImage) -> List[Dict[str, Layer]]:
    """
    TODO ちょっとちがう
    [{'尻尾的なアレ': PixelLayer('尻尾的なアレ' size=386x255)},
 {'パーカー裏地': PixelLayer('パーカー裏地' size=382x457 invisible)},
 {'*服装2': {'*服装2': {'!左腕': {'!左腕': {'*基本': PixelLayer('*基本' size=182x477)}}}}},
 {'*服装1': {'*服装1': {'!右腕': {'!右腕': {'*基本': PixelLayer('*基本' size=202x474)}}}}},
 {'!口': {'!口': {'*むー': PixelLayer('*むー' size=43x29 invisible)}}},
 {'!顔色': {'!顔色': {'*ほっぺ': PixelLayer('*ほっぺ' size=271x51)}}},
 {'!目': {'!目': {'*目セット': {'*目セット': {'!黒目': {'!黒目': {'*普通目': PixelLayer('*普通目' size=207x83)}}}}}}},
 {'!眉': {'!眉': {'*普通眉': PixelLayer('*普通眉' size=216x18 invisible)}}},
 {'!枝豆': {'!枝豆': {'*パーカー(裏地とセットで使用)': PixelLayer('*パーカー(裏地とセットで使用)' size=538x930 invisible)}}},
 {'記号など': {'記号など': {'アヒルちゃん': PixelLayer('アヒルちゃん' size=158x116 invisible)}}}]
"""
    return [_layer_as_dict(layer) for layer in psd]
