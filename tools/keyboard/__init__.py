from .default.admin.keyboard import Keyboard as kbAdminDef
from .inline.admin.keyboard import Keyboard as kbAdmin

from .default.user.keyboard import Keyboard as kbUserDef
from .inline.admin.keyboard import Keyboard as kbUser

__all__ = [
    "kbAdminDef",
    "kbAdmin",
    "kbUserDef",
    "kbUser"
]