U
    ��_�  �                   @   s\   d Z ddlZddlmZmZ ze W n ek
r<   eZY nX dd� Ze	dkrXe
e� � dS )z<
This module contains various helper functions for git DVCS
�    N�   )�exec_command�exec_command_rcc               	   C   s  t j} | �| �| �t j�t��ddd��}t j�|�}| �|�s~z$ddlm	} |�
d�sbd| W S W n tk
rx   Y nX dS z|tdd	d
d|d� tddddd|d��� }|�d�r�|�dd�\}}}}|d }n|�dd�\}}}|dkr�W dS d| W S  ttfk
�r   Y nX dS )Nz..z.git�   )�rev�$�+� �gitzupdate-indexz-qz	--refresh)�cwdZdescribez--longz--dirtyz--tagz-dirty�-�   z.modr   �0)�os�path�normpath�join�dirname�abspath�__file__�existsZ_gitrevisionr   �
startswith�ImportErrorr   r   �strip�endswith�rsplit�FileNotFoundError�WindowsError)r   Zgitdirr   r   Zrecent�tagZchangesZdirty� r   �?/storage/emulated/0/python/pyinstaller/PyInstaller/utils/git.py�get_repo_revision   s4    $

�



r!   �__main__)�__doc__r   �compatr   r   r   �	NameErrorr   r!   �__name__�printr   r   r   r    �<module>   s   
!