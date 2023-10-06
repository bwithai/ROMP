In order to run this package locally https://github.com/facebookresearch/pytorch3d/blob/main/docs/tutorials/render_densepose.ipynb


```bash
pip install torch==2.0.1
```

Now run this code in main.py
```python
import os
import sys
import torch
import subprocess

need_pytorch3d = False
try:
    import pytorch3d
except ModuleNotFoundError:
    need_pytorch3d = True

if need_pytorch3d:
    if torch.__version__.startswith(("1.13.", "2.0.")) and sys.platform.startswith("linux"):
        # We try to install PyTorch3D via a released wheel.
        pyt_version_str = torch.__version__.split("+")[0].replace(".", "")
        version_str = "".join([
            f"py3{sys.version_info.minor}_cu",
            torch.version.cuda.replace(".", ""),
            f"_pyt{pyt_version_str}"
        ])
        subprocess.run(['pip', 'install', 'fvcore', 'iopath'])
        subprocess.run(['pip', 'install', '--no-index', '--no-cache-dir', 'pytorch3d', '-f',
                        f'https://dl.fbaipublicfiles.com/pytorch3d/packaging/wheels/{version_str}/download.html'])
    else:
        # We try to install PyTorch3D from source.
        subprocess.run(['pip', 'install', 'git+https://github.com/facebookresearch/pytorch3d.git@stable'])

```

```bash
pip install chumpy==0.70
pip install matplotlib==3.8.0
pip install scipy==1.11.3
```

