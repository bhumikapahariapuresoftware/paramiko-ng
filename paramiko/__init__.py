# Copyright (C) 2003-2011  Robey Pointer <robeypointer@gmail.com>
# Copyright (C) 2013-2019  Jeff Forcier <jeff@bitprophet.org>
# Copyright (C) 2019-2020  Pierce Lopez <pierce.lopez@gmail.com>
#
# This file is part of paramiko.
#
# Paramiko is free software; you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation; either version 2.1 of the License, or (at your option)
# any later version.
#
# Paramiko is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Paramiko; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA.

from paramiko.transport import SecurityOptions, Transport
from paramiko.client import (
    SSHClient, MissingHostKeyPolicy, AutoAddPolicy, RejectPolicy,
    WarningPolicy,
)
from paramiko.auth_handler import AuthHandler
from paramiko.ssh_gss import GSSAuth, GSS_AUTH_AVAILABLE, GSS_EXCEPTIONS
from paramiko.channel import Channel, ChannelFile, ChannelStderrFile, ChannelStdinFile
from paramiko.ssh_exception import (
    SSHException, PasswordRequiredException, BadAuthenticationType,
    ChannelException, BadHostKeyException, AuthenticationException,
    ProxyCommandFailure,
)
from paramiko.server import ServerInterface, SubsystemHandler, InteractiveQuery
from paramiko.rsakey import RSAKey
from paramiko.dsskey import DSSKey
from paramiko.ecdsakey import ECDSAKey
from paramiko.ed25519key import Ed25519Key
from paramiko.sftp import SFTPError
from paramiko.sftp_client import SFTP, SFTPClient
from paramiko.sftp_server import SFTPServer
from paramiko.sftp_attr import SFTPAttributes
from paramiko.sftp_handle import SFTPHandle
from paramiko.sftp_si import SFTPServerInterface
from paramiko.sftp_file import SFTPFile
from paramiko.message import Message
from paramiko.packet import Packetizer
from paramiko.file import BufferedFile
from paramiko.agent import Agent, AgentKey
from paramiko.pkey import (
    PKey,
    PublicBlob,
    load_private_key,
    load_private_key_file,
)
from paramiko.hostkeys import HostKeys
from paramiko.config import SSHConfig
from paramiko.proxy import ProxyCommand
from paramiko.common import io_sleep
from paramiko.common import (
    AUTH_SUCCESSFUL, AUTH_PARTIALLY_SUCCESSFUL, AUTH_FAILED, OPEN_SUCCEEDED,
    OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED, OPEN_FAILED_CONNECT_FAILED,
    OPEN_FAILED_UNKNOWN_CHANNEL_TYPE, OPEN_FAILED_RESOURCE_SHORTAGE,
)
from paramiko.sftp import (
    SFTP_OK, SFTP_EOF, SFTP_NO_SUCH_FILE, SFTP_PERMISSION_DENIED, SFTP_FAILURE,
    SFTP_BAD_MESSAGE, SFTP_NO_CONNECTION, SFTP_CONNECTION_LOST,
    SFTP_OP_UNSUPPORTED,
)
from paramiko._version import __version__, __version_info__  # noqa: F401


__author__ = "various"
__license__ = "GNU Lesser General Public License (LGPL)"
__pkgname__ = "paramiko-ng"

__all__ = [
    'Transport',
    'SSHClient',
    'MissingHostKeyPolicy',
    'AutoAddPolicy',
    'RejectPolicy',
    'WarningPolicy',
    'SecurityOptions',
    'AuthHandler',
    'Channel',
    'ChannelFile',
    'ChannelStderrFile',
    'ChannelStdinFile',
    'PKey',
    'RSAKey',
    'DSSKey',
    'ECDSAKey',
    'Ed25519Key',
    'PublicBlob',
    'load_private_key',
    'load_private_key_file',
    'Message',
    'Packetizer',
    'SSHException',
    'AuthenticationException',
    'PasswordRequiredException',
    'BadAuthenticationType',
    'ChannelException',
    'BadHostKeyException',
    'ProxyCommand',
    'ProxyCommandFailure',
    'GSSAuth',
    'GSS_AUTH_AVAILABLE',
    'GSS_EXCEPTIONS',
    'AUTH_SUCCESSFUL',
    'AUTH_PARTIALLY_SUCCESSFUL',
    'AUTH_FAILED',
    'OPEN_SUCCEEDED',
    'OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED',
    'OPEN_FAILED_CONNECT_FAILED',
    'OPEN_FAILED_UNKNOWN_CHANNEL_TYPE',
    'OPEN_FAILED_RESOURCE_SHORTAGE',
    'SFTP',
    'SFTPFile',
    'SFTPHandle',
    'SFTPClient',
    'SFTPServer',
    'SFTPError',
    'SFTPAttributes',
    'SFTPServerInterface',
    'SFTP_OK',
    'SFTP_EOF',
    'SFTP_NO_SUCH_FILE',
    'SFTP_PERMISSION_DENIED',
    'SFTP_FAILURE',
    'SFTP_BAD_MESSAGE',
    'SFTP_NO_CONNECTION',
    'SFTP_CONNECTION_LOST',
    'SFTP_OP_UNSUPPORTED',
    'ServerInterface',
    'SubsystemHandler',
    'InteractiveQuery',
    'BufferedFile',
    'Agent',
    'AgentKey',
    'HostKeys',
    'SSHConfig',
    'io_sleep',
]
