U
    ��_�D  �                   @   s   d Z ddlZddlZddlZddlZddlZddlZddlZddlZddl	m
Z
 ddlmZmZ ddlmZ ddlmZmZmZmZmZmZmZ dd	lmZ dd
lmZ zddlmZ W n ek
r�   Y nX e�e �Z!dd� Z"dd� Z#dd� Z$dd� Z%dd� Z&da'dd� Z(dd� Z)dd� Z*dS )z?
Utility functions related to analyzing/bundling dependencies.
�    N�   )�ExecCommandFailed)�util�modulegraph)�compat)�	is_darwin�is_unix�
is_freebsd�
is_openbsd�is_py37�BYTECODE_MAGIC�PY3_BASE_MODULES�   )�include_library)�log)�source_hashc                 C   s   d� dd� tD ��}d� dd� tD ��}|d | }t�|�}�z�tj�| �rXt�| � t�	d� t
j| dd���P}d|_	t|�� �}|jd	d
� d� |D �] }t|�tjtjfkr�|�|j�r�t�|j�}	t|	j�}
|	jd@ }t|�tjk�r|j�dd�d }n|j�dd�d }t�� ��}|�t� t�rv|�t �!dd�� t"|jd��}|�#� }W 5 Q R X t$|�}|�|� n|�t �!d|
|�� t%�&|j'|� t
�(|�}|�)||�*� � W 5 Q R X q�W 5 Q R X W n0 t+k
�r� } zt�,d� � W 5 d}~X Y nX dS )z�
    Package basic Python modules into .zip file. The .zip file with basic
    modules is necessary to have on PYTHONPATH for initializing libpython3
    in order to run the frozen executable with Python 3.
    �|c                 S   s   g | ]}d | �qS )z(^%s$)� ��.0�xr   r   �B/storage/emulated/0/python/pyinstaller/PyInstaller/depend/utils.py�
<listcomp>8   s     z+create_py3_base_library.<locals>.<listcomp>c                 S   s   g | ]}d | �qS )z
(^%s\..*$)r   r   r   r   r   r   9   s     z'Adding python files to base_library.zip�w)�mode�   c                 S   s   | j S �N)�
identifier)�itemr   r   r   �<lambda>G   �    z)create_py3_base_library.<locals>.<lambda>)�keyl   �� �.�/z/__init__.pycz.pycz<Ir   �rbz<IIz&base_library.zip could not be created!N)-�joinr   �re�compile�os�path�exists�remove�logger�debug�zipfile�ZipFile�listZflatten�sort�typer   �SourceModule�Package�matchr   �stat�filename�int�st_mtime�st_size�replace�io�BytesIO�writer   r   �struct�pack�open�read�importlib_source_hash�marshal�dump�code�ZipInfo�writestr�getvalue�	Exception�error)�libzip_filename�graphZregex_modulesZregex_submodZ	regex_strZmodule_filter�zfZgraph_nodes�mod�st�	timestamp�size�new_nameZfc�fs�source_bytesr   �info�er   r   r   �create_py3_base_library.   sP    






��


*
rX   c                 C   s�   g }t | |� t|�}t|�D ]X}|s2|�|� q|tj�|�krz
| j}W n   d}Y nX t�	d||� |�|� qt
|�}|S )NZUNKNOWNzUIgnoring %s imported from %s - ctypes imports are only supported using bare filenames)�)__recursivly_scan_code_objects_for_ctypes�setr0   r+   r(   r)   �basename�co_filenamer,   �warning�_resolveCtypesImports)�co�binaries�binaryr7   r   r   r   �scan_code_for_ctypess   s$    


 �rb   c                 C   s   |� tt�| ��� d S r   )�extend�"__scan_code_instruction_for_ctypesr   Ziterate_instructions)r_   r`   r   r   r   rY   �   s
    ��rY   c                 #   s$  � fdd�}z�t � �}d}d}|r,|j|kr0W q|j}|dkrZt � �}|j|krTW q|j}|dkrl|� V  n�|dkr�t � �}|j|kr�|jdkr�|� V  q�|jd	 V  nV|jd
kr�|dkr�t � �}|j|kr�|jdkr�|� }|r�tj�|�}|r�tj�|�V  W q t	k
�r   Y �q Y qX qdS )z�
    Detects ctypes dependencies, using reasonable heuristics that
    should cover most common ctypes usages; returns a tuple of two
    lists, one containing names of binaries detected as
    dependencies, the other containing warnings.
    c                     s*   t � �} | jdkr&| j}t|t�r&|S dS )zuExtracts library name from an expected LOAD_CONST instruction and
        appends it to local binaries list.
        �
LOAD_CONSTN)�next�opname�argval�
isinstance�str)�instructionZsoname��instructionsr   r   �_libFromConst�   s
    

z9__scan_code_instruction_for_ctypes.<locals>._libFromConst)�LOAD_GLOBAL�	LOAD_NAME)�	LOAD_ATTR�LOAD_METHOD�ctypes)�CDLLZWinDLLZOleDLL�PyDLL)�cdll�windllZoledll�pydll�LoadLibraryz.dllrq   )r   �find_libraryN)
rf   rg   rh   rs   r   rz   r(   r)   r[   �StopIteration)rm   rn   rk   Zexpected_opsZload_method�name�libname�libr   rl   r   rd   �   s@    





	

rd   c           	         sD  ddl m} ddlm�  tr"d�ntr,d�nd�� �fdd	�}�fd
d�}g }|� }| D ]�}|tj�|�d �}tr�|dkr�|}t	�
�d��tj�D ],}tj�tj�||��r�tj�||�} q�q�tdkr�t�  |tkr�t| }tj�|�s�t�nd}|dk�rt|��sqXt�d|� qXt|��s&qX|�||df� qX||� |S )a  
    Completes ctypes BINARY entries for modules with their full path.

    Input is a list of c-binary-names (as found by
    `scan_code_instruction_for_ctypes`). Output is a list of tuples
    ready to be appended to the ``binaries`` of a modules.

    This function temporarily extents PATH, LD_LIBRARY_PATH or
    DYLD_LIBRARY_PATH (depending on the plattform) by CONF['pathex']
    so shared libs will be search there, too.

    Example:
    >>> _resolveCtypesImports(['libgs.so'])
    [(libgs.so', ''/usr/lib/libgs.so', 'BINARY')]

    r   )rz   r   )�CONF�LD_LIBRARY_PATH�DYLD_LIBRARY_PATH�PATHc                     sB   t j�� d �} t���}|d k	r2t j�| |f�} t��| � |S )N�pathex)r(   �pathsepr%   r   �getenv�setenv)r)   �old�r   �envvarr   r   �	_setPaths  s    
z(_resolveCtypesImports.<locals>._setPathsc                    s$   | d krt �� � nt �� | � d S r   )r   �unsetenvr�   )r�   )r�   r   r   �_restorePaths!  s    z,_resolveCtypesImports.<locals>._restorePathsN� z(library %s required via ctypes not found�BINARY)�ctypes.utilrz   �configr   r   r   r(   r)   �splitextr   r�   �splitr�   �isfiler%   �LDCONFIG_CACHE�load_ldconfig_cache�AssertionErrorr   r,   r]   �append)	Z	cbinariesrz   r�   r�   �retr�   ZcbinZcpath�dr   r�   r   r^   �   sF    


r^   c                  C   sV  t dk	rdS ddlm}  | d�}|dkrB| dd�}|dkrBi a dS tsJtr^d}d}t�d�}nd	}d
}t�d�}zt�||�}W n$ t	k
r�   t
�d� i a Y dS X |�� �� |d� }i a |D ]�}|�|�}|�� d }ts�t�r6tj�|��dd
�d }	d|�d
� }
|
�|	��st�|	d |
t|	�d�  }
n
|�d
�}
|
t kr�|t |
< q�dS )z�
    Create a cache of the `ldconfig`-output to call it only once.
    It contains thousands of libraries and running it on every dylib
    is expensive.
    Nr   )�find_executable�ldconfigz"/usr/sbin:/sbin:/usr/bin:/usr/sbinz-rr   z^\s+\d+:-l(\S+)(\s.*)? => (\S+)z-pr   z^\s+(\S+)(\s.*)? => (\S+)z/Failed to execute ldconfig. Disabling LD cache.�����z.sor~   )r�   Zdistutils.spawnr�   r	   r
   r&   r'   r   �exec_commandr   r,   r]   �strip�
splitlinesr5   �groupsr(   r)   r[   r�   �group�
startswithr�   �len)r�   r�   Zldconfig_argZsplitlines_count�pattern�text�line�mr)   Zbnamer|   r   r   r   r�   V  sJ    �	




r�   c                 C   sZ   d}| rV| |krVt j�| �d �� dkrDt j�| �s@t j�| �rD| S | }t j�| �} qdS )z�
    Return the path to the python egg file, if the path points to a
    file inside a (or to an egg directly).
    Return `None` otherwise.
    Nr   z.egg)r(   r)   r�   �lowerr�   �isdir�dirname)r)   Zlastpathr   r   r   �get_path_to_egg�  s    r�   c                 C   s   t | �dk	S )za
    Check if path points to a file inside a python egg file (or to an egg
       directly).
    N)r�   )r)   r   r   r   �is_path_to_egg�  s    r�   )+�__doc__rs   r�   r<   rD   r(   r&   r?   r.   �
exceptionsr   Zlib.modulegraphr   r   r�   r   r   r   r	   r
   r   r   r   �dylibr   r   �loggingZimportlib.utilr   rC   �ImportError�	getLogger�__name__r,   rX   rb   rY   rd   r^   r�   r�   r�   r�   r   r   r   r   �<module>   s8   $
E"	`VO