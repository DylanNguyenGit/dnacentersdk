# -*- coding: utf-8 -*-
"""Test suite for the community-developed Python SDK for the DNA Center APIs.

Copyright (c) 2019 Cisco and/or its affiliates.

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

import dnacentersdk


class TestDNACenterSDK:
    """Test the package-level code."""

    def test_package_contents(self):
        """Ensure the package contains the correct top-level objects."""
        # DNA Center API Wrapper
        assert hasattr(dnacentersdk, "DNACenterAPI")

        # Exceptions
        assert hasattr(dnacentersdk, "ApiError")
        assert hasattr(dnacentersdk, "AccessTokenError")
        assert hasattr(dnacentersdk, "RateLimitError")
        assert hasattr(dnacentersdk, "RateLimitWarning")
        assert hasattr(dnacentersdk, "dnacentersdkException")

        # Data Models
        assert hasattr(dnacentersdk, "mydict_data_factory")
        assert hasattr(dnacentersdk, "json_schema_validate")
        assert hasattr(dnacentersdk, "JSONSchemaValidator01B09A254B9AB259")
        assert hasattr(dnacentersdk, "JSONSchemaValidator00AeC9B1422AB27E")
        assert hasattr(dnacentersdk, "JSONSchemaValidator7781Fa0548A98342")
        assert hasattr(dnacentersdk, "JSONSchemaValidator109D1B4F4289Aecd")
        assert hasattr(dnacentersdk, "JSONSchemaValidator6099Da82477B858A")
        assert hasattr(dnacentersdk, "JSONSchemaValidator83A3B9404Cb88787")
        assert hasattr(dnacentersdk, "JSONSchemaValidator9480Fa1F47Ca9254")
        assert hasattr(dnacentersdk, "JSONSchemaValidator9C9A785741CbB41F")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorA7B42836408A8E74")
        assert hasattr(dnacentersdk, "JSONSchemaValidator62B05B2C40A9B216")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorF393Abe84989Bb48")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorD0A1Abfa435B841D")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorF6B119Ad4D4AAf16")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorC8Bf6B65414A9Bc7")
        assert hasattr(dnacentersdk, "JSONSchemaValidator00A2Fa6146089317")
        assert hasattr(dnacentersdk, "JSONSchemaValidator2E9DB85840FbB1Cf")
        assert hasattr(dnacentersdk, "JSONSchemaValidator1399891C42A8Be64")
        assert hasattr(dnacentersdk, "JSONSchemaValidator4695090D403B8Eaa")
        assert hasattr(dnacentersdk, "JSONSchemaValidator45Bc7A8344A8Bc1E")
        assert hasattr(dnacentersdk, "JSONSchemaValidator4D86A993469A9Da9")
        assert hasattr(dnacentersdk, "JSONSchemaValidator8091A9B84BfbA53B")
        assert hasattr(dnacentersdk, "JSONSchemaValidator429C28154BdaA13D")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorCaa3Ea704D78B37E")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorEab7Abe048Fb99Ad")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorC1A359B14C89B573")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorEe9AAb01487A8896")
        assert hasattr(dnacentersdk, "JSONSchemaValidator069D9823451B892D")
        assert hasattr(dnacentersdk, "JSONSchemaValidator17929Bc7465BB564")
        assert hasattr(dnacentersdk, "JSONSchemaValidator10B06A6A4F7BB3Cb")
        assert hasattr(dnacentersdk, "JSONSchemaValidator1Da5Ebdd434AAcfe")
        assert hasattr(dnacentersdk, "JSONSchemaValidator44974Ba5435A801D")
        assert hasattr(dnacentersdk, "JSONSchemaValidator4C8CAb5F435A80F4")
        assert hasattr(dnacentersdk, "JSONSchemaValidator55B439Dc4239B140")
        assert hasattr(dnacentersdk, "JSONSchemaValidator6BacB8D14639Bdc7")
        assert hasattr(dnacentersdk, "JSONSchemaValidator4D9CA8E2431A8A24")
        assert hasattr(dnacentersdk, "JSONSchemaValidator3D9B99C343398A27")
        assert hasattr(dnacentersdk, "JSONSchemaValidator709FDa3C42B8877A")
        assert hasattr(dnacentersdk, "JSONSchemaValidator33B799D04D0A8907")
        assert hasattr(dnacentersdk, "JSONSchemaValidator7Aa3Da9D4E098Ef2")
        assert hasattr(dnacentersdk, "JSONSchemaValidator63Bb88B74F59Aa17")
        assert hasattr(dnacentersdk, "JSONSchemaValidator9788B8Fc4418831D")
        assert hasattr(dnacentersdk, "JSONSchemaValidator948EA8194348Bc0B")
        assert hasattr(dnacentersdk, "JSONSchemaValidator47A1B84B4E1B8044")
        assert hasattr(dnacentersdk, "JSONSchemaValidator99872A134D0A9Fb4")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorA5Ac99774C6BB541")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorA4967Be64DfaAa1A")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorA6B798Ab4AcaA34E")
        assert hasattr(dnacentersdk, "JSONSchemaValidator58A3699E489B9529")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorB68A6Bd8473A9A25")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorC1Ba9A424C08A01B")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorBf859Ac64A0BA19C")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorC5AcD9Fa4C1A8Abc")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorDb8E09234A988Bab")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorF5Ac590C4Ca9975A")
        assert hasattr(dnacentersdk, "JSONSchemaValidator89B36B4649999D81")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorFba0D80747Eb82E8")
        assert hasattr(dnacentersdk, "JSONSchemaValidator979688084B7BA60D")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorA6965B454C9A8663")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorF6Ac994F451BA011")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorFf816B8E435897Eb")
        assert hasattr(dnacentersdk, "JSONSchemaValidator26B44Ab04649A183")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorA1A9387346Ba92B1")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorE78BB8A2449B9Eed")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorF5A269C44F2A95Fa")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorE487F8D3481B94F2")
        assert hasattr(dnacentersdk, "JSONSchemaValidator33Bb2B9D40199E14")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorD6B8Ca774739Adf4")
        assert hasattr(dnacentersdk, "JSONSchemaValidator3F89Bbfc4F6B8B50")
        assert hasattr(dnacentersdk, "JSONSchemaValidator42B6A86E44B8Bdfc")
        assert hasattr(dnacentersdk, "JSONSchemaValidator9698C8Ec4A0B8C1A")
        assert hasattr(dnacentersdk, "JSONSchemaValidator55Bc3Bf94E38B6Ff")
        assert hasattr(dnacentersdk, "JSONSchemaValidator8A9D2B76443B914E")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorA395Fae644Ca899C")
        assert hasattr(dnacentersdk, "JSONSchemaValidator7Ab9A8Bd4F3B86A4")
        assert hasattr(dnacentersdk, "JSONSchemaValidator0C8F7A0B49B9Aedd")
        assert hasattr(dnacentersdk, "JSONSchemaValidator8Cb6783B4FabA1F4")
        assert hasattr(dnacentersdk, "JSONSchemaValidator4Dbe3Bc743A891Bc")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorBc8AAb4746Ca883D")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorFb9BEb664F2ABa4C")
        assert hasattr(dnacentersdk, "JSONSchemaValidator0A9C988445Cb91C8")
        assert hasattr(dnacentersdk, "JSONSchemaValidator21A6Db2540298F55")
        assert hasattr(dnacentersdk, "JSONSchemaValidator3086C9624F498B85")
        assert hasattr(dnacentersdk, "JSONSchemaValidator0B836B7B4B6A9Fd5")
        assert hasattr(dnacentersdk, "JSONSchemaValidator1E962Af345B8B59F")
        assert hasattr(dnacentersdk, "JSONSchemaValidator09B0F9Ce4239Ae10")
        assert hasattr(dnacentersdk, "JSONSchemaValidator5889Fb844939A13B")
        assert hasattr(dnacentersdk, "JSONSchemaValidator2499E9Ad42E8Ae5B")
        assert hasattr(dnacentersdk, "JSONSchemaValidator3Cb24Acb486B89D2")
        assert hasattr(dnacentersdk, "JSONSchemaValidator80AcB88E4Ac9Ac6D")
        assert hasattr(dnacentersdk, "JSONSchemaValidator6F9819E84178870C")
        assert hasattr(dnacentersdk, "JSONSchemaValidator7989F86846FaAf99")
        assert hasattr(dnacentersdk, "JSONSchemaValidator8Da0391947088A5A")
        assert hasattr(dnacentersdk, "JSONSchemaValidator7E92F9Eb46Db8320")
        assert hasattr(dnacentersdk, "JSONSchemaValidator9E857B5A4A0BBcdb")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorA4B6C87A4Ffb9Efa")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorAeb4Dad04A99Bbe3")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorAf8D7B0E470B8Ae2")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorBab6C9E5440885Cc")
        assert hasattr(dnacentersdk, "JSONSchemaValidator70A479A6462A9496")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorCf9418234D9AB37E")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorD8A619974A8A8C48")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorE6B3Db8046C99654")
        assert hasattr(dnacentersdk, "JSONSchemaValidator848B5A7B4F9B8C12")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorD9A1Fa9C4068B23C")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorF09319674049A7D4")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorCdab9B474899Ae06")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorF3B26B5544CaBab9")
        assert hasattr(dnacentersdk, "JSONSchemaValidator7Fbe4B804879Baa4")
        assert hasattr(dnacentersdk, "JSONSchemaValidator828828F44F28Bd0D")
        assert hasattr(dnacentersdk, "JSONSchemaValidator0Db7Da744C0B83D8")
        assert hasattr(dnacentersdk, "JSONSchemaValidator3D923B184Dc9A4Ca")
        assert hasattr(dnacentersdk, "JSONSchemaValidator3B9EF9674429Be4C")
        assert hasattr(dnacentersdk, "JSONSchemaValidator20B19B52464B8972")
        assert hasattr(dnacentersdk, "JSONSchemaValidator38Bd0B884B89A785")
        assert hasattr(dnacentersdk, "JSONSchemaValidator5Db21B8E43FaB7D8")
        assert hasattr(dnacentersdk, "JSONSchemaValidator288DF9494F2A9746")
        assert hasattr(dnacentersdk, "JSONSchemaValidator349C888443B89A58")
        assert hasattr(dnacentersdk, "JSONSchemaValidator1C894B5848EaB214")
        assert hasattr(dnacentersdk, "JSONSchemaValidator84B33A9E480ABcaf")
        assert hasattr(dnacentersdk, "JSONSchemaValidator4Bb22Af046Fa8F08")
        assert hasattr(dnacentersdk, "JSONSchemaValidator888F585C49B88441")
        assert hasattr(dnacentersdk, "JSONSchemaValidator4Eb56A614Cc9A2D2")
        assert hasattr(dnacentersdk, "JSONSchemaValidator82918A1B4D289C5C")
        assert hasattr(dnacentersdk, "JSONSchemaValidator8Db939744649A782")
        assert hasattr(dnacentersdk, "JSONSchemaValidator5B8639224Cd88Ea7")
        assert hasattr(dnacentersdk, "JSONSchemaValidator84B37Ae54C59Ab28")
        assert hasattr(dnacentersdk, "JSONSchemaValidator70Ad397649E9B4D3")
        assert hasattr(dnacentersdk, "JSONSchemaValidator81Bb4804405A8D2F")
        assert hasattr(dnacentersdk, "JSONSchemaValidator84Ad8B0E42CaB48A")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorB7BcAa084E2B90D0")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorB9855Ad54Ae98156")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorBa9DC85B4B8A9A17")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorCd8469E647CaAb0E")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorD0A4B88145AaBb51")
        assert hasattr(dnacentersdk, "JSONSchemaValidator819F9Aa54FeaB7Bf")
        assert hasattr(dnacentersdk, "JSONSchemaValidator8Fa8Eb404A4A8D96")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorF5947A4C439A8Bf0")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorAeb9Eb67460B92Df")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorB888792D43BaBa46")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorC3B3C9Ef4E6B8A09")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorC9809B6744F8A502")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorD888Ab6D4D59A8C1")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorCd98780F4888A66D")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorF49548C54Be8A3E2")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorFfa748Cc44E9A437")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorEb8249E34F69B0F1")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorF6826A8E41BbA242")
        assert hasattr(dnacentersdk, "JSONSchemaValidator89B2Fb144F5BB09B")
        assert hasattr(dnacentersdk, "JSONSchemaValidator17A82Ac94Cf99Ab0")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorEeb168Eb41988E07")
        assert hasattr(dnacentersdk, "JSONSchemaValidator50B589Fd4C7A930A")
        assert hasattr(dnacentersdk, "JSONSchemaValidator6284Db4649Aa8D31")
        assert hasattr(dnacentersdk, "JSONSchemaValidator9Ba14A9E441B8A60")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorB2B8Cb91459AA58F")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorC2B5Fb764D888375")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorB9B48Ac8463A8Aba")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorCa91Da84401ABba1")
        assert hasattr(dnacentersdk, "JSONSchemaValidator149AA93B4Ddb80Dd")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorE2AdBa7943BaB3E9")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorAc8AE94C4E69A09D")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorCca098344A489Dfa")
        assert hasattr(dnacentersdk, "JSONSchemaValidator8A96Fb954D09A349")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorDb9F997F4E59Aec1")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorC7A6592B4B98A369")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorCca519Ba45EbB423")
        assert hasattr(dnacentersdk, "JSONSchemaValidator98A39Bf4485A9871")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorBead7B3443B996A7")
        assert hasattr(dnacentersdk, "JSONSchemaValidatorCb81B93540BaAab0")
