"""
conda create -n zunda-psd pyton=3.8 -y
pip install psd-tools

"""
from pathlib import Path
from typing import Any, Dict

from psd_tools import PSDImage

psd = PSDImage.open('ずんだもん立ち絵素材2.3/ずんだもん立ち絵素材2.3.psd')
print(psd)
p_dir = Path('zundamon')
p_dir.mkdir(parents=True, exist_ok=True)
psd.save(str(p_dir.joinpath('all.png')))

def parse_ad_dict(psd:PSDImage)->Dict[str,Any]:
    pass
for layer in psd:
    print(layer)
    if layer.is_group():
        for child in layer:
            if child.kind == 'pixel':
                print(' ' + str(child))
                print(f' bbox:{child.bbox}')
                child.topil().save(str(p_dir.joinpath(f'{child.name}.png')))
