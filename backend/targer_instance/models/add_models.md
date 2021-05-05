Open a terminal in this folder, then execute the following commands to download the models:
<table>
<tr><td>COMBO.h5:</td><td>wget http://ltdata1.informatik.uni-hamburg.de/targer/COMBO.h5</td></tr>
<tr><td>ES.h5:</td><td>wget http://ltdata1.informatik.uni-hamburg.de/targer/ES.h5</td></tr>
<tr><td>ES_dep.h5:</td><td>wget http://ltdata1.informatik.uni-hamburg.de/targer/ES_dep.h5</td></tr>
<tr><td>IBM.h5:</td><td>wget http://ltdata1.informatik.uni-hamburg.de/targer/IBM.h5</td></tr>
<tr><td>model_new_es.hdf5</td><td>wget http://ltdata1.informatik.uni-hamburg.de/targer/model_new_es.hdf5</td></tr>
<tr><td>model_new_wd.hdf5</td><td>wget http://ltdata1.informatik.uni-hamburg.de/targer/model_new_wd.hdf5</td></tr>
<tr><td>WD.h5:</td><td>wget http://ltdata1.informatik.uni-hamburg.de/targer/WD.h5</td></tr>
<tr><td>WD_dep.h5</td><td>wget http://ltdata1.informatik.uni-hamburg.de/targer/WD_dep.h5</td></tr>
</table>

Shell Command:\
`wget http://ltdata1.informatik.uni-hamburg.de/targer/COMBO.h5 &&
wget http://ltdata1.informatik.uni-hamburg.de/targer/ES.h5 &&
wget http://ltdata1.informatik.uni-hamburg.de/targer/ES_dep.h5 &&
wget http://ltdata1.informatik.uni-hamburg.de/targer/IBM.h5 &&
wget http://ltdata1.informatik.uni-hamburg.de/targer/WD.h5 &&
wget http://ltdata1.informatik.uni-hamburg.de/targer/WD_dep.h5 &&
wget http://ltdata1.informatik.uni-hamburg.de/targer/model_new_es.hdf5 &&
wget http://ltdata1.informatik.uni-hamburg.de/targer/model_new_wd.hdf5`

**On Windows** it gets a little more cumbersome as `wget` is not coming with Windows by default.
Instead you can download the models with `bitsadmin` (built-in cli download tool), see the [documentation examples](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-examples).
