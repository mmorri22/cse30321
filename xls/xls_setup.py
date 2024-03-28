#@title First Run Only #1 - Allocate Memory - (You will lose previous work if you run again) {run:"auto"}

!rm -rf *

#@title First Run Only #2 - Python Library Imports to support XLS and OpenLane {run:"auto"}

import os
import pathlib
import sys
import jinja2
import IPython.display
import PIL.Image
import graphviz
import pathlib

from IPython.display import display, display_png

#@title  First Run Only #3 - XLS Environment Setup {run:"auto"}

xls_version = 'v0.0.0-4699-gfb023174' #@param {type:"string"}

!echo '📦 downloading xls-{xls_version}'
!curl --show-error -L https://github.com/proppy/xls/releases/download/{xls_version}/xls-{xls_version}-linux-x64.tar.gz | tar xzf - --strip-components=1
!echo '🧪 setting up colab integration'
!python -m pip install --quiet --no-cache-dir --ignore-installed https://github.com/proppy/xls/releases/download/{xls_version}/xls_colab-0.0.0-py3-none-any.whl
!python -m pip install logger
!python -m pip install colabtools
import logger
import xls.contrib.colab
_ = xls.contrib.colab.register_dslx_magic()

# Must verify xls_work_dir is created
!if test -d xls_work_dir; then echo "xls_work_dir exists"; else mkdir xls_work_dir;  fi

#@title  First Run Only #4 - OpenRoad Setup {run:"auto"}

yosys_version = '0.38_93_g84116c9a3' #@param {type:"string"}
openroad_version = '2.0_12381_g01bba3695' #@param {type:"string"}
rules_hdl_version = '2eb050e80a5c42ac3ffdb7e70392d86a6896dfc7' #@param {type:"string"}

!echo '🛣️ installing openroad and friends'
!curl -L -O https://repo.anaconda.com/miniconda/Miniconda3-py310_24.1.2-0-Linux-x86_64.sh
!bash Miniconda3-py310_24.1.2-0-Linux-x86_64.sh -b -p conda-env/
import pathlib
conda_prefix_path = pathlib.Path('conda-env')
CONDA_PREFIX = str(conda_prefix_path.resolve())
%env CONDA_PREFIX={CONDA_PREFIX}
!conda-env/bin/conda install -yq -c "litex-hub" openroad={openroad_version} yosys={yosys_version}


#@title  First Run Only #5 - Organizing Access to PDKs {run:"auto"}

!gsutil cp gs://proppy-eda/pdk_info_asap7.zip .
!gsutil cp gs://proppy-eda/pdk_info_sky130.zip .

!unzip -q -o pdk_info_asap7.zip
!unzip -q -o pdk_info_sky130.zip

!echo '🧰 generating PDK metadata'
!curl --show-error -L  https://github.com/hdl/bazel_rules_hdl/archive/{rules_hdl_version}.tar.gz | tar xzf - --strip-components=1
!curl -L -O https://github.com/protocolbuffers/protobuf/releases/download/v24.3/protoc-24.3-linux-x86_64.zip
!unzip -q -o protoc-24.3-linux-x86_64.zip
!{sys.executable} -m pip install protobuf

#@title  First Run Only #6 - ASAP7 PDK Organization Setup{run:"auto"}

!mkdir -p org_theopenroadproject_asap7sc7p5t_28/{LEF,techlef_misc} asap7/dependency_support/org_theopenroadproject_asap7_pdk_r1p7/
!cp asap7/asap7sc7p5t_28_R_1x_220121a.lef org_theopenroadproject_asap7sc7p5t_28/LEF/
!cp asap7/asap7_tech_1x_201209.lef org_theopenroadproject_asap7sc7p5t_28/techlef_misc/
!cp asap7/asap7_rvt_1x_SS.lib org_theopenroadproject_asap7sc7p5t_28/
!cp asap7/tracks.tcl asap7/dependency_support/org_theopenroadproject_asap7_pdk_r1p7/
!cp asap7/pdn_config.pdn asap7/dependency_support/org_theopenroadproject_asap7_pdk_r1p7/
!cp asap7/rc_script.tcl asap7/dependency_support/org_theopenroadproject_asap7_pdk_r1p7/
!bin/protoc --python_out=. pdk/proto/pdk_info.proto


#@title sky130 PDK Organization Setup - Part 1 {run:"auto"}
!mkdir -p com_google_skywater_pdk_sky130_fd_sc_hd/
!mkdir -p com_google_skywater_pdk_sky130_fd_sc_hd/cells
!mkdir -p com_google_skywater_pdk_sky130_fd_sc_hd/tech
!mkdir -p com_google_skywater_pdk_sky130_fd_sc_hd/timing

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/a2111o
!cp sky130/sky130_fd_sc_hd__a2111o_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a2111o/sky130_fd_sc_hd__a2111o_1.lef
!cp sky130/sky130_fd_sc_hd__a2111o_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a2111o/sky130_fd_sc_hd__a2111o_2.lef
!cp sky130/sky130_fd_sc_hd__a2111o_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a2111o/sky130_fd_sc_hd__a2111o_4.lef
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/a2111oi
!cp sky130/sky130_fd_sc_hd__a2111oi_0.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a2111oi/sky130_fd_sc_hd__a2111oi_0.lef
!cp sky130/sky130_fd_sc_hd__a2111oi_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a2111oi/sky130_fd_sc_hd__a2111oi_1.lef
!cp sky130/sky130_fd_sc_hd__a2111oi_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a2111oi/sky130_fd_sc_hd__a2111oi_2.lef
!cp sky130/sky130_fd_sc_hd__a2111oi_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a2111oi/sky130_fd_sc_hd__a2111oi_4.lef
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/a211o
!cp sky130/sky130_fd_sc_hd__a211o_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a211o/sky130_fd_sc_hd__a211o_1.lef
!cp sky130/sky130_fd_sc_hd__a211o_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a211o/sky130_fd_sc_hd__a211o_2.lef
!cp sky130/sky130_fd_sc_hd__a211o_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a211o/sky130_fd_sc_hd__a211o_4.lef
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/a211oi
!cp sky130/sky130_fd_sc_hd__a211oi_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a211oi/sky130_fd_sc_hd__a211oi_1.lef
!cp sky130/sky130_fd_sc_hd__a211oi_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a211oi/sky130_fd_sc_hd__a211oi_2.lef
!cp sky130/sky130_fd_sc_hd__a211oi_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a211oi/sky130_fd_sc_hd__a211oi_4.lef
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/a21bo
!cp sky130/sky130_fd_sc_hd__a21bo_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a21bo/sky130_fd_sc_hd__a21bo_1.lef
!cp sky130/sky130_fd_sc_hd__a21bo_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a21bo/sky130_fd_sc_hd__a21bo_2.lef
!cp sky130/sky130_fd_sc_hd__a21bo_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a21bo/sky130_fd_sc_hd__a21bo_4.lef
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/a21boi
!cp sky130/sky130_fd_sc_hd__a21boi_0.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a21boi/sky130_fd_sc_hd__a21boi_0.lef
!cp sky130/sky130_fd_sc_hd__a21boi_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a21boi/sky130_fd_sc_hd__a21boi_1.lef
!cp sky130/sky130_fd_sc_hd__a21boi_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a21boi/sky130_fd_sc_hd__a21boi_2.lef
!cp sky130/sky130_fd_sc_hd__a21boi_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a21boi/sky130_fd_sc_hd__a21boi_4.lef
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/a21o
!cp sky130/sky130_fd_sc_hd__a21o_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a21o/sky130_fd_sc_hd__a21o_1.lef
!cp sky130/sky130_fd_sc_hd__a21o_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a21o/sky130_fd_sc_hd__a21o_2.lef
!cp sky130/sky130_fd_sc_hd__a21o_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a21o/sky130_fd_sc_hd__a21o_4.lef
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/a21oi
!cp sky130/sky130_fd_sc_hd__a21oi_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a21oi/sky130_fd_sc_hd__a21oi_1.lef
!cp sky130/sky130_fd_sc_hd__a21oi_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a21oi/sky130_fd_sc_hd__a21oi_2.lef
!cp sky130/sky130_fd_sc_hd__a21oi_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a21oi/sky130_fd_sc_hd__a21oi_4.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/a221o
!cp sky130/sky130_fd_sc_hd__a221o_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a221o/sky130_fd_sc_hd__a221o_1.lef
!cp sky130/sky130_fd_sc_hd__a221o_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a221o/sky130_fd_sc_hd__a221o_2.lef
!cp sky130/sky130_fd_sc_hd__a221o_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a221o/sky130_fd_sc_hd__a221o_4.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/a221oi
!cp sky130/sky130_fd_sc_hd__a221oi_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a221oi/sky130_fd_sc_hd__a221oi_1.lef
!cp sky130/sky130_fd_sc_hd__a221oi_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a221oi/sky130_fd_sc_hd__a221oi_2.lef
!cp sky130/sky130_fd_sc_hd__a221oi_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a221oi/sky130_fd_sc_hd__a221oi_4.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/a222oi
!cp sky130/sky130_fd_sc_hd__a222oi_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a222oi/sky130_fd_sc_hd__a222oi_1.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/a22o
!cp sky130/sky130_fd_sc_hd__a22o_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a22o/sky130_fd_sc_hd__a22o_1.lef
!cp sky130/sky130_fd_sc_hd__a22o_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a22o/sky130_fd_sc_hd__a22o_2.lef
!cp sky130/sky130_fd_sc_hd__a22o_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a22o/sky130_fd_sc_hd__a22o_4.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/a22oi
!cp sky130/sky130_fd_sc_hd__a22oi_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a22oi/sky130_fd_sc_hd__a22oi_1.lef
!cp sky130/sky130_fd_sc_hd__a22oi_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a22oi/sky130_fd_sc_hd__a22oi_2.lef
!cp sky130/sky130_fd_sc_hd__a22oi_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a22oi/sky130_fd_sc_hd__a22oi_4.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/a2bb2o
!cp sky130/sky130_fd_sc_hd__a2bb2o_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a2bb2o/sky130_fd_sc_hd__a2bb2o_1.lef
!cp sky130/sky130_fd_sc_hd__a2bb2o_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a2bb2o/sky130_fd_sc_hd__a2bb2o_2.lef
!cp sky130/sky130_fd_sc_hd__a2bb2o_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a2bb2o/sky130_fd_sc_hd__a2bb2o_4.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/a2bb2oi
!cp sky130/sky130_fd_sc_hd__a2bb2oi_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a2bb2oi/sky130_fd_sc_hd__a2bb2oi_1.lef
!cp sky130/sky130_fd_sc_hd__a2bb2oi_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a2bb2oi/sky130_fd_sc_hd__a2bb2oi_2.lef
!cp sky130/sky130_fd_sc_hd__a2bb2oi_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a2bb2oi/sky130_fd_sc_hd__a2bb2oi_4.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/a311o
!cp sky130/sky130_fd_sc_hd__a311o_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a311o/sky130_fd_sc_hd__a311o_1.lef
!cp sky130/sky130_fd_sc_hd__a311o_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a311o/sky130_fd_sc_hd__a311o_2.lef
!cp sky130/sky130_fd_sc_hd__a311o_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a311o/sky130_fd_sc_hd__a311o_4.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/a311oi
!cp sky130/sky130_fd_sc_hd__a311oi_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a311oi/sky130_fd_sc_hd__a311oi_1.lef
!cp sky130/sky130_fd_sc_hd__a311oi_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a311oi/sky130_fd_sc_hd__a311oi_2.lef
!cp sky130/sky130_fd_sc_hd__a311oi_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a311oi/sky130_fd_sc_hd__a311oi_4.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/a31o
!cp sky130/sky130_fd_sc_hd__a31o_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a31o/sky130_fd_sc_hd__a31o_1.lef
!cp sky130/sky130_fd_sc_hd__a31o_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a31o/sky130_fd_sc_hd__a31o_2.lef
!cp sky130/sky130_fd_sc_hd__a31o_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a31o/sky130_fd_sc_hd__a31o_4.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/a31oi
!cp sky130/sky130_fd_sc_hd__a31oi_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a31oi/sky130_fd_sc_hd__a31oi_1.lef
!cp sky130/sky130_fd_sc_hd__a31oi_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a31oi/sky130_fd_sc_hd__a31oi_2.lef
!cp sky130/sky130_fd_sc_hd__a31oi_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a31oi/sky130_fd_sc_hd__a31oi_4.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/a32o
!cp sky130/sky130_fd_sc_hd__a32o_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a32o/sky130_fd_sc_hd__a32o_1.lef
!cp sky130/sky130_fd_sc_hd__a32o_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a32o/sky130_fd_sc_hd__a32o_2.lef
!cp sky130/sky130_fd_sc_hd__a32o_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a32o/sky130_fd_sc_hd__a32o_4.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/a32oi
!cp sky130/sky130_fd_sc_hd__a32oi_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a32oi/sky130_fd_sc_hd__a32oi_1.lef
!cp sky130/sky130_fd_sc_hd__a32oi_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a32oi/sky130_fd_sc_hd__a32oi_2.lef
!cp sky130/sky130_fd_sc_hd__a32oi_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a32oi/sky130_fd_sc_hd__a32oi_4.lef


#@title sky130 PDK Organization Setup - Part 2 {run:"auto"}

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/a41o
!cp sky130/sky130_fd_sc_hd__a41o_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a41o/sky130_fd_sc_hd__a41o_1.lef
!cp sky130/sky130_fd_sc_hd__a41o_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a41o/sky130_fd_sc_hd__a41o_2.lef
!cp sky130/sky130_fd_sc_hd__a41o_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a41o/sky130_fd_sc_hd__a41o_4.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/a41oi
!cp sky130/sky130_fd_sc_hd__a41oi_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a41oi/sky130_fd_sc_hd__a41oi_1.lef
!cp sky130/sky130_fd_sc_hd__a41oi_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a41oi/sky130_fd_sc_hd__a41oi_2.lef
!cp sky130/sky130_fd_sc_hd__a41oi_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/a41oi/sky130_fd_sc_hd__a41oi_4.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/and2
!cp sky130/sky130_fd_sc_hd__and2_0.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/and2/sky130_fd_sc_hd__and2_0.lef
!cp sky130/sky130_fd_sc_hd__and2_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/and2/sky130_fd_sc_hd__and2_1.lef
!cp sky130/sky130_fd_sc_hd__and2_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/and2/sky130_fd_sc_hd__and2_2.lef
!cp sky130/sky130_fd_sc_hd__and2_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/and2/sky130_fd_sc_hd__and2_4.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/and2b
!cp sky130/sky130_fd_sc_hd__and2b_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/and2b/sky130_fd_sc_hd__and2b_1.lef
!cp sky130/sky130_fd_sc_hd__and2b_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/and2b/sky130_fd_sc_hd__and2b_2.lef
!cp sky130/sky130_fd_sc_hd__and2b_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/and2b/sky130_fd_sc_hd__and2b_4.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/and3
!cp sky130/sky130_fd_sc_hd__and3_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/and3/sky130_fd_sc_hd__and3_1.lef
!cp sky130/sky130_fd_sc_hd__and3_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/and3/sky130_fd_sc_hd__and3_2.lef
!cp sky130/sky130_fd_sc_hd__and3_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/and3/sky130_fd_sc_hd__and3_4.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/and3b
!cp sky130/sky130_fd_sc_hd__and3b_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/and3b/sky130_fd_sc_hd__and3b_1.lef
!cp sky130/sky130_fd_sc_hd__and3b_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/and3b/sky130_fd_sc_hd__and3b_2.lef
!cp sky130/sky130_fd_sc_hd__and3b_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/and3b/sky130_fd_sc_hd__and3b_4.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/and4
!cp sky130/sky130_fd_sc_hd__and4_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/and4/sky130_fd_sc_hd__and4_1.lef
!cp sky130/sky130_fd_sc_hd__and4_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/and4/sky130_fd_sc_hd__and4_2.lef
!cp sky130/sky130_fd_sc_hd__and4_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/and4/sky130_fd_sc_hd__and4_4.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/and4b
!cp sky130/sky130_fd_sc_hd__and4b_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/and4b/sky130_fd_sc_hd__and4b_1.lef
!cp sky130/sky130_fd_sc_hd__and4b_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/and4b/sky130_fd_sc_hd__and4b_2.lef
!cp sky130/sky130_fd_sc_hd__and4b_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/and4b/sky130_fd_sc_hd__and4b_4.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/and4bb
!cp sky130/sky130_fd_sc_hd__and4bb_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/and4bb/sky130_fd_sc_hd__and4bb_1.lef
!cp sky130/sky130_fd_sc_hd__and4bb_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/and4bb/sky130_fd_sc_hd__and4bb_2.lef
!cp sky130/sky130_fd_sc_hd__and4bb_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/and4bb/sky130_fd_sc_hd__and4bb_4.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/buf
!cp sky130/sky130_fd_sc_hd__buf_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/buf/sky130_fd_sc_hd__buf_1.lef
!cp sky130/sky130_fd_sc_hd__buf_12.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/buf/sky130_fd_sc_hd__buf_12.lef
!cp sky130/sky130_fd_sc_hd__buf_16.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/buf/sky130_fd_sc_hd__buf_16.lef
!cp sky130/sky130_fd_sc_hd__buf_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/buf/sky130_fd_sc_hd__buf_2.lef
!cp sky130/sky130_fd_sc_hd__buf_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/buf/sky130_fd_sc_hd__buf_4.lef
!cp sky130/sky130_fd_sc_hd__buf_6.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/buf/sky130_fd_sc_hd__buf_6.lef
!cp sky130/sky130_fd_sc_hd__buf_8.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/buf/sky130_fd_sc_hd__buf_8.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/bufbuf
!cp sky130/sky130_fd_sc_hd__bufbuf_16.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/bufbuf/sky130_fd_sc_hd__bufbuf_16.lef
!cp sky130/sky130_fd_sc_hd__bufbuf_8.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/bufbuf/sky130_fd_sc_hd__bufbuf_8.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/bufinv
!cp sky130/sky130_fd_sc_hd__bufinv_16.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/bufinv/sky130_fd_sc_hd__bufinv_16.lef
!cp sky130/sky130_fd_sc_hd__bufinv_8.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/bufinv/sky130_fd_sc_hd__bufinv_8.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/clkbuf
!cp sky130/sky130_fd_sc_hd__clkbuf_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/clkbuf/sky130_fd_sc_hd__clkbuf_1.lef
!cp sky130/sky130_fd_sc_hd__clkbuf_16.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/clkbuf/sky130_fd_sc_hd__clkbuf_16.lef
!cp sky130/sky130_fd_sc_hd__clkbuf_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/clkbuf/sky130_fd_sc_hd__clkbuf_2.lef
!cp sky130/sky130_fd_sc_hd__clkbuf_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/clkbuf/sky130_fd_sc_hd__clkbuf_4.lef
!cp sky130/sky130_fd_sc_hd__clkbuf_8.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/clkbuf/sky130_fd_sc_hd__clkbuf_8.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/clkdlybuf4s15
!cp sky130/sky130_fd_sc_hd__clkdlybuf4s15_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/clkdlybuf4s15/sky130_fd_sc_hd__clkdlybuf4s15_1.lef
!cp sky130/sky130_fd_sc_hd__clkdlybuf4s15_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/clkdlybuf4s15/sky130_fd_sc_hd__clkdlybuf4s15_2.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/clkdlybuf4s18
!cp sky130/sky130_fd_sc_hd__clkdlybuf4s18_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/clkdlybuf4s18/sky130_fd_sc_hd__clkdlybuf4s18_1.lef
!cp sky130/sky130_fd_sc_hd__clkdlybuf4s18_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/clkdlybuf4s18/sky130_fd_sc_hd__clkdlybuf4s18_2.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/clkdlybuf4s25
!cp sky130/sky130_fd_sc_hd__clkdlybuf4s25_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/clkdlybuf4s25/sky130_fd_sc_hd__clkdlybuf4s25_1.lef
!cp sky130/sky130_fd_sc_hd__clkdlybuf4s25_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/clkdlybuf4s25/sky130_fd_sc_hd__clkdlybuf4s25_2.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/clkdlybuf4s50
!cp sky130/sky130_fd_sc_hd__clkdlybuf4s50_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/clkdlybuf4s50/sky130_fd_sc_hd__clkdlybuf4s50_1.lef
!cp sky130/sky130_fd_sc_hd__clkdlybuf4s50_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/clkdlybuf4s50/sky130_fd_sc_hd__clkdlybuf4s50_2.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/clkinv
!cp sky130/sky130_fd_sc_hd__clkinv_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/clkinv/sky130_fd_sc_hd__clkinv_1.lef
!cp sky130/sky130_fd_sc_hd__clkinv_16.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/clkinv/sky130_fd_sc_hd__clkinv_16.lef
!cp sky130/sky130_fd_sc_hd__clkinv_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/clkinv/sky130_fd_sc_hd__clkinv_2.lef
!cp sky130/sky130_fd_sc_hd__clkinv_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/clkinv/sky130_fd_sc_hd__clkinv_4.lef
!cp sky130/sky130_fd_sc_hd__clkinv_8.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/clkinv/sky130_fd_sc_hd__clkinv_8.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/clkinvlp
!cp sky130/sky130_fd_sc_hd__clkinvlp_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/clkinvlp/sky130_fd_sc_hd__clkinvlp_2.lef
!cp sky130/sky130_fd_sc_hd__clkinvlp_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/clkinvlp/sky130_fd_sc_hd__clkinvlp_4.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/conb
!cp sky130/sky130_fd_sc_hd__conb_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/conb/sky130_fd_sc_hd__conb_1.lef

#@title sky130 PDK Organization Setup - Part 3 {run:"auto"}

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/decap
!cp sky130/sky130_fd_sc_hd__decap_12.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/decap/sky130_fd_sc_hd__decap_12.lef
!cp sky130/sky130_fd_sc_hd__decap_3.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/decap/sky130_fd_sc_hd__decap_3.lef
!cp sky130/sky130_fd_sc_hd__decap_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/decap/sky130_fd_sc_hd__decap_4.lef
!cp sky130/sky130_fd_sc_hd__decap_6.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/decap/sky130_fd_sc_hd__decap_6.lef
!cp sky130/sky130_fd_sc_hd__decap_8.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/decap/sky130_fd_sc_hd__decap_8.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/dfbbn
!cp sky130/sky130_fd_sc_hd__dfbbn_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dfbbn/sky130_fd_sc_hd__dfbbn_1.lef
!cp sky130/sky130_fd_sc_hd__dfbbn_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dfbbn/sky130_fd_sc_hd__dfbbn_2.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/dfbbp
!cp sky130/sky130_fd_sc_hd__dfbbp_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dfbbp/sky130_fd_sc_hd__dfbbp_1.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/dfrbp
!cp sky130/sky130_fd_sc_hd__dfrbp_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dfrbp/sky130_fd_sc_hd__dfrbp_1.lef
!cp sky130/sky130_fd_sc_hd__dfrbp_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dfrbp/sky130_fd_sc_hd__dfrbp_2.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/dfrtn
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/dfrtp
!cp sky130/sky130_fd_sc_hd__dfrtn_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dfrtn/sky130_fd_sc_hd__dfrtn_1.lef
!cp sky130/sky130_fd_sc_hd__dfrtp_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dfrtp/sky130_fd_sc_hd__dfrtp_1.lef
!cp sky130/sky130_fd_sc_hd__dfrtp_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dfrtp/sky130_fd_sc_hd__dfrtp_2.lef
!cp sky130/sky130_fd_sc_hd__dfrtp_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dfrtp/sky130_fd_sc_hd__dfrtp_4.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/dfsbp
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/dfstp
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/dfxbp
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/dfxtp
!cp sky130/sky130_fd_sc_hd__dfsbp_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dfsbp/sky130_fd_sc_hd__dfsbp_1.lef
!cp sky130/sky130_fd_sc_hd__dfsbp_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dfsbp/sky130_fd_sc_hd__dfsbp_2.lef
!cp sky130/sky130_fd_sc_hd__dfstp_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dfstp/sky130_fd_sc_hd__dfstp_1.lef
!cp sky130/sky130_fd_sc_hd__dfstp_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dfstp/sky130_fd_sc_hd__dfstp_2.lef
!cp sky130/sky130_fd_sc_hd__dfstp_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dfstp/sky130_fd_sc_hd__dfstp_4.lef
!cp sky130/sky130_fd_sc_hd__dfxbp_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dfxbp/sky130_fd_sc_hd__dfxbp_1.lef
!cp sky130/sky130_fd_sc_hd__dfxbp_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dfxbp/sky130_fd_sc_hd__dfxbp_2.lef
!cp sky130/sky130_fd_sc_hd__dfxtp_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dfxtp/sky130_fd_sc_hd__dfxtp_1.lef
!cp sky130/sky130_fd_sc_hd__dfxtp_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dfxtp/sky130_fd_sc_hd__dfxtp_2.lef
!cp sky130/sky130_fd_sc_hd__dfxtp_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dfxtp/sky130_fd_sc_hd__dfxtp_4.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/diode
!cp sky130/sky130_fd_sc_hd__diode_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/diode/sky130_fd_sc_hd__diode_2.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlclkp
!cp sky130/sky130_fd_sc_hd__dlclkp_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlclkp/sky130_fd_sc_hd__dlclkp_1.lef
!cp sky130/sky130_fd_sc_hd__dlclkp_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlclkp/sky130_fd_sc_hd__dlclkp_2.lef
!cp sky130/sky130_fd_sc_hd__dlclkp_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlclkp/sky130_fd_sc_hd__dlclkp_4.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlrbn
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlrbp
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlrtn
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlrtp
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlxbn
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlxbp
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlxtn
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlxtp
!cp sky130/sky130_fd_sc_hd__dlrbn_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlrbn/sky130_fd_sc_hd__dlrbn_1.lef
!cp sky130/sky130_fd_sc_hd__dlrbn_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlrbn/sky130_fd_sc_hd__dlrbn_2.lef
!cp sky130/sky130_fd_sc_hd__dlrbp_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlrbp/sky130_fd_sc_hd__dlrbp_1.lef
!cp sky130/sky130_fd_sc_hd__dlrbp_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlrbp/sky130_fd_sc_hd__dlrbp_2.lef
!cp sky130/sky130_fd_sc_hd__dlrtn_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlrtn/sky130_fd_sc_hd__dlrtn_1.lef
!cp sky130/sky130_fd_sc_hd__dlrtn_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlrtn/sky130_fd_sc_hd__dlrtn_2.lef
!cp sky130/sky130_fd_sc_hd__dlrtn_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlrtn/sky130_fd_sc_hd__dlrtn_4.lef
!cp sky130/sky130_fd_sc_hd__dlrtp_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlrtp/sky130_fd_sc_hd__dlrtp_1.lef
!cp sky130/sky130_fd_sc_hd__dlrtp_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlrtp/sky130_fd_sc_hd__dlrtp_2.lef
!cp sky130/sky130_fd_sc_hd__dlrtp_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlrtp/sky130_fd_sc_hd__dlrtp_4.lef
!cp sky130/sky130_fd_sc_hd__dlxbn_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlxbn/sky130_fd_sc_hd__dlxbn_1.lef
!cp sky130/sky130_fd_sc_hd__dlxbn_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlxbn/sky130_fd_sc_hd__dlxbn_2.lef
!cp sky130/sky130_fd_sc_hd__dlxbp_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlxbp/sky130_fd_sc_hd__dlxbp_1.lef
!cp sky130/sky130_fd_sc_hd__dlxtn_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlxtn/sky130_fd_sc_hd__dlxtn_1.lef
!cp sky130/sky130_fd_sc_hd__dlxtn_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlxtn/sky130_fd_sc_hd__dlxtn_2.lef
!cp sky130/sky130_fd_sc_hd__dlxtn_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlxtn/sky130_fd_sc_hd__dlxtn_4.lef
!cp sky130/sky130_fd_sc_hd__dlxtp_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlxtp/sky130_fd_sc_hd__dlxtp_1.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlygate4sd1
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlygate4sd2
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlygate4sd3
!cp sky130/sky130_fd_sc_hd__dlygate4sd1_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlygate4sd1/sky130_fd_sc_hd__dlygate4sd1_1.lef
!cp sky130/sky130_fd_sc_hd__dlygate4sd2_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlygate4sd2/sky130_fd_sc_hd__dlygate4sd2_1.lef
!cp sky130/sky130_fd_sc_hd__dlygate4sd3_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlygate4sd3/sky130_fd_sc_hd__dlygate4sd3_1.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlymetal6s2s
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlymetal6s4s
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlymetal6s6s
!cp sky130/sky130_fd_sc_hd__dlymetal6s2s_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlymetal6s2s/sky130_fd_sc_hd__dlymetal6s2s_1.lef
!cp sky130/sky130_fd_sc_hd__dlymetal6s4s_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlymetal6s4s/sky130_fd_sc_hd__dlymetal6s4s_1.lef
!cp sky130/sky130_fd_sc_hd__dlymetal6s6s_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/dlymetal6s6s/sky130_fd_sc_hd__dlymetal6s6s_1.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/ebufn
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/edfxbp
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/edfxtp
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/einvn
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/einvp
!cp sky130/sky130_fd_sc_hd__ebufn_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/ebufn/sky130_fd_sc_hd__ebufn_1.lef
!cp sky130/sky130_fd_sc_hd__ebufn_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/ebufn/sky130_fd_sc_hd__ebufn_2.lef
!cp sky130/sky130_fd_sc_hd__ebufn_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/ebufn/sky130_fd_sc_hd__ebufn_4.lef
!cp sky130/sky130_fd_sc_hd__ebufn_8.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/ebufn/sky130_fd_sc_hd__ebufn_8.lef
!cp sky130/sky130_fd_sc_hd__edfxbp_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/edfxbp/sky130_fd_sc_hd__edfxbp_1.lef
!cp sky130/sky130_fd_sc_hd__edfxtp_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/edfxtp/sky130_fd_sc_hd__edfxtp_1.lef
!cp sky130/sky130_fd_sc_hd__einvn_0.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/einvn/sky130_fd_sc_hd__einvn_0.lef
!cp sky130/sky130_fd_sc_hd__einvn_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/einvn/sky130_fd_sc_hd__einvn_1.lef
!cp sky130/sky130_fd_sc_hd__einvn_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/einvn/sky130_fd_sc_hd__einvn_2.lef
!cp sky130/sky130_fd_sc_hd__einvn_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/einvn/sky130_fd_sc_hd__einvn_4.lef
!cp sky130/sky130_fd_sc_hd__einvn_8.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/einvn/sky130_fd_sc_hd__einvn_8.lef
!cp sky130/sky130_fd_sc_hd__einvp_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/einvp/sky130_fd_sc_hd__einvp_1.lef
!cp sky130/sky130_fd_sc_hd__einvp_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/einvp/sky130_fd_sc_hd__einvp_2.lef
!cp sky130/sky130_fd_sc_hd__einvp_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/einvp/sky130_fd_sc_hd__einvp_4.lef
!cp sky130/sky130_fd_sc_hd__einvp_8.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/einvp/sky130_fd_sc_hd__einvp_8.lef

#@title sky130 PDK Organization Setup - Part 4 {run:"auto"}

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/fa
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/fah
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/fahcin
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/fahcon
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/fill
!cp sky130/sky130_fd_sc_hd__fa_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/fa/sky130_fd_sc_hd__fa_1.lef
!cp sky130/sky130_fd_sc_hd__fa_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/fa/sky130_fd_sc_hd__fa_2.lef
!cp sky130/sky130_fd_sc_hd__fa_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/fa/sky130_fd_sc_hd__fa_4.lef
!cp sky130/sky130_fd_sc_hd__fah_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/fah/sky130_fd_sc_hd__fah_1.lef
!cp sky130/sky130_fd_sc_hd__fahcin_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/fahcin/sky130_fd_sc_hd__fahcin_1.lef
!cp sky130/sky130_fd_sc_hd__fahcon_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/fahcon/sky130_fd_sc_hd__fahcon_1.lef
!cp sky130/sky130_fd_sc_hd__fill_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/fill/sky130_fd_sc_hd__fill_1.lef
!cp sky130/sky130_fd_sc_hd__fill_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/fill/sky130_fd_sc_hd__fill_2.lef
!cp sky130/sky130_fd_sc_hd__fill_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/fill/sky130_fd_sc_hd__fill_4.lef
!cp sky130/sky130_fd_sc_hd__fill_8.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/fill/sky130_fd_sc_hd__fill_8.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/ha
!cp sky130/sky130_fd_sc_hd__ha_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/ha/sky130_fd_sc_hd__ha_1.lef
!cp sky130/sky130_fd_sc_hd__ha_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/ha/sky130_fd_sc_hd__ha_2.lef
!cp sky130/sky130_fd_sc_hd__ha_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/ha/sky130_fd_sc_hd__ha_4.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/inv
!cp sky130/sky130_fd_sc_hd__inv_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/inv/sky130_fd_sc_hd__inv_1.lef
!cp sky130/sky130_fd_sc_hd__inv_12.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/inv/sky130_fd_sc_hd__inv_12.lef
!cp sky130/sky130_fd_sc_hd__inv_16.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/inv/sky130_fd_sc_hd__inv_16.lef
!cp sky130/sky130_fd_sc_hd__inv_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/inv/sky130_fd_sc_hd__inv_2.lef
!cp sky130/sky130_fd_sc_hd__inv_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/inv/sky130_fd_sc_hd__inv_4.lef
!cp sky130/sky130_fd_sc_hd__inv_6.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/inv/sky130_fd_sc_hd__inv_6.lef
!cp sky130/sky130_fd_sc_hd__inv_8.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/inv/sky130_fd_sc_hd__inv_8.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_bleeder
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_clkbufkapwr
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_clkinvkapwr
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_decapkapwr
!cp sky130/sky130_fd_sc_hd__lpflow_bleeder_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_bleeder/sky130_fd_sc_hd__lpflow_bleeder_1.lef
!cp sky130/sky130_fd_sc_hd__lpflow_clkbufkapwr_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_clkbufkapwr/sky130_fd_sc_hd__lpflow_clkbufkapwr_1.lef
!cp sky130/sky130_fd_sc_hd__lpflow_clkbufkapwr_16.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_clkbufkapwr/sky130_fd_sc_hd__lpflow_clkbufkapwr_16.lef
!cp sky130/sky130_fd_sc_hd__lpflow_clkbufkapwr_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_clkbufkapwr/sky130_fd_sc_hd__lpflow_clkbufkapwr_2.lef
!cp sky130/sky130_fd_sc_hd__lpflow_clkbufkapwr_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_clkbufkapwr/sky130_fd_sc_hd__lpflow_clkbufkapwr_4.lef
!cp sky130/sky130_fd_sc_hd__lpflow_clkbufkapwr_8.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_clkbufkapwr/sky130_fd_sc_hd__lpflow_clkbufkapwr_8.lef
!cp sky130/sky130_fd_sc_hd__lpflow_clkinvkapwr_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_clkinvkapwr/sky130_fd_sc_hd__lpflow_clkinvkapwr_1.lef
!cp sky130/sky130_fd_sc_hd__lpflow_clkinvkapwr_16.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_clkinvkapwr/sky130_fd_sc_hd__lpflow_clkinvkapwr_16.lef
!cp sky130/sky130_fd_sc_hd__lpflow_clkinvkapwr_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_clkinvkapwr/sky130_fd_sc_hd__lpflow_clkinvkapwr_2.lef
!cp sky130/sky130_fd_sc_hd__lpflow_clkinvkapwr_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_clkinvkapwr/sky130_fd_sc_hd__lpflow_clkinvkapwr_4.lef
!cp sky130/sky130_fd_sc_hd__lpflow_clkinvkapwr_8.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_clkinvkapwr/sky130_fd_sc_hd__lpflow_clkinvkapwr_8.lef
!cp sky130/sky130_fd_sc_hd__lpflow_decapkapwr_12.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_decapkapwr/sky130_fd_sc_hd__lpflow_decapkapwr_12.lef
!cp sky130/sky130_fd_sc_hd__lpflow_decapkapwr_3.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_decapkapwr/sky130_fd_sc_hd__lpflow_decapkapwr_3.lef
!cp sky130/sky130_fd_sc_hd__lpflow_decapkapwr_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_decapkapwr/sky130_fd_sc_hd__lpflow_decapkapwr_4.lef
!cp sky130/sky130_fd_sc_hd__lpflow_decapkapwr_6.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_decapkapwr/sky130_fd_sc_hd__lpflow_decapkapwr_6.lef
!cp sky130/sky130_fd_sc_hd__lpflow_decapkapwr_8.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_decapkapwr/sky130_fd_sc_hd__lpflow_decapkapwr_8.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_inputiso0n
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_inputiso0p
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_inputiso1n
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_inputiso1p
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_inputisolatch
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_isobufsrc
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_isobufsrckapwr
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_lsbuf_lh_hl_isowell_tap
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_lsbuf_lh_isowell
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_lsbuf_lh_isowell_tap
!cp sky130/sky130_fd_sc_hd__lpflow_inputiso0n_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_inputiso0n/sky130_fd_sc_hd__lpflow_inputiso0n_1.lef
!cp sky130/sky130_fd_sc_hd__lpflow_inputiso0p_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_inputiso0p/sky130_fd_sc_hd__lpflow_inputiso0p_1.lef
!cp sky130/sky130_fd_sc_hd__lpflow_inputiso1n_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_inputiso1n/sky130_fd_sc_hd__lpflow_inputiso1n_1.lef
!cp sky130/sky130_fd_sc_hd__lpflow_inputiso1p_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_inputiso1p/sky130_fd_sc_hd__lpflow_inputiso1p_1.lef
!cp sky130/sky130_fd_sc_hd__lpflow_inputisolatch_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_inputisolatch/sky130_fd_sc_hd__lpflow_inputisolatch_1.lef
!cp sky130/sky130_fd_sc_hd__lpflow_isobufsrc_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_isobufsrc/sky130_fd_sc_hd__lpflow_isobufsrc_1.lef
!cp sky130/sky130_fd_sc_hd__lpflow_isobufsrc_16.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_isobufsrc/sky130_fd_sc_hd__lpflow_isobufsrc_16.lef
!cp sky130/sky130_fd_sc_hd__lpflow_isobufsrc_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_isobufsrc/sky130_fd_sc_hd__lpflow_isobufsrc_2.lef
!cp sky130/sky130_fd_sc_hd__lpflow_isobufsrc_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_isobufsrc/sky130_fd_sc_hd__lpflow_isobufsrc_4.lef
!cp sky130/sky130_fd_sc_hd__lpflow_isobufsrc_8.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_isobufsrc/sky130_fd_sc_hd__lpflow_isobufsrc_8.lef
!cp sky130/sky130_fd_sc_hd__lpflow_isobufsrckapwr_16.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_isobufsrckapwr/sky130_fd_sc_hd__lpflow_isobufsrckapwr_16.lef
!cp sky130/sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_lsbuf_lh_hl_isowell_tap/sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_1.lef
!cp sky130/sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_lsbuf_lh_hl_isowell_tap/sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_2.lef
!cp sky130/sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_lsbuf_lh_hl_isowell_tap/sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_4.lef
!cp sky130/sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_lsbuf_lh_isowell/sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_4.lef
!cp sky130/sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_lsbuf_lh_isowell_tap/sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_1.lef
!cp sky130/sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_lsbuf_lh_isowell_tap/sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_2.lef
!cp sky130/sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/lpflow_lsbuf_lh_isowell_tap/sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_4.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/macro_sparecell
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/maj3
!cp sky130/sky130_fd_sc_hd__macro_sparecell.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/macro_sparecell/sky130_fd_sc_hd__macro_sparecell.lef
!cp sky130/sky130_fd_sc_hd__maj3_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/maj3/sky130_fd_sc_hd__maj3_1.lef
!cp sky130/sky130_fd_sc_hd__maj3_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/maj3/sky130_fd_sc_hd__maj3_2.lef
!cp sky130/sky130_fd_sc_hd__maj3_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/maj3/sky130_fd_sc_hd__maj3_4.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/mux2
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/mux2i
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/mux4
!cp sky130/sky130_fd_sc_hd__mux2_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/mux2/sky130_fd_sc_hd__mux2_1.lef
!cp sky130/sky130_fd_sc_hd__mux2_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/mux2/sky130_fd_sc_hd__mux2_2.lef
!cp sky130/sky130_fd_sc_hd__mux2_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/mux2/sky130_fd_sc_hd__mux2_4.lef
!cp sky130/sky130_fd_sc_hd__mux2_8.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/mux2/sky130_fd_sc_hd__mux2_8.lef
!cp sky130/sky130_fd_sc_hd__mux2i_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/mux2i/sky130_fd_sc_hd__mux2i_1.lef
!cp sky130/sky130_fd_sc_hd__mux2i_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/mux2i/sky130_fd_sc_hd__mux2i_2.lef
!cp sky130/sky130_fd_sc_hd__mux2i_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/mux2i/sky130_fd_sc_hd__mux2i_4.lef
!cp sky130/sky130_fd_sc_hd__mux4_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/mux4/sky130_fd_sc_hd__mux4_1.lef
!cp sky130/sky130_fd_sc_hd__mux4_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/mux4/sky130_fd_sc_hd__mux4_2.lef
!cp sky130/sky130_fd_sc_hd__mux4_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/mux4/sky130_fd_sc_hd__mux4_4.lef

#@title sky130 PDK Organization Setup - Part 5 {run:"auto"}

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/nand2
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/nand2b
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/nand3
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/nand3b
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/nand4
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/nand4b
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/nand4bb
!cp sky130/sky130_fd_sc_hd__nand2_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nand2/sky130_fd_sc_hd__nand2_1.lef
!cp sky130/sky130_fd_sc_hd__nand2_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nand2/sky130_fd_sc_hd__nand2_2.lef
!cp sky130/sky130_fd_sc_hd__nand2_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nand2/sky130_fd_sc_hd__nand2_4.lef
!cp sky130/sky130_fd_sc_hd__nand2_8.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nand2/sky130_fd_sc_hd__nand2_8.lef
!cp sky130/sky130_fd_sc_hd__nand2b_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nand2b/sky130_fd_sc_hd__nand2b_1.lef
!cp sky130/sky130_fd_sc_hd__nand2b_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nand2b/sky130_fd_sc_hd__nand2b_2.lef
!cp sky130/sky130_fd_sc_hd__nand2b_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nand2b/sky130_fd_sc_hd__nand2b_4.lef
!cp sky130/sky130_fd_sc_hd__nand3_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nand3/sky130_fd_sc_hd__nand3_1.lef
!cp sky130/sky130_fd_sc_hd__nand3_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nand3/sky130_fd_sc_hd__nand3_2.lef
!cp sky130/sky130_fd_sc_hd__nand3_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nand3/sky130_fd_sc_hd__nand3_4.lef
!cp sky130/sky130_fd_sc_hd__nand3b_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nand3b/sky130_fd_sc_hd__nand3b_1.lef
!cp sky130/sky130_fd_sc_hd__nand3b_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nand3b/sky130_fd_sc_hd__nand3b_2.lef
!cp sky130/sky130_fd_sc_hd__nand3b_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nand3b/sky130_fd_sc_hd__nand3b_4.lef
!cp sky130/sky130_fd_sc_hd__nand4_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nand4/sky130_fd_sc_hd__nand4_1.lef
!cp sky130/sky130_fd_sc_hd__nand4_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nand4/sky130_fd_sc_hd__nand4_2.lef
!cp sky130/sky130_fd_sc_hd__nand4_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nand4/sky130_fd_sc_hd__nand4_4.lef
!cp sky130/sky130_fd_sc_hd__nand4b_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nand4b/sky130_fd_sc_hd__nand4b_1.lef
!cp sky130/sky130_fd_sc_hd__nand4b_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nand4b/sky130_fd_sc_hd__nand4b_2.lef
!cp sky130/sky130_fd_sc_hd__nand4b_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nand4b/sky130_fd_sc_hd__nand4b_4.lef
!cp sky130/sky130_fd_sc_hd__nand4bb_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nand4bb/sky130_fd_sc_hd__nand4bb_1.lef
!cp sky130/sky130_fd_sc_hd__nand4bb_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nand4bb/sky130_fd_sc_hd__nand4bb_2.lef
!cp sky130/sky130_fd_sc_hd__nand4bb_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nand4bb/sky130_fd_sc_hd__nand4bb_4.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/nor2
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/nor2b
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/nor3
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/nor3b
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/nor4
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/nor4b
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/nor4bb
!cp sky130/sky130_fd_sc_hd__nor2_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nor2/sky130_fd_sc_hd__nor2_1.lef
!cp sky130/sky130_fd_sc_hd__nor2_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nor2/sky130_fd_sc_hd__nor2_2.lef
!cp sky130/sky130_fd_sc_hd__nor2_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nor2/sky130_fd_sc_hd__nor2_4.lef
!cp sky130/sky130_fd_sc_hd__nor2_8.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nor2/sky130_fd_sc_hd__nor2_8.lef
!cp sky130/sky130_fd_sc_hd__nor2b_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nor2b/sky130_fd_sc_hd__nor2b_1.lef
!cp sky130/sky130_fd_sc_hd__nor2b_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nor2b/sky130_fd_sc_hd__nor2b_2.lef
!cp sky130/sky130_fd_sc_hd__nor2b_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nor2b/sky130_fd_sc_hd__nor2b_4.lef
!cp sky130/sky130_fd_sc_hd__nor3_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nor3/sky130_fd_sc_hd__nor3_1.lef
!cp sky130/sky130_fd_sc_hd__nor3_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nor3/sky130_fd_sc_hd__nor3_2.lef
!cp sky130/sky130_fd_sc_hd__nor3_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nor3/sky130_fd_sc_hd__nor3_4.lef
!cp sky130/sky130_fd_sc_hd__nor3b_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nor3b/sky130_fd_sc_hd__nor3b_1.lef
!cp sky130/sky130_fd_sc_hd__nor3b_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nor3b/sky130_fd_sc_hd__nor3b_2.lef
!cp sky130/sky130_fd_sc_hd__nor3b_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nor3b/sky130_fd_sc_hd__nor3b_4.lef
!cp sky130/sky130_fd_sc_hd__nor4_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nor4/sky130_fd_sc_hd__nor4_1.lef
!cp sky130/sky130_fd_sc_hd__nor4_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nor4/sky130_fd_sc_hd__nor4_2.lef
!cp sky130/sky130_fd_sc_hd__nor4_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nor4/sky130_fd_sc_hd__nor4_4.lef
!cp sky130/sky130_fd_sc_hd__nor4b_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nor4b/sky130_fd_sc_hd__nor4b_1.lef
!cp sky130/sky130_fd_sc_hd__nor4b_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nor4b/sky130_fd_sc_hd__nor4b_2.lef
!cp sky130/sky130_fd_sc_hd__nor4b_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nor4b/sky130_fd_sc_hd__nor4b_4.lef
!cp sky130/sky130_fd_sc_hd__nor4bb_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nor4bb/sky130_fd_sc_hd__nor4bb_1.lef
!cp sky130/sky130_fd_sc_hd__nor4bb_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nor4bb/sky130_fd_sc_hd__nor4bb_2.lef
!cp sky130/sky130_fd_sc_hd__nor4bb_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/nor4bb/sky130_fd_sc_hd__nor4bb_4.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/o2111a
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/o2111ai
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/o211a
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/o211ai
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/o21a
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/o21ai
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/o21ba
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/o21bai
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/o221a
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/o221ai
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/o22a
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/o22ai
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/o2bb2a
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/o2bb2ai
!cp sky130/sky130_fd_sc_hd__o2111a_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o2111a/sky130_fd_sc_hd__o2111a_1.lef
!cp sky130/sky130_fd_sc_hd__o2111a_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o2111a/sky130_fd_sc_hd__o2111a_2.lef
!cp sky130/sky130_fd_sc_hd__o2111a_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o2111a/sky130_fd_sc_hd__o2111a_4.lef
!cp sky130/sky130_fd_sc_hd__o2111ai_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o2111ai/sky130_fd_sc_hd__o2111ai_1.lef
!cp sky130/sky130_fd_sc_hd__o2111ai_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o2111ai/sky130_fd_sc_hd__o2111ai_2.lef
!cp sky130/sky130_fd_sc_hd__o2111ai_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o2111ai/sky130_fd_sc_hd__o2111ai_4.lef
!cp sky130/sky130_fd_sc_hd__o211a_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o211a/sky130_fd_sc_hd__o211a_1.lef
!cp sky130/sky130_fd_sc_hd__o211a_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o211a/sky130_fd_sc_hd__o211a_2.lef
!cp sky130/sky130_fd_sc_hd__o211a_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o211a/sky130_fd_sc_hd__o211a_4.lef
!cp sky130/sky130_fd_sc_hd__o211ai_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o211ai/sky130_fd_sc_hd__o211ai_1.lef
!cp sky130/sky130_fd_sc_hd__o211ai_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o211ai/sky130_fd_sc_hd__o211ai_2.lef
!cp sky130/sky130_fd_sc_hd__o211ai_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o211ai/sky130_fd_sc_hd__o211ai_4.lef
!cp sky130/sky130_fd_sc_hd__o21a_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o21a/sky130_fd_sc_hd__o21a_1.lef
!cp sky130/sky130_fd_sc_hd__o21a_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o21a/sky130_fd_sc_hd__o21a_2.lef
!cp sky130/sky130_fd_sc_hd__o21a_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o21a/sky130_fd_sc_hd__o21a_4.lef
!cp sky130/sky130_fd_sc_hd__o21ai_0.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o21ai/sky130_fd_sc_hd__o21ai_0.lef
!cp sky130/sky130_fd_sc_hd__o21ai_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o21ai/sky130_fd_sc_hd__o21ai_1.lef
!cp sky130/sky130_fd_sc_hd__o21ai_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o21ai/sky130_fd_sc_hd__o21ai_2.lef
!cp sky130/sky130_fd_sc_hd__o21ai_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o21ai/sky130_fd_sc_hd__o21ai_4.lef
!cp sky130/sky130_fd_sc_hd__o21ba_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o21ba/sky130_fd_sc_hd__o21ba_1.lef
!cp sky130/sky130_fd_sc_hd__o21ba_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o21ba/sky130_fd_sc_hd__o21ba_2.lef
!cp sky130/sky130_fd_sc_hd__o21ba_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o21ba/sky130_fd_sc_hd__o21ba_4.lef
!cp sky130/sky130_fd_sc_hd__o21bai_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o21bai/sky130_fd_sc_hd__o21bai_1.lef
!cp sky130/sky130_fd_sc_hd__o21bai_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o21bai/sky130_fd_sc_hd__o21bai_2.lef
!cp sky130/sky130_fd_sc_hd__o21bai_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o21bai/sky130_fd_sc_hd__o21bai_4.lef
!cp sky130/sky130_fd_sc_hd__o221a_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o221a/sky130_fd_sc_hd__o221a_1.lef
!cp sky130/sky130_fd_sc_hd__o221a_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o221a/sky130_fd_sc_hd__o221a_2.lef
!cp sky130/sky130_fd_sc_hd__o221a_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o221a/sky130_fd_sc_hd__o221a_4.lef
!cp sky130/sky130_fd_sc_hd__o221ai_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o221ai/sky130_fd_sc_hd__o221ai_1.lef
!cp sky130/sky130_fd_sc_hd__o221ai_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o221ai/sky130_fd_sc_hd__o221ai_2.lef
!cp sky130/sky130_fd_sc_hd__o221ai_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o221ai/sky130_fd_sc_hd__o221ai_4.lef
!cp sky130/sky130_fd_sc_hd__o22a_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o22a/sky130_fd_sc_hd__o22a_1.lef
!cp sky130/sky130_fd_sc_hd__o22a_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o22a/sky130_fd_sc_hd__o22a_2.lef
!cp sky130/sky130_fd_sc_hd__o22a_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o22a/sky130_fd_sc_hd__o22a_4.lef
!cp sky130/sky130_fd_sc_hd__o22ai_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o22ai/sky130_fd_sc_hd__o22ai_1.lef
!cp sky130/sky130_fd_sc_hd__o22ai_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o22ai/sky130_fd_sc_hd__o22ai_2.lef
!cp sky130/sky130_fd_sc_hd__o22ai_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o22ai/sky130_fd_sc_hd__o22ai_4.lef
!cp sky130/sky130_fd_sc_hd__o2bb2a_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o2bb2a/sky130_fd_sc_hd__o2bb2a_1.lef
!cp sky130/sky130_fd_sc_hd__o2bb2a_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o2bb2a/sky130_fd_sc_hd__o2bb2a_2.lef
!cp sky130/sky130_fd_sc_hd__o2bb2a_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o2bb2a/sky130_fd_sc_hd__o2bb2a_4.lef
!cp sky130/sky130_fd_sc_hd__o2bb2ai_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o2bb2ai/sky130_fd_sc_hd__o2bb2ai_1.lef
!cp sky130/sky130_fd_sc_hd__o2bb2ai_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o2bb2ai/sky130_fd_sc_hd__o2bb2ai_2.lef
!cp sky130/sky130_fd_sc_hd__o2bb2ai_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o2bb2ai/sky130_fd_sc_hd__o2bb2ai_4.lef

#@title sky130 PDK Organization Setup - Part 6 {run:"auto"}

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/o311a
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/o311ai
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/o31a
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/o31ai
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/o32a
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/o32ai
!cp sky130/sky130_fd_sc_hd__o311a_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o311a/sky130_fd_sc_hd__o311a_1.lef
!cp sky130/sky130_fd_sc_hd__o311a_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o311a/sky130_fd_sc_hd__o311a_2.lef
!cp sky130/sky130_fd_sc_hd__o311a_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o311a/sky130_fd_sc_hd__o311a_4.lef
!cp sky130/sky130_fd_sc_hd__o311ai_0.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o311ai/sky130_fd_sc_hd__o311ai_0.lef
!cp sky130/sky130_fd_sc_hd__o311ai_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o311ai/sky130_fd_sc_hd__o311ai_1.lef
!cp sky130/sky130_fd_sc_hd__o311ai_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o311ai/sky130_fd_sc_hd__o311ai_2.lef
!cp sky130/sky130_fd_sc_hd__o311ai_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o311ai/sky130_fd_sc_hd__o311ai_4.lef
!cp sky130/sky130_fd_sc_hd__o31a_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o31a/sky130_fd_sc_hd__o31a_1.lef
!cp sky130/sky130_fd_sc_hd__o31a_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o31a/sky130_fd_sc_hd__o31a_2.lef
!cp sky130/sky130_fd_sc_hd__o31a_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o31a/sky130_fd_sc_hd__o31a_4.lef
!cp sky130/sky130_fd_sc_hd__o31ai_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o31ai/sky130_fd_sc_hd__o31ai_1.lef
!cp sky130/sky130_fd_sc_hd__o31ai_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o31ai/sky130_fd_sc_hd__o31ai_2.lef
!cp sky130/sky130_fd_sc_hd__o31ai_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o31ai/sky130_fd_sc_hd__o31ai_4.lef
!cp sky130/sky130_fd_sc_hd__o32a_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o32a/sky130_fd_sc_hd__o32a_1.lef
!cp sky130/sky130_fd_sc_hd__o32a_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o32a/sky130_fd_sc_hd__o32a_2.lef
!cp sky130/sky130_fd_sc_hd__o32a_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o32a/sky130_fd_sc_hd__o32a_4.lef
!cp sky130/sky130_fd_sc_hd__o32ai_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o32ai/sky130_fd_sc_hd__o32ai_1.lef
!cp sky130/sky130_fd_sc_hd__o32ai_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o32ai/sky130_fd_sc_hd__o32ai_2.lef
!cp sky130/sky130_fd_sc_hd__o32ai_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o32ai/sky130_fd_sc_hd__o32ai_4.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/o41a
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/o41ai
!cp sky130/sky130_fd_sc_hd__o41a_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o41a/sky130_fd_sc_hd__o41a_1.lef
!cp sky130/sky130_fd_sc_hd__o41a_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o41a/sky130_fd_sc_hd__o41a_2.lef
!cp sky130/sky130_fd_sc_hd__o41a_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o41a/sky130_fd_sc_hd__o41a_4.lef
!cp sky130/sky130_fd_sc_hd__o41ai_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o41ai/sky130_fd_sc_hd__o41ai_1.lef
!cp sky130/sky130_fd_sc_hd__o41ai_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o41ai/sky130_fd_sc_hd__o41ai_2.lef
!cp sky130/sky130_fd_sc_hd__o41ai_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/o41ai/sky130_fd_sc_hd__o41ai_4.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/or2
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/or2b
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/or3
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/or3b
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/or4
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/or4b
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/or4bb
!cp sky130/sky130_fd_sc_hd__or2_0.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/or2/sky130_fd_sc_hd__or2_0.lef
!cp sky130/sky130_fd_sc_hd__or2_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/or2/sky130_fd_sc_hd__or2_1.lef
!cp sky130/sky130_fd_sc_hd__or2_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/or2/sky130_fd_sc_hd__or2_2.lef
!cp sky130/sky130_fd_sc_hd__or2_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/or2/sky130_fd_sc_hd__or2_4.lef
!cp sky130/sky130_fd_sc_hd__or2b_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/or2b/sky130_fd_sc_hd__or2b_1.lef
!cp sky130/sky130_fd_sc_hd__or2b_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/or2b/sky130_fd_sc_hd__or2b_2.lef
!cp sky130/sky130_fd_sc_hd__or2b_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/or2b/sky130_fd_sc_hd__or2b_4.lef
!cp sky130/sky130_fd_sc_hd__or3_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/or3/sky130_fd_sc_hd__or3_1.lef
!cp sky130/sky130_fd_sc_hd__or3_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/or3/sky130_fd_sc_hd__or3_2.lef
!cp sky130/sky130_fd_sc_hd__or3_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/or3/sky130_fd_sc_hd__or3_4.lef
!cp sky130/sky130_fd_sc_hd__or3b_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/or3b/sky130_fd_sc_hd__or3b_1.lef
!cp sky130/sky130_fd_sc_hd__or3b_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/or3b/sky130_fd_sc_hd__or3b_2.lef
!cp sky130/sky130_fd_sc_hd__or3b_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/or3b/sky130_fd_sc_hd__or3b_4.lef
!cp sky130/sky130_fd_sc_hd__or4_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/or4/sky130_fd_sc_hd__or4_1.lef
!cp sky130/sky130_fd_sc_hd__or4_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/or4/sky130_fd_sc_hd__or4_2.lef
!cp sky130/sky130_fd_sc_hd__or4_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/or4/sky130_fd_sc_hd__or4_4.lef
!cp sky130/sky130_fd_sc_hd__or4b_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/or4b/sky130_fd_sc_hd__or4b_1.lef
!cp sky130/sky130_fd_sc_hd__or4b_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/or4b/sky130_fd_sc_hd__or4b_2.lef
!cp sky130/sky130_fd_sc_hd__or4b_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/or4b/sky130_fd_sc_hd__or4b_4.lef
!cp sky130/sky130_fd_sc_hd__or4bb_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/or4bb/sky130_fd_sc_hd__or4bb_1.lef
!cp sky130/sky130_fd_sc_hd__or4bb_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/or4bb/sky130_fd_sc_hd__or4bb_2.lef
!cp sky130/sky130_fd_sc_hd__or4bb_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/or4bb/sky130_fd_sc_hd__or4bb_4.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/probe_p
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/probec_p
!cp sky130/sky130_fd_sc_hd__probe_p_8.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/probe_p/sky130_fd_sc_hd__probe_p_8.lef
!cp sky130/sky130_fd_sc_hd__probec_p_8.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/probec_p/sky130_fd_sc_hd__probec_p_8.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/sdfbbn
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/sdfbbp
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/sdfrbp
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/sdfrtn
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/sdfrtp
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/sdfsbp
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/sdfstp
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/sdfxbp
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/sdfxtp
!cp sky130/sky130_fd_sc_hd__sdfbbn_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/sdfbbn/sky130_fd_sc_hd__sdfbbn_1.lef
!cp sky130/sky130_fd_sc_hd__sdfbbn_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/sdfbbn/sky130_fd_sc_hd__sdfbbn_2.lef
!cp sky130/sky130_fd_sc_hd__sdfbbp_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/sdfbbp/sky130_fd_sc_hd__sdfbbp_1.lef
!cp sky130/sky130_fd_sc_hd__sdfrbp_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/sdfrbp/sky130_fd_sc_hd__sdfrbp_1.lef
!cp sky130/sky130_fd_sc_hd__sdfrbp_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/sdfrbp/sky130_fd_sc_hd__sdfrbp_2.lef
!cp sky130/sky130_fd_sc_hd__sdfrtn_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/sdfrtn/sky130_fd_sc_hd__sdfrtn_1.lef
!cp sky130/sky130_fd_sc_hd__sdfrtp_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/sdfrtp/sky130_fd_sc_hd__sdfrtp_1.lef
!cp sky130/sky130_fd_sc_hd__sdfrtp_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/sdfrtp/sky130_fd_sc_hd__sdfrtp_2.lef
!cp sky130/sky130_fd_sc_hd__sdfrtp_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/sdfrtp/sky130_fd_sc_hd__sdfrtp_4.lef
!cp sky130/sky130_fd_sc_hd__sdfsbp_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/sdfsbp/sky130_fd_sc_hd__sdfsbp_1.lef
!cp sky130/sky130_fd_sc_hd__sdfsbp_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/sdfsbp/sky130_fd_sc_hd__sdfsbp_2.lef
!cp sky130/sky130_fd_sc_hd__sdfstp_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/sdfstp/sky130_fd_sc_hd__sdfstp_1.lef
!cp sky130/sky130_fd_sc_hd__sdfstp_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/sdfstp/sky130_fd_sc_hd__sdfstp_2.lef
!cp sky130/sky130_fd_sc_hd__sdfstp_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/sdfstp/sky130_fd_sc_hd__sdfstp_4.lef
!cp sky130/sky130_fd_sc_hd__sdfxbp_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/sdfxbp/sky130_fd_sc_hd__sdfxbp_1.lef
!cp sky130/sky130_fd_sc_hd__sdfxbp_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/sdfxbp/sky130_fd_sc_hd__sdfxbp_2.lef
!cp sky130/sky130_fd_sc_hd__sdfxtp_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/sdfxtp/sky130_fd_sc_hd__sdfxtp_1.lef
!cp sky130/sky130_fd_sc_hd__sdfxtp_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/sdfxtp/sky130_fd_sc_hd__sdfxtp_2.lef
!cp sky130/sky130_fd_sc_hd__sdfxtp_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/sdfxtp/sky130_fd_sc_hd__sdfxtp_4.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/sdlclkp
!cp sky130/sky130_fd_sc_hd__sdlclkp_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/sdlclkp/sky130_fd_sc_hd__sdlclkp_1.lef
!cp sky130/sky130_fd_sc_hd__sdlclkp_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/sdlclkp/sky130_fd_sc_hd__sdlclkp_2.lef
!cp sky130/sky130_fd_sc_hd__sdlclkp_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/sdlclkp/sky130_fd_sc_hd__sdlclkp_4.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/sedfxbp
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/sedfxtp
!cp sky130/sky130_fd_sc_hd__sedfxbp_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/sedfxbp/sky130_fd_sc_hd__sedfxbp_1.lef
!cp sky130/sky130_fd_sc_hd__sedfxbp_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/sedfxbp/sky130_fd_sc_hd__sedfxbp_2.lef
!cp sky130/sky130_fd_sc_hd__sedfxtp_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/sedfxtp/sky130_fd_sc_hd__sedfxtp_1.lef
!cp sky130/sky130_fd_sc_hd__sedfxtp_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/sedfxtp/sky130_fd_sc_hd__sedfxtp_2.lef
!cp sky130/sky130_fd_sc_hd__sedfxtp_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/sedfxtp/sky130_fd_sc_hd__sedfxtp_4.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/tap
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/tapvgnd
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/tapvgnd2
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/tapvpwrvgnd
!cp sky130/sky130_fd_sc_hd__tap_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/tap/sky130_fd_sc_hd__tap_1.lef
!cp sky130/sky130_fd_sc_hd__tap_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/tap/sky130_fd_sc_hd__tap_2.lef
!cp sky130/sky130_fd_sc_hd__tapvgnd_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/tapvgnd/sky130_fd_sc_hd__tapvgnd_1.lef
!cp sky130/sky130_fd_sc_hd__tapvgnd2_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/tapvgnd2/sky130_fd_sc_hd__tapvgnd2_1.lef
!cp sky130/sky130_fd_sc_hd__tapvpwrvgnd_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/tapvpwrvgnd/sky130_fd_sc_hd__tapvpwrvgnd_1.lef

!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/xnor2
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/xnor3
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/xor2
!mkdir com_google_skywater_pdk_sky130_fd_sc_hd/cells/xor3
!cp sky130/sky130_fd_sc_hd__xnor2_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/xnor2/sky130_fd_sc_hd__xnor2_1.lef
!cp sky130/sky130_fd_sc_hd__xnor2_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/xnor2/sky130_fd_sc_hd__xnor2_2.lef
!cp sky130/sky130_fd_sc_hd__xnor2_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/xnor2/sky130_fd_sc_hd__xnor2_4.lef
!cp sky130/sky130_fd_sc_hd__xnor3_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/xnor3/sky130_fd_sc_hd__xnor3_1.lef
!cp sky130/sky130_fd_sc_hd__xnor3_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/xnor3/sky130_fd_sc_hd__xnor3_2.lef
!cp sky130/sky130_fd_sc_hd__xnor3_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/xnor3/sky130_fd_sc_hd__xnor3_4.lef
!cp sky130/sky130_fd_sc_hd__xor2_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/xor2/sky130_fd_sc_hd__xor2_1.lef
!cp sky130/sky130_fd_sc_hd__xor2_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/xor2/sky130_fd_sc_hd__xor2_2.lef
!cp sky130/sky130_fd_sc_hd__xor2_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/xor2/sky130_fd_sc_hd__xor2_4.lef
!cp sky130/sky130_fd_sc_hd__xor3_1.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/xor3/sky130_fd_sc_hd__xor3_1.lef
!cp sky130/sky130_fd_sc_hd__xor3_2.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/xor3/sky130_fd_sc_hd__xor3_2.lef
!cp sky130/sky130_fd_sc_hd__xor3_4.lef com_google_skywater_pdk_sky130_fd_sc_hd/cells/xor3/sky130_fd_sc_hd__xor3_4.lef

!cp sky130/sky130_fd_sc_hd.tlef com_google_skywater_pdk_sky130_fd_sc_hd/tech/sky130_fd_sc_hd.tlef
!cp sky130/sky130_fd_sc_hd__ff_100C_1v95.lib com_google_skywater_pdk_sky130_fd_sc_hd/timing/sky130_fd_sc_hd__ff_100C_1v95.lib

!mkdir sky130/dependency_support
!mkdir sky130/dependency_support/com_google_skywater_pdk
!mkdir sky130/dependency_support/com_google_skywater_pdk/sky130_fd_sc_hd/
!cp sky130/tracks.tcl sky130/dependency_support/com_google_skywater_pdk/sky130_fd_sc_hd/tracks.tcl
!cp sky130/pdn_config.pdn sky130/dependency_support/com_google_skywater_pdk/sky130_fd_sc_hd/pdn_config.pdn