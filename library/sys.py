# encoding: utf-8
# module sys
# from (built-in)
# by generator 1.147
"""
This module provides access to some objects used or maintained by the
interpreter and to functions that interact strongly with the interpreter.

Dynamic objects:

argv -- command line arguments; argv[0] is the script pathname if known
path -- module search path; path[0] is the script directory, else ''
modules -- dictionary of loaded modules

displayhook -- called to show results in an interactive session
excepthook -- called to handle any uncaught exception other than SystemExit
  To customize printing in an interactive session or to install a custom
  top-level exception handler, assign other functions to replace these.

stdin -- standard input file object; used by input()
stdout -- standard output file object; used by print()
stderr -- standard error object; used for error messages
  By assigning other file objects (or objects that behave like files)
  to these, it is possible to redirect all of the interpreter's I/O.

last_exc - the last uncaught exception
  Only available in an interactive session after a
  traceback has been printed.
last_type -- type of last uncaught exception
last_value -- value of last uncaught exception
last_traceback -- traceback of last uncaught exception
  These three are the (deprecated) legacy representation of last_exc.

Static objects:

builtin_module_names -- tuple of module names built into this interpreter
copyright -- copyright notice pertaining to this interpreter
exec_prefix -- prefix used to find the machine-specific Python library
executable -- absolute path of the executable binary of the Python interpreter
float_info -- a named tuple with information about the float implementation.
float_repr_style -- string indicating the style of repr() output for floats
hash_info -- a named tuple with information about the hash algorithm.
hexversion -- version information encoded as a single integer
implementation -- Python implementation information.
int_info -- a named tuple with information about the int implementation.
maxsize -- the largest supported length of containers.
maxunicode -- the value of the largest Unicode code point
platform -- platform identifier
prefix -- prefix used to find the Python library
thread_info -- a named tuple with information about the thread implementation.
version -- the version of this interpreter as a string
version_info -- version information as a named tuple
__stdin__ -- the original stdin; don't touch!
__stdout__ -- the original stdout; don't touch!
__stderr__ -- the original stderr; don't touch!
__displayhook__ -- the original displayhook; don't touch!
__excepthook__ -- the original excepthook; don't touch!

Functions:

displayhook() -- print an object to the screen, and save it in builtins._
excepthook() -- print an exception and its traceback to sys.stderr
exception() -- return the current thread's active exception
exc_info() -- return information about the current thread's active exception
exit() -- exit the interpreter by raising SystemExit
getdlopenflags() -- returns flags to be used for dlopen() calls
getprofile() -- get the global profiling function
getrefcount() -- return the reference count for an object (plus one :-)
getrecursionlimit() -- return the max recursion depth for the interpreter
getsizeof() -- return the size of an object in bytes
gettrace() -- get the global debug tracing function
setdlopenflags() -- set the flags to be used for dlopen() calls
setprofile() -- set the global profiling function
setrecursionlimit() -- set the max recursion depth for the interpreter
settrace() -- set the global debug tracing function
"""

# imports
import sys.monitoring as monitoring # <module 'sys.monitoring'>
from _io import __stderr__, __stdin__, __stdout__, stderr, stdin, stdout


# Variables with simple values

abiflags = ''

api_version = 1013

base_exec_prefix = '/Library/Frameworks/Python.framework/Versions/3.13'

base_prefix = '/Library/Frameworks/Python.framework/Versions/3.13'

byteorder = 'little'

copyright = 'Copyright (c) 2001-2024 Python Software Foundation.\nAll Rights Reserved.\n\nCopyright (c) 2000 BeOpen.com.\nAll Rights Reserved.\n\nCopyright (c) 1995-2001 Corporation for National Research Initiatives.\nAll Rights Reserved.\n\nCopyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.\nAll Rights Reserved.'

dont_write_bytecode = True

executable = '/Users/xabiduluc/Library/Caches/JetBrains/PyCharm2024.2/demo/PyCharmLearningProject/venv/bin/python'

exec_prefix = '/Users/xabiduluc/Library/Caches/JetBrains/PyCharm2024.2/demo/PyCharmLearningProject/venv'

float_repr_style = 'short'

hexversion = 51183856

maxsize = 9223372036854775807
maxunicode = 1114111

platform = 'darwin'
platlibdir = 'lib'

prefix = '/Users/xabiduluc/Library/Caches/JetBrains/PyCharm2024.2/demo/PyCharmLearningProject/venv'

pycache_prefix = None

version = '3.13.0 (v3.13.0:60403a5409f, Oct  7 2024, 00:37:40) [Clang 15.0.0 (clang-1500.3.9.4)]'

_base_executable = '/Library/Frameworks/Python.framework/Versions/3.13/bin/python3.13'

_framework = 'Python'

_home = '/usr/local/bin'

_stdlib_dir = '/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13'

# functions

def activate_stack_trampoline(*args, **kwargs): # real signature unknown
    """ Activate stack profiler trampoline *backend*. """
    pass

def addaudithook(*args, **kwargs): # real signature unknown
    """ Adds a new audit hook callback. """
    pass

def audit(*args, **kwargs): # real signature unknown
    """ Passes the event to any audit hooks that are attached. """
    pass

def breakpointhook(*args, **kwargs): # real signature unknown
    """ This hook function is called by built-in breakpoint(). """
    pass

def call_tracing(*args, **kwargs): # real signature unknown
    """
    Call func(*args), while tracing is enabled.
    
    The tracing state is saved, and restored afterwards.  This is intended
    to be called from a debugger from a checkpoint, to recursively debug
    some other code.
    """
    pass

def deactivate_stack_trampoline(*args, **kwargs): # real signature unknown
    """
    Deactivate the current stack profiler trampoline backend.
    
    If no stack profiler is activated, this function has no effect.
    """
    pass

def displayhook(*args, **kwargs): # real signature unknown
    """ Print an object to sys.stdout and also save it in builtins._ """
    pass

def excepthook(*args, **kwargs): # real signature unknown
    """ Handle an exception by displaying it with a traceback on sys.stderr. """
    pass

def exception(*args, **kwargs): # real signature unknown
    """
    Return the current exception.
    
    Return the most recent exception caught by an except clause
    in the current stack frame or in an older stack frame, or None
    if no such exception exists.
    """
    pass

def exc_info(*args, **kwargs): # real signature unknown
    """
    Return current exception information: (type, value, traceback).
    
    Return information about the most recent exception caught by an except
    clause in the current stack frame or in an older stack frame.
    """
    pass

def exit(*args, **kwargs): # real signature unknown
    """
    Exit the interpreter by raising SystemExit(status).
    
    If the status is omitted or None, it defaults to zero (i.e., success).
    If the status is an integer, it will be used as the system exit status.
    If it is another kind of object, it will be printed and the system
    exit status will be one (i.e., failure).
    """
    pass

def getallocatedblocks(*args, **kwargs): # real signature unknown
    """ Return the number of memory blocks currently allocated. """
    pass

def getdefaultencoding(*args, **kwargs): # real signature unknown
    """ Return the current default encoding used by the Unicode implementation. """
    pass

def getdlopenflags(*args, **kwargs): # real signature unknown
    """
    Return the current value of the flags that are used for dlopen calls.
    
    The flag constants are defined in the os module.
    """
    pass

def getfilesystemencodeerrors(*args, **kwargs): # real signature unknown
    """ Return the error mode used Unicode to OS filename conversion. """
    pass

def getfilesystemencoding(*args, **kwargs): # real signature unknown
    """ Return the encoding used to convert Unicode filenames to OS filenames. """
    pass

def getprofile(*args, **kwargs): # real signature unknown
    """
    Return the profiling function set with sys.setprofile.
    
    See the profiler chapter in the library manual.
    """
    pass

def getrecursionlimit(*args, **kwargs): # real signature unknown
    """
    Return the current value of the recursion limit.
    
    The recursion limit is the maximum depth of the Python interpreter
    stack.  This limit prevents infinite recursion from causing an overflow
    of the C stack and crashing Python.
    """
    pass

def getrefcount(): # real signature unknown; restored from __doc__
    """
    Return the reference count of object.
    
    The count returned is generally one higher than you might expect,
    because it includes the (temporary) reference as an argument to
    getrefcount().
    """
    pass

def getsizeof(p_object, default=None): # real signature unknown; restored from __doc__
    """
    getsizeof(object [, default]) -> int
    
    Return the size of object in bytes.
    """
    return 0

def getswitchinterval(*args, **kwargs): # real signature unknown
    """ Return the current thread switch interval; see sys.setswitchinterval(). """
    pass

def gettrace(*args, **kwargs): # real signature unknown
    """
    Return the global debug tracing function set with sys.settrace.
    
    See the debugger chapter in the library manual.
    """
    pass

def getunicodeinternedsize(*args, **kwargs): # real signature unknown
    """ Return the number of elements of the unicode interned dictionary """
    pass

def get_asyncgen_hooks(*args, **kwargs): # real signature unknown
    """
    Return the installed asynchronous generators hooks.
    
    This returns a namedtuple of the form (firstiter, finalizer).
    """
    pass

def get_coroutine_origin_tracking_depth(*args, **kwargs): # real signature unknown
    """ Check status of origin tracking for coroutine objects in this thread. """
    pass

def get_int_max_str_digits(*args, **kwargs): # real signature unknown
    """ Return the maximum string digits limit for non-binary int<->str conversions. """
    pass

def intern(*args, **kwargs): # real signature unknown
    """
    ``Intern'' the given string.
    
    This enters the string in the (global) table of interned strings whose
    purpose is to speed up dictionary lookups. Return the string itself or
    the previously interned string object with the same value.
    """
    pass

def is_finalizing(*args, **kwargs): # real signature unknown
    """ Return True if Python is exiting. """
    pass

def is_stack_trampoline_active(*args, **kwargs): # real signature unknown
    """ Return *True* if a stack profiler trampoline is active. """
    pass

def setdlopenflags(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Set the flags used by the interpreter for dlopen calls.
    
    This is used, for example, when the interpreter loads extension
    modules. Among other things, this will enable a lazy resolving of
    symbols when importing a module, if called as sys.setdlopenflags(0).
    To share symbols across extension modules, call as
    sys.setdlopenflags(os.RTLD_GLOBAL).  Symbolic names for the flag
    modules can be found in the os module (RTLD_xxx constants, e.g.
    os.RTLD_LAZY).
    """
    pass

def setprofile(*args, **kwargs): # real signature unknown
    """
    Set the profiling function.
    
    It will be called on each function call and return.  See the profiler
    chapter in the library manual.
    """
    pass

def setrecursionlimit(*args, **kwargs): # real signature unknown
    """
    Set the maximum depth of the Python interpreter stack to n.
    
    This limit prevents infinite recursion from causing an overflow of the C
    stack and crashing Python.  The highest possible limit is platform-
    dependent.
    """
    pass

def setswitchinterval(*args, **kwargs): # real signature unknown
    """
    Set the ideal thread switching delay inside the Python interpreter.
    
    The actual frequency of switching threads can be lower if the
    interpreter executes long sequences of uninterruptible code
    (this is implementation-specific and workload-dependent).
    
    The parameter must represent the desired switching delay in seconds
    A typical value is 0.005 (5 milliseconds).
    """
    pass

def settrace(*args, **kwargs): # real signature unknown
    """
    Set the global debug tracing function.
    
    It will be called on each function call.  See the debugger chapter
    in the library manual.
    """
    pass

def set_asyncgen_hooks(firstiter=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    set_asyncgen_hooks([firstiter] [, finalizer])
    
    Set a finalizer for async generators objects.
    """
    pass

def set_coroutine_origin_tracking_depth(*args, **kwargs): # real signature unknown
    """
    Enable or disable origin tracking for coroutine objects in this thread.
    
    Coroutine objects will track 'depth' frames of traceback information
    about where they came from, available in their cr_origin attribute.
    
    Set a depth of 0 to disable.
    """
    pass

def set_int_max_str_digits(*args, **kwargs): # real signature unknown
    """ Set the maximum string digits limit for non-binary int<->str conversions. """
    pass

def unraisablehook(*args, **kwargs): # real signature unknown
    """
    Handle an unraisable exception.
    
    The unraisable argument has the following attributes:
    
    * exc_type: Exception type.
    * exc_value: Exception value, can be None.
    * exc_traceback: Exception traceback, can be None.
    * err_msg: Error message, can be None.
    * object: Object causing the exception, can be None.
    """
    pass

def _baserepl(*args, **kwargs): # real signature unknown
    """ Private function for getting the base REPL """
    pass

def _clear_internal_caches(*args, **kwargs): # real signature unknown
    """ Clear all internal performance-related caches. """
    pass

def _clear_type_cache(*args, **kwargs): # real signature unknown
    """ Clear the internal type lookup cache. """
    pass

def _current_exceptions(*args, **kwargs): # real signature unknown
    """
    Return a dict mapping each thread's identifier to its current raised exception.
    
    This function should be used for specialized purposes only.
    """
    pass

def _current_frames(*args, **kwargs): # real signature unknown
    """
    Return a dict mapping each thread's thread id to its current stack frame.
    
    This function should be used for specialized purposes only.
    """
    pass

def _debugmallocstats(*args, **kwargs): # real signature unknown
    """
    Print summary info to stderr about the state of pymalloc's structures.
    
    In Py_DEBUG mode, also perform some expensive internal consistency
    checks.
    """
    pass

def _getframe(*args, **kwargs): # real signature unknown
    """
    Return a frame object from the call stack.
    
    If optional integer depth is given, return the frame object that many
    calls below the top of the stack.  If that is deeper than the call
    stack, ValueError is raised.  The default for depth is zero, returning
    the frame at the top of the call stack.
    
    This function should be used for internal and specialized purposes
    only.
    """
    pass

def _getframemodulename(*args, **kwargs): # real signature unknown
    """
    Return the name of the module for a calling frame.
    
    The default depth returns the module containing the call to this API.
    A more typical use in a library will pass a depth of 1 to get the user's
    module rather than the library module.
    
    If no frame, module, or name can be found, returns None.
    """
    pass

def _get_cpu_count_config(*args, **kwargs): # real signature unknown
    """ Private function for getting PyConfig.cpu_count """
    pass

def _is_gil_enabled(*args, **kwargs): # real signature unknown
    """ Return True if the GIL is currently enabled and False otherwise. """
    pass

def _is_interned(*args, **kwargs): # real signature unknown
    """ Return True if the given string is "interned". """
    pass

def _setprofileallthreads(*args, **kwargs): # real signature unknown
    """
    Set the profiling function in all running threads belonging to the current interpreter.
    
    It will be called on each function call and return.  See the profiler
    chapter in the library manual.
    """
    pass

def _settraceallthreads(*args, **kwargs): # real signature unknown
    """
    Set the global debug tracing function in all running threads belonging to the current interpreter.
    
    It will be called on each function call. See the debugger chapter
    in the library manual.
    """
    pass

def __breakpointhook__(*args, **kwargs): # real signature unknown
    """ This hook function is called by built-in breakpoint(). """
    pass

def __displayhook__(*args, **kwargs): # real signature unknown
    """ Print an object to sys.stdout and also save it in builtins._ """
    pass

def __excepthook__(*args, **kwargs): # real signature unknown
    """ Handle an exception by displaying it with a traceback on sys.stderr. """
    pass

def __interactivehook__(): # reliably restored by inspect
    """
    Configure readline completion on interactive prompts.
    
    If the readline module can be imported, the hook will set the Tab key
    as completion key and register ~/.python_history as history file.
    This can be overridden in the sitecustomize or usercustomize module,
    or in a PYTHONSTARTUP file.
    """
    pass

def __unraisablehook__(*args, **kwargs): # real signature unknown
    """
    Handle an unraisable exception.
    
    The unraisable argument has the following attributes:
    
    * exc_type: Exception type.
    * exc_value: Exception value, can be None.
    * exc_traceback: Exception traceback, can be None.
    * err_msg: Error message, can be None.
    * object: Object causing the exception, can be None.
    """
    pass

# classes

class __loader__(object):
    """
    Meta path import for built-in modules.
    
    All methods are either class or static methods to avoid the need to
    instantiate the class.
    """
    def create_module(spec): # reliably restored by inspect
        """ Create a built-in module """
        pass

    def exec_module(module): # reliably restored by inspect
        """ Exec a built-in module """
        pass

    @classmethod
    def find_spec(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def get_code(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have code objects. """
        pass

    @classmethod
    def get_source(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have source code. """
        pass

    @classmethod
    def is_package(cls, *args, **kwargs): # real signature unknown
        """ Return False as built-in modules are never packages. """
        pass

    @classmethod
    def load_module(cls, *args, **kwargs): # real signature unknown
        """
        Load the specified module into sys.modules and return it.
        
        This method is deprecated.  Use loader.exec_module() instead.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    _ORIGIN = 'built-in'
    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__firstlineno__': 971, '__doc__': 'Meta path import for built-in modules.\\n\\nAll methods are either class or static methods to avoid the need to\\ninstantiate the class.\\n\\n', '_ORIGIN': 'built-in', 'find_spec': <classmethod(<function BuiltinImporter.find_spec at 0x100ae7380>)>, 'create_module': <staticmethod(<function BuiltinImporter.create_module at 0x100ae7420>)>, 'exec_module': <staticmethod(<function BuiltinImporter.exec_module at 0x100ae74c0>)>, 'get_code': <classmethod(<function BuiltinImporter.get_code at 0x100ae7600>)>, 'get_source': <classmethod(<function BuiltinImporter.get_source at 0x100ae7740>)>, 'is_package': <classmethod(<function BuiltinImporter.is_package at 0x100ae7880>)>, 'load_module': <classmethod(<function _load_module_shim at 0x100ae6700>)>, '__static_attributes__': (), '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"
    __firstlineno__ = 971
    __static_attributes__ = ()


# variables with complex values

argv = [] # real value of type <class 'list'> skipped

builtin_module_names = () # real value of type <class 'tuple'> skipped

flags = (
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    False,
    0,
    0,
    False,
    4300,
)

float_info = (
    1.7976931348623157e+308,
    1024,
    308,
    2.2250738585072014e-308,
    -1021,
    -307,
    15,
    53,
    2.220446049250313e-16,
    2,
    1,
)

hash_info = (
    64,
    2305843009213693951,
    314159,
    0,
    1000003,
    'siphash13',
    64,
    128,
    0,
)

implementation = None # (!) real value is "namespace(name='cpython', cache_tag='cpython-313', version=sys.version_info(major=3, minor=13, micro=0, releaselevel='final', serial=0), hexversion=51183856, _multiarch='darwin')"

int_info = (
    30,
    4,
    4300,
    640,
)

meta_path = [
    None, # (!) real value is '<_virtualenv._Finder object at 0x100abaf90>'
    __loader__,
    None, # (!) real value is "<class '_frozen_importlib.FrozenImporter'>"
    None, # (!) real value is "<class '_frozen_importlib_external.PathFinder'>"
    None, # (!) real value is '<six._SixMetaPathImporter object at 0x101107380>'
]

modules = {} # real value of type <class 'dict'> skipped

orig_argv = [
    '/Library/Frameworks/Python.framework/Versions/3.13/Resources/Python.app/Contents/MacOS/Python',
    '-B',
    '-c',
    'from multiprocessing.spawn import spawn_main; spawn_main(tracker_fd=6, pipe_handle=8)',
    '--multiprocessing-fork',
]

path = [
    '/Applications/PyCharm.app/Contents/plugins/python-ce/helpers',
    '/Applications/PyCharm.app/Contents/plugins/python-ce/helpers/generator3',
    '/Applications/PyCharm.app/Contents/plugins/python-ce/helpers',
    '/Library/Frameworks/Python.framework/Versions/3.13/lib/python313.zip',
    '/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13',
    '/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/lib-dynload',
    '/Users/xabiduluc/Library/Caches/JetBrains/PyCharm2024.2/demo/PyCharmLearningProject/venv/lib/python3.13/site-packages',
]

path_hooks = [
    None, # (!) real value is "<class 'zipimport.zipimporter'>"
    None, # (!) real value is '<function FileFinder.path_hook.<locals>.path_hook_for_FileFinder at 0x100b549a0>'
]

path_importer_cache = {} # real value of type <class 'dict'> skipped

stdlib_module_names = None # (!) real value is "frozenset({'hmac', '_lsprof', '_py_abc', '_sqlite3', 'sre_compile', 'pathlib', 'operator', 'datetime', '__future__', 'sched', '_pyio', 'tarfile', '_uuid', 'tkinter', 'multiprocessing', 'sre_parse', '_sha2', 'antigravity', 'ensurepip', 'platform', 'shlex', '_collections', 'cmath', 'trace', '_heapq', '_operator', '_sysconfig', 'posixpath', 'glob', 'syslog', 'colorsys', 'fractions', 'urllib', 'getopt', '_pyrepl', 'fcntl', 'gzip', '_imp', '_threading_local', 'subprocess', '_suggestions', '_codecs_kr', '_frozen_importlib_external', 'weakref', '_symtable', '_queue', 'tomllib', 'codeop', 'ast', '_tkinter', 'pyclbr', 'hashlib', 'pyexpat', 'mimetypes', 'queue', 'shelve', 'sysconfig', 'html', 'sys', '_csv', '_curses', 'resource', 'readline', 'pickletools', 'string', 'inspect', 'zlib', 'functools', '_strptime', 'importlib', 'encodings', 'termios', 'pydoc_data', '_signal', '_codecs_hk', 'fnmatch', 'pty', '_colorize', '_android_support', '_codecs_jp', '_blake2', '_warnings', 'ipaddress', 'keyword', '_interpqueues', 'decimal', 'gc', '_json', '_bz2', '_string', '_pickle', '_winapi', 're', 'code', 'select', 'tabnanny', 'uuid', '_collections_abc', '_statistics', 'winreg', 'xml', 'dbm', 'collections', 'cProfile', '_pydecimal', 'profile', 'socket', 'genericpath', 'http', '_codecs_tw', 'marshal', 'reprlib', 'array', 'bisect', 'codecs', 'faulthandler', 'sqlite3', 'modulefinder', 'turtledemo', 'lzma', 'builtins', 'linecache', 'time', '_asyncio', 'site', 'getpass', 'numbers', '_opcode', 'secrets', 'concurrent', '_contextvars', 'os', 'tracemalloc', 'filecmp', '_ctypes', 'math', 'token', 'atexit', 'turtle', '_elementtree', '_codecs', 'enum', '_sha3', 'zoneinfo', 'cmd', 'zipfile', 'struct', '_thread', 'io', 'errno', '_posixshmem', 'curses', '_tracemalloc', '_md5', '_lzma', 'pkgutil', 'winsound', '_socket', 'bdb', '_abc', 'bz2', 'py_compile', 'opcode', '_sitebuiltins', '_sre', '_tokenize', '_scproxy', '_wmi', 'types', 'netrc', 'tokenize', 'configparser', 'posix', 'mmap', '_markupbase', 'asyncio', 'msvcrt', 'plistlib', '_pydatetime', 'selectors', '_datetime', 'copy', 'symtable', 'nturl2path', 'compileall', 'pydoc', 'nt', '_posixsubprocess', 'grp', '_ios_support', 'zipimport', '_io', 'runpy', 'socketserver', '_frozen_importlib', 'unittest', 'binascii', '_decimal', 'shutil', 'logging', 'threading', '_dbm', 'statistics', 'difflib', 'timeit', 'stat', 'wave', 'webbrowser', 'typing', 'doctest', '_locale', '_osx_support', 'unicodedata', 'dataclasses', '_random', '_hashlib', '_struct', 'pprint', 'pwd', '_ssl', 'ftplib', 'idlelib', 'dis', 'wsgiref', '_stat', 'zipapp', 'calendar', 'argparse', 'pdb', 'tty', 'optparse', 'quopri', 'ssl', 'copyreg', 'warnings', '_codecs_iso2022', 'random', '_aix_support', '_typing', 'abc', 'mailbox', 'locale', 'gettext', 'poplib', 'traceback', '_functools', '_zoneinfo', 'ctypes', 'tempfile', '_curses_panel', '_pylong', 'stringprep', '_sha1', 'contextvars', '_multiprocessing', '_weakref', 'csv', '_overlapped', 'fileinput', 'signal', '_multibytecodec', 'this', 'textwrap', 'base64', 'email', '_weakrefset', 'json', 'xmlrpc', 'ntpath', 'pstats', 'graphlib', 'pickle', 'smtplib', '_ast', 'contextlib', '_interpreters', '_compat_pickle', '_gdbm', '_compression', 'itertools', 'heapq', 'sre_constants', 'imaplib', '_bisect', 'rlcompleter', 'venv', '_codecs_cn', '_interpchannels', '_opcode_metadata'})"

thread_info = (
    'pthread',
    'mutex+cond',
    None,
)

version_info = (
    3,
    13,
    0,
    'final',
    0,
)

warnoptions = []

_git = (
    'CPython',
    'v3.13.0',
    '60403a5409f',
)

_xoptions = {}

__spec__ = None # (!) real value is "ModuleSpec(name='sys', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

# intermittent names
exc_value = Exception()
exc_traceback=None
