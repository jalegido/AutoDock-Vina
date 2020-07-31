# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
#################################################################
# If you used AutoDock Vina in your work, please cite:          #
#                                                               #
# O. Trott, A. J. Olson,                                        #
# AutoDock Vina: improving the speed and accuracy of docking    #
# with a new scoring function, efficient optimization and       #
# multithreading, Journal of Computational Chemistry 31 (2010)  #
# 455-461                                                       #
#                                                               #
# DOI 10.1002/jcc.21334                                         #
#                                                               #
# Please see http://vina.scripps.edu for more information.      #
#################################################################

"""


import sys
if sys.platform.find("linux") != -1:
    dlflags = sys.getdlopenflags()
    import ctypes
    sys.setdlopenflags(dlflags | ctypes.RTLD_GLOBAL)



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _vina
else:
    import _vina

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)



if sys.platform.find("linux") != -1:
    sys.setdlopenflags(dlflags)

class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _vina.delete_SwigPyIterator

    def value(self) -> "PyObject *":
        return _vina.SwigPyIterator_value(self)

    def incr(self, n: "size_t"=1) -> "swig::SwigPyIterator *":
        return _vina.SwigPyIterator_incr(self, n)

    def decr(self, n: "size_t"=1) -> "swig::SwigPyIterator *":
        return _vina.SwigPyIterator_decr(self, n)

    def distance(self, x: "SwigPyIterator") -> "ptrdiff_t":
        return _vina.SwigPyIterator_distance(self, x)

    def equal(self, x: "SwigPyIterator") -> "bool":
        return _vina.SwigPyIterator_equal(self, x)

    def copy(self) -> "swig::SwigPyIterator *":
        return _vina.SwigPyIterator_copy(self)

    def next(self) -> "PyObject *":
        return _vina.SwigPyIterator_next(self)

    def __next__(self) -> "PyObject *":
        return _vina.SwigPyIterator___next__(self)

    def previous(self) -> "PyObject *":
        return _vina.SwigPyIterator_previous(self)

    def advance(self, n: "ptrdiff_t") -> "swig::SwigPyIterator *":
        return _vina.SwigPyIterator_advance(self, n)

    def __eq__(self, x: "SwigPyIterator") -> "bool":
        return _vina.SwigPyIterator___eq__(self, x)

    def __ne__(self, x: "SwigPyIterator") -> "bool":
        return _vina.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n: "ptrdiff_t") -> "swig::SwigPyIterator &":
        return _vina.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n: "ptrdiff_t") -> "swig::SwigPyIterator &":
        return _vina.SwigPyIterator___isub__(self, n)

    def __add__(self, n: "ptrdiff_t") -> "swig::SwigPyIterator *":
        return _vina.SwigPyIterator___add__(self, n)

    def __sub__(self, *args) -> "ptrdiff_t":
        return _vina.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _vina:
_vina.SwigPyIterator_swigregister(SwigPyIterator)

class IntVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self) -> "swig::SwigPyIterator *":
        return _vina.IntVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self) -> "bool":
        return _vina.IntVector___nonzero__(self)

    def __bool__(self) -> "bool":
        return _vina.IntVector___bool__(self)

    def __len__(self) -> "std::vector< int >::size_type":
        return _vina.IntVector___len__(self)

    def __getslice__(self, i: "std::vector< int >::difference_type", j: "std::vector< int >::difference_type") -> "std::vector< int,std::allocator< int > > *":
        return _vina.IntVector___getslice__(self, i, j)

    def __setslice__(self, *args) -> "void":
        return _vina.IntVector___setslice__(self, *args)

    def __delslice__(self, i: "std::vector< int >::difference_type", j: "std::vector< int >::difference_type") -> "void":
        return _vina.IntVector___delslice__(self, i, j)

    def __delitem__(self, *args) -> "void":
        return _vina.IntVector___delitem__(self, *args)

    def __getitem__(self, *args) -> "std::vector< int >::value_type const &":
        return _vina.IntVector___getitem__(self, *args)

    def __setitem__(self, *args) -> "void":
        return _vina.IntVector___setitem__(self, *args)

    def pop(self) -> "std::vector< int >::value_type":
        return _vina.IntVector_pop(self)

    def append(self, x: "std::vector< int >::value_type const &") -> "void":
        return _vina.IntVector_append(self, x)

    def empty(self) -> "bool":
        return _vina.IntVector_empty(self)

    def size(self) -> "std::vector< int >::size_type":
        return _vina.IntVector_size(self)

    def swap(self, v: "IntVector") -> "void":
        return _vina.IntVector_swap(self, v)

    def begin(self) -> "std::vector< int >::iterator":
        return _vina.IntVector_begin(self)

    def end(self) -> "std::vector< int >::iterator":
        return _vina.IntVector_end(self)

    def rbegin(self) -> "std::vector< int >::reverse_iterator":
        return _vina.IntVector_rbegin(self)

    def rend(self) -> "std::vector< int >::reverse_iterator":
        return _vina.IntVector_rend(self)

    def clear(self) -> "void":
        return _vina.IntVector_clear(self)

    def get_allocator(self) -> "std::vector< int >::allocator_type":
        return _vina.IntVector_get_allocator(self)

    def pop_back(self) -> "void":
        return _vina.IntVector_pop_back(self)

    def erase(self, *args) -> "std::vector< int >::iterator":
        return _vina.IntVector_erase(self, *args)

    def __init__(self, *args):
        _vina.IntVector_swiginit(self, _vina.new_IntVector(*args))

    def push_back(self, x: "std::vector< int >::value_type const &") -> "void":
        return _vina.IntVector_push_back(self, x)

    def front(self) -> "std::vector< int >::value_type const &":
        return _vina.IntVector_front(self)

    def back(self) -> "std::vector< int >::value_type const &":
        return _vina.IntVector_back(self)

    def assign(self, n: "std::vector< int >::size_type", x: "std::vector< int >::value_type const &") -> "void":
        return _vina.IntVector_assign(self, n, x)

    def resize(self, *args) -> "void":
        return _vina.IntVector_resize(self, *args)

    def insert(self, *args) -> "void":
        return _vina.IntVector_insert(self, *args)

    def reserve(self, n: "std::vector< int >::size_type") -> "void":
        return _vina.IntVector_reserve(self, n)

    def capacity(self) -> "std::vector< int >::size_type":
        return _vina.IntVector_capacity(self)
    __swig_destroy__ = _vina.delete_IntVector

# Register IntVector in _vina:
_vina.IntVector_swigregister(IntVector)

class DoubleVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self) -> "swig::SwigPyIterator *":
        return _vina.DoubleVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self) -> "bool":
        return _vina.DoubleVector___nonzero__(self)

    def __bool__(self) -> "bool":
        return _vina.DoubleVector___bool__(self)

    def __len__(self) -> "std::vector< double >::size_type":
        return _vina.DoubleVector___len__(self)

    def __getslice__(self, i: "std::vector< double >::difference_type", j: "std::vector< double >::difference_type") -> "std::vector< double,std::allocator< double > > *":
        return _vina.DoubleVector___getslice__(self, i, j)

    def __setslice__(self, *args) -> "void":
        return _vina.DoubleVector___setslice__(self, *args)

    def __delslice__(self, i: "std::vector< double >::difference_type", j: "std::vector< double >::difference_type") -> "void":
        return _vina.DoubleVector___delslice__(self, i, j)

    def __delitem__(self, *args) -> "void":
        return _vina.DoubleVector___delitem__(self, *args)

    def __getitem__(self, *args) -> "std::vector< double >::value_type const &":
        return _vina.DoubleVector___getitem__(self, *args)

    def __setitem__(self, *args) -> "void":
        return _vina.DoubleVector___setitem__(self, *args)

    def pop(self) -> "std::vector< double >::value_type":
        return _vina.DoubleVector_pop(self)

    def append(self, x: "std::vector< double >::value_type const &") -> "void":
        return _vina.DoubleVector_append(self, x)

    def empty(self) -> "bool":
        return _vina.DoubleVector_empty(self)

    def size(self) -> "std::vector< double >::size_type":
        return _vina.DoubleVector_size(self)

    def swap(self, v: "DoubleVector") -> "void":
        return _vina.DoubleVector_swap(self, v)

    def begin(self) -> "std::vector< double >::iterator":
        return _vina.DoubleVector_begin(self)

    def end(self) -> "std::vector< double >::iterator":
        return _vina.DoubleVector_end(self)

    def rbegin(self) -> "std::vector< double >::reverse_iterator":
        return _vina.DoubleVector_rbegin(self)

    def rend(self) -> "std::vector< double >::reverse_iterator":
        return _vina.DoubleVector_rend(self)

    def clear(self) -> "void":
        return _vina.DoubleVector_clear(self)

    def get_allocator(self) -> "std::vector< double >::allocator_type":
        return _vina.DoubleVector_get_allocator(self)

    def pop_back(self) -> "void":
        return _vina.DoubleVector_pop_back(self)

    def erase(self, *args) -> "std::vector< double >::iterator":
        return _vina.DoubleVector_erase(self, *args)

    def __init__(self, *args):
        _vina.DoubleVector_swiginit(self, _vina.new_DoubleVector(*args))

    def push_back(self, x: "std::vector< double >::value_type const &") -> "void":
        return _vina.DoubleVector_push_back(self, x)

    def front(self) -> "std::vector< double >::value_type const &":
        return _vina.DoubleVector_front(self)

    def back(self) -> "std::vector< double >::value_type const &":
        return _vina.DoubleVector_back(self)

    def assign(self, n: "std::vector< double >::size_type", x: "std::vector< double >::value_type const &") -> "void":
        return _vina.DoubleVector_assign(self, n, x)

    def resize(self, *args) -> "void":
        return _vina.DoubleVector_resize(self, *args)

    def insert(self, *args) -> "void":
        return _vina.DoubleVector_insert(self, *args)

    def reserve(self, n: "std::vector< double >::size_type") -> "void":
        return _vina.DoubleVector_reserve(self, n)

    def capacity(self) -> "std::vector< double >::size_type":
        return _vina.DoubleVector_capacity(self)
    __swig_destroy__ = _vina.delete_DoubleVector

# Register DoubleVector in _vina:
_vina.DoubleVector_swigregister(DoubleVector)

class StringVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self) -> "swig::SwigPyIterator *":
        return _vina.StringVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self) -> "bool":
        return _vina.StringVector___nonzero__(self)

    def __bool__(self) -> "bool":
        return _vina.StringVector___bool__(self)

    def __len__(self) -> "std::vector< std::string >::size_type":
        return _vina.StringVector___len__(self)

    def __getslice__(self, i: "std::vector< std::string >::difference_type", j: "std::vector< std::string >::difference_type") -> "std::vector< std::string,std::allocator< std::string > > *":
        return _vina.StringVector___getslice__(self, i, j)

    def __setslice__(self, *args) -> "void":
        return _vina.StringVector___setslice__(self, *args)

    def __delslice__(self, i: "std::vector< std::string >::difference_type", j: "std::vector< std::string >::difference_type") -> "void":
        return _vina.StringVector___delslice__(self, i, j)

    def __delitem__(self, *args) -> "void":
        return _vina.StringVector___delitem__(self, *args)

    def __getitem__(self, *args) -> "std::vector< std::string >::value_type const &":
        return _vina.StringVector___getitem__(self, *args)

    def __setitem__(self, *args) -> "void":
        return _vina.StringVector___setitem__(self, *args)

    def pop(self) -> "std::vector< std::string >::value_type":
        return _vina.StringVector_pop(self)

    def append(self, x: "std::vector< std::string >::value_type const &") -> "void":
        return _vina.StringVector_append(self, x)

    def empty(self) -> "bool":
        return _vina.StringVector_empty(self)

    def size(self) -> "std::vector< std::string >::size_type":
        return _vina.StringVector_size(self)

    def swap(self, v: "StringVector") -> "void":
        return _vina.StringVector_swap(self, v)

    def begin(self) -> "std::vector< std::string >::iterator":
        return _vina.StringVector_begin(self)

    def end(self) -> "std::vector< std::string >::iterator":
        return _vina.StringVector_end(self)

    def rbegin(self) -> "std::vector< std::string >::reverse_iterator":
        return _vina.StringVector_rbegin(self)

    def rend(self) -> "std::vector< std::string >::reverse_iterator":
        return _vina.StringVector_rend(self)

    def clear(self) -> "void":
        return _vina.StringVector_clear(self)

    def get_allocator(self) -> "std::vector< std::string >::allocator_type":
        return _vina.StringVector_get_allocator(self)

    def pop_back(self) -> "void":
        return _vina.StringVector_pop_back(self)

    def erase(self, *args) -> "std::vector< std::string >::iterator":
        return _vina.StringVector_erase(self, *args)

    def __init__(self, *args):
        _vina.StringVector_swiginit(self, _vina.new_StringVector(*args))

    def push_back(self, x: "std::vector< std::string >::value_type const &") -> "void":
        return _vina.StringVector_push_back(self, x)

    def front(self) -> "std::vector< std::string >::value_type const &":
        return _vina.StringVector_front(self)

    def back(self) -> "std::vector< std::string >::value_type const &":
        return _vina.StringVector_back(self)

    def assign(self, n: "std::vector< std::string >::size_type", x: "std::vector< std::string >::value_type const &") -> "void":
        return _vina.StringVector_assign(self, n, x)

    def resize(self, *args) -> "void":
        return _vina.StringVector_resize(self, *args)

    def insert(self, *args) -> "void":
        return _vina.StringVector_insert(self, *args)

    def reserve(self, n: "std::vector< std::string >::size_type") -> "void":
        return _vina.StringVector_reserve(self, n)

    def capacity(self) -> "std::vector< std::string >::size_type":
        return _vina.StringVector_capacity(self)
    __swig_destroy__ = _vina.delete_StringVector

# Register StringVector in _vina:
_vina.StringVector_swigregister(StringVector)

class ConstCharVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self) -> "swig::SwigPyIterator *":
        return _vina.ConstCharVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self) -> "bool":
        return _vina.ConstCharVector___nonzero__(self)

    def __bool__(self) -> "bool":
        return _vina.ConstCharVector___bool__(self)

    def __len__(self) -> "std::vector< char const * >::size_type":
        return _vina.ConstCharVector___len__(self)

    def __getslice__(self, i: "std::vector< char const * >::difference_type", j: "std::vector< char const * >::difference_type") -> "std::vector< char const *,std::allocator< char const * > > *":
        return _vina.ConstCharVector___getslice__(self, i, j)

    def __setslice__(self, *args) -> "void":
        return _vina.ConstCharVector___setslice__(self, *args)

    def __delslice__(self, i: "std::vector< char const * >::difference_type", j: "std::vector< char const * >::difference_type") -> "void":
        return _vina.ConstCharVector___delslice__(self, i, j)

    def __delitem__(self, *args) -> "void":
        return _vina.ConstCharVector___delitem__(self, *args)

    def __getitem__(self, *args) -> "std::vector< char const * >::value_type":
        return _vina.ConstCharVector___getitem__(self, *args)

    def __setitem__(self, *args) -> "void":
        return _vina.ConstCharVector___setitem__(self, *args)

    def pop(self) -> "std::vector< char const * >::value_type":
        return _vina.ConstCharVector_pop(self)

    def append(self, x: "std::vector< char const * >::value_type") -> "void":
        return _vina.ConstCharVector_append(self, x)

    def empty(self) -> "bool":
        return _vina.ConstCharVector_empty(self)

    def size(self) -> "std::vector< char const * >::size_type":
        return _vina.ConstCharVector_size(self)

    def swap(self, v: "ConstCharVector") -> "void":
        return _vina.ConstCharVector_swap(self, v)

    def begin(self) -> "std::vector< char const * >::iterator":
        return _vina.ConstCharVector_begin(self)

    def end(self) -> "std::vector< char const * >::iterator":
        return _vina.ConstCharVector_end(self)

    def rbegin(self) -> "std::vector< char const * >::reverse_iterator":
        return _vina.ConstCharVector_rbegin(self)

    def rend(self) -> "std::vector< char const * >::reverse_iterator":
        return _vina.ConstCharVector_rend(self)

    def clear(self) -> "void":
        return _vina.ConstCharVector_clear(self)

    def get_allocator(self) -> "std::vector< char const * >::allocator_type":
        return _vina.ConstCharVector_get_allocator(self)

    def pop_back(self) -> "void":
        return _vina.ConstCharVector_pop_back(self)

    def erase(self, *args) -> "std::vector< char const * >::iterator":
        return _vina.ConstCharVector_erase(self, *args)

    def __init__(self, *args):
        _vina.ConstCharVector_swiginit(self, _vina.new_ConstCharVector(*args))

    def push_back(self, x: "std::vector< char const * >::value_type") -> "void":
        return _vina.ConstCharVector_push_back(self, x)

    def front(self) -> "std::vector< char const * >::value_type":
        return _vina.ConstCharVector_front(self)

    def back(self) -> "std::vector< char const * >::value_type":
        return _vina.ConstCharVector_back(self)

    def assign(self, n: "std::vector< char const * >::size_type", x: "std::vector< char const * >::value_type") -> "void":
        return _vina.ConstCharVector_assign(self, n, x)

    def resize(self, *args) -> "void":
        return _vina.ConstCharVector_resize(self, *args)

    def insert(self, *args) -> "void":
        return _vina.ConstCharVector_insert(self, *args)

    def reserve(self, n: "std::vector< char const * >::size_type") -> "void":
        return _vina.ConstCharVector_reserve(self, n)

    def capacity(self) -> "std::vector< char const * >::size_type":
        return _vina.ConstCharVector_capacity(self)
    __swig_destroy__ = _vina.delete_ConstCharVector

# Register ConstCharVector in _vina:
_vina.ConstCharVector_swigregister(ConstCharVector)

class Vina(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, exhaustiveness: "int"=8, cpu: "int"=0, seed: "int"=0, no_cache: "bool"=False, verbosity: "int"=2):
        _vina.Vina_swiginit(self, _vina.new_Vina(exhaustiveness, cpu, seed, no_cache, verbosity))
    __swig_destroy__ = _vina.delete_Vina

    def set_receptor(self, *args) -> "void":
        return _vina.Vina_set_receptor(self, *args)

    def set_ligand(self, *args) -> "void":
        return _vina.Vina_set_ligand(self, *args)

    def set_weights(self, weight_gauss1: "double const"=-0.035579, weight_gauss2: "double const"=-0.005156, weight_repulsion: "double const"=0.840245, weight_hydrophobic: "double const"=-0.035069, weight_hydrogen: "double const"=-0.587439, weight_rot: "double const"=0.05846) -> "void":
        return _vina.Vina_set_weights(self, weight_gauss1, weight_gauss2, weight_repulsion, weight_hydrophobic, weight_hydrogen, weight_rot)

    def set_forcefield(self) -> "void":
        return _vina.Vina_set_forcefield(self)

    def set_box(self, center_x: "double", center_y: "double", center_z: "double", size_x: "int", size_y: "int", size_z: "int", granularity: "double"=0.375) -> "void":
        return _vina.Vina_set_box(self, center_x, center_y, center_z, size_x, size_y, size_z, granularity)

    def compute_vina_grid(self) -> "void":
        return _vina.Vina_compute_vina_grid(self)

    def randomize(self, max_steps: "int const"=10000) -> "void":
        return _vina.Vina_randomize(self, max_steps)

    def score_robust(self) -> "void":
        return _vina.Vina_score_robust(self)

    def score(self) -> "double":
        return _vina.Vina_score(self)

    def optimize(self, max_steps: "int const"=0) -> "void":
        return _vina.Vina_optimize(self, max_steps)

    def global_search(self, n_poses: "int const"=20, min_rmsd: "double const"=1.0) -> "void":
        return _vina.Vina_global_search(self, n_poses, min_rmsd)

    def write_results(self, output_name: "std::string const &", how_many: "int"=9, energy_range: "double"=3.0) -> "void":
        return _vina.Vina_write_results(self, output_name, how_many, energy_range)

    def write_pose(self, *args) -> "void":
        return _vina.Vina_write_pose(self, *args)

    def test(self) -> "int":
        r"""test(Vina self) -> int"""
        return _vina.Vina_test(self)

# Register Vina in _vina:
_vina.Vina_swigregister(Vina)



