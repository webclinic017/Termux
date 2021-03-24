U
    ��_�  �                   @   s�   d dl Z d dlZd dlZd dlZd dlZd dlZd dlZze W n ek
rX   e	ZY nX ddl
mZmZmZmZ ddd�Zdd� Zdd	� Ze�d
�Zejd  dkr�dZndZdd� Zdd� ZdS )�    N�   )�StringIO�BytesIO�get_instructions�
_READ_MODEc                 C   sj   | � d�}|dk	r.t|ttf�r.tj�|�g}|D ]2} t�| |�}|d dk	rZ|d �	�  |d g}q2|S )z;
    same as imp.find_module, but handles dotted names
    �.Nr   r   )
�split�
isinstance�str�unicode�os�path�realpath�imp�find_module�close)�namer   �names�result� r   �J/storage/emulated/0/python/pyinstaller/PyInstaller/lib/modulegraph/util.py�imp_find_module   s    
r   c                 C   s�   zt j| }W nZ tk
rh   t jD ],}z||�}W  qVW q$ tk
rN   Y q$X q$d }t j�||� Y nX |d kr�zt�| |g�W S  tk
r�   Y d S X |�| �S )N)�sys�path_importer_cache�KeyError�
path_hooks�ImportError�
setdefaultr   r   )r   �	path_item�importer�	path_hookr   r   r   �_check_importer_for_path!   s"    

r!   c                 c   sl  t �dt� | tjkr2| ddddtjfffV  dS tj}d}| �d�D �]}|D ]�}t	||�}t
|d��r"|j�d�s�|j�d�r�t|�|��}||jdttjff}nt|j�d�s�|j�d	�r�|�|�}tt�� d
 t�|� �}||jddtjff}n"d|jtj�|j�d dtjff} �q:qPt|t�rP �q:qP �qZ||fV  tj�||�g}qFdS td| f ��dS )zr
    yields namepart, tuple_or_importer for each path item

    raise ImportError if a name can not be found.
    z,imp_walk will be removed in a future versionN� r   �load_modulez.pyz.pywz.pycz.pyos       �rb�����zNo module named %s)�warnings�warn�DeprecationWarningr   �builtin_module_namesr   Z	C_BUILTINr   r   r!   �hasattr�endswithr   �
get_sourcer   �	PY_SOURCE�get_coder   Z	get_magic�marshal�dumps�PY_COMPILEDr   �splitext�C_EXTENSIONr	   �tuple�joinr   )r   �paths�resZnamepartr   �fp�cor   r   r   �imp_walk7   sJ    �


���


r:   s   coding[:=]\s*([-\w.]+)�   �asciizutf-8c                 C   s@   t d�D ]2}| �� }t�|�}|d k	r|�d��d�  S qtS )Nr;   r   r<   )�range�readline�	cookie_re�search�group�decode�default_encoding)r8   �i�ln�mr   r   r   �guess_encodings   s    
rG   c                 c   sH   t | �D ]
}|V  qdV  | jD ]"}t�|�r t|�D ]
}|V  q6q dS )z�Delivers the byte-code instructions as a continuous stream.

    Yields `dis.Instruction`. After each code-block (`co_code`), `None` is
    yielded to mark the end of the block and to interrupt the steam.
    N)r   �	co_consts�inspect�iscode�iterate_instructions)�code_object�instructionZconstantr   r   r   rK      s    

rK   )N)r   r   r   �rer/   r&   rI   r   �	NameErrorr
   �_compatr   r   r   r   r   r!   r:   �compiler?   �version_inforC   rG   rK   r   r   r   r   �<module>   s(   

5
