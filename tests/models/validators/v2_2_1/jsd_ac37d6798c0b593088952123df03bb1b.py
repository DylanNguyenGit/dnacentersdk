# -*- coding: utf-8 -*-
"""Cisco DNA Center retrieveRFProfiles data model.

Copyright (c) 2019-2021 Cisco Systems.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import fastjsonschema
import json
from dnacentersdk.exceptions import MalformedRequest

from builtins import *


class JSONSchemaValidatorAc37D6798C0B593088952123Df03Bb1B(object):
    """retrieveRFProfiles request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorAc37D6798C0B593088952123Df03Bb1B, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "items": {
                "properties": {
                "aRadioChannels": {
                "type": "string"
                },
                "bRadioChannels": {
                "type": "string"
                },
                "channelWidth": {
                "type": "string"
                },
                "dataRatesA": {
                "type": "string"
                },
                "dataRatesB": {
                "type": "string"
                },
                "defaultRfProfile": {
                "type": "boolean"
                },
                "enableARadioType": {
                "type": "boolean"
                },
                "enableBRadioType": {
                "type": "boolean"
                },
                "enableBrownField": {
                "type": "boolean"
                },
                "enableCustom": {
                "type": "boolean"
                },
                "mandatoryDataRatesA": {
                "type": "string"
                },
                "mandatoryDataRatesB": {
                "type": "string"
                },
                "maxPowerLevelA": {
                "type": "string"
                },
                "maxPowerLevelB": {
                "type": "string"
                },
                "minPowerLevelA": {
                "type": "string"
                },
                "minPowerLevelB": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "parentProfileA": {
                "type": "string"
                },
                "parentProfileB": {
                "type": "string"
                },
                "powerThresholdV1A": {
                "type": "integer"
                },
                "powerThresholdV1B": {
                "type": "integer"
                },
                "rxSopThresholdA": {
                "type": "string"
                },
                "rxSopThresholdB": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                }'''.replace("\n" + ' ' * 16, '')
        ))

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                '{} is invalid. Reason: {}'.format(request, e.message)
            )
