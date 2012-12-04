#
# otopi -- plugable installer
# Copyright (C) 2012 Red Hat, Inc.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#


"""Constants."""


from . import util


@util.export
@util.codegen
class Types(object):
    NONE = 'none'
    BOOLEAN = 'bool'
    INTEGER = 'int'
    STRING = 'str'
    MULTI_STRING = 'multi-str'
    OBJECT = 'object'


@util.export
@util.codegen
class Const(object):
    ENVIRONMENT_APPEND_PREFIX = 'APPEND:'
    LOGGER_BASE = 'otopi'
    LOG_FILE_PREFIX = 'otopi'
    DEFAULT_CONFIG_FILE = '/etc/otopi.conf'
    DEFAULT_COMMAND_SEARCH_PATH = ":".join(
        (
            '/usr/local/sbin',
            '/usr/local/bin',
            '/usr/sbin',
            '/usr/bin',
            '/sbin',
            '/bin',
        )
    )
    CONFIG_SECTION_DEFAULT = 'environment:default'
    CONFIG_SECTION_INIT = 'environment:init'
    CONFIG_SECTION_OVERRIDES = 'environment:override'
    DIALOG_DIALECT_MACHINE = 'machine'
    DIALOG_DIALECT_HUMAN = 'human'
    PACKAGER_KEEP_ALIVE_INTERVAL = 30


@util.export
@util.codegen
class SystemEnvironment(object):
    DEBUG = 'OTOPI_DEBUG'
    LOG_FILE = 'OTOPI_LOGFILE'
    LOG_DIR = 'OTOPI_LOGDIR'
    CONFIG = 'OTOPI_CONFIG'


@util.export
@util.codegen
class BaseEnv(object):
    ERROR = 'BASE/error'
    ABORTED = 'BASE/aborted'
    EXCEPTION_INFO = 'BASE/exceptionInfo'
    LOG = 'BASE/log'
    PLUGIN_PATH = 'BASE/pluginPath'
    PLUGIN_GROUPS = 'BASE/pluginGroups'
    DEBUG = 'BASE/debug'
    COMMAND_PREFIX = 'COMMAND/'


@util.export
@util.codegen
class CoreEnv(object):
    PACKAGE_NAME = 'INFO/PACKAGE_NAME'
    PACKAGE_VERSION = 'INFO/PACKAGE_VERSION'
    INTERNAL_PACKAGES_TRANSACTION = 'CORE/internalPackageTransaction'
    MAIN_TRANSACTION = 'CORE/mainTransaction'
    MODIFIED_FILES = 'CORE/modifiedFiles'
    LOG_FILE_NAME_PREFIX = 'CORE/logFileNamePrefix'
    LOG_DIR = 'CORE/logDir'
    LOG_FILE_NAME = 'CORE/logFileName'
    LOG_FILTER = 'CORE/logFilter'
    LOG_FILE_HANDLE = 'CORE/logFileHandle'
    LOG_REMOVE_AT_EXIT = 'CORE/logRemoveAtExit'
    CONFIG_FILE_NAME = 'CORE/configFileName'


@util.export
@util.codegen
class DialogEnv(object):
    DIALECT = 'DIALOG/dialect'
    CUSTOMIZATION = 'DIALOG/customization'
    BOUNDARY = 'DIALOG/boundary'
    CLI_VERSION = 'DIALOG/cliVersion'


@util.export
@util.codegen
class SysEnv(object):
    CLOCK_MAX_GAP = 'SYSTEM/clockMaxGap'
    CLOCK_SET = 'SYSTEM/clockSet'
    REBOOT = 'SYSTEM/reboot'
    REBOOT_ALLOW = 'SYSTEM/rebootAllow'
    REBOOT_DEFER_TIME = 'SYSTEM/rebootDeferTime'
    COMMAND_PATH = 'SYSTEM/commandPath'


@util.export
@util.codegen
class NetEnv(object):
    SSH_ENABLE = 'NETWORK/sshEnable'
    SSH_KEY = 'NETWORK/sshKey'
    SSH_USER = 'NETWORK/sshUser'
    IPTABLES_ENABLE = 'NETWORK/iptablesEnable'
    IPTABLES_RULES = 'NETWORK/iptablesRules'


@util.export
@util.codegen
class PackEnv(object):
    YUMPACKAGER_ENABLED = 'PACKAGER/yumpackagerEnabled'
    KEEP_ALIVE_INTERVAL = 'PACKAGER/keepAliveInterval'


@util.export
@util.codegen
class Queries(object):
    CUSTOMIZATION_COMMAND = 'CUSTOMIZATION_COMMAND'
    TERMINATION_COMMAND = 'TERMINATION_COMMAND'
    TIME = 'TIME'


@util.export
@util.codegen
class Confirms(object):
    GPG_KEY = 'GPG_KEY'