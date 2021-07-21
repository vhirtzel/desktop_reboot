# SPDX-License-Identifier: BSD-3-Clause
#
# Copyright 2020 Raritan Inc. All rights reserved.
#
# This is an auto-generated file.

#
# Section generated by IdlC from "ServerMonitor.idl"
#

import raritan.rpc
from raritan.rpc import Interface, Structure, ValueObject, Enumeration, typecheck, DecodeException
import raritan.rpc.event

import raritan.rpc.idl

import raritan.rpc.servermon


# interface
class ServerMonitor(Interface):
    idlType = "servermon.ServerMonitor:2.0.1"

    # enumeration
    class ServerReachability(Enumeration):
        idlType = "servermon.ServerMonitor_2_0_1.ServerReachability:1.0.0"
        values = ["WAITING", "REACHABLE", "UNREACHABLE", "ERROR"]

    ServerReachability.WAITING = ServerReachability(0)
    ServerReachability.REACHABLE = ServerReachability(1)
    ServerReachability.UNREACHABLE = ServerReachability(2)
    ServerReachability.ERROR = ServerReachability(3)

    # enumeration
    class ServerPowerState(Enumeration):
        idlType = "servermon.ServerMonitor_2_0_1.ServerPowerState:1.0.0"
        values = ["UNKNOWN", "ON", "OFF", "SHUTTING_DOWN"]

    ServerPowerState.UNKNOWN = ServerPowerState(0)
    ServerPowerState.ON = ServerPowerState(1)
    ServerPowerState.OFF = ServerPowerState(2)
    ServerPowerState.SHUTTING_DOWN = ServerPowerState(3)

    # enumeration
    class ServerPowerControlResult(Enumeration):
        idlType = "servermon.ServerMonitor_2_0_1.ServerPowerControlResult:1.0.0"
        values = ["NO_ERROR", "SHUTDOWN_CMD_FAILED", "SWITCHING_OFF_FAILED", "SWITCHING_ON_FAILED", "POWER_CHECK_TIMEOUT"]

    ServerPowerControlResult.NO_ERROR = ServerPowerControlResult(0)
    ServerPowerControlResult.SHUTDOWN_CMD_FAILED = ServerPowerControlResult(1)
    ServerPowerControlResult.SWITCHING_OFF_FAILED = ServerPowerControlResult(2)
    ServerPowerControlResult.SWITCHING_ON_FAILED = ServerPowerControlResult(3)
    ServerPowerControlResult.POWER_CHECK_TIMEOUT = ServerPowerControlResult(4)

    # enumeration
    class ServerPowerCheckMethod(Enumeration):
        idlType = "servermon.ServerMonitor_2_0_1.ServerPowerCheckMethod:1.0.0"
        values = ["TIMER", "POWER_DROP"]

    ServerPowerCheckMethod.TIMER = ServerPowerCheckMethod(0)
    ServerPowerCheckMethod.POWER_DROP = ServerPowerCheckMethod(1)

    # structure
    class ServerPowerSettings(Structure):
        idlType = "servermon.ServerMonitor_2_0_1.ServerPowerSettings:1.0.0"
        elements = ["enabled", "target", "powerCheck", "powerThreshold", "timeout", "shutdownCmd", "username", "password", "sshPort"]

        def __init__(self, enabled, target, powerCheck, powerThreshold, timeout, shutdownCmd, username, password, sshPort):
            typecheck.is_bool(enabled, AssertionError)
            typecheck.is_remote_obj(target, AssertionError)
            typecheck.is_enum(powerCheck, raritan.rpc.servermon.ServerMonitor.ServerPowerCheckMethod, AssertionError)
            typecheck.is_double(powerThreshold, AssertionError)
            typecheck.is_int(timeout, AssertionError)
            typecheck.is_string(shutdownCmd, AssertionError)
            typecheck.is_string(username, AssertionError)
            typecheck.is_string(password, AssertionError)
            typecheck.is_int(sshPort, AssertionError)

            self.enabled = enabled
            self.target = target
            self.powerCheck = powerCheck
            self.powerThreshold = powerThreshold
            self.timeout = timeout
            self.shutdownCmd = shutdownCmd
            self.username = username
            self.password = password
            self.sshPort = sshPort

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                enabled = json['enabled'],
                target = Interface.decode(json['target'], agent),
                powerCheck = raritan.rpc.servermon.ServerMonitor.ServerPowerCheckMethod.decode(json['powerCheck']),
                powerThreshold = json['powerThreshold'],
                timeout = json['timeout'],
                shutdownCmd = json['shutdownCmd'],
                username = json['username'],
                password = json['password'],
                sshPort = json['sshPort'],
            )
            return obj

        def encode(self):
            json = {}
            json['enabled'] = self.enabled
            json['target'] = Interface.encode(self.target)
            json['powerCheck'] = raritan.rpc.servermon.ServerMonitor.ServerPowerCheckMethod.encode(self.powerCheck)
            json['powerThreshold'] = self.powerThreshold
            json['timeout'] = self.timeout
            json['shutdownCmd'] = self.shutdownCmd
            json['username'] = self.username
            json['password'] = self.password
            json['sshPort'] = self.sshPort
            return json

    # structure
    class ServerSettings(Structure):
        idlType = "servermon.ServerMonitor_2_0_1.ServerSettings:1.0.0"
        elements = ["host", "enabled", "pingInterval", "retryInterval", "activationCount", "failureCount", "resumeDelay", "resumeCount", "powerSettings"]

        def __init__(self, host, enabled, pingInterval, retryInterval, activationCount, failureCount, resumeDelay, resumeCount, powerSettings):
            typecheck.is_string(host, AssertionError)
            typecheck.is_bool(enabled, AssertionError)
            typecheck.is_int(pingInterval, AssertionError)
            typecheck.is_int(retryInterval, AssertionError)
            typecheck.is_int(activationCount, AssertionError)
            typecheck.is_int(failureCount, AssertionError)
            typecheck.is_int(resumeDelay, AssertionError)
            typecheck.is_int(resumeCount, AssertionError)
            typecheck.is_struct(powerSettings, raritan.rpc.servermon.ServerMonitor.ServerPowerSettings, AssertionError)

            self.host = host
            self.enabled = enabled
            self.pingInterval = pingInterval
            self.retryInterval = retryInterval
            self.activationCount = activationCount
            self.failureCount = failureCount
            self.resumeDelay = resumeDelay
            self.resumeCount = resumeCount
            self.powerSettings = powerSettings

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                host = json['host'],
                enabled = json['enabled'],
                pingInterval = json['pingInterval'],
                retryInterval = json['retryInterval'],
                activationCount = json['activationCount'],
                failureCount = json['failureCount'],
                resumeDelay = json['resumeDelay'],
                resumeCount = json['resumeCount'],
                powerSettings = raritan.rpc.servermon.ServerMonitor.ServerPowerSettings.decode(json['powerSettings'], agent),
            )
            return obj

        def encode(self):
            json = {}
            json['host'] = self.host
            json['enabled'] = self.enabled
            json['pingInterval'] = self.pingInterval
            json['retryInterval'] = self.retryInterval
            json['activationCount'] = self.activationCount
            json['failureCount'] = self.failureCount
            json['resumeDelay'] = self.resumeDelay
            json['resumeCount'] = self.resumeCount
            json['powerSettings'] = raritan.rpc.servermon.ServerMonitor.ServerPowerSettings.encode(self.powerSettings)
            return json

    # structure
    class ServerStatus(Structure):
        idlType = "servermon.ServerMonitor_2_0_1.ServerStatus:1.0.0"
        elements = ["powerState", "lastPowerControlResult", "reachable", "lastRequest", "lastResponse", "requests", "responses", "failures", "resumes"]

        def __init__(self, powerState, lastPowerControlResult, reachable, lastRequest, lastResponse, requests, responses, failures, resumes):
            typecheck.is_enum(powerState, raritan.rpc.servermon.ServerMonitor.ServerPowerState, AssertionError)
            typecheck.is_enum(lastPowerControlResult, raritan.rpc.servermon.ServerMonitor.ServerPowerControlResult, AssertionError)
            typecheck.is_enum(reachable, raritan.rpc.servermon.ServerMonitor.ServerReachability, AssertionError)
            typecheck.is_time(lastRequest, AssertionError)
            typecheck.is_time(lastResponse, AssertionError)
            typecheck.is_int(requests, AssertionError)
            typecheck.is_int(responses, AssertionError)
            typecheck.is_int(failures, AssertionError)
            typecheck.is_int(resumes, AssertionError)

            self.powerState = powerState
            self.lastPowerControlResult = lastPowerControlResult
            self.reachable = reachable
            self.lastRequest = lastRequest
            self.lastResponse = lastResponse
            self.requests = requests
            self.responses = responses
            self.failures = failures
            self.resumes = resumes

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                powerState = raritan.rpc.servermon.ServerMonitor.ServerPowerState.decode(json['powerState']),
                lastPowerControlResult = raritan.rpc.servermon.ServerMonitor.ServerPowerControlResult.decode(json['lastPowerControlResult']),
                reachable = raritan.rpc.servermon.ServerMonitor.ServerReachability.decode(json['reachable']),
                lastRequest = raritan.rpc.Time.decode(json['lastRequest']),
                lastResponse = raritan.rpc.Time.decode(json['lastResponse']),
                requests = json['requests'],
                responses = json['responses'],
                failures = json['failures'],
                resumes = json['resumes'],
            )
            return obj

        def encode(self):
            json = {}
            json['powerState'] = raritan.rpc.servermon.ServerMonitor.ServerPowerState.encode(self.powerState)
            json['lastPowerControlResult'] = raritan.rpc.servermon.ServerMonitor.ServerPowerControlResult.encode(self.lastPowerControlResult)
            json['reachable'] = raritan.rpc.servermon.ServerMonitor.ServerReachability.encode(self.reachable)
            json['lastRequest'] = raritan.rpc.Time.encode(self.lastRequest)
            json['lastResponse'] = raritan.rpc.Time.encode(self.lastResponse)
            json['requests'] = self.requests
            json['responses'] = self.responses
            json['failures'] = self.failures
            json['resumes'] = self.resumes
            return json

    # value object
    class ServerPowerStateEvent(raritan.rpc.idl.Event):
        idlType = "servermon.ServerMonitor_2_0_1.ServerPowerStateEvent:1.0.0"

        def __init__(self, id, host, oldPowerState, newPowerState, source):
            super(raritan.rpc.servermon.ServerMonitor.ServerPowerStateEvent, self).__init__(source)
            typecheck.is_int(id, AssertionError)
            typecheck.is_string(host, AssertionError)
            typecheck.is_enum(oldPowerState, raritan.rpc.servermon.ServerMonitor.ServerPowerState, AssertionError)
            typecheck.is_enum(newPowerState, raritan.rpc.servermon.ServerMonitor.ServerPowerState, AssertionError)

            self.id = id
            self.host = host
            self.oldPowerState = oldPowerState
            self.newPowerState = newPowerState

        def encode(self):
            json = super(raritan.rpc.servermon.ServerMonitor.ServerPowerStateEvent, self).encode()
            json['id'] = self.id
            json['host'] = self.host
            json['oldPowerState'] = raritan.rpc.servermon.ServerMonitor.ServerPowerState.encode(self.oldPowerState)
            json['newPowerState'] = raritan.rpc.servermon.ServerMonitor.ServerPowerState.encode(self.newPowerState)
            return json

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                id = json['id'],
                host = json['host'],
                oldPowerState = raritan.rpc.servermon.ServerMonitor.ServerPowerState.decode(json['oldPowerState']),
                newPowerState = raritan.rpc.servermon.ServerMonitor.ServerPowerState.decode(json['newPowerState']),
                # for idl.Event
                source = Interface.decode(json['source'], agent),
            )
            return obj

        def listElements(self):
            elements = ["id", "host", "oldPowerState", "newPowerState"]
            elements = elements + super(raritan.rpc.servermon.ServerMonitor.ServerPowerStateEvent, self).listElements()
            return elements

    # value object
    class ServerPowerControlInitiatedEvent(raritan.rpc.event.UserEvent):
        idlType = "servermon.ServerMonitor_2_0_1.ServerPowerControlInitiatedEvent:1.0.0"

        def __init__(self, id, host, on, actUserName, actIpAddr, source):
            super(raritan.rpc.servermon.ServerMonitor.ServerPowerControlInitiatedEvent, self).__init__(actUserName, actIpAddr, source)
            typecheck.is_int(id, AssertionError)
            typecheck.is_string(host, AssertionError)
            typecheck.is_bool(on, AssertionError)

            self.id = id
            self.host = host
            self.on = on

        def encode(self):
            json = super(raritan.rpc.servermon.ServerMonitor.ServerPowerControlInitiatedEvent, self).encode()
            json['id'] = self.id
            json['host'] = self.host
            json['on'] = self.on
            return json

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                id = json['id'],
                host = json['host'],
                on = json['on'],
                # for event.UserEvent
                actUserName = json['actUserName'],
                actIpAddr = json['actIpAddr'],
                # for idl.Event
                source = Interface.decode(json['source'], agent),
            )
            return obj

        def listElements(self):
            elements = ["id", "host", "on"]
            elements = elements + super(raritan.rpc.servermon.ServerMonitor.ServerPowerControlInitiatedEvent, self).listElements()
            return elements

    # value object
    class ServerPowerControlCompletedEvent(raritan.rpc.idl.Event):
        idlType = "servermon.ServerMonitor_2_0_1.ServerPowerControlCompletedEvent:1.0.0"

        def __init__(self, id, host, result, source):
            super(raritan.rpc.servermon.ServerMonitor.ServerPowerControlCompletedEvent, self).__init__(source)
            typecheck.is_int(id, AssertionError)
            typecheck.is_string(host, AssertionError)
            typecheck.is_enum(result, raritan.rpc.servermon.ServerMonitor.ServerPowerControlResult, AssertionError)

            self.id = id
            self.host = host
            self.result = result

        def encode(self):
            json = super(raritan.rpc.servermon.ServerMonitor.ServerPowerControlCompletedEvent, self).encode()
            json['id'] = self.id
            json['host'] = self.host
            json['result'] = raritan.rpc.servermon.ServerMonitor.ServerPowerControlResult.encode(self.result)
            return json

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                id = json['id'],
                host = json['host'],
                result = raritan.rpc.servermon.ServerMonitor.ServerPowerControlResult.decode(json['result']),
                # for idl.Event
                source = Interface.decode(json['source'], agent),
            )
            return obj

        def listElements(self):
            elements = ["id", "host", "result"]
            elements = elements + super(raritan.rpc.servermon.ServerMonitor.ServerPowerControlCompletedEvent, self).listElements()
            return elements

    # value object
    class ServerReachabilityEvent(raritan.rpc.idl.Event):
        idlType = "servermon.ServerMonitor_2_0_1.ServerReachabilityEvent:1.0.0"

        def __init__(self, id, host, reachable, source):
            super(raritan.rpc.servermon.ServerMonitor.ServerReachabilityEvent, self).__init__(source)
            typecheck.is_int(id, AssertionError)
            typecheck.is_string(host, AssertionError)
            typecheck.is_enum(reachable, raritan.rpc.servermon.ServerMonitor.ServerReachability, AssertionError)

            self.id = id
            self.host = host
            self.reachable = reachable

        def encode(self):
            json = super(raritan.rpc.servermon.ServerMonitor.ServerReachabilityEvent, self).encode()
            json['id'] = self.id
            json['host'] = self.host
            json['reachable'] = raritan.rpc.servermon.ServerMonitor.ServerReachability.encode(self.reachable)
            return json

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                id = json['id'],
                host = json['host'],
                reachable = raritan.rpc.servermon.ServerMonitor.ServerReachability.decode(json['reachable']),
                # for idl.Event
                source = Interface.decode(json['source'], agent),
            )
            return obj

        def listElements(self):
            elements = ["id", "host", "reachable"]
            elements = elements + super(raritan.rpc.servermon.ServerMonitor.ServerReachabilityEvent, self).listElements()
            return elements

    # value object
    class ServerAddedEvent(raritan.rpc.event.UserEvent):
        idlType = "servermon.ServerMonitor_2_0_1.ServerAddedEvent:1.0.0"

        def __init__(self, id, settings, actUserName, actIpAddr, source):
            super(raritan.rpc.servermon.ServerMonitor.ServerAddedEvent, self).__init__(actUserName, actIpAddr, source)
            typecheck.is_int(id, AssertionError)
            typecheck.is_struct(settings, raritan.rpc.servermon.ServerMonitor.ServerSettings, AssertionError)

            self.id = id
            self.settings = settings

        def encode(self):
            json = super(raritan.rpc.servermon.ServerMonitor.ServerAddedEvent, self).encode()
            json['id'] = self.id
            json['settings'] = raritan.rpc.servermon.ServerMonitor.ServerSettings.encode(self.settings)
            return json

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                id = json['id'],
                settings = raritan.rpc.servermon.ServerMonitor.ServerSettings.decode(json['settings'], agent),
                # for event.UserEvent
                actUserName = json['actUserName'],
                actIpAddr = json['actIpAddr'],
                # for idl.Event
                source = Interface.decode(json['source'], agent),
            )
            return obj

        def listElements(self):
            elements = ["id", "settings"]
            elements = elements + super(raritan.rpc.servermon.ServerMonitor.ServerAddedEvent, self).listElements()
            return elements

    # value object
    class ServerSettingsChangedEvent(raritan.rpc.event.UserEvent):
        idlType = "servermon.ServerMonitor_2_0_1.ServerSettingsChangedEvent:1.0.0"

        def __init__(self, id, oldSettings, newSettings, actUserName, actIpAddr, source):
            super(raritan.rpc.servermon.ServerMonitor.ServerSettingsChangedEvent, self).__init__(actUserName, actIpAddr, source)
            typecheck.is_int(id, AssertionError)
            typecheck.is_struct(oldSettings, raritan.rpc.servermon.ServerMonitor.ServerSettings, AssertionError)
            typecheck.is_struct(newSettings, raritan.rpc.servermon.ServerMonitor.ServerSettings, AssertionError)

            self.id = id
            self.oldSettings = oldSettings
            self.newSettings = newSettings

        def encode(self):
            json = super(raritan.rpc.servermon.ServerMonitor.ServerSettingsChangedEvent, self).encode()
            json['id'] = self.id
            json['oldSettings'] = raritan.rpc.servermon.ServerMonitor.ServerSettings.encode(self.oldSettings)
            json['newSettings'] = raritan.rpc.servermon.ServerMonitor.ServerSettings.encode(self.newSettings)
            return json

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                id = json['id'],
                oldSettings = raritan.rpc.servermon.ServerMonitor.ServerSettings.decode(json['oldSettings'], agent),
                newSettings = raritan.rpc.servermon.ServerMonitor.ServerSettings.decode(json['newSettings'], agent),
                # for event.UserEvent
                actUserName = json['actUserName'],
                actIpAddr = json['actIpAddr'],
                # for idl.Event
                source = Interface.decode(json['source'], agent),
            )
            return obj

        def listElements(self):
            elements = ["id", "oldSettings", "newSettings"]
            elements = elements + super(raritan.rpc.servermon.ServerMonitor.ServerSettingsChangedEvent, self).listElements()
            return elements

    # value object
    class ServerDeletedEvent(raritan.rpc.event.UserEvent):
        idlType = "servermon.ServerMonitor_2_0_1.ServerDeletedEvent:1.0.0"

        def __init__(self, id, actUserName, actIpAddr, source):
            super(raritan.rpc.servermon.ServerMonitor.ServerDeletedEvent, self).__init__(actUserName, actIpAddr, source)
            typecheck.is_int(id, AssertionError)

            self.id = id

        def encode(self):
            json = super(raritan.rpc.servermon.ServerMonitor.ServerDeletedEvent, self).encode()
            json['id'] = self.id
            return json

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                id = json['id'],
                # for event.UserEvent
                actUserName = json['actUserName'],
                actIpAddr = json['actIpAddr'],
                # for idl.Event
                source = Interface.decode(json['source'], agent),
            )
            return obj

        def listElements(self):
            elements = ["id"]
            elements = elements + super(raritan.rpc.servermon.ServerMonitor.ServerDeletedEvent, self).listElements()
            return elements

    # structure
    class Server(Structure):
        idlType = "servermon.ServerMonitor_2_0_1.Server:1.0.0"
        elements = ["settings", "status"]

        def __init__(self, settings, status):
            typecheck.is_struct(settings, raritan.rpc.servermon.ServerMonitor.ServerSettings, AssertionError)
            typecheck.is_struct(status, raritan.rpc.servermon.ServerMonitor.ServerStatus, AssertionError)

            self.settings = settings
            self.status = status

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                settings = raritan.rpc.servermon.ServerMonitor.ServerSettings.decode(json['settings'], agent),
                status = raritan.rpc.servermon.ServerMonitor.ServerStatus.decode(json['status'], agent),
            )
            return obj

        def encode(self):
            json = {}
            json['settings'] = raritan.rpc.servermon.ServerMonitor.ServerSettings.encode(self.settings)
            json['status'] = raritan.rpc.servermon.ServerMonitor.ServerStatus.encode(self.status)
            return json

    ERR_NO_SUCH_ID = 1

    ERR_INVALID_SETTINGS = 2

    ERR_DUPLICATE_HOSTNAME = 3

    ERR_MAX_SERVERS_REACHED = 4

    class _addServer(Interface.Method):
        name = 'addServer'

        @staticmethod
        def encode(settings):
            typecheck.is_struct(settings, raritan.rpc.servermon.ServerMonitor.ServerSettings, AssertionError)
            args = {}
            args['settings'] = raritan.rpc.servermon.ServerMonitor.ServerSettings.encode(settings)
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            id = rsp['id']
            typecheck.is_int(_ret_, DecodeException)
            typecheck.is_int(id, DecodeException)
            return (_ret_, id)

    class _modifyServer(Interface.Method):
        name = 'modifyServer'

        @staticmethod
        def encode(id, settings):
            typecheck.is_int(id, AssertionError)
            typecheck.is_struct(settings, raritan.rpc.servermon.ServerMonitor.ServerSettings, AssertionError)
            args = {}
            args['id'] = id
            args['settings'] = raritan.rpc.servermon.ServerMonitor.ServerSettings.encode(settings)
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            typecheck.is_int(_ret_, DecodeException)
            return _ret_

    class _deleteServer(Interface.Method):
        name = 'deleteServer'

        @staticmethod
        def encode(id):
            typecheck.is_int(id, AssertionError)
            args = {}
            args['id'] = id
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            typecheck.is_int(_ret_, DecodeException)
            return _ret_

    class _getServer(Interface.Method):
        name = 'getServer'

        @staticmethod
        def encode(id):
            typecheck.is_int(id, AssertionError)
            args = {}
            args['id'] = id
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            server = raritan.rpc.servermon.ServerMonitor.Server.decode(rsp['server'], agent)
            typecheck.is_int(_ret_, DecodeException)
            typecheck.is_struct(server, raritan.rpc.servermon.ServerMonitor.Server, DecodeException)
            return (_ret_, server)

    class _listServers(Interface.Method):
        name = 'listServers'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = dict([(
                elem['key'],
                raritan.rpc.servermon.ServerMonitor.Server.decode(elem['value'], agent))
                for elem in rsp['_ret_']])
            return _ret_

    class _powerControl(Interface.Method):
        name = 'powerControl'

        @staticmethod
        def encode(id, on):
            typecheck.is_int(id, AssertionError)
            typecheck.is_bool(on, AssertionError)
            args = {}
            args['id'] = id
            args['on'] = on
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            typecheck.is_int(_ret_, DecodeException)
            return _ret_
    def __init__(self, target, agent):
        super(ServerMonitor, self).__init__(target, agent)
        self.addServer = ServerMonitor._addServer(self)
        self.modifyServer = ServerMonitor._modifyServer(self)
        self.deleteServer = ServerMonitor._deleteServer(self)
        self.getServer = ServerMonitor._getServer(self)
        self.listServers = ServerMonitor._listServers(self)
        self.powerControl = ServerMonitor._powerControl(self)