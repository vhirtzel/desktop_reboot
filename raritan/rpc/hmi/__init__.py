# SPDX-License-Identifier: BSD-3-Clause
#
# Copyright 2020 Raritan Inc. All rights reserved.
#
# This is an auto-generated file.

#
# Section generated by IdlC from "ExternalBeeper.idl"
#

import raritan.rpc
from raritan.rpc import Interface, Structure, ValueObject, Enumeration, typecheck, DecodeException
import raritan.rpc.hmi

import raritan.rpc.idl


# interface
class ExternalBeeper(Interface):
    idlType = "hmi.ExternalBeeper:1.0.1"

    # enumeration
    class State(Enumeration):
        idlType = "hmi.ExternalBeeper_1_0_1.State:1.0.0"
        values = ["OFF", "ON", "ALARMING"]

    State.OFF = State(0)
    State.ON = State(1)
    State.ALARMING = State(2)

    # value object
    class StateChangedEvent(raritan.rpc.idl.Event):
        idlType = "hmi.ExternalBeeper_1_0_1.StateChangedEvent:1.0.0"

        def __init__(self, oldState, newState, source):
            super(raritan.rpc.hmi.ExternalBeeper.StateChangedEvent, self).__init__(source)
            typecheck.is_enum(oldState, raritan.rpc.hmi.ExternalBeeper.State, AssertionError)
            typecheck.is_enum(newState, raritan.rpc.hmi.ExternalBeeper.State, AssertionError)

            self.oldState = oldState
            self.newState = newState

        def encode(self):
            json = super(raritan.rpc.hmi.ExternalBeeper.StateChangedEvent, self).encode()
            json['oldState'] = raritan.rpc.hmi.ExternalBeeper.State.encode(self.oldState)
            json['newState'] = raritan.rpc.hmi.ExternalBeeper.State.encode(self.newState)
            return json

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                oldState = raritan.rpc.hmi.ExternalBeeper.State.decode(json['oldState']),
                newState = raritan.rpc.hmi.ExternalBeeper.State.decode(json['newState']),
                # for idl.Event
                source = Interface.decode(json['source'], agent),
            )
            return obj

        def listElements(self):
            elements = ["oldState", "newState"]
            elements = elements + super(raritan.rpc.hmi.ExternalBeeper.StateChangedEvent, self).listElements()
            return elements

    class _getState(Interface.Method):
        name = 'getState'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = raritan.rpc.hmi.ExternalBeeper.State.decode(rsp['_ret_'])
            typecheck.is_enum(_ret_, raritan.rpc.hmi.ExternalBeeper.State, DecodeException)
            return _ret_

    class _alarm(Interface.Method):
        name = 'alarm'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            return None

    class _on(Interface.Method):
        name = 'on'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            return None

    class _off(Interface.Method):
        name = 'off'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            return None
    def __init__(self, target, agent):
        super(ExternalBeeper, self).__init__(target, agent)
        self.getState = ExternalBeeper._getState(self)
        self.alarm = ExternalBeeper._alarm(self)
        self.on = ExternalBeeper._on(self)
        self.off = ExternalBeeper._off(self)

#
# Section generated by IdlC from "InternalBeeper.idl"
#

import raritan.rpc
from raritan.rpc import Interface, Structure, ValueObject, Enumeration, typecheck, DecodeException
import raritan.rpc.event

import raritan.rpc.hmi

import raritan.rpc.idl


# interface
class InternalBeeper(Interface):
    idlType = "hmi.InternalBeeper:2.0.1"

    # enumeration
    class State(Enumeration):
        idlType = "hmi.InternalBeeper_2_0_1.State:1.0.0"
        values = ["OFF", "ON_NOTIFICATION", "ON_ACTIVATION"]

    State.OFF = State(0)
    State.ON_NOTIFICATION = State(1)
    State.ON_ACTIVATION = State(2)

    # value object
    class MuteChangedEvent(raritan.rpc.event.UserEvent):
        idlType = "hmi.InternalBeeper_2_0_1.MuteChangedEvent:1.0.0"

        def __init__(self, muted, actUserName, actIpAddr, source):
            super(raritan.rpc.hmi.InternalBeeper.MuteChangedEvent, self).__init__(actUserName, actIpAddr, source)
            typecheck.is_bool(muted, AssertionError)

            self.muted = muted

        def encode(self):
            json = super(raritan.rpc.hmi.InternalBeeper.MuteChangedEvent, self).encode()
            json['muted'] = self.muted
            return json

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                muted = json['muted'],
                # for event.UserEvent
                actUserName = json['actUserName'],
                actIpAddr = json['actIpAddr'],
                # for idl.Event
                source = Interface.decode(json['source'], agent),
            )
            return obj

        def listElements(self):
            elements = ["muted"]
            elements = elements + super(raritan.rpc.hmi.InternalBeeper.MuteChangedEvent, self).listElements()
            return elements

    # value object
    class StateChangedEvent(raritan.rpc.idl.Event):
        idlType = "hmi.InternalBeeper_2_0_1.StateChangedEvent:1.0.0"

        def __init__(self, state, reason, mutedTemporarily, source):
            super(raritan.rpc.hmi.InternalBeeper.StateChangedEvent, self).__init__(source)
            typecheck.is_enum(state, raritan.rpc.hmi.InternalBeeper.State, AssertionError)
            typecheck.is_string(reason, AssertionError)
            typecheck.is_bool(mutedTemporarily, AssertionError)

            self.state = state
            self.reason = reason
            self.mutedTemporarily = mutedTemporarily

        def encode(self):
            json = super(raritan.rpc.hmi.InternalBeeper.StateChangedEvent, self).encode()
            json['state'] = raritan.rpc.hmi.InternalBeeper.State.encode(self.state)
            json['reason'] = self.reason
            json['mutedTemporarily'] = self.mutedTemporarily
            return json

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                state = raritan.rpc.hmi.InternalBeeper.State.decode(json['state']),
                reason = json['reason'],
                mutedTemporarily = json['mutedTemporarily'],
                # for idl.Event
                source = Interface.decode(json['source'], agent),
            )
            return obj

        def listElements(self):
            elements = ["state", "reason", "mutedTemporarily"]
            elements = elements + super(raritan.rpc.hmi.InternalBeeper.StateChangedEvent, self).listElements()
            return elements

    class _mute(Interface.Method):
        name = 'mute'

        @staticmethod
        def encode(muted):
            typecheck.is_bool(muted, AssertionError)
            args = {}
            args['muted'] = muted
            return args

        @staticmethod
        def decode(rsp, agent):
            return None

    class _isMuted(Interface.Method):
        name = 'isMuted'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            typecheck.is_bool(_ret_, DecodeException)
            return _ret_

    class _activate(Interface.Method):
        name = 'activate'

        @staticmethod
        def encode(on, reason, timeout):
            typecheck.is_bool(on, AssertionError)
            typecheck.is_string(reason, AssertionError)
            typecheck.is_int(timeout, AssertionError)
            args = {}
            args['on'] = on
            args['reason'] = reason
            args['timeout'] = timeout
            return args

        @staticmethod
        def decode(rsp, agent):
            return None

    class _getState(Interface.Method):
        name = 'getState'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = raritan.rpc.hmi.InternalBeeper.State.decode(rsp['_ret_'])
            reason = rsp['reason']
            mutedTemporarily = rsp['mutedTemporarily']
            typecheck.is_enum(_ret_, raritan.rpc.hmi.InternalBeeper.State, DecodeException)
            typecheck.is_string(reason, DecodeException)
            typecheck.is_bool(mutedTemporarily, DecodeException)
            return (_ret_, reason, mutedTemporarily)

    class _muteCurrentActivation(Interface.Method):
        name = 'muteCurrentActivation'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            return None
    def __init__(self, target, agent):
        super(InternalBeeper, self).__init__(target, agent)
        self.mute = InternalBeeper._mute(self)
        self.isMuted = InternalBeeper._isMuted(self)
        self.activate = InternalBeeper._activate(self)
        self.getState = InternalBeeper._getState(self)
        self.muteCurrentActivation = InternalBeeper._muteCurrentActivation(self)